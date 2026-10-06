/* =====================================================================================================
   MedQuizPlus — médico 3D del Hero (Three.js + GLTFLoader)

   · Carga ÚNICAMENTE 'Sin_nombre.glb' (con anti-caché). No existe ningún modelo de respaldo.
   · Pose fija, de pie, con los brazos caídos a los costados (se bajan por código desde la pose inicial en A/T).
   · Respiración procedimental: seno del tiempo sobre el cuerpo, el pecho y los hombros.
   · Seguimiento del cursor: cuello y cabeza giran con inercia (lerp en dos etapas) y límites en grados.
   · Materiales opacos y mates; luz direccional a 45° con sombras suaves + luz hemisférica de relleno.
   · Si el .glb no carga, la landing sigue intacta y el hueco 3D se oculta (sin respaldo).

   Conexión con el proyecto (IDs y clases existentes, sin cambios):
   · pro.js crea  <div class="orbit">  dentro de .hero-demo;  pro.css lo coloca a la derecha de la tarjeta del quiz
     (≥ 1280 px) o encima de ella (< 1280 px).
   · Este archivo añade el <canvas class="orbit__gl"> dentro de .orbit y escucha el evento 'fx:correct' (quiz acertado).
   ===================================================================================================== */
import * as THREE from "three";
import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";
import { MeshoptDecoder } from "three/addons/libs/meshopt_decoder.module.js";

/* =====================================================================================================
   CONFIGURACIÓN — todo lo ajustable está aquí.  Unidades: la escena mide ~3,4 de alto (el médico completo).
   rotationY negativo = el médico se gira hacia la IZQUIERDA (hacia el texto del Hero).
   ===================================================================================================== */
const CONFIG = {
  modelPath: "./Sin_nombre.glb",       // único modelo
  cacheBust: true,                     // true → '?v=' + Date.now()  ·  "texto" → versión fija ('?v=texto', permite caché)  ·  false → sin parámetro
  baseHeight: 3.4,                     // altura base del médico en la escena

  breakpoints: { mobileMax: 767.98, tabletMax: 1279.98 },

  /* escala y posición por dispositivo. scale > 1 agranda · positionY > 0 sube · positionX > 0 mueve a la derecha */
  desktop: { scale: 1.0,  positionX: 0, positionY: 0.12,  positionZ: 0, rotationY: -0.28, rotationX: 0 },
  tablet:  { scale: 0.95, positionX: 0, positionY: 0.04,  positionZ: 0, rotationY: -0.14, rotationX: 0 },
  mobile:  { scale: 0.9,  positionX: 0, positionY: 0,     positionZ: 0, rotationY: 0,     rotationX: 0 },

  /* postura: los brazos caen a los costados (rotaciones sobre los huesos Arm y ForeArm de Mixamo) */
  pose: {
    relaxArms: true,
    armDropDeg: 50,                    // cuánto baja cada brazo desde la pose abierta inicial
    forearmBendDeg: 12,                // flexión suave de los codos hacia delante
    palmTwistDeg: 0                    // gira los antebrazos para que las palmas miren al cuerpo (+ / −)
  },

  /* animación base del GLB: desactivada = pose fija. Si la activas, se reproduce en bucle a esta velocidad */
  animation: { enabled: false, timeScale: 0.25 },

  /* seguimiento del cursor (cuello + cabeza). Las coordenadas del cursor se normalizan de −1 a +1 */
  tracking: {
    maxYawDeg: 25,                     // máximo hacia los lados
    maxPitchDeg: 15,                   // máximo hacia arriba / abajo
    neckShare: 0.4,                    // reparto del giro: 40 % cuello · 60 % cabeza
    lerp: 0.06,                        // inercia (0.05–0.08). Menor = más suave y con más "masa"
    mass: 0.12,                        // segunda etapa de suavizado: elimina tirones del ratón
    restLookAtUser: 0.6,               // en reposo la cabeza compensa el giro del cuerpo y mira al usuario (0..1)
    idleGaze: 0.05,                    // deriva casi imperceptible de la mirada cuando el cursor no se mueve
    bodyFollow: 0.04,                  // giro mínimo del cuerpo entero con el cursor (rad)
    parallax: { desktop: 0.04, tablet: 0.02, mobile: 0 },   // desplazamiento máx. del médico (unidades de escena)
    touch: false                       // true = pequeño movimiento con el dedo; no bloquea el scroll
  },

  /* respiración: Math.sin(tiempo * speed) */
  breathing: {
    speed: 1.5,
    bodyBob: 0.002,                    // oscilación vertical del cuerpo (position.y)
    chestPitch: 0.02,                  // expansión del pecho (rad)
    shoulderLift: 0.03                 // elevación de los hombros (rad)
  },

  materials: { roughness: 0.70, metalness: 0.05, sharpenTextures: true },

  lights: {
    key: 1.2,                          // DirectionalLight principal
    keyPosition: [3.5, 4.95, 3.5],     // elevación 45° · azimut 45° (arriba, a la derecha y al frente)
    fill: 0.6,                         // HemisphereLight de relleno
    shadows: true,                     // sombras suaves: relieve en los pliegues del ambo y la bata
    shadowMapSize: 1024,
    shadowSoftness: 3
  },

  render: { pixelRatioCap: 2, pixelRatioCapMobile: 1.5 }
};

