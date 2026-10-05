/* MedQuizPlus — médico 3D del hero: carga 'medico.glb' (Three.js + GLTFLoader).
   - El personaje se mueve EN BLOQUE (sin deformar la malla ni mover los ojos por separado).
   - El ratón inclina todo el grupo con ángulos pequeños (maxRotationY / maxRotationX).
   - Render nítido (antialias + píxeles de alta densidad + anisotropía) y colores reales (sRGB).
   - Respiración: oscilación vertical suave en bucle.
   Si 'medico.glb' no carga, se usa el médico procedural de hero3d-fallback.js. */
import * as THREE from "three";
import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";
import { DRACOLoader } from "three/addons/loaders/DRACOLoader.js";
import { MeshoptDecoder } from "three/addons/libs/meshopt_decoder.module.js";
import { RoomEnvironment } from "three/addons/environments/RoomEnvironment.js";

(function () {
  "use strict";

  /* ---------- ajustes ---------- */
  var MODEL_URL = "medico.glb";
  var FACE_Y = 0;              /* orientación inicial: 0 = de frente a la cámara */
  var MODEL_HEIGHT = 3.4;      /* altura del médico en unidades de la escena (escala final) */
  var maxRotationY = 0.15;     /* giro máximo izquierda/derecha (rad) */
  var maxRotationX = 0.1;      /* inclinación máxima arriba/abajo (rad) */
  var BREATH_AMP = 0.03;       /* amplitud de la respiración (unidades de escena) */
  var BREATH_SPEED = 1.9;      /* velocidad de la respiración (rad/s) */

  var orbit = document.querySelector(".hero .orbit");
  if (!orbit) return;

  var reduced = false, fine = false;
  try { reduced = matchMedia("(prefers-reduced-motion: reduce)").matches; } catch (e) {}
  try { fine = matchMedia("(hover: hover) and (pointer: fine)").matches; } catch (e) {}

  /* ---------- 2) renderer nítido ---------- */
  var renderer;
  try {
    renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: "high-performance" });
  } catch (e) { return fallback("sin WebGL"); }
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.NoToneMapping;          /* colores reales: sin filtro de tonos */
  renderer.setClearColor(0x000000, 0);
  renderer.domElement.setAttribute("aria-hidden", "true");
  var maxAniso = renderer.capabilities.getMaxAnisotropy();

  var scene = new THREE.Scene();

  /* ---------- 3) iluminación ---------- */
  scene.add(new THREE.AmbientLight(0xffffff, 1.2));
  var sun = new THREE.DirectionalLight(0xffffff, 2.0); sun.position.set(5, 8, 5); scene.add(sun);
  /* reflejos suaves para que los mapas metálico/rugosidad no se vean negros (el color lo dan las luces de arriba) */
  var pmrem = new THREE.PMREMGenerator(renderer);
  scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture;
  scene.environmentIntensity = 0.3;

  var camera = new THREE.PerspectiveCamera(26, 1, 0.1, 80);
  camera.position.set(0, 0, 10.5);
  camera.lookAt(0, 0, 0);

  /* grupo del personaje: el centro del cuerpo queda en el origen, así gira en bloque sobre su centro */
  var group = new THREE.Group(); scene.add(group);
  var model = null;
  var tx = 0, ty = 0, hx = 0, hy = 0, visible = true, raf = 0, t0 = performance.now(), last = t0, hop = -10;
  var cv = renderer.domElement; cv.className = "orbit__gl";
  orbit.classList.add("orbit--loading");
  orbit.appendChild(cv);

  /* ---------- 1) carga del GLB (Draco y Meshopt por si está comprimido) ---------- */
  var loader = new GLTFLoader();
  var draco = new DRACOLoader(); draco.setDecoderPath("https://www.gstatic.com/draco/versioned/decoders/1.5.6/");
  loader.setDRACOLoader(draco); loader.setMeshoptDecoder(MeshoptDecoder);
  loader.load(MODEL_URL, onLoad, undefined, function (err) { fallback(err && err.message ? err.message : "no se pudo cargar " + MODEL_URL); });

  function sharpen(tex, isColor) {
    if (!tex) return;
    tex.anisotropy = maxAniso;
    tex.minFilter = THREE.LinearMipmapLinearFilter;
    tex.magFilter = THREE.LinearFilter;
    tex.generateMipmaps = true;
    if (isColor) tex.colorSpace = THREE.SRGBColorSpace;
    tex.needsUpdate = true;
  }

  function onLoad(gltf) {
    model = gltf.scene;
    model.traverse(function (child) {
      if (!child.isMesh) return;
      child.frustumCulled = false;
      var ms = Array.isArray(child.material) ? child.material : [child.material];
      ms.forEach(function (m) {
        if (!m) return;
        sharpen(m.map, true); sharpen(m.emissiveMap, true);      /* color: textura nítida con anisotropía */
        sharpen(m.normalMap); sharpen(m.metalnessMap); sharpen(m.roughnessMap); sharpen(m.aoMap);
        /* el mapa metálico del modelo marca también la esclera de los ojos: sin este tope se ven como un aro negro */
        if ("metalness" in m) m.metalness = Math.min(m.metalness, 0.25);
        m.needsUpdate = true;
      });
    });

    /* encuadre: escala a MODEL_HEIGHT y centra el cuerpo en el origen del grupo */
    var box = new THREE.Box3().setFromObject(model), size = box.getSize(new THREE.Vector3()), c = box.getCenter(new THREE.Vector3());
    var k = MODEL_HEIGHT / Math.max(size.y, 0.0001);
    model.scale.multiplyScalar(k);
    model.position.set(-c.x * k, -c.y * k, -c.z * k);
    model.rotation.y = FACE_Y;
    group.add(model);

    fit();
    orbit.classList.remove("orbit--loading");
    orbit.classList.add("has-3d", "orbit--glb");
    fit();
    frame(performance.now());
    if (reduced) { addEventListener("resize", function () { frame(performance.now()); }); return; }
    if ("IntersectionObserver" in window) new IntersectionObserver(function (e) { visible = e[0].isIntersecting; if (visible) kick(); }).observe(orbit);
    document.addEventListener("visibilitychange", kick);
    kick();
  }

  /* encaja al médico completo (alto y ancho) según el tamaño del contenedor */
  function fit() {
    var w = Math.max(orbit.clientWidth, 1), h = Math.max(orbit.clientHeight, 1);
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    var t = Math.tan(THREE.MathUtils.degToRad(camera.fov) / 2);
    var needH = (MODEL_HEIGHT * 1.2) / 2 / t;
    var needW = (MODEL_HEIGHT * 0.5) / 2 / (t * camera.aspect);
    camera.position.z = Math.max(needH, needW);
    camera.updateProjectionMatrix();
  }
  if ("ResizeObserver" in window) new ResizeObserver(function () { fit(); if (reduced && model) frame(performance.now()); }).observe(orbit);
  else addEventListener("resize", fit);

  /* ---------- 1) seguimiento del ratón: rota TODO el grupo, con ángulos pequeños ---------- */
  if (fine && !reduced) {
    addEventListener("pointermove", function (e) {
      var r = orbit.getBoundingClientRect(), cx = r.left + r.width / 2, cy = r.top + r.height * 0.3;
      tx = Math.max(-1, Math.min(1, (e.clientX - cx) / (innerWidth * 0.5)));
      ty = Math.max(-1, Math.min(1, (e.clientY - cy) / (innerHeight * 0.5)));
    }, { passive: true });
    document.addEventListener("pointerleave", function () { tx = 0; ty = 0; });
    window.addEventListener("pointerout", function (e) { if (!e.relatedTarget) { tx = 0; ty = 0; } });
  }
  window.addEventListener("fx:correct", function () { hop = (performance.now() - t0) / 1000; if (!reduced && model) kick(); });

  function frame(now) {
    raf = 0;
    var dt = Math.min((now - last) / 1000, 0.1); last = now;
    var t = (now - t0) / 1000;
    if (!reduced) {
      var kf = 1 - Math.exp(-dt * 6);                         /* suavizado independiente de los fps */
      hx += (tx - hx) * kf; hy += (ty - hy) * kf;
      group.rotation.y = hx * maxRotationY;                    /* giro en bloque izquierda/derecha */
      group.rotation.x = hy * maxRotationX;                    /* inclinación en bloque arriba/abajo */
      /* 4) respiración en bucle: oscilación vertical suave */
      var h = t - hop, jump = (h >= 0 && h < 0.9) ? Math.abs(Math.sin(h * 3.5)) * 0.3 * (1 - h / 0.9) : 0;
      group.position.y = Math.sin(t * BREATH_SPEED) * BREATH_AMP + jump;
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
