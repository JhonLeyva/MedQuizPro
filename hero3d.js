/* =====================================================================================================
   MedQuizPlus — médico 3D del Hero (Three.js + GLTFLoader) · Sistema de reposo procedimental ("Procedural Human Idle")

   · Carga ÚNICAMENTE 'Sin_nombre.glb' (con anti-caché). No usa animaciones pregrabadas ni modelos de respaldo.
   · Postura: brazos verticales pegados al torso, palmas hacia los muslos y dedos semi-curvados (se calcula sobre los huesos Mixamo).
   · Reposo vivo: respiración torácica/clavicular, balanceo de peso entre los pies, micro-movimiento de los dedos y
     un gesto de mano ocasional (cada 6–10 s, aleatorio).
   · Parpadeo: motor listo para morph targets / nodos de párpado. Este modelo NO los tiene, así que no parpadea (ver README del mensaje).
   · Mirada: cuello y cabeza siguen el cursor (lerp 0.04) con límites fisiológicos ±22° (yaw) y ±12° (pitch).
   · Materiales opacos y mates; luz direccional a 45° con sombras de 2048 px + luz hemisférica de relleno.
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
   CONFIGURACIÓN — todo lo ajustable está aquí.  Ángulos en grados (…Deg) o radianes (rad).
   Unidades de escena: el médico completo mide ~3,4.  rotationY negativo = se gira hacia la IZQUIERDA (hacia el texto).
   ===================================================================================================== */