(function () {
  "use strict";

  const orbit = document.querySelector(".hero .orbit");
  if (!orbit) return;

  const mq = (q) => { try { return matchMedia(q).matches; } catch (e) { return false; } };
  const reduced = mq("(prefers-reduced-motion: reduce)");
  const hasMouse = mq("(hover: hover) and (pointer: fine)");
  const DEG = Math.PI / 180;
  const clamp = (v, lo, hi) => (v < lo ? lo : v > hi ? hi : v);
  const lerpK = (l, dt) => 1 - Math.pow(1 - l, dt * 60);          // lerp independiente de los fps

  /* ------------------------------------------------------------------ renderer ------------------- */
  let renderer;
  try {
    renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: "high-performance" });
  } catch (e) { return fail("este navegador no soporta WebGL"); }
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.NoToneMapping;                     // colores reales de la textura
  renderer.setClearColor(0x000000, 0);
  renderer.domElement.setAttribute("aria-hidden", "true");
  const canvas = renderer.domElement; canvas.className = "orbit__gl";
  const maxAniso = renderer.capabilities.getMaxAnisotropy();

  /* ------------------------------------------------------------------ escena y luces ------------- */
  const scene = new THREE.Scene();
  const L = CONFIG.lights;
  /* Three.js usa luces físicas: una intensidad de 1.0 equivale a ~0.32 de brillo. Se multiplica por π para que los valores de CONFIG se comporten como los de siempre (1.2 / 0.6) */
  scene.add(new THREE.HemisphereLight(0xffffff, 0xb8c4c9, L.fill * Math.PI));
  const key = new THREE.DirectionalLight(0xfff6ec, L.key * Math.PI);
  key.position.fromArray(L.keyPosition); scene.add(key);
  if (L.shadows) {
    renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFSoftShadowMap;
    key.castShadow = true; key.shadow.mapSize.set(L.shadowMapSize, L.shadowMapSize);
    key.shadow.radius = L.shadowSoftness; key.shadow.bias = -0.0004; key.shadow.normalBias = 0.025;
    const sc = key.shadow.camera; sc.left = -2.6; sc.right = 2.6; sc.top = 2.6; sc.bottom = -2.6; sc.near = 0.5; sc.far = 20; sc.updateProjectionMatrix();
  }
  const camera = new THREE.PerspectiveCamera(26, 1, 0.1, 80);
  camera.position.set(0, 0, 10.5);

  /* jerarquía: scene → anchor (posición / escala / parallax / respiración) → group (giro) → model */
  const anchor = new THREE.Group(), group = new THREE.Group();
  anchor.add(group); scene.add(anchor);

  /* ------------------------------------------------------------------ estado --------------------- */
  let model = null, mixer = null, playing = false, ready = false, running = false, visible = true;
  let raf = 0, elapsed = 0, hop = -10, widthRatio = 0.55, restYaw = 0, clipDuration = 0;
  const clock = new THREE.Clock(false);
  const P = { device: "desktop", cfg: CONFIG.desktop, parallax: 0 };
  const aim = { x: 0, y: 0 };                                     // objetivo normalizado del cursor (−1..1)
  const s1 = { x: 0, y: 0 }, s2 = { x: 0, y: 0 };                // suavizado en dos etapas (inercia + masa)
  const gaze = { yaw: 0, pitch: 0 };                              // último ángulo aplicado (depuración)
  const bone = {};                                                // huesos: spine2, shL, shR, neck, head
  const AX_X = new THREE.Vector3(1, 0, 0), AX_Y = new THREE.Vector3(0, 1, 0), AX_Z = new THREE.Vector3(0, 0, 1);
  const axP = new THREE.Vector3();
  const qd = new THREE.Quaternion(), qa = new THREE.Quaternion(), qb = new THREE.Quaternion(), qp = new THREE.Quaternion(), ql = new THREE.Quaternion();

  orbit.classList.add("has-3d", "orbit--glb", "orbit--loading");  // el espacio queda reservado: sin saltos de diseño
  orbit.appendChild(canvas);

  /* ------------------------------------------------------------------ carga ---------------------- */
  const loader = new GLTFLoader();
  loader.setMeshoptDecoder(MeshoptDecoder);
  const url = CONFIG.modelPath + (CONFIG.cacheBust === true ? "?v=" + Date.now() : CONFIG.cacheBust ? "?v=" + CONFIG.cacheBust : "");
  try {
    loader.load(url, onLoad, undefined, (err) => fail("no se pudo cargar " + url + (err && err.message ? " (" + err.message + ")" : "")));
  } catch (err) { fail(String(err)); }

  function sharpen(tex, isColor) {
    if (!tex) return;
    tex.anisotropy = maxAniso; tex.minFilter = THREE.LinearMipmapLinearFilter; tex.magFilter = THREE.LinearFilter; tex.generateMipmaps = true;
    if (isColor) tex.colorSpace = THREE.SRGBColorSpace;
    tex.needsUpdate = true;
  }

  function onLoad(gltf) {
    try {
      model = gltf.scene;
      const M = CONFIG.materials;
      model.traverse((child) => {                                  // materiales opacos y mates
        if (!child.isMesh) return;
        child.frustumCulled = false;
        if (L.shadows) { child.castShadow = true; child.receiveShadow = true; }
        (Array.isArray(child.material) ? child.material : [child.material]).forEach((m) => {
          if (!m) return;
          m.transparent = false;                                   // el GLB viene en modo BLEND: se fuerza opaco
          m.depthWrite = true;
          m.opacity = 1; m.alphaTest = 0; m.blending = THREE.NormalBlending; m.side = THREE.FrontSide;
          if ("roughness" in m) m.roughness = M.roughness;
          if ("metalness" in m) m.metalness = M.metalness;
          if (m.roughnessMap) m.roughnessMap = null;               // los mapas anularían los valores fijos
          if (m.metalnessMap) m.metalnessMap = null;
          if (m.specularIntensity != null) m.specularIntensity = 0.4;
          if (M.sharpenTextures) { sharpen(m.map, true); sharpen(m.emissiveMap, true); sharpen(m.normalMap); sharpen(m.aoMap); }
          m.needsUpdate = true;
        });
      });
      group.add(model);

      setupPose(gltf.animations || []);                            // pose fija (o animación lenta si está activada)
      findBones();
      const box = extents(), size = box.getSize(new THREE.Vector3()), c = box.getCenter(new THREE.Vector3());
      const k = CONFIG.baseHeight / Math.max(size.y, 1e-4);        // escala base y centrado del cuerpo en el origen
      model.scale.multiplyScalar(k);
      model.position.set(-c.x * k, -c.y * k, -c.z * k);
      widthRatio = clamp((size.x / Math.max(size.y, 1e-4)) * 1.15, 0.4, 1.2);   // ancho real en esta pose + margen
      applyResponsive();
      model.updateMatrixWorld(true);

      ready = true;
      orbit.classList.remove("orbit--loading");
      orbit.setAttribute("data-3d", "ready");
      frame(0);
      if (!reduced) start();
    } catch (err) { fail(String(err)); }
  }

  /* ------------------------------------------------------------------ esqueleto y pose ----------- */
  const boneByName = (n) => model.getObjectByName("mixamorig" + n) || model.getObjectByName("mixamorig:" + n) || model.getObjectByName(n) || null;

  /* rotación PERMANENTE de un hueso en ejes del mundo (solo al preparar la pose) */
  function rotateWorld(b, axis, angle) {
    if (!b || !b.parent || !angle) return;
    qd.setFromAxisAngle(axis, angle);
    b.parent.updateWorldMatrix(true, false); b.parent.getWorldQuaternion(qp);
    ql.copy(qp).invert().multiply(qd).multiply(qp);
    b.quaternion.premultiply(ql);
  }

  function setupPose(clips) {
    const A = CONFIG.animation;
    if (A.enabled && !reduced && clips.length) {                   // animación base en bucle, lenta
      const clip = clips.slice().sort((a, b) => b.duration - a.duration)[0];
      clip.tracks.forEach((t) => {                                 // la cadera no "viaja": el médico se queda en su sitio
        if (!/hips.*\.position$|^root.*\.position$|armature.*\.position$/i.test(t.name) || t.getValueSize() !== 3) return;
        const v = t.values, x0 = v[0], z0 = v[2];
        for (let i = 0; i < v.length; i += 3) { v[i] = x0; v[i + 2] = z0; }
      });
      clipDuration = clip.duration;
      mixer = new THREE.AnimationMixer(model);
      const action = mixer.clipAction(clip); action.setLoop(THREE.LoopRepeat, Infinity); action.play();
      mixer.timeScale = A.timeScale; mixer.setTime(0); playing = true;
      return;
    }
    /* pose fija: brazos a los costados */
    const Pz = CONFIG.pose;
    if (!Pz.relaxArms) return;
    const d = Pz.armDropDeg * DEG, e = Pz.forearmBendDeg * DEG, tw = Pz.palmTwistDeg * DEG;
    const la = boneByName("LeftArm"), ra = boneByName("RightArm"), lf = boneByName("LeftForeArm"), rf = boneByName("RightForeArm");
    const lh = boneByName("LeftHand"), rh = boneByName("RightHand");
    rotateWorld(la, AX_Z, -d); rotateWorld(ra, AX_Z, d);           // el brazo izquierdo del personaje está en +X: bajarlo = giro negativo sobre Z
    if (la) la.updateWorldMatrix(true, true); if (ra) ra.updateWorldMatrix(true, true);
    rotateWorld(lf, AX_X, -e); rotateWorld(rf, AX_X, -e);          // codos algo flexionados hacia delante
    if (tw && lf && lh) twist(lf, lh, tw);
    if (tw && rf && rh) twist(rf, rh, -tw);
    model.updateMatrixWorld(true);
  }
  function twist(b, child, angle) {                                // gira un antebrazo sobre su propio eje
    const p0 = new THREE.Vector3(), p1 = new THREE.Vector3();
    b.getWorldPosition(p0); child.getWorldPosition(p1);
    rotateWorld(b, p1.sub(p0).normalize(), angle);
  }

  function findBones() {
    bone.spine2 = boneByName("Spine2"); bone.shL = boneByName("LeftShoulder"); bone.shR = boneByName("RightShoulder");
    bone.neck = boneByName("Neck"); bone.head = boneByName("Head");
    ["spine2", "shL", "shR", "neck", "head"].forEach((k) => { if (bone[k]) bone[k].userData.base = bone[k].quaternion.clone(); });
    if (!bone.head && window.console) console.warn("[hero3d] sin hueso Head: el seguimiento se aplica al grupo completo");
  }

  /* caja del médico medida con los huesos (con mallas animadas Three.js subestima el tamaño) */
  function extents() {
    const box = new THREE.Box3(), v = new THREE.Vector3(), N = playing ? 24 : 1;
    if (playing) mixer.timeScale = 1;
    for (let i = 0; i < N; i++) {
      if (playing) mixer.setTime(clipDuration * i / N);
      model.updateMatrixWorld(true);
      model.traverse((o) => { if (o.isBone) { o.getWorldPosition(v); box.expandByPoint(v); } });
    }
    if (playing) { mixer.setTime(0); mixer.timeScale = CONFIG.animation.timeScale; model.updateMatrixWorld(true); }
    return box.isEmpty() ? box.setFromObject(model) : box;
  }

  /* restaura la rotación base del hueso y le suma un giro en ejes del MUNDO (yaw sobre Y · pitch sobre el eje lateral del cuerpo · roll sobre Z) */
  function turnBone(b, yaw, pitch, roll) {
    if (!b || !b.parent) return;
    if (!playing) b.quaternion.copy(b.userData.base);               // pose fija: se vuelve a la base cada cuadro; con animación el mixer reescribe
    if (!yaw && !pitch && !roll) return;
    qa.setFromAxisAngle(AX_Y, yaw); qb.setFromAxisAngle(axP, pitch); qd.copy(qa).multiply(qb);
    if (roll) { qa.setFromAxisAngle(AX_Z, roll); qd.multiply(qa); }
    b.parent.getWorldQuaternion(qp);
    ql.copy(qp).invert().multiply(qd).multiply(qp);
    b.quaternion.premultiply(ql);
  }

  /* ------------------------------------------------------------------ responsive ---------------- */
  const deviceNow = () => { const w = window.innerWidth; return w <= CONFIG.breakpoints.mobileMax ? "mobile" : w <= CONFIG.breakpoints.tabletMax ? "tablet" : "desktop"; };

  function applyResponsive() {
    P.device = deviceNow(); P.cfg = CONFIG[P.device];
    P.parallax = (hasMouse || (CONFIG.tracking.touch && P.device !== "desktop")) ? CONFIG.tracking.parallax[P.device] : 0;
    restYaw = -P.cfg.rotationY * CONFIG.tracking.restLookAtUser;      // la cabeza compensa el giro del cuerpo: mira al usuario
    anchor.scale.setScalar(P.cfg.scale);
    group.rotation.order = "YXZ";
    const w = Math.max(orbit.clientWidth, 1), h = Math.max(orbit.clientHeight, 1);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, P.device === "mobile" ? CONFIG.render.pixelRatioCapMobile : CONFIG.render.pixelRatioCap));
    renderer.setSize(w, h, false);
    camera.aspect = w / h;                                            // sin deformaciones al cambiar el tamaño
    const t = Math.tan(THREE.MathUtils.degToRad(camera.fov) / 2);
    camera.position.z = Math.max((CONFIG.baseHeight * 1.18) / 2 / t, (CONFIG.baseHeight * widthRatio) / 2 / (t * camera.aspect));
    camera.updateProjectionMatrix();
    if (ready && !running) frame(0);
  }
  let resizeQueued = false;
  const onResize = () => { if (resizeQueued) return; resizeQueued = true; requestAnimationFrame(() => { resizeQueued = false; applyResponsive(); }); };
  window.addEventListener("resize", onResize);
  if ("ResizeObserver" in window) new ResizeObserver(onResize).observe(orbit);

  /* ------------------------------------------------------------------ cursor --------------------- */
  function setAim(clientX, clientY, strength) {
    const r = orbit.getBoundingClientRect(), cx = r.left + r.width / 2, cy = r.top + r.height * 0.3;
    const dx = clientX - cx, dy = clientY - cy;                       // cada lado se normaliza aparte: el borde de la ventana siempre da ±1
    aim.x = clamp(dx < 0 ? dx / Math.max(cx, 1) : dx / Math.max(window.innerWidth - cx, 1), -1, 1) * strength;
    aim.y = clamp(dy < 0 ? dy / Math.max(cy, 1) : dy / Math.max(window.innerHeight - cy, 1), -1, 1) * strength;
  }
  const resetAim = () => { aim.x = aim.y = 0; };
  if (!reduced) {
    if (hasMouse) {
      window.addEventListener("mousemove", (e) => setAim(e.clientX, e.clientY, 1), { passive: true });
      document.addEventListener("mouseleave", resetAim);
    } else if (CONFIG.tracking.touch) {
      window.addEventListener("pointermove", (e) => { if (e.pointerType === "touch") setAim(e.clientX, e.clientY, 0.35); }, { passive: true });
      window.addEventListener("pointerup", resetAim, { passive: true });
    }
  }
  window.addEventListener("fx:correct", () => { if (!reduced && ready) { hop = elapsed; start(); } });   // quiz acertado: salto + asentimiento

  /* ------------------------------------------------------------------ bucle de render ------------ */
  function frame(dt) {
    elapsed += dt;
    const T = CONFIG.tracking, Br = CONFIG.breathing, live = !reduced;
    if (playing && live) mixer.update(dt);                            // solo si la animación está activada

    /* cursor → suavizado en dos etapas (lerp con inercia baja + segunda etapa de "masa") */
    const k1 = lerpK(T.lerp, dt), k2 = lerpK(T.mass, dt);
    s1.x = THREE.MathUtils.lerp(s1.x, aim.x, k1); s1.y = THREE.MathUtils.lerp(s1.y, aim.y, k1);
    s2.x = THREE.MathUtils.lerp(s2.x, s1.x, k2);  s2.y = THREE.MathUtils.lerp(s2.y, s1.y, k2);

    /* respiración: Math.sin(tiempo * 1.5) */
    const still = live && !playing, br = still ? Math.sin(elapsed * Br.speed) : 0, sw = still ? Math.sin(elapsed * 0.5) : 0;
    const h = elapsed - hop;
    const jump = live && h >= 0 && h < 0.9 ? Math.abs(Math.sin(h * 3.5)) * 0.25 * (1 - h / 0.9) : 0;
    const nod = live && h >= 0 && h < 0.7 ? Math.sin(h / 0.7 * Math.PI) * 0.22 : 0;

    group.rotation.set(P.cfg.rotationX + s2.y * T.bodyFollow * 0.5, P.cfg.rotationY + s2.x * T.bodyFollow + sw * 0.01, 0);
    anchor.position.set(P.cfg.positionX + s2.x * P.parallax, P.cfg.positionY - s2.y * P.parallax + br * Br.bodyBob + jump, P.cfg.positionZ);

    /* mirada: yaw ±maxYaw (horizontal) · pitch ±maxPitch (vertical). Sin cursor, deriva mínima y mira al usuario */
    const maxYaw = T.maxYawDeg * DEG, maxPitch = T.maxPitchDeg * DEG;
    const gx = s2.x + (live ? Math.sin(elapsed * 0.45) * T.idleGaze : 0), gy = s2.y + (live ? Math.cos(elapsed * 0.33) * T.idleGaze * 0.7 : 0);
    const yaw = clamp(restYaw + gx * (gx < 0 ? maxYaw + restYaw : maxYaw - restYaw), -maxYaw, maxYaw);
    const pitch = clamp(gy * maxPitch, -maxPitch, maxPitch);
    gaze.yaw = yaw; gaze.pitch = pitch;

    axP.set(Math.cos(group.rotation.y), 0, -Math.sin(group.rotation.y));   // eje lateral del cuerpo (para asentir)
    if (bone.head) {
      turnBone(bone.spine2, 0, br * Br.chestPitch, 0);                 // el pecho se expande
      turnBone(bone.shL, 0, 0, br * Br.shoulderLift);                  // los hombros suben y bajan
      turnBone(bone.shR, 0, 0, -br * Br.shoulderLift);
      turnBone(bone.neck, yaw * T.neckShare, pitch * T.neckShare, 0);
      turnBone(bone.head, yaw * (1 - T.neckShare), pitch * (1 - T.neckShare) + nod, 0);
    } else {                                                           // sin huesos: se mueve el grupo completo con los mismos límites
      group.rotation.y += yaw; group.rotation.x += pitch;
    }
    renderer.render(scene, camera);
  }
  function loop() { raf = 0; if (!running) return; frame(Math.min(clock.getDelta(), 0.1)); raf = requestAnimationFrame(loop); }
  function start() {
    if (reduced || !ready || running || !visible || document.visibilityState !== "visible") return;
    running = true; clock.start(); clock.getDelta(); raf = requestAnimationFrame(loop);
  }
  function stop() { running = false; if (raf) cancelAnimationFrame(raf); raf = 0; clock.stop(); }

  /* un único observador: pausa el render fuera de pantalla o con la pestaña oculta */
  document.addEventListener("visibilitychange", () => { if (document.visibilityState === "visible") start(); else stop(); });
  if ("IntersectionObserver" in window) new IntersectionObserver((e) => { visible = e[0].isIntersecting; if (visible) start(); else stop(); }).observe(orbit);

  /* ------------------------------------------------------------------ error: sin respaldo -------- */
  function fail(reason) {
    if (window.console) console.error("[hero3d] " + reason + ". No se muestra ningún modelo (no hay respaldo); la landing sigue funcionando.");
    try { stop(); } catch (e) {}
    try { renderer.dispose(); if (canvas.parentNode) canvas.parentNode.removeChild(canvas); } catch (e) {}
    orbit.classList.remove("orbit--loading", "orbit--glb", "has-3d");
    orbit.style.display = "none";
  }

  /* @debug-hook */
})();
