/* MedQuizPlus — médico 3D del Hero (Three.js + GLTFLoader).
   Carga ÚNICAMENTE 'Sin_nombre.glb' y mantiene su animación base con un AnimationMixer a velocidad muy baja
   (CONFIG.animation.timeScale), así se ve vivo y de pie sin bailar. No se fuerza ninguna rotación de brazos.
   Interactividad: cuello y cabeza siguen el cursor con inercia, limitados a 20°. Materiales opacos y mates (roughness 0.7).
   Si el .glb no carga, la landing sigue intacta y se usa el médico procedural de hero3d-fallback.js.

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
    maxHeadYawDeg: 20,              // giro máximo de cuello+cabeza a izquierda/derecha (grados) — nunca pasa de aquí
    maxHeadPitchDeg: 12,            // inclinación máxima arriba/abajo (grados)
    neckShare: 0.4,                 // reparto del giro: 40 % cuello, 60 % cabeza
    restLookAtUser: 0.6,            // en reposo la cabeza compensa el giro del cuerpo y mira al usuario (0 = no, 1 = totalmente)
    rotationLerp: 0.06,             // inercia: menor = más suave (se aplica por cada 1/60 s)
    idleGaze: 0.07,                 // deriva sutil de la mirada cuando el cursor no se mueve (fracción del giro máximo)
    maxRotationY: 0.05,             // giro mínimo del cuerpo entero con el cursor (rad)
    maxRotationX: 0.025,
    parallaxStrength: 0.04,         // desplazamiento máximo en X/Y (unidades de escena)
    parallaxByDevice: { desktop: 1, tablet: 0.5, mobile: 0 },   // multiplicador por dispositivo
    touch: false                    // true = pequeño movimiento con el dedo (pointermove táctil); no bloquea el scroll
  },

  animation: {
    enabled: true,                  // true = reproduce la animación base de Sin_nombre.glb en bucle; false = pose fija (ver 'pose')
    timeScale: 0.25,                // velocidad: 1 = normal · 0.2–0.3 = muy lenta: el personaje se ve vivo y de pie, sin bailar
    lockRootMotion: true            // la cadera no "viaja": el médico se queda en su sitio y el bucle no da saltos
  },

  pose: {                           // solo con animation.enabled = false o con "reducir movimiento": se muestra la pose inicial del esqueleto, sin tocar ningún hueso
    time: "rest"
  },

  idle: {                           // respiración y micro-movimiento (seno/coseno). Solo en pose fija; con animación se desactiva. 0 = apagado
    speed: 1.7,                     // ciclos de respiración (rad/s)
    bodyBob: 0.011,                 // vaivén vertical del cuerpo (unidades de escena)
    sway: 0.012                     // balanceo lento del cuerpo, peso de un pie a otro (rad)
  },

  materials: {
    transparent: false,             // fuerza material opaco (el GLB viene con alphaMode BLEND y eso hacía que la ropa se superpusiera)
    depthWrite: true,
    roughness: 0.7,                 // telas opacas del ambo y la bata
    metalness: 0.1,
    sharpenTextures: true,          // anisotropía máxima y filtros mipmap
    fallbackMaterial: { color: 0xc9d6dc, roughness: 0.6, metalness: 0.1 }   // solo si el GLB no trae textura
  },

  look: {
    ambient: 0.6,                   // luz ambiental suave (intensidad moderada)
    key: 2.2,                       // luz direccional principal
    keyPosition: [3.5, 4.95, 3.5],  // elevación 45° y 45° hacia la derecha/frente
    shadows: true,                  // sombras suaves: relieve y volumen en la ropa
    shadowMapSize: 1024,
    shadowSoftness: 3,              // radio de suavizado (PCFSoft)
    environment: 0.25,              // reflejos suaves (0 = apagado)
    pixelRatioCap: 2,
    pixelRatioCapMobile: 1.5
  }
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
  var model = null, mixer = null, clipDuration = 0, poseTimeUsed = 0, clock = new THREE.Clock(false);
  var gaze = { yaw: 0, pitch: 0 };                              // último ángulo aplicado a cuello+cabeza (para depurar)
  var B = {};                                                   // huesos de interacción: neck, head (+ rotación base de cada uno)
  var P = { device: "desktop", cfg: CONFIG.desktop, parallax: 0 }, widthRatio = 0.5;   // ancho que ocupa el médico respecto a su altura
  var target = { rx: 0, ry: 0, px: 0, py: 0 }, cur = { rx: 0, ry: 0, px: 0, py: 0 };
  var raf = 0, visible = true, running = false, hop = -10, elapsed = 0, ready = false, restYaw = 0;
  var AX_Y = new THREE.Vector3(0, 1, 0), AX_Z = new THREE.Vector3(0, 0, 1), _axP = new THREE.Vector3();
  var _qd = new THREE.Quaternion(), _qa = new THREE.Quaternion(), _qb = new THREE.Quaternion(), _qp = new THREE.Quaternion(), _ql = new THREE.Quaternion();
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

  /* Caja del médico con los huesos (con mallas animadas Three.js subestima el tamaño). Si hay animación, se recorre
     todo el clip para que ninguna postura se salga del recuadro. */
  function extents() {
    var box = new THREE.Box3(), v = new THREE.Vector3(), N = mixer ? 24 : 1, dur = clipDuration, i;
    if (mixer) mixer.timeScale = 1;
    for (i = 0; i < N; i++) {
      if (mixer) mixer.setTime(dur * i / N);
      model.updateMatrixWorld(true);
      model.traverse(function (o) { if (o.isBone) { o.getWorldPosition(v); box.expandByPoint(v); } });
    }
    if (mixer) { mixer.setTime(0); mixer.timeScale = CONFIG.animation.timeScale; model.updateMatrixWorld(true); }
    return box.isEmpty() ? box.setFromObject(model) : box;
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

      group.add(model);
      setupAnimation(gltf.animations || []);                    // animación lenta en bucle, o pose fija si no hay clip / reducir movimiento
      var box = extents(), size = box.getSize(new THREE.Vector3()), c = box.getCenter(new THREE.Vector3());
      var k = CONFIG.baseHeight / Math.max(size.y, 1e-4);
      model.scale.multiplyScalar(k);
      model.position.set(-c.x * k, -c.y * k, -c.z * k);
      widthRatio = Math.min(Math.max((size.x / Math.max(size.y, 1e-4)) * 1.2, 0.4), 1.2);   // ancho real durante TODA la animación + margen
      findBones();
      applyResponsive();
      model.updateMatrixWorld(true);

      renderer.render(scene, camera);
      ready = true;
      orbit.classList.remove("orbit--loading");
      orbit.setAttribute("data-3d", "ready");

      if (reduced) { frame(); return; }                          // movimiento reducido: pose fija, sin movimiento
      start();
    } catch (err) { fallback(String(err)); }
  }

  /* ---------- animación incluida en el GLB ---------- */
  function lockRoot(clip) {
    clip.tracks.forEach(function (t) {
      if (!/hips.*\.position$|^root.*\.position$|armature.*\.position$/i.test(t.name) || t.getValueSize() !== 3) return;
      var v = t.values, x0 = v[0], z0 = v[2];
      for (var i = 0; i < v.length; i += 3) { v[i] = x0; v[i + 2] = z0; }      // conserva solo el movimiento vertical de la cadera
    });
  }
  function setupAnimation(clips) {
    var A = CONFIG.animation;
    if (!A.enabled || reduced || !clips.length) { setupPose(); return; }   // pose fija (también con "reducir movimiento")
    var clip = clips.slice().sort(function (a, b) { return b.duration - a.duration; })[0];
    if (A.lockRootMotion) lockRoot(clip);
    clipDuration = clip.duration;
    mixer = new THREE.AnimationMixer(model);                  // un único mixer
    var action = mixer.clipAction(clip); action.setLoop(THREE.LoopRepeat, Infinity); action.clampWhenFinished = false; action.play();
    mixer.timeScale = A.timeScale;                            // velocidad lenta
    mixer.setTime(0);
    if (window.console) console.info("[hero3d] animación '" + clip.name + "' (" + clip.duration.toFixed(1) + " s) en bucle a velocidad x" + A.timeScale + ". Animaciones disponibles: " + clips.map(function (c) { return c.name; }).join(", "));
  }

  /* ---------- pose fija (sin animación) ---------- */
  function boneByName(n) { return model.getObjectByName("mixamorig" + n) || model.getObjectByName("mixamorig:" + n) || model.getObjectByName(n) || null; }
  function setupPose() {
    if (window.console) console.info("[hero3d] pose fija: pose inicial del esqueleto (sin reproducir animación).");
  }

  /* ---------- huesos de interacción ---------- */
  function findBones() {
    B.neck = boneByName("Neck"); B.head = boneByName("Head");
    ["neck", "head"].forEach(function (k) { if (B[k]) B[k].userData.base = B[k].quaternion.clone(); });   // rotación base (pose fija)
    if (!B.head && window.console) console.warn("[hero3d] el modelo no tiene hueso Head: el seguimiento se aplica al grupo completo");
  }
  /* Restaura la pose base del hueso y le suma un giro en ejes del MUNDO (yaw sobre Y, pitch sobre el eje lateral del cuerpo, roll sobre Z) */
  function turnBone(b, yaw, pitch, roll, axisP) {
    if (!b || !b.parent) return;
    if (!mixer) b.quaternion.copy(b.userData.base);          // sin mixer hay que volver a la pose base; con mixer los huesos se reescriben cada cuadro
    if (!yaw && !pitch && !roll) return;
    _qa.setFromAxisAngle(AX_Y, yaw); _qb.setFromAxisAngle(axisP, pitch); _qd.copy(_qa).multiply(_qb);
    if (roll) { _qa.setFromAxisAngle(AX_Z, roll); _qd.multiply(_qa); }
    b.parent.getWorldQuaternion(_qp);
    _ql.copy(_qp).invert().multiply(_qd).multiply(_qp);
    b.quaternion.premultiply(_ql);
  }

  /* ---------- responsive ---------- */
  function deviceNow() {
    var w = window.innerWidth;
    return w <= CONFIG.breakpoints.mobileMax ? "mobile" : (w <= CONFIG.breakpoints.tabletMax ? "tablet" : "desktop");
  }
  function applyResponsive() {
    P.device = deviceNow(); P.cfg = CONFIG[P.device];
    restYaw = -P.cfg.rotationY * CONFIG.interaction.restLookAtUser;          // la cabeza compensa el giro del cuerpo: mira al usuario
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
    hop = elapsed; start();                                     // al acertar: pequeño salto y un asentimiento con la cabeza
  });

  /* ---------- bucle único ---------- */
  function lerpK(l, dt) { return 1 - Math.pow(1 - l, dt * 60); }       // lerp independiente de los fps
  var DEG = Math.PI / 180;
  function clamp(v, lo, hi) { return v < lo ? lo : v > hi ? hi : v; }
  function frame() {
    var dt = Math.min(clock.getDelta(), 0.1);
    elapsed += dt;
    var I = CONFIG.interaction, Id = CONFIG.idle, t = elapsed, live = !reduced;
    if (mixer && live) mixer.update(dt);                          // la animación avanza SIEMPRE, con o sin cursor
    var k = lerpK(I.rotationLerp, dt);
    cur.ry = THREE.MathUtils.lerp(cur.ry, target.ry, k); cur.rx = THREE.MathUtils.lerp(cur.rx, target.rx, k);
    cur.px = THREE.MathUtils.lerp(cur.px, target.px, k); cur.py = THREE.MathUtils.lerp(cur.py, target.py, k);

    /* respiración / micro-movimiento: solo senos y cosenos del tiempo */
    var still = live && !mixer;                                   // el micro-movimiento (respirar) solo se añade si el cuerpo está en pose fija
    var br = still ? Math.sin(t * Id.speed) : 0, sw = still ? Math.sin(t * 0.55) : 0, dr = still ? 1 : 0;
    var h = t - hop, jump = (live && h >= 0 && h < 0.9) ? Math.abs(Math.sin(h * 3.5)) * 0.25 * (1 - h / 0.9) : 0;
    var nod = (live && h >= 0 && h < 0.7) ? Math.sin(h / 0.7 * Math.PI) * 0.22 : 0;

    group.rotation.set(P.cfg.rotationX + cur.rx * I.maxRotationX, P.cfg.rotationY + cur.ry * I.maxRotationY + sw * Id.sway, 0);
    anchor.position.set(P.cfg.positionX + cur.px * P.parallax, P.cfg.positionY + cur.py * P.parallax + br * Id.bodyBob + jump, P.cfg.positionZ);

    /* mirada: el cursor mueve cuello y cabeza con los límites en grados; sin cursor, la mirada deriva muy poco */
    var maxYaw = I.maxHeadYawDeg * DEG, maxPitch = I.maxHeadPitchDeg * DEG;
    var gdr = live ? 1 : 0, gx = cur.ry + gdr * Math.sin(t * 0.45) * I.idleGaze, gy = cur.rx + gdr * Math.cos(t * 0.33) * I.idleGaze * 0.7;
    var yaw = clamp(restYaw + gx * (gx < 0 ? maxYaw + restYaw : maxYaw - restYaw), -maxYaw, maxYaw);   // en reposo mira al usuario; los extremos del cursor llegan justo al límite
    var pitch = clamp(gy * maxPitch, -maxPitch, maxPitch);
    gaze.yaw = yaw; gaze.pitch = pitch;
    var bodyYaw = group.rotation.y;
    _axP.set(Math.cos(bodyYaw), 0, -Math.sin(bodyYaw));                          // eje lateral del cuerpo (para asentir)
    if (!B.head) group.rotation.y += yaw * 0.5, group.rotation.x += pitch * 0.5;     // sin huesos: el grupo completo sigue la mirada (también ≤ 20°)
    turnBone(B.neck, yaw * I.neckShare, pitch * I.neckShare, 0, _axP);
    turnBone(B.head, yaw * (1 - I.neckShare), pitch * (1 - I.neckShare) + nod, 0, _axP);
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