const CONFIG = {
  modelPath: "./Sin_nombre.glb",       // único modelo
  cacheBust: true,                     // true → '?v=' + Date.now()  ·  "texto" → versión fija ('?v=texto', permite caché)  ·  false → sin parámetro
  baseHeight: 3.4,

  breakpoints: { mobileMax: 767.98, tabletMax: 1279.98 },

  /* escala y posición por dispositivo. scale > 1 agranda · positionY > 0 sube · positionX > 0 mueve a la derecha */
  desktop: { scale: 1.0,  positionX: 0, positionY: 0.12, positionZ: 0, rotationY: -0.28, rotationX: 0 },
  tablet:  { scale: 0.95, positionX: 0, positionY: 0.04, positionZ: 0, rotationY: -0.14, rotationX: 0 },
  mobile:  { scale: 0.9,  positionX: 0, positionY: 0,    positionZ: 0, rotationY: 0,     rotationX: 0 },

  /* 1 · POSTURA BASE (Rigging Alignment) */
  pose: {
    shoulderDropDeg: 5,                // clavículas algo caídas
    armGapDeg: 5,                      // separación del brazo respecto a la vertical (0 = pegado al torso)
    forearmBendDeg: 9,                 // flexión del codo hacia delante
    wristBendDeg: 5,                   // flexión de la muñeca hacia delante
    palmTargetForward: 0.12,           // 0 = palmas exactamente hacia los muslos · >0 = ligeramente hacia delante
    fingerClose: 0.9,                  // 0..1 cierra el "abanico": alinea índice, anular y meñique con el dedo medio
    fingerCurlDeg:  [18, 26, 20],      // curvatura en reposo de las 3 falanges (hacia la palma)
    thumbCurlDeg:   [22, 24, 16]
  },

  /* 2 · RESPIRACIÓN Y BALANCEO DE PESO (t = tiempo acumulado en segundos) */
  breathing: {
    speed: 1.2,
    chestPitch: 0.02,                  // Chest.rotation.x = sin(t·1.2)·0.02  (expansión torácica)
    bodyBob: 0.003,                    // position.y += sin(t·1.2)·0.003
    shoulderLift: 0.015                // elevación clavicular
  },
  sway: {
    speed: 0.4,
    shiftX: 0.002,                     // position.x += sin(t·0.4)·0.002  (peso de un pie a otro)
    pelvisRoll: 0.012,                 // inclinación pélvica (rad)
    spineRoll: 0.008,                  // contra-inclinación espinal, desfasada
    spinePhase: 0.9
  },

  /* 3 · MANOS Y DEDOS */
  fingers: {
    idleAmp: 0.04,                     // finger = base + sin(t·0.8 + offset)·0.04
    idleSpeed: 0.8,
    grip: { minGap: 6, maxGap: 10, minDur: 1.4, maxDur: 2.2, extraDeg: [16, 24, 18] }   // gesto aleatorio: cerrar la mano y volver
  },

  /* 4 · PARPADEO (solo si el modelo trae morph targets o nodos de párpado) */
  blink: {
    minGap: 2.5, maxGap: 5.0,          // segundos entre parpadeos
    duration: 0.15,                    // 0 → 1 → 0 en ~150 ms
    doubleChance: 0.15,
    morphNames: /blink|eyesclosed|eyeclose/i,
    nodeNames: /eyelid|lid|blink/i
  },

  /* 5 · SEGUIMIENTO DEL CURSOR (coordenadas normalizadas −1..1) */
  tracking: {
    maxYawDeg: 22,
    maxPitchDeg: 12,
    neckShare: 0.4,                    // reparto del giro: 40 % cuello · 60 % cabeza
    lerp: 0.04,                        // masa del cráneo: menor = más pesado
    mass: 0.10,                        // segunda etapa de suavizado (elimina tirones del ratón)
    restLookAtUser: 0.6,               // en reposo la cabeza compensa el giro del cuerpo y mira al usuario
    idleGaze: 0.04,
    bodyFollow: 0.03,
    parallax: { desktop: 0.03, tablet: 0.015, mobile: 0 },
    touch: false
  },

  /* 6 · MATERIALES Y LUCES (PBR) */
  materials: { roughness: 0.68, metalness: 0.05, sharpenTextures: true },
  lights: {
    key: 1.2,                          // DirectionalLight a 45° (elevación y azimut)
    keyPosition: [3.5, 4.95, 3.5],
    fill: 0.6,                         // HemisphereLight: relleno para pliegues de la ropa y tonos de piel
    shadows: true,
    shadowMapSize: 2048,               // sombras de alta definición
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
  const rand = (a, b) => a + Math.random() * (b - a);
  const smooth = (x) => { x = clamp(x, 0, 1); return x * x * (3 - 2 * x); };

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
  /* Three.js usa luces físicas: 1.0 equivale a ~0.32 de brillo. Se multiplica por π para que 1.2 / 0.6 se comporten como valores "clásicos" */
  scene.add(new THREE.HemisphereLight(0xffffff, 0xb8c4c9, L.fill * Math.PI));
  const key = new THREE.DirectionalLight(0xfff6ec, L.key * Math.PI);
  key.position.fromArray(L.keyPosition); scene.add(key);
  if (L.shadows) {
    renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFSoftShadowMap;
    key.castShadow = true; key.shadow.mapSize.set(L.shadowMapSize, L.shadowMapSize);
    key.shadow.radius = L.shadowSoftness; key.shadow.bias = -0.0003; key.shadow.normalBias = 0.02;
    const sc = key.shadow.camera; sc.left = -2.4; sc.right = 2.4; sc.top = 2.4; sc.bottom = -2.4; sc.near = 0.5; sc.far = 20; sc.updateProjectionMatrix();
  }
  const camera = new THREE.PerspectiveCamera(26, 1, 0.1, 80);
  camera.position.set(0, 0, 10.5);

  /* jerarquía: scene → anchor (posición / escala / respiración / balanceo) → group (giro) → model */
  const anchor = new THREE.Group(), group = new THREE.Group();
  anchor.add(group); scene.add(anchor);

  /* ------------------------------------------------------------------ estado --------------------- */
  let model = null, ready = false, running = false, visible = true;
  let raf = 0, elapsed = 0, hop = -10, widthRatio = 0.5, restYaw = 0;
  const clock = new THREE.Clock(false);
  const P = { device: "desktop", cfg: CONFIG.desktop, parallax: 0 };
  const aim = { x: 0, y: 0 }, s1 = { x: 0, y: 0 }, s2 = { x: 0, y: 0 };   // cursor objetivo + suavizado en dos etapas
  const gaze = { yaw: 0, pitch: 0 };                                       // último ángulo aplicado (depuración)
  const bone = {};                                                         // hips, spine1, spine2, shL, shR, neck, head
  const fingerBones = [];                                                  // { b, base, axisP, side, finger, joint, offset }
  const blinkState = { morphs: [], nodes: [], next: 0, start: -1, queued: false };
  const gripState = { next: 0, side: 0, start: -1, dur: 1.8 };
  const AX_X = new THREE.Vector3(1, 0, 0), AX_Y = new THREE.Vector3(0, 1, 0), AX_Z = new THREE.Vector3(0, 0, 1);
  const axP = new THREE.Vector3();
  const qd = new THREE.Quaternion(), qa = new THREE.Quaternion(), qb = new THREE.Quaternion(), qp = new THREE.Quaternion(), ql = new THREE.Quaternion();
  const v0 = new THREE.Vector3(), v1 = new THREE.Vector3(), v2 = new THREE.Vector3();

  orbit.classList.add("has-3d", "orbit--glb", "orbit--loading");           // el espacio queda reservado: sin saltos de diseño
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
      model.traverse((child) => {
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

      alignRig();                                                  // 1 · postura base: brazos, palmas y dedos
      findBones();
      setupBlink();                                                // 4 · parpadeo (si hay morph targets / nodos)
      gripState.next = rand(CONFIG.fingers.grip.minGap, CONFIG.fingers.grip.maxGap);
      blinkState.next = rand(CONFIG.blink.minGap, CONFIG.blink.maxGap);

      const box = extents(), size = box.getSize(new THREE.Vector3()), c = box.getCenter(new THREE.Vector3());
      const k = CONFIG.baseHeight / Math.max(size.y, 1e-4);        // escala base y centrado del cuerpo en el origen
      model.scale.multiplyScalar(k);
      model.position.set(-c.x * k, -c.y * k, -c.z * k);
      widthRatio = clamp((size.x / Math.max(size.y, 1e-4)) * 1.15, 0.35, 1.2);
      applyResponsive();
      model.updateMatrixWorld(true);

      ready = true;
      orbit.classList.remove("orbit--loading");
      orbit.setAttribute("data-3d", "ready");
      frame(0);
      if (!reduced) start();
    } catch (err) { fail(String(err)); }
  }

  /* ================================================================== 1 · RIGGING ALIGNMENT ===== */
  const boneByName = (n) => model.getObjectByName("mixamorig" + n) || model.getObjectByName("mixamorig:" + n) || model.getObjectByName(n) || null;
  const wpos = (b, out) => b.getWorldPosition(out);

  /* rotación PERMANENTE de un hueso con un cuaternión expresado en ejes del mundo */
  function rotateQ(b, qW) {
    b.parent.updateWorldMatrix(true, false); b.parent.getWorldQuaternion(qp);
    ql.copy(qp).invert().multiply(qW).multiply(qp);
    b.quaternion.premultiply(ql);
    b.updateWorldMatrix(true, true);
  }
  const rotateAxis = (b, axis, angle) => { if (b && b.parent && angle) rotateQ(b, qd.setFromAxisAngle(axis, angle)); };
  /* rota el hueso b para que el segmento b→child apunte hacia la dirección dir (mundo) */
  function aimBone(b, child, dir) {
    if (!b || !child) return;
    b.updateWorldMatrix(true, true);
    wpos(b, v0); wpos(child, v1); v1.sub(v0).normalize();
    rotateQ(b, qb.setFromUnitVectors(v1, dir.clone().normalize()));
  }
  function segDir(b, child, out) { b.updateWorldMatrix(true, true); wpos(b, v0); wpos(child, out); return out.sub(v0).normalize(); }

  function alignRig() {
    const Z = CONFIG.pose;
    model.updateMatrixWorld(true);
    const sides = [{ n: "Left", s: 1 }, { n: "Right", s: -1 }];       // el lado "Left" del personaje está en +X
    const rig = sides.map((S) => {
      const o = { s: S.s, name: S.n };
      ["Shoulder", "Arm", "ForeArm", "Hand"].forEach((k) => { o[k] = boneByName(S.n + k); });
      o.fingers = ["Thumb", "Index", "Middle", "Ring", "Pinky"].map((f) => [1, 2, 3, 4].map((j) => boneByName(S.n + "Hand" + f + j)));
      return o;
    });

    /* normal de la palma en coordenadas del hueso de la mano (se mide ANTES de mover nada; en la pose inicial las palmas miran hacia delante, +Z) */
    rig.forEach((o) => {
      if (!o.Hand || !o.fingers[2][0] || !o.fingers[1][0] || !o.fingers[4][0]) return;
      wpos(o.Hand, v0); wpos(o.fingers[2][0], v1); wpos(o.fingers[1][0], v2);
      const dir = v1.clone().sub(v0).normalize(), lat = wpos(o.fingers[4][0], new THREE.Vector3()).sub(v2);
      const n = dir.clone().cross(lat).normalize(); if (n.z < 0) n.negate();
      o.nLocal = n.applyQuaternion(o.Hand.getWorldQuaternion(new THREE.Quaternion()).invert());
    });

    rig.forEach((o) => {
      const s = o.s;
      rotateAxis(o.Shoulder, AX_Z, -s * Z.shoulderDropDeg * DEG);                                     // clavícula caída
      const ga = Z.armGapDeg * DEG, fb = Z.forearmBendDeg * DEG, wb = Z.wristBendDeg * DEG;
      aimBone(o.Arm, o.ForeArm, new THREE.Vector3(s * Math.sin(ga), -Math.cos(ga), 0.02));            // brazo: vertical, pegado al torso
      aimBone(o.ForeArm, o.Hand, new THREE.Vector3(s * Math.sin(ga * 0.5), -Math.cos(fb), Math.sin(fb)));   // antebrazo: vertical con codo suave
      aimBone(o.Hand, o.fingers[2][0], new THREE.Vector3(s * Math.sin(ga * 0.3), -Math.cos(wb + fb), Math.sin(wb + fb)));   // muñeca recta

      /* palmas hacia los muslos: se gira el antebrazo sobre su eje hasta que la normal de la palma apunte hacia el cuerpo */
      if (o.nLocal && o.ForeArm && o.Hand) {
        const axis = segDir(o.ForeArm, o.Hand, new THREE.Vector3());
        const nW = o.nLocal.clone().applyQuaternion(o.Hand.getWorldQuaternion(new THREE.Quaternion()));
        const target = new THREE.Vector3(-s, 0, Z.palmTargetForward).normalize();
        const pn = nW.clone().sub(axis.clone().multiplyScalar(nW.dot(axis))).normalize();
        const pt = target.clone().sub(axis.clone().multiplyScalar(target.dot(axis))).normalize();
        rotateAxis(o.ForeArm, axis, Math.atan2(pn.clone().cross(pt).dot(axis), pn.dot(pt)));
      }
    });

    /* dedos: se junta el "abanico" y se curvan las falanges hacia dentro */
    rig.forEach((o) => {
      if (!o.nLocal || !o.Hand) return;
      const nW = o.nLocal.clone().applyQuaternion(o.Hand.getWorldQuaternion(new THREE.Quaternion())).normalize();
      const mid = o.fingers[2];
      if (mid[0] && mid[1]) {
        const dm = segDir(mid[0], mid[1], new THREE.Vector3());
        [1, 3, 4].forEach((fi) => {                                                                 // índice, anular, meñique → paralelos al medio
          const f = o.fingers[fi]; if (!f[0] || !f[1]) return;
          const df = segDir(f[0], f[1], new THREE.Vector3());
          const pf = df.clone().sub(nW.clone().multiplyScalar(df.dot(nW))).normalize(), pm = dm.clone().sub(nW.clone().multiplyScalar(dm.dot(nW))).normalize();
          rotateAxis(f[0], nW, Math.atan2(pf.clone().cross(pm).dot(nW), pf.dot(pm)) * Z.fingerClose);
        });
      }
      o.fingers.forEach((f, fi) => {                                                                // curvatura en reposo (proximal → distal)
        const curl = fi === 0 ? Z.thumbCurlDeg : Z.fingerCurlDeg;
        for (let j = 0; j < 3; j++) {
          if (!f[j] || !f[j + 1]) continue;
          const d = segDir(f[j], f[j + 1], new THREE.Vector3());
          rotateAxis(f[j], d.clone().cross(nW).normalize(), curl[j] * DEG);
        }
      });
      /* se guarda la rotación final y el eje de curvatura (en el espacio del hueso padre) para la animación de los dedos */
      o.fingers.forEach((f, fi) => {
        for (let j = 0; j < 3; j++) {
          if (!f[j] || !f[j + 1]) continue;
          const d = segDir(f[j], f[j + 1], new THREE.Vector3());
          const axisW = d.clone().cross(nW).normalize();
          f[j].parent.updateWorldMatrix(true, false); f[j].parent.getWorldQuaternion(qp);
          fingerBones.push({ b: f[j], base: f[j].quaternion.clone(), axisP: axisW.applyQuaternion(qp.clone().invert()), side: o.s > 0 ? 0 : 1, finger: fi, joint: j, offset: fi * 0.7 + j * 0.35 + (o.s > 0 ? 0 : 1.9) });
        }
      });
    });
    model.updateMatrixWorld(true);

    if (window.console) {                                                                           // comprobación: ángulo de cada brazo respecto a la vertical
      const ang = rig.map((o) => { if (!o.Arm || !o.ForeArm || !o.Hand) return "?"; const a = segDir(o.Arm, o.ForeArm, new THREE.Vector3()), f = segDir(o.ForeArm, o.Hand, new THREE.Vector3()); return o.name + ": brazo " + (Math.acos(-a.y) / DEG).toFixed(1) + "°, antebrazo " + (Math.acos(-f.y) / DEG).toFixed(1) + "° de la vertical"; });
      console.info("[hero3d] postura base → " + ang.join(" · ") + " · dedos animados: " + fingerBones.length);
    }
  }

  function findBones() {
    bone.hips = boneByName("Hips"); bone.spine1 = boneByName("Spine1"); bone.spine2 = boneByName("Spine2");
    bone.shL = boneByName("LeftShoulder"); bone.shR = boneByName("RightShoulder"); bone.neck = boneByName("Neck"); bone.head = boneByName("Head");
    ["hips", "spine1", "spine2", "shL", "shR", "neck", "head"].forEach((k) => { if (bone[k]) bone[k].userData.base = bone[k].quaternion.clone(); });
    if (!bone.head && window.console) console.warn("[hero3d] sin hueso Head: el seguimiento se aplica al grupo completo");
  }

  function extents() {                                             // caja medida con los huesos (con mallas con piel Three.js subestima el tamaño)
    const box = new THREE.Box3(), v = new THREE.Vector3();
    model.updateMatrixWorld(true);
    model.traverse((o) => { if (o.isBone) { o.getWorldPosition(v); box.expandByPoint(v); } });
    return box.isEmpty() ? box.setFromObject(model) : box;
  }

  /* vuelve a la rotación base del hueso y le suma un giro en ejes del MUNDO (yaw sobre Y · pitch sobre el eje lateral del cuerpo · roll sobre Z) */
  function turnBone(b, yaw, pitch, roll) {
    if (!b || !b.parent) return;
    b.quaternion.copy(b.userData.base);
    if (!yaw && !pitch && !roll) return;
    qa.setFromAxisAngle(AX_Y, yaw); qb.setFromAxisAngle(axP, pitch); qd.copy(qa).multiply(qb);
    if (roll) { qa.setFromAxisAngle(AX_Z, roll); qd.multiply(qa); }
    b.parent.getWorldQuaternion(qp);
    ql.copy(qp).invert().multiply(qd).multiply(qp);
    b.quaternion.premultiply(ql);
  }

  /* ================================================================== 4 · PARPADEO ============= */
  function setupBlink() {
    const Bk = CONFIG.blink;
    model.traverse((o) => {
      if (o.isMesh && o.morphTargetDictionary) Object.keys(o.morphTargetDictionary).forEach((name) => { if (Bk.morphNames.test(name)) blinkState.morphs.push({ mesh: o, idx: o.morphTargetDictionary[name] }); });
      else if (o.name && Bk.nodeNames.test(o.name) && !o.isBone) blinkState.nodes.push({ node: o, sy: o.scale.y });
    });
    if (window.console) console.info(blinkState.morphs.length || blinkState.nodes.length ? "[hero3d] parpadeo: " + blinkState.morphs.length + " morph targets, " + blinkState.nodes.length + " nodos de párpado" : "[hero3d] parpadeo: este modelo no tiene morph targets ni nodos de párpado, no se puede parpadear");
  }
  function updateBlink(t) {
    if (!blinkState.morphs.length && !blinkState.nodes.length) return;
    const Bk = CONFIG.blink;
    if (blinkState.start < 0 && t >= blinkState.next) { blinkState.start = t; blinkState.queued = Math.random() < Bk.doubleChance; }   // 15 % de doble parpadeo
    let v = 0;
    if (blinkState.start >= 0) {
      const u = (t - blinkState.start) / Bk.duration;
      if (u >= 1) {
        if (blinkState.queued) { blinkState.queued = false; blinkState.start = t + 0.11; }          // segundo parpadeo seguido
        else { blinkState.start = -1; blinkState.next = t + rand(Bk.minGap, Bk.maxGap); }
      } else if (u >= 0) v = Math.sin(u * Math.PI);                                                  // 0 → 1 → 0 en ~150 ms
    }
    blinkState.morphs.forEach((m) => { m.mesh.morphTargetInfluences[m.idx] = v; });
    blinkState.nodes.forEach((n) => { n.node.scale.y = n.sy * (1 - 0.92 * v); });
  }

  /* ================================================================== responsive =============== */
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

  /* ================================================================== 5 · CURSOR ================ */
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

  /* ================================================================== bucle de render =========== */
  function frame(dt) {
    elapsed += dt;
    const t = elapsed, live = !reduced;
    const T = CONFIG.tracking, Br = CONFIG.breathing, Sw = CONFIG.sway, Fg = CONFIG.fingers;

    /* cursor → suavizado en dos etapas: lerp con inercia 0.04 (masa del cráneo) + segunda etapa */
    const k1 = lerpK(T.lerp, dt), k2 = lerpK(T.mass, dt);
    s1.x = THREE.MathUtils.lerp(s1.x, aim.x, k1); s1.y = THREE.MathUtils.lerp(s1.y, aim.y, k1);
    s2.x = THREE.MathUtils.lerp(s2.x, s1.x, k2);  s2.y = THREE.MathUtils.lerp(s2.y, s1.y, k2);

    /* 2 · respiración y balanceo: funciones del tiempo acumulado */
    const br = live ? Math.sin(t * Br.speed) : 0, sw = live ? Math.sin(t * Sw.speed) : 0;
    const h = t - hop;
    const jump = live && h >= 0 && h < 0.9 ? Math.abs(Math.sin(h * 3.5)) * 0.25 * (1 - h / 0.9) : 0;
    const nod = live && h >= 0 && h < 0.7 ? Math.sin(h / 0.7 * Math.PI) * 0.22 : 0;

    group.rotation.set(P.cfg.rotationX + s2.y * T.bodyFollow * 0.5, P.cfg.rotationY + s2.x * T.bodyFollow, 0);
    anchor.position.set(
      P.cfg.positionX + s2.x * P.parallax + sw * Sw.shiftX,                     // traslación de peso entre los pies
      P.cfg.positionY - s2.y * P.parallax + br * Br.bodyBob + jump,             // micro-movimiento vertical de la respiración
      P.cfg.positionZ);

    /* mirada: yaw ±22° · pitch ±12°. Sin cursor, deriva mínima y mira al usuario */
    const maxYaw = T.maxYawDeg * DEG, maxPitch = T.maxPitchDeg * DEG;
    const gx = s2.x + (live ? Math.sin(t * 0.45) * T.idleGaze : 0), gy = s2.y + (live ? Math.cos(t * 0.33) * T.idleGaze * 0.7 : 0);
    const yaw = clamp(restYaw + gx * (gx < 0 ? maxYaw + restYaw : maxYaw - restYaw), -maxYaw, maxYaw);
    const pitch = clamp(gy * maxPitch, -maxPitch, maxPitch);
    gaze.yaw = yaw; gaze.pitch = pitch;

    axP.set(Math.cos(group.rotation.y), 0, -Math.sin(group.rotation.y));        // eje lateral del cuerpo (para inclinar y asentir)
    if (bone.head) {
      turnBone(bone.hips, 0, 0, sw * Sw.pelvisRoll);                           // inclinación pélvica
      turnBone(bone.spine1, 0, 0, -sw * Sw.pelvisRoll * 0.7 + Math.sin(t * Sw.speed + Sw.spinePhase) * Sw.spineRoll);   // contra-inclinación espinal desfasada
      turnBone(bone.spine2, 0, br * Br.chestPitch, 0);                          // Chest.rotation.x = sin(t·1.2)·0.02
      turnBone(bone.shL, 0, 0, br * Br.shoulderLift);                           // elevación clavicular
      turnBone(bone.shR, 0, 0, -br * Br.shoulderLift);
      turnBone(bone.neck, yaw * T.neckShare, pitch * T.neckShare, 0);
      turnBone(bone.head, yaw * (1 - T.neckShare), pitch * (1 - T.neckShare) + nod, 0);
    } else {                                                                    // sin huesos: se mueve el grupo completo con los mismos límites
      group.rotation.y += yaw; group.rotation.x += pitch;
    }

    /* 3 · dedos: sub-ciclo armónico + gesto aleatorio de mano cada 6–10 s */
    if (live && fingerBones.length) {
      if (gripState.start < 0 && t >= gripState.next) { gripState.start = t; gripState.side = Math.random() < 0.5 ? 0 : 1; gripState.dur = rand(Fg.grip.minDur, Fg.grip.maxDur); }
      let grip = 0;
      if (gripState.start >= 0) {
        const u = (t - gripState.start) / gripState.dur;
        if (u >= 1) { gripState.start = -1; gripState.next = t + rand(Fg.grip.minGap, Fg.grip.maxGap); }
        else grip = smooth(u < 0.35 ? u / 0.35 : 1 - (u - 0.35) / 0.65);          // cierra la mano y vuelve al reposo
      }
      for (let i = 0; i < fingerBones.length; i++) {
        const f = fingerBones[i];
        const ang = Math.sin(t * Fg.idleSpeed + f.offset) * Fg.idleAmp + (f.side === gripState.side ? grip * Fg.grip.extraDeg[f.joint] * DEG * (f.finger === 0 ? 0.6 : 1) : 0);
        f.b.quaternion.copy(f.base).premultiply(qd.setFromAxisAngle(f.axisP, ang));
      }
    }

    updateBlink(t);
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

  /* ================================================================== error: sin respaldo ======= */
  function fail(reason) {
    if (window.console) console.error("[hero3d] " + reason + ". No se muestra ningún modelo (no hay respaldo); la landing sigue funcionando.");
    try { stop(); } catch (e) {}
    try { renderer.dispose(); if (canvas.parentNode) canvas.parentNode.removeChild(canvas); } catch (e) {}
    orbit.classList.remove("orbit--loading", "orbit--glb", "has-3d");
    orbit.style.display = "none";
  }

  /* @debug-hook */
})();
