/* MedQuizPlus — médico 3D del Hero (Three.js + GLTFLoader).
   Carga 'medico.glb', reproduce su animación integrada en bucle, y reacciona al cursor de forma sutil
   (giro limitado + micro-parallax + mirada de la cabeza si el modelo tiene huesos).
   Si 'medico.glb' no carga, la landing sigue intacta y se usa el médico procedural de hero3d-fallback.js.

   Conexión con el proyecto (sin cambios de IDs/clases):
   - pro.js crea  <div class="orbit"> dentro de .hero-demo; pro.css lo coloca a la derecha de la tarjeta del quiz
     (≥1280 px) o encima de ella (<1280 px).
   - Este archivo solo añade el <canvas class="orbit__gl"> dentro de .orbit y reacciona al evento 'fx:correct'. */
import * as THREE from "three";
import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";
import { DRACOLoader } from "three/addons/loaders/DRACOLoader.js";
import { MeshoptDecoder } from "three/addons/libs/meshopt_decoder.module.js";
import { RoomEnvironment } from "three/addons/environments/RoomEnvironment.js";

/* =====================================================================
   CONFIGURACIÓN — todo lo ajustable está aquí
   Unidades: la escena mide ~3,4 de alto (el médico completo). Los ángulos están en radianes.
   rotationY negativo = el médico mira hacia la IZQUIERDA (hacia el texto del Hero).
   ===================================================================== */
const CONFIG = {
  modelPath: "Sin_nombre.glb",
  fallbackModule: "./hero3d-fallback.js?v=1",
  baseHeight: 3.4,                  // altura base del médico (escena); 'scale' la multiplica

  // Hasta qué ancho de ventana (px) se considera cada dispositivo
  breakpoints: { mobileMax: 767.98, tabletMax: 1279.98 },

  desktop: { scale: 1.0,  positionX: 0, positionY: 0,     positionZ: 0, rotationY: -0.32, rotationX: 0 },
  tablet:  { scale: 0.9,  positionX: 0, positionY: -0.04, positionZ: 0, rotationY: -0.16, rotationX: 0 },
  mobile:  { scale: 0.82, positionX: 0, positionY: -0.1,  positionZ: 0, rotationY: 0,     rotationX: 0 },

  interaction: {
    maxRotationY: 0.14,             // giro máximo del cuerpo a izquierda/derecha
    maxRotationX: 0.07,             // inclinación máxima arriba/abajo
    rotationLerp: 0.05,             // inercia: menor = más suave (se aplica por cada 1/60 s)
    parallaxStrength: 0.06,         // desplazamiento máximo en X/Y (unidades de escena)
    parallaxByDevice: { desktop: 1, tablet: 0.5, mobile: 0 },   // multiplicador por dispositivo
    headFollow: true,               // si el modelo tiene huesos Head/Neck, la cabeza mira un poco hacia el cursor
    headYaw: 0.2,                   // giro extra máximo de la cabeza (rad)
    headPitch: 0.1,                 // inclinación extra máxima de la cabeza (rad)
    touch: false                    // true = pequeño movimiento con el dedo (pointermove táctil); no bloquea el scroll
  },

  animation: {
    prefer: /idle|breath|stand|wait|talk|present|wave|salud|reposo|respir/i,        // clip principal preferido
    celebrate: /dance|baile|cheer|celebr|victory|happy|jump|clap|aplaus/i,          // clip para cuando aciertas
    celebrateSeconds: 3.2,
    fadeSeconds: 0.45,
    lockRootMotion: true            // evita que la cadera "viaje": sin saltos al repetir el bucle
  },

  materials: {
    transparent: false,             // fuerza material opaco (el GLB viene con alphaMode BLEND y eso hacía que la ropa se superpusiera)
    depthWrite: true,
    roughness: 0.75,                // menos brillo
    metalness: 0.1,
    sharpenTextures: true,          // anisotropía máxima y filtros mipmap
    fallbackMaterial: { color: 0xc9d6dc, roughness: 0.6, metalness: 0.1 }   // solo si el GLB no trae textura
  },

  look: {
    ambient: 0.65,                  // luz ambiental suave (intensidad moderada)
    key: 2.2,                       // luz direccional principal
    keyPosition: [3.5, 4.95, 3.5],  // elevación 45° y 45° hacia la derecha/frente
    shadows: true,                  // sombras suaves: relieve y volumen en la ropa
    shadowMapSize: 1024,
    shadowSoftness: 3,              // radio de suavizado (PCFSoft)
    environment: 0.25,              // reflejos suaves (0 = apagado)
    pixelRatioCap: 2,
    pixelRatioCapMobile: 1.5
  },

  breathing: { amplitude: 0.03, speed: 1.9 }   // solo si el modelo NO trae animación propia
};

