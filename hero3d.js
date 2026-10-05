/* MedQuizPlus — médico 3D del hero: carga 'medico.glb' (Three.js + GLTFLoader).
   Colores reales (sRGB, sin tone mapping), luces nítidas, a la derecha de la tarjeta del quiz,
   la cabeza/cuerpo siguen al cursor y respira en bucle. Si el archivo no carga, usa el médico procedural
   de hero3d-fallback.js. */
import * as THREE from "three";
import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";
import { DRACOLoader } from "three/addons/loaders/DRACOLoader.js";
import { MeshoptDecoder } from "three/addons/libs/meshopt_decoder.module.js";
import { RoomEnvironment } from "three/addons/environments/RoomEnvironment.js";

(function () {
  "use strict";
  var MODEL_URL = "medico.glb";
  var FACE_Y = 0;            /* orientación inicial: 0 = de frente a la cámara (cambia solo si tu modelo mira a otro lado) */
  var TARGET_H = 3.9;        /* altura base del médico en unidades de la escena */
  var MODEL_SCALE = 0.88;    /* escala final: 1 = tamaño base; menor = más pequeño */
  var maxRotationY = 0.15;   /* giro máximo de la cabeza a izquierda/derecha (radianes) */
  var maxRotationX = 0.1;    /* giro máximo de la cabeza arriba/abajo (radianes) */
  var H3 = TARGET_H * MODEL_SCALE;   /* altura final usada para encuadrar */

  var orbit = document.querySelector(".hero .orbit");
  if (!orbit) return;

  var reduced = false, fine = false;
  try { reduced = matchMedia("(prefers-reduced-motion: reduce)").matches; } catch (e) {}
  try { fine = matchMedia("(hover: hover) and (pointer: fine)").matches; } catch (e) {}
  var lite = innerWidth < 768 || (navigator.hardwareConcurrency || 4) < 4;

  var renderer;
  try { renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: "high-performance" }); } catch (e) { return fallback("sin WebGL"); }

  /* 2) colores reales: salida sRGB y sin tone mapping (el filmic desvía los tonos) */
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.NoToneMapping;
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, lite ? 1.5 : 2));
  renderer.setClearColor(0x000000, 0);
  renderer.domElement.setAttribute("aria-hidden", "true");

  var scene = new THREE.Scene();
  var pmrem = new THREE.PMREMGenerator(renderer);
  scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture;
  scene.environmentIntensity = 0.35;           /* solo para brillos; el color lo dan las luces directas */

  var camera = new THREE.PerspectiveCamera(26, 1, 0.1, 80);
  camera.position.set(0, 0, 10.5);
  camera.lookAt(0, 0, 0);

  /* luces nítidas: principal cálida de frente, relleno suave, contraluz fría */
  var key = new THREE.DirectionalLight(0xffffff, 2.6); key.position.set(2.5, 3.5, 5); scene.add(key);
  var fill = new THREE.DirectionalLight(0xffffff, 0.9); fill.position.set(-4, 1, 3); scene.add(fill);
  var rim = new THREE.DirectionalLight(0xbfeee8, 1.2); rim.position.set(-2, 3, -4); scene.add(rim);
  scene.add(new THREE.HemisphereLight(0xffffff, 0xcfd8dc, 0.8));

  var holder = new THREE.Group(); scene.add(holder);   /* pivote en los pies: aquí respira y salta */
  var model = null, head = null, neck = null, chest = null, mixer = null;
  var tx = 0, ty = 0, hx = 0, hy = 0, visible = true, raf = 0, t0 = performance.now(), hop = -10;
  var cv = renderer.domElement; cv.className = "orbit__gl";
  orbit.classList.add("orbit--loading");
  orbit.appendChild(cv);

  /* 1) carga del GLB (con soporte de Draco y Meshopt por si lo exportaste comprimido) */
  var loader = new GLTFLoader();
  var draco = new DRACOLoader(); draco.setDecoderPath("https://www.gstatic.com/draco/versioned/decoders/1.5.6/");
  loader.setDRACOLoader(draco); loader.setMeshoptDecoder(MeshoptDecoder);
  loader.load(MODEL_URL, onLoad, undefined, function (err) { fallback(err && err.message ? err.message : "no se pudo cargar " + MODEL_URL); });

  /* Mallas sin huesos: se detecta el cuello (la sección más angosta) y un shader gira SOLO la cabeza
     y expande el pecho al respirar. Todo ocurre en la GPU; la malla original no se modifica. */
  var deform = null;
  function setupDeform(mesh) {
    if (!mesh.isMesh || mesh.isSkinnedMesh || !mesh.geometry.attributes.position) return null;
    if (mesh.quaternion.angleTo(new THREE.Quaternion()) > 1e-3) return null;
    var pos = mesh.geometry.attributes.position, S = mesh.scale.clone(), T = mesh.position.clone(), n = pos.count, i, y, minY = 1e9, maxY = -1e9;
    for (i = 0; i < n; i++) { y = pos.getY(i) * S.y + T.y; if (y < minY) minY = y; if (y > maxY) maxY = y; }
    var H = maxY - minY; if (!(H > 0)) return null;
    var N = 90, bins = [];
    for (i = 0; i < N; i++) bins.push({ a: 1e9, b: -1e9, c: 1e9, d: -1e9 });
    for (i = 0; i < n; i++) {
      var x = pos.getX(i) * S.x + T.x, z = pos.getZ(i) * S.z + T.z, k = Math.min(N - 1, Math.floor(((pos.getY(i) * S.y + T.y) - minY) / H * N)), B = bins[k];
      if (x < B.a) B.a = x; if (x > B.b) B.b = x; if (z < B.c) B.c = z; if (z > B.d) B.d = z;
    }
    var best = -1, bw = 1e9;                       /* cuello = sección más angosta entre el 45 % y el 70 % de la altura */
    for (i = Math.floor(N * 0.45); i < Math.floor(N * 0.7); i++) { var w = bins[i].b - bins[i].a; if (w > 0 && w < bw) { bw = w; best = i; } }
    if (best < 0) return null;
    var nb = bins[best], neckY = minY + (best + 0.5) / N * H;
    var u = {
      uS: { value: S }, uT: { value: T }, uPivot: { value: new THREE.Vector3((nb.a + nb.b) / 2, neckY, (nb.c + nb.d) / 2) },
      uBlend: { value: new THREE.Vector2(neckY - 0.012 * H, neckY + 0.05 * H) },
      uTorso: { value: new THREE.Vector4(minY + 0.3 * H, minY + 0.42 * H, minY + 0.5 * H, minY + 0.58 * H) },
      uYaw: { value: 0 }, uPitch: { value: 0 }, uBreath: { value: 0 }
    };
    var ms = Array.isArray(mesh.material) ? mesh.material : [mesh.material];
    ms.forEach(function (m) {
      m.onBeforeCompile = function (sh) {
        Object.keys(u).forEach(function (k) { sh.uniforms[k] = u[k]; });
        sh.vertexShader = "uniform vec3 uS; uniform vec3 uT; uniform vec3 uPivot; uniform vec2 uBlend; uniform vec4 uTorso; uniform float uYaw; uniform float uPitch; uniform float uBreath;\n" + sh.vertexShader
          .replace("#include <beginnormal_vertex>",
            "vec3 fxU = position * uS + uT;\n" +
            "float fxHW = smoothstep(uBlend.x, uBlend.y, fxU.y);\n" +
            "float fxBump = smoothstep(uTorso.x, uTorso.y, fxU.y) * (1.0 - smoothstep(uTorso.z, uTorso.w, fxU.y));\n" +
            "float fcy = cos(uYaw * fxHW), fsy = sin(uYaw * fxHW), fcx = cos(uPitch * fxHW), fsx = sin(uPitch * fxHW);\n" +
            "mat3 fxR = mat3(fcy, 0.0, -fsy, 0.0, 1.0, 0.0, fsy, 0.0, fcy) * mat3(1.0, 0.0, 0.0, 0.0, fcx, fsx, 0.0, -fsx, fcx);\n" +
            "vec3 objectNormal = normalize(normalize(fxR * normalize(vec3(normal) / uS)) * uS);\n" +
            "#ifdef USE_TANGENT\nvec3 objectTangent = vec3(tangent.xyz);\n#endif\n")
          .replace("#include <begin_vertex>",
            "vec3 transformed = vec3(position);\n" +
            "{ vec3 fu = transformed * uS + uT;\n" +
            "  fu = fxR * (fu - uPivot) + uPivot;\n" +
            "  fu.xz = uPivot.xz + (fu.xz - uPivot.xz) * (1.0 + uBreath * fxBump);\n" +
            "  fu.y += uBreath * 0.25 * fxBump;\n" +
            "  transformed = (fu - uT) / uS; }\n" +
            "#ifdef USE_ALPHAHASH\nvPosition = vec3(position);\n#endif\n");
      };
      m.customProgramCacheKey = function () { return "mqp-doc-deform"; };
      m.needsUpdate = true;
    });
    return u;
  }

  function pickBone(re, skip) {
    var found = null;
    model.traverse(function (o) {
      if (found || !re.test(o.name) || (skip && skip.test(o.name))) return;
      found = o;
    });
    return found;
  }

  function onLoad(gltf) {
    model = gltf.scene;
    model.traverse(function (o) {
      if (o.isMesh) {
        o.frustumCulled = false;                      /* evita que desaparezca al animarse los huesos */
        var ms = Array.isArray(o.material) ? o.material : [o.material];
        ms.forEach(function (m) {
          if (!m) return;
          if (m.map) m.map.colorSpace = THREE.SRGBColorSpace;
          if (m.emissiveMap) m.emissiveMap.colorSpace = THREE.SRGBColorSpace;
          if ("envMapIntensity" in m) m.envMapIntensity = 0.6;
          m.needsUpdate = true;
        });
      }
    });

    /* encuadre automático: escala, centra y apoya los pies en y = 0 */
    var box = new THREE.Box3().setFromObject(model), size = box.getSize(new THREE.Vector3()), c = box.getCenter(new THREE.Vector3());
    var k = H3 / Math.max(size.y, 0.0001);
    model.scale.setScalar(k);
    model.position.set(-c.x * k, -box.min.y * k, -c.z * k);
    model.rotation.y = FACE_Y;
    holder.add(model);
    holder.position.y = -H3 / 2;

    /* huesos / nodos para el seguimiento del cursor (si no hay, gira todo el modelo) */
    head = pickBone(/(^|[^a-z])head($|[^a-z])|mixamorig:?head$|^cabeza$/i, /top|end|hair|helmet|ear|eye|jaw/i);
    neck = pickBone(/(^|[^a-z])neck($|[^a-z])|mixamorig:?neck$|^cuello$/i, /end/i);
    chest = pickBone(/spine2|upper.?chest|(^|[^a-z])chest($|[^a-z])|spine1/i);
    [head, neck, chest].forEach(function (b) { if (b) b.userData.rest = b.quaternion.clone(); });

    if (!head) { model.traverse(function (o) { if (!deform && o.isMesh) deform = setupDeform(o); }); }

    /* si el GLB trae su propia animación (p. ej. reposo), se reproduce en bucle debajo del seguimiento */
    if (gltf.animations && gltf.animations.length && !reduced) {
      mixer = new THREE.AnimationMixer(model);
      var idle = gltf.animations.find(function (a) { return /idle|reposo|breath/i.test(a.name); }) || gltf.animations[0];
      mixer.clipAction(idle).play();
    }

    size_();
    orbit.classList.remove("orbit--loading");
    orbit.classList.add("has-3d", "orbit--glb");
    size_();
    frame(performance.now());
    if (reduced) { addEventListener("resize", function () { frame(performance.now()); }); return; }
    if ("IntersectionObserver" in window) new IntersectionObserver(function (e) { visible = e[0].isIntersecting; if (visible) kick(); }).observe(orbit);
    document.addEventListener("visibilitychange", kick);
    kick();
  }

  function size_() {
    var w = Math.max(orbit.clientWidth, 1), h = Math.max(orbit.clientHeight, 1);
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    /* que el médico entre completo aunque el contenedor sea angosto */
    var fovV = THREE.MathUtils.degToRad(camera.fov), need = (H3 * 1.18) / 2 / Math.tan(fovV / 2);
    var needW = (H3 * 0.5) / 2 / (Math.tan(fovV / 2) * camera.aspect);
    camera.position.z = Math.max(need, needW);
    camera.updateProjectionMatrix();
  }
  if ("ResizeObserver" in window) new ResizeObserver(function () { size_(); if (reduced && model) frame(performance.now()); }).observe(orbit); else addEventListener("resize", size_);

  /* 4) seguimiento del cursor: se mide desde el centro del propio médico */
  if (fine && !reduced) {
    addEventListener("pointermove", function (e) {
      var r = orbit.getBoundingClientRect(), cx = r.left + r.width / 2, cy = r.top + r.height * 0.28;
      tx = Math.max(-1, Math.min(1, (e.clientX - cx) / (innerWidth * 0.5)));
      ty = Math.max(-1, Math.min(1, (e.clientY - cy) / (innerHeight * 0.5)));
    }, { passive: true });
  }
  document.addEventListener("pointerleave", function () { tx = 0; ty = 0; });
  window.addEventListener("pointerout", function (e) { if (!e.relatedTarget) { tx = 0; ty = 0; } });
  window.addEventListener("fx:correct", function () { hop = (performance.now() - t0) / 1000; if (!reduced && model) kick(); });

  var qWorld = new THREE.Quaternion(), qDelta = new THREE.Quaternion(), qParent = new THREE.Quaternion(), qLocal = new THREE.Quaternion(), eul = new THREE.Euler();
  /* gira un hueso en ejes del MUNDO (da igual cómo estén orientados sus ejes locales) */
  function turn(bone, rx, ry) {
    if (!bone || !bone.parent) return;
    eul.set(rx, ry, 0, "YXZ"); qDelta.setFromEuler(eul);
    bone.parent.updateWorldMatrix(true, false);
    bone.parent.getWorldQuaternion(qParent);
    qLocal.copy(qParent).invert().multiply(qDelta).multiply(qParent);
    bone.quaternion.copy(qLocal).multiply(bone.userData.rest);
    bone.updateWorldMatrix(false, true);
  }

  var last = performance.now();
  function frame(now) {
    raf = 0;
    var dt = Math.min((now - last) / 1000, 0.1); last = now;
    var t = (now - t0) / 1000;
    if (mixer) mixer.update(dt);
    if (!reduced) {
      /* 5) respiración en bucle: pecho que sube y baja, anclada en los pies */
      var b = Math.sin(t * 1.9);
      holder.scale.set(1 + b * 0.004, 1 + b * 0.011, 1 + b * 0.004);
      /* salto de alegría al acertar en el quiz */
      var h = t - hop;
      holder.position.y = -H3 / 2 + (h >= 0 && h < 0.9 ? Math.abs(Math.sin(h * 3.5)) * 0.3 * (1 - h / 0.9) : 0);
      var kf = 1 - Math.exp(-Math.min(dt, 0.1) * 7);   /* suavizado independiente de los fps */
      hx += (tx - hx) * kf; hy += (ty - hy) * kf;
      if (head) {
        turn(chest, b * 0.012, 0);
        turn(neck, hy * maxRotationX * 0.4, hx * maxRotationY * 0.4);
        turn(head, hy * maxRotationX * 0.6, hx * maxRotationY * 0.6);
      } else if (deform) {
        /* sin huesos: la cabeza gira por shader; el cuerpo acompaña muy poco */
        deform.uYaw.value = hx * maxRotationY; deform.uPitch.value = hy * maxRotationX; deform.uBreath.value = b * 0.018;
        holder.rotation.y = 0; holder.rotation.x = 0;                    /* el cuerpo no gira: solo la cabeza, y muy poco */
      } else {
        holder.rotation.y = hx * maxRotationY; holder.rotation.x = hy * maxRotationX;   /* último recurso: gira todo el modelo, con los mismos límites */
      }
    }
    renderer.render(scene, camera);
    if (!reduced && visible && document.visibilityState === "visible") raf = requestAnimationFrame(frame);
  }
  function kick() { if (!raf && model) raf = requestAnimationFrame(frame); }

  /* si no hay modelo, se usa el médico procedural */
  function fallback(reason) {
    if (window.console) console.warn("[hero3d] " + reason + " → médico de respaldo");
    try { renderer.dispose(); if (cv.parentNode) cv.parentNode.removeChild(cv); } catch (e) {}
    orbit.classList.remove("orbit--loading");
    import("./hero3d-fallback.js?v=1").catch(function () {});
  }
})();