(function () {
  "use strict";

  var orbit = document.querySelector(".hero .orbit");
  if (!orbit) return;

  function mq(q) { try { return matchMedia(q).matches; } catch (e) { return false; } }
  var reduced = mq("(prefers-reduced-motion: reduce)");
  var hasMouse = mq("(hover: hover) and (pointer: fine)");

  /* ---------- renderer ---------- */
  var renderer;
  try {
    renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: "high-performance" });
  } catch (e) { return fallback("sin WebGL"); }
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.NoToneMapping;               // colores reales
  renderer.setClearColor(0x000000, 0);
  renderer.domElement.setAttribute("aria-hidden", "true");
  var maxAniso = renderer.capabilities.getMaxAnisotropy();

  var scene = new THREE.Scene();
  scene.add(new THREE.AmbientLight(0xffffff, CONFIG.look.ambient));
  var key = new THREE.DirectionalLight(0xfff6ec, CONFIG.look.key);
  key.position.fromArray(CONFIG.look.keyPosition); scene.add(key);
  if (CONFIG.look.shadows) {
    renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFSoftShadowMap;
    key.castShadow = true; key.shadow.mapSize.set(CONFIG.look.shadowMapSize, CONFIG.look.shadowMapSize);
    key.shadow.radius = CONFIG.look.shadowSoftness; key.shadow.bias = -0.0004; key.shadow.normalBias = 0.025;
    var sc = key.shadow.camera; sc.left = -2.6; sc.right = 2.6; sc.top = 2.6; sc.bottom = -2.6; sc.near = 0.5; sc.far = 20; sc.updateProjectionMatrix();
  }
  if (CONFIG.look.environment > 0) {
    scene.environment = new THREE.PMREMGenerator(renderer).fromScene(new RoomEnvironment(), 0.04).texture;
    scene.environmentIntensity = CONFIG.look.environment;
  }
  var camera = new THREE.PerspectiveCamera(26, 1, 0.1, 80);
  camera.position.set(0, 0, 10.5);

  /* jerarquía: scene → anchor (posición/escala/parallax) → group (giro) → model */
  var anchor = new THREE.Group(), group = new THREE.Group();
  anchor.add(group); scene.add(anchor);

  /* ---------- estado (todo preasignado: nada se crea dentro del bucle) ---------- */
  var model = null, mixer = null, clock = new THREE.Clock(false);
  var mainAction = null, celebAction = null, celebUntil = 0, celebrating = false;
  var headBone = null, neckBone = null;
  var P = { device: "desktop", cfg: CONFIG.desktop, parallax: 0 }, widthRatio = 0.5;   // ancho que ocupa el médico respecto a su altura
  var target = { rx: 0, ry: 0, px: 0, py: 0 }, cur = { rx: 0, ry: 0, px: 0, py: 0 };
  var raf = 0, visible = true, running = false, hop = -10, elapsed = 0, ready = false;
  var _e = new THREE.Euler(), _qd = new THREE.Quaternion(), _qp = new THREE.Quaternion(), _ql = new THREE.Quaternion();
  var cv = renderer.domElement; cv.className = "orbit__gl";

  /* estado de carga: el espacio queda reservado (layout idéntico) y se muestra un indicador discreto */
  orbit.classList.add("has-3d", "orbit--glb", "orbit--loading");
  orbit.appendChild(cv);

  /* ---------- carga ---------- */
  try {
    var loader = new GLTFLoader();
    var draco = new DRACOLoader(); draco.setDecoderPath("https://www.gstatic.com/draco/versioned/decoders/1.5.6/");
    loader.setDRACOLoader(draco); loader.setMeshoptDecoder(MeshoptDecoder);
    loader.load(CONFIG.modelPath, onLoad, undefined, function (err) { fallback(err && err.message ? err.message : "no se pudo cargar " + CONFIG.modelPath); });
  } catch (err) { fallback(String(err)); }

  function sharpen(tex, isColor) {
    if (!tex) return;
    tex.anisotropy = maxAniso; tex.minFilter = THREE.LinearMipmapLinearFilter; tex.magFilter = THREE.LinearFilter; tex.generateMipmaps = true;
    if (isColor) tex.colorSpace = THREE.SRGBColorSpace;
    tex.needsUpdate = true;
  }

  /* Caja del modelo. Con mallas animadas (SkinnedMesh) Three.js subestima su tamaño: se mide con los huesos, que es exacto. */
  function measure(root) {
    root.updateMatrixWorld(true);
    var skinned = false, v = new THREE.Vector3(), box = new THREE.Box3();
    root.traverse(function (o) { if (o.isSkinnedMesh) skinned = true; });
    if (!skinned) return box.setFromObject(root);
    root.traverse(function (o) { if (o.isBone) { o.getWorldPosition(v); box.expandByPoint(v); } });
    return box.isEmpty() ? box.setFromObject(root) : box;
  }

  function onLoad(gltf) {
    try {
      model = gltf.scene;
      model.traverse(function (child) {
        if (!child.isMesh) return;
        child.frustumCulled = false;                             // evita parpadeos con mallas animadas
        if (CONFIG.look.shadows) { child.castShadow = true; child.receiveShadow = true; }   // la ropa se auto-sombrea: da relieve
        if (!child.material || (!child.material.map && child.material.color && child.material.color.getHex() === 0xffffff && !child.material.vertexColors)) {
          child.material = new THREE.MeshStandardMaterial(CONFIG.materials.fallbackMaterial);   // GLB sin color: material neutro
        }
        var C = CONFIG.materials;
        (Array.isArray(child.material) ? child.material : [child.material]).forEach(function (m) {
          if (!m) return;
          m.transparent = C.transparent;                         // 1) correcciones de material pedidas
          m.depthWrite = C.depthWrite;
          if ("roughness" in m) m.roughness = C.roughness;
          if ("metalness" in m) m.metalness = C.metalness;
          m.opacity = 1; m.alphaTest = 0; m.blending = THREE.NormalBlending;
          m.side = THREE.FrontSide;                              // doble cara + transparencia era lo que mezclaba capas de ropa
          if (m.roughnessMap) m.roughnessMap = null;             // los mapas anulan los valores fijos: se usan los de arriba
          if (m.metalnessMap) m.metalnessMap = null;
          if (m.specularIntensity != null) m.specularIntensity = 0.5;
          if (C.sharpenTextures) { sharpen(m.map, true); sharpen(m.emissiveMap, true); sharpen(m.normalMap); sharpen(m.aoMap); }
          m.needsUpdate = true;
        });
      });

      /* escala base y centrado: el cuerpo queda centrado en el origen del grupo */
      var box = measure(model), size = box.getSize(new THREE.Vector3()), c = box.getCenter(new THREE.Vector3());
      var k = CONFIG.baseHeight / Math.max(size.y, 1e-4);
      model.scale.multiplyScalar(k);
      model.position.set(-c.x * k, -c.y * k, -c.z * k);
      group.add(model);

      setupAnimation(gltf.animations || []);
      model.updateMatrixWorld(true);
      widthRatio = sampleExtents();
      findHeadBones();
      applyResponsive();
      model.updateMatrixWorld(true);

      renderer.render(scene, camera);
      ready = true;
      orbit.classList.remove("orbit--loading");
      orbit.setAttribute("data-3d", "ready");

      if (reduced) { if (mixer) { mixer.setTime(0); } frame(); return; }   // movimiento reducido: pose fija
      start();
    } catch (err) { fallback(String(err)); }
  }

  /* ---------- animación integrada ---------- */
  function lockRoot(clip) {
    clip.tracks.forEach(function (t) {
      if (!/hips.*\.position$|^root.*\.position$|armature.*\.position$/i.test(t.name) || t.getValueSize() !== 3) return;
      var v = t.values, x0 = v[0], z0 = v[2];
      for (var i = 0; i < v.length; i += 3) { v[i] = x0; v[i + 2] = z0; }   // conserva solo el movimiento vertical de la cadera
    });
  }
  function setupAnimation(clips) {
    if (!clips.length) return;
    if (CONFIG.animation.lockRootMotion) clips.forEach(lockRoot);
    var A = CONFIG.animation, idle = clips.filter(function (c) { return A.prefer.test(c.name); })[0];
    var celeb = clips.filter(function (c) { return c !== idle && A.celebrate.test(c.name); })[0];
    var main = idle || clips.filter(function (c) { return c !== celeb; }).sort(function (a, b) { return b.duration - a.duration; })[0] || clips[0];
    if (window.console) console.info("[hero3d] animaciones:", clips.map(function (c) { return c.name + " (" + c.duration.toFixed(1) + "s)"; }).join(", "), "→ principal:", main.name, celeb && celeb !== main ? "· al acertar: " + celeb.name : "");
    mixer = new THREE.AnimationMixer(model);              // un único mixer
    mainAction = mixer.clipAction(main); mainAction.setLoop(THREE.LoopRepeat, Infinity); mainAction.clampWhenFinished = false; mainAction.play();
    if (celeb && celeb !== main) { celebAction = mixer.clipAction(celeb); celebAction.setLoop(THREE.LoopRepeat, Infinity); celebAction.enabled = true; }
  }
  /* Mide cuánto ocupa el médico a lo ancho durante TODA la animación (muestrea el clip) para que nunca se corte */
  function sampleExtents() {
    if (!mixer || !mainAction) return 0.5;
    var v = new THREE.Vector3(), clip = mainAction.getClip(), dur = Math.max(clip.duration, 0.01), N = 16, minX = 1e9, maxX = -1e9, minY = 1e9, maxY = -1e9;
    for (var i = 0; i < N; i++) {
      mixer.setTime(dur * i / N); model.updateMatrixWorld(true);
      model.traverse(function (o) { if (!o.isBone) return; o.getWorldPosition(v); if (v.x < minX) minX = v.x; if (v.x > maxX) maxX = v.x; if (v.y < minY) minY = v.y; if (v.y > maxY) maxY = v.y; });
    }
    mixer.setTime(0); model.updateMatrixWorld(true);
    var ratio = ((maxX - minX) * 1.12) / Math.max(maxY - minY, 1e-4);          // 12 % de margen (manos, pelo)
    return Math.min(Math.max(ratio, 0.5), 1.1);
  }
  function findHeadBones() {
    if (!CONFIG.interaction.headFollow) return;
    model.traverse(function (o) {
      if (!o.isBone) return;
      if (!headBone && /(^|[^a-z])head$|mixamorig:?head$/i.test(o.name)) headBone = o;
      else if (!neckBone && /(^|[^a-z])neck$|mixamorig:?neck$/i.test(o.name)) neckBone = o;
    });
  }
  /* giro adicional de un hueso en ejes del MUNDO, sin importar cómo estén orientados sus ejes locales */
  function turnBone(b, rx, ry) {
    _e.set(rx, ry, 0, "YXZ"); _qd.setFromEuler(_e);
    b.parent.getWorldQuaternion(_qp);
    _ql.copy(_qp).invert().multiply(_qd).multiply(_qp);
    b.quaternion.premultiply(_ql);
    b.updateMatrixWorld(true);
  }

  /* ---------- responsive ---------- */
  function deviceNow() {
    var w = window.innerWidth;
    return w <= CONFIG.breakpoints.mobileMax ? "mobile" : (w <= CONFIG.breakpoints.tabletMax ? "tablet" : "desktop");
  }
  function applyResponsive() {
    P.device = deviceNow(); P.cfg = CONFIG[P.device];
    var I = CONFIG.interaction;
    P.parallax = I.parallaxStrength * I.parallaxByDevice[P.device] * (hasMouse || (I.touch && P.device !== "desktop") ? 1 : 0);
    anchor.scale.setScalar(P.cfg.scale);
    group.rotation.order = "YXZ";

    var w = Math.max(orbit.clientWidth, 1), h = Math.max(orbit.clientHeight, 1);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, P.device === "mobile" ? CONFIG.look.pixelRatioCapMobile : CONFIG.look.pixelRatioCap));
    renderer.setSize(w, h, false);
    camera.aspect = w / h;                                   // sin deformaciones al cambiar el tamaño
    var t = Math.tan(THREE.MathUtils.degToRad(camera.fov) / 2);
    camera.position.z = Math.max((CONFIG.baseHeight * 1.2) / 2 / t, (CONFIG.baseHeight * widthRatio) / 2 / (t * camera.aspect));
    camera.updateProjectionMatrix();
    if (!running && ready) frame();
  }
  var resizeQueued = false;
  function onResize() { if (resizeQueued) return; resizeQueued = true; requestAnimationFrame(function () { resizeQueued = false; applyResponsive(); }); }
  window.addEventListener("resize", onResize);
  if ("ResizeObserver" in window) new ResizeObserver(onResize).observe(orbit);

  /* ---------- interacción ---------- */
  function setTarget(clientX, clientY, strength) {
    var r = orbit.getBoundingClientRect(), cx = r.left + r.width / 2, cy = r.top + r.height * 0.3;
    /* cada lado se normaliza por separado: el borde izquierdo de la ventana da -1 y el derecho +1, aunque el médico esté a un lado */
    var dx = clientX - cx, dy = clientY - cy;
    var nx = dx < 0 ? dx / Math.max(cx, 1) : dx / Math.max(window.innerWidth - cx, 1);
    var ny = dy < 0 ? dy / Math.max(cy, 1) : dy / Math.max(window.innerHeight - cy, 1);
    nx = nx < -1 ? -1 : nx > 1 ? 1 : nx; ny = ny < -1 ? -1 : ny > 1 ? 1 : ny;
    target.ry = nx * strength; target.rx = ny * strength; target.px = nx * strength; target.py = -ny * strength;
  }
  if (!reduced) {
    if (hasMouse) {
      window.addEventListener("mousemove", function (e) { setTarget(e.clientX, e.clientY, 1); }, { passive: true });
      document.addEventListener("mouseleave", resetTarget);
    } else if (CONFIG.interaction.touch) {
      window.addEventListener("pointermove", function (e) { if (e.pointerType === "touch") setTarget(e.clientX, e.clientY, 0.35); }, { passive: true });
      window.addEventListener("pointerup", resetTarget, { passive: true });
    }
  }
  function resetTarget() { target.rx = target.ry = target.px = target.py = 0; }
  window.addEventListener("fx:correct", function () {
    if (reduced || !ready) return;
    if (celebAction) {                                          // clip de celebración distinto del principal
      celebUntil = elapsed + CONFIG.animation.celebrateSeconds; celebrating = true;
      celebAction.reset().play(); celebAction.crossFadeFrom(mainAction, CONFIG.animation.fadeSeconds, false);
    } else if (!mixer) hop = elapsed;                           // modelo sin animación: pequeño salto
    start();
  });

  /* ---------- bucle único ---------- */
  function lerpK(l, dt) { return 1 - Math.pow(1 - l, dt * 60); }       // lerp independiente de los fps
  function frame() {
    var dt = Math.min(clock.getDelta(), 0.1);
    elapsed += dt;
    if (mixer && !reduced) {
      if (celebrating && elapsed > celebUntil) { celebrating = false; mainAction.reset().play(); mainAction.crossFadeFrom(celebAction, CONFIG.animation.fadeSeconds, false); }
      mixer.update(dt);                                          // la animación propia continúa siempre
    }
    if (!reduced) {
      var I = CONFIG.interaction, k = lerpK(I.rotationLerp, dt);
      cur.ry = THREE.MathUtils.lerp(cur.ry, target.ry, k); cur.rx = THREE.MathUtils.lerp(cur.rx, target.rx, k);
      cur.px = THREE.MathUtils.lerp(cur.px, target.px, k); cur.py = THREE.MathUtils.lerp(cur.py, target.py, k);
      group.rotation.set(P.cfg.rotationX + cur.rx * I.maxRotationX, P.cfg.rotationY + cur.ry * I.maxRotationY, 0);
      var bob = 0;
      if (!mixer) {
        var h = elapsed - hop, jump = (h >= 0 && h < 0.9) ? Math.abs(Math.sin(h * 3.5)) * 0.3 * (1 - h / 0.9) : 0;
        bob = Math.sin(elapsed * CONFIG.breathing.speed) * CONFIG.breathing.amplitude + jump;
      }
      anchor.position.set(P.cfg.positionX + cur.px * P.parallax, P.cfg.positionY + cur.py * P.parallax + bob, P.cfg.positionZ);
      if (headBone && P.device !== "mobile") {                     // la cabeza mira un poco hacia el cursor (encima de la animación)
        model.updateMatrixWorld(true);
        if (neckBone) turnBone(neckBone, cur.rx * I.headPitch * 0.4, cur.ry * I.headYaw * 0.4);
        turnBone(headBone, cur.rx * I.headPitch * 0.6, cur.ry * I.headYaw * 0.6);
      }
    }
    renderer.render(scene, camera);
  }
  function loop() { raf = 0; if (!running) return; frame(); raf = requestAnimationFrame(loop); }
  function start() {
    if (reduced || !ready || running || !visible || document.visibilityState !== "visible") return;
    running = true; clock.start(); clock.getDelta(); raf = requestAnimationFrame(loop);
  }
  function stopLoop() { running = false; if (raf) cancelAnimationFrame(raf); raf = 0; clock.stop(); }
  /* un único observador de visibilidad: pausa el render y la animación fuera de pantalla o con la pestaña oculta */
  document.addEventListener("visibilitychange", function () { if (document.visibilityState === "visible") start(); else stopLoop(); });
  function watchVisibility() {
    if (!("IntersectionObserver" in window)) return;
    new IntersectionObserver(function (e) { visible = e[0].isIntersecting; if (visible) start(); else stopLoop(); }).observe(orbit);
  }

  /* ---------- error / respaldo ---------- */
  function fallback(reason) {
    if (window.console) console.warn("[hero3d] " + reason + " → médico de respaldo (la landing sigue funcionando)");
    stopLoop();
    try { renderer.dispose(); if (cv.parentNode) cv.parentNode.removeChild(cv); } catch (e) {}
    orbit.classList.remove("orbit--loading", "orbit--glb", "has-3d");
    orbit.removeAttribute("data-3d");
    import(CONFIG.fallbackModule).catch(function () {});
  }

  /* @debug-hook */
  watchVisibility();
})();
