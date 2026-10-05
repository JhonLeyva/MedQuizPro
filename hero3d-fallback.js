/* MedQuizPlus — médico 3D animado del hero (Three.js, WebGL). Si algo falla, quedan los anillos CSS de pro.css.
   Todo se modela con formas simples (estilo arcilla): no necesita descargar modelos ni texturas. */
import * as THREE from "three";
import { RoomEnvironment } from "three/addons/environments/RoomEnvironment.js";

(function () {
  "use strict";
  var orbit = document.querySelector(".hero .orbit");
  if (!orbit) return;

  var reduced = false, fine = false;
  try { reduced = matchMedia("(prefers-reduced-motion: reduce)").matches; } catch (e) {}
  try { fine = matchMedia("(hover: hover) and (pointer: fine)").matches; } catch (e) {}
  var lite = innerWidth < 768 || (navigator.hardwareConcurrency || 4) < 4;

  var renderer;
  try { renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: "high-performance" }); } catch (e) { return; }
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, lite ? 1.5 : 2));
  renderer.setClearColor(0x000000, 0);
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.0;
  renderer.domElement.setAttribute("aria-hidden", "true");

  var scene = new THREE.Scene();
  var pmrem = new THREE.PMREMGenerator(renderer);
  scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture;
  scene.environmentIntensity = 0.55;

  var camera = new THREE.PerspectiveCamera(28, 1, 0.1, 60);
  camera.position.set(0, 0.25, 10.5);
  camera.lookAt(0, 0.15, 0);

  var key = new THREE.DirectionalLight(0xfff1de, 2.4); key.position.set(2.5, 3.5, 4); scene.add(key);
  var rim = new THREE.DirectionalLight(0x2dd4bf, 2.2); rim.position.set(-3.5, 2, -2); scene.add(rim);
  scene.add(new THREE.HemisphereLight(0xffffff, 0x9adfd6, 0.7));

  function mat(color, rough, extra) { return new THREE.MeshStandardMaterial(Object.assign({ color: color, roughness: rough == null ? 0.55 : rough, metalness: 0 }, extra || {})); }
  var M = {
    skin: mat(0xf0c3a0, 0.62), hair: mat(0x4a3225, 0.5), coat: mat(0xf1f4f6, 0.5), scrubs: mat(0x38bdc4, 0.5),
    dark: mat(0x1b2230, 0.35), steth: mat(0x334155, 0.4), silver: new THREE.MeshStandardMaterial({ color: 0xd8e0e8, metalness: 1, roughness: 0.25 }),
    cheek: mat(0xf29b8c, 0.8), white: mat(0xffffff, 0.4), teal: mat(0x2dd4bf, 0.4), iris: mat(0x7a4326, 0.35), coat2: mat(0xdfe5ea, 0.6), mouth: mat(0x6b2230, 0.7), pants: mat(0x4b5563, 0.7),
    glow: new THREE.MeshBasicMaterial({ color: 0x2dd4bf, transparent: true, opacity: 0.14 })
  };
  var seg = lite ? 20 : 36;

  var root = new THREE.Group(); scene.add(root);

  /* disco de luz detrás del médico */
  var disc = new THREE.Mesh(new THREE.CircleGeometry(1.75, 64), M.glow); disc.position.set(0, 0.1, -1.4); root.add(disc);
  var ringBack = new THREE.Mesh(new THREE.TorusGeometry(1.9, 0.015, 8, 96), new THREE.MeshBasicMaterial({ color: 0x2dd4bf, transparent: true, opacity: 0.45 })); ringBack.position.copy(disc.position); root.add(ringBack);

  var body = new THREE.Group(); root.add(body);
  function V(x, y, z) { return new THREE.Vector3(x, y, z); }
  function box(w, h, d, material, x, y, z, parent) { var m = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), material); m.position.set(x, y, z); (parent || body).add(m); return m; }
  function cross(size, material) {
    var g = new THREE.Group();
    g.add(new THREE.Mesh(new THREE.BoxGeometry(size, size * 0.34, size * 0.3), material)); g.add(new THREE.Mesh(new THREE.BoxGeometry(size * 0.34, size, size * 0.3), material)); return g;
  }

  /* torso: bata abierta (gris muy claro) sobre cuello en V azul-verdoso, cinturón y pantalón */
  var prof = [[0, -1.7], [0.7, -1.7], [0.82, -1.45], [0.8, -0.6], [0.72, 0.1], [0.66, 0.5], [0.5, 0.76], [0.28, 0.84], [0, 0.86]].map(function (p) { return new THREE.Vector2(p[0], p[1]); });
  var coat = new THREE.Mesh(new THREE.LatheGeometry(prof, seg), M.coat); coat.scale.z = 0.62; body.add(coat);
  var scrubs = new THREE.Mesh(new THREE.CapsuleGeometry(0.27, 1.45, 8, 20), M.scrubs); scrubs.scale.z = 0.5; scrubs.position.set(0, -0.28, 0.5); body.add(scrubs);
  var vneck = new THREE.Mesh(new THREE.ConeGeometry(0.2, 0.36, 3), M.skin); vneck.rotation.set(Math.PI, 0, Math.PI); vneck.scale.set(1, 1, 0.45); vneck.position.set(0, 0.68, 0.6); body.add(vneck);
  /* solapas */
  [-1, 1].forEach(function (sd) {
    var l = box(0.2, 1.15, 0.05, M.coat, 0.42 * sd, 0.22, 0.52); l.rotation.z = 0.2 * sd; l.rotation.y = -0.15 * sd;
    var c = box(0.22, 0.16, 0.05, M.coat, 0.3 * sd, 0.74, 0.5); c.rotation.z = 0.7 * sd;
  });
  /* credencial y bolsillos */
  box(0.26, 0.15, 0.03, M.white, 0.5, 0.0, 0.62); box(0.12, 0.15, 0.032, M.teal, 0.43, 0.0, 0.62);
  box(0.34, 0.3, 0.03, M.coat2, 0.5, -1.15, 0.54); box(0.34, 0.3, 0.03, M.coat2, -0.5, -1.15, 0.54);
  

  /* cabeza (pivota en el cuello para seguir el mouse) */
  var neck = new THREE.Mesh(new THREE.CylinderGeometry(0.17, 0.2, 0.36, 20), M.skin); neck.position.set(0, 0.98, 0); body.add(neck);
  var head = new THREE.Group(); head.position.set(0, 1.02, 0); body.add(head);
  var skull = new THREE.Mesh(new THREE.SphereGeometry(0.58, seg, seg), M.skin); skull.scale.set(0.98, 1.08, 0.98); skull.position.y = 0.6; head.add(skull);
  /* pelo: casquete + mechones peinados hacia arriba y a un lado */
  var cap = new THREE.Mesh(new THREE.SphereGeometry(0.6, seg, seg, 0, Math.PI * 2, 0, Math.PI * 0.5), M.hair); cap.scale.set(1.0, 1.1, 1.05); cap.position.set(0, 0.64, -0.03); cap.rotation.x = -0.22; head.add(cap);
  [[0.1, 1.27, 0.2, 0.74, 0.3, 0.52, -0.22], [-0.2, 1.2, 0.26, 0.5, 0.26, 0.42, 0.5], [0.38, 1.12, 0.16, 0.4, 0.24, 0.36, -0.9]].forEach(function (t) {
    var m = new THREE.Mesh(new THREE.SphereGeometry(0.2, 18, 16), M.hair); m.position.set(t[0], t[1], t[2]); m.scale.set(t[3] * 1.2, t[4], t[5]); m.rotation.z = t[6]; head.add(m);
  });
  [-1, 1].forEach(function (sd) {
    var ear = new THREE.Mesh(new THREE.SphereGeometry(0.11, 14, 14), M.skin); ear.scale.set(0.55, 1, 0.8); ear.position.set(0.57 * sd, 0.55, 0); head.add(ear);
    var side = new THREE.Mesh(new THREE.SphereGeometry(0.17, 14, 14), M.hair); side.scale.set(0.7, 1.2, 1.1); side.position.set(0.5 * sd, 0.74, -0.06); head.add(side);
  });
  /* ojos grandes y expresivos, cejas gruesas, lentes de pasta */
  var eyes = [];
  [-1, 1].forEach(function (sd) {
    var eyeG = new THREE.Group(); eyeG.position.set(0.2 * sd, 0.62, 0.46); head.add(eyeG); eyes.push(eyeG);
    var sclera = new THREE.Mesh(new THREE.SphereGeometry(0.1, 20, 20), M.white); sclera.scale.set(1, 1.05, 0.6); eyeG.add(sclera);
    var iris = new THREE.Mesh(new THREE.SphereGeometry(0.068, 20, 20), M.iris); iris.scale.set(1, 1, 0.5); iris.position.z = 0.035; eyeG.add(iris);
    var pupil = new THREE.Mesh(new THREE.SphereGeometry(0.036, 14, 14), M.dark); pupil.scale.set(1, 1, 0.5); pupil.position.z = 0.058; eyeG.add(pupil);
    var shine = new THREE.Mesh(new THREE.SphereGeometry(0.017, 8, 8), M.white); shine.position.set(0.02, 0.03, 0.075); eyeG.add(shine);
    var frame = new THREE.Mesh(new THREE.TorusGeometry(0.155, 0.024, 10, 44), M.dark); frame.scale.set(1.12, 0.96, 1); frame.position.set(0.2 * sd, 0.62, 0.55); head.add(frame);
    var brow = new THREE.Mesh(new THREE.CapsuleGeometry(0.022, 0.16, 4, 8), M.hair); brow.rotation.z = Math.PI / 2 + 0.13 * sd; brow.position.set(0.2 * sd, 0.85, 0.56); head.add(brow);
    var cheek = new THREE.Mesh(new THREE.SphereGeometry(0.08, 14, 14), M.cheek); cheek.scale.set(1, 0.6, 0.3); cheek.position.set(0.34 * sd, 0.42, 0.47); head.add(cheek);
  });
  var bridge = new THREE.Mesh(new THREE.CylinderGeometry(0.014, 0.014, 0.1, 6), M.dark); bridge.rotation.z = Math.PI / 2; bridge.position.set(0, 0.64, 0.56); head.add(bridge);
  var nose = new THREE.Mesh(new THREE.SphereGeometry(0.075, 16, 16), M.skin); nose.scale.set(0.95, 1.05, 1.15); nose.position.set(0, 0.5, 0.58); head.add(nose);
  /* sonrisa con dientes */
  var mouth = new THREE.Mesh(new THREE.CircleGeometry(0.15, 28, Math.PI, Math.PI), M.mouth); mouth.position.set(0, 0.4, 0.545); head.add(mouth);
  var teeth = new THREE.Mesh(new THREE.CircleGeometry(0.135, 28, Math.PI + 0.12, Math.PI - 0.24), M.white); teeth.scale.set(1, 0.55, 1); teeth.position.set(0, 0.405, 0.552); head.add(teeth);
  var lip = new THREE.Mesh(new THREE.TorusGeometry(0.15, 0.014, 8, 28, Math.PI), M.cheek); lip.rotation.z = Math.PI; lip.position.set(0, 0.4, 0.55); head.add(lip);

  /* brazos: cada tramo se orienta entre dos puntos (hombro-codo-muñeca) para poder mezclar poses */
  function limb(r, material) {
    var shaft = new THREE.Mesh(new THREE.CylinderGeometry(r, r, 1, 16), material); body.add(shaft);
    return shaft;
  }
  function place(shaft, A, B) {
    var d = new THREE.Vector3().subVectors(B, A), len = d.length();
    shaft.position.copy(A).addScaledVector(d, 0.5); shaft.scale.set(1, len, 1); shaft.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), d.normalize());
  }
  function joint(r, material) { var m = new THREE.Mesh(new THREE.SphereGeometry(r, 16, 16), material); body.add(m); return m; }
  function makeArm(sd) {
    return { sd: sd, up: limb(0.17, M.coat), fo: limb(0.15, M.coat), cuff: limb(0.156, M.coat), sh: joint(0.18, M.coat), el: joint(0.17, M.coat), hand: joint(0.155, M.skin), E: V(), W: V() };
  }
  var armW = makeArm(-1), armC = makeArm(1); /* armW saluda (lado izquierdo, visible); armC queda cruzado */
  var watch = new THREE.Group(); body.add(watch);
  var wcase = new THREE.Mesh(new THREE.CylinderGeometry(0.1, 0.1, 0.05, 24), M.silver); wcase.rotation.x = Math.PI / 2; watch.add(wcase);
  var wface = new THREE.Mesh(new THREE.CircleGeometry(0.08, 24), M.white); wface.position.z = 0.028; watch.add(wface);
  var wband = new THREE.Mesh(new THREE.TorusGeometry(0.13, 0.03, 8, 24), M.dark); wband.rotation.y = Math.PI / 2; wband.visible = false; watch.add(wband);

  var P = {
    crossE: { "-1": V(-0.84, -0.5, 0.3), "1": V(0.84, -0.5, 0.26) },
    crossW: { "-1": V(0.56, -0.42, 0.7), "1": V(-0.6, -0.56, 0.54) },
    upE: { "-1": V(-1.1, 0.5, 0.25), "1": V(1.1, 0.5, 0.25) },
    upW: { "-1": V(-1.02, 1.5, 0.3), "1": V(1.02, 1.5, 0.3) }
  };
  function poseArm(arm, k, w, t) { /* k: 0 = cruzado, 1 = levantado; w = oscilación del saludo */
    var sd = String(arm.sd), S = V(0.62 * arm.sd, 0.52, 0.02);
    arm.E.lerpVectors(P.crossE[sd], P.upE[sd], k);
    arm.W.lerpVectors(P.crossW[sd], P.upW[sd], k); arm.W.x += w * arm.sd * 0.22 * k;
    place(arm.up, S, arm.E); place(arm.fo, arm.E, arm.W);
    var dir = new THREE.Vector3().subVectors(arm.W, arm.E).normalize(), cuffA = arm.W.clone().addScaledVector(dir, -0.22);
    place(arm.cuff, cuffA, arm.W);
    arm.sh.position.copy(S); arm.el.position.copy(arm.E); arm.hand.position.copy(arm.W).addScaledVector(dir, 0.1);
  }
  poseArm(armW, 0, 0, 0); poseArm(armC, 0, 0, 0);

  /* objetos flotantes: cruz, píldora y esfera */
  var floaters = [];
  var fx1 = cross(0.42, M.teal); fx1.position.set(1.65, 1.3, 0.2); root.add(fx1); floaters.push({ o: fx1, y: 1.3, p: 0, s: 0.9 });
  var pill = new THREE.Group();
  var ph1 = new THREE.Mesh(new THREE.CapsuleGeometry(0.1, 0.22, 6, 16), M.white), ph2 = new THREE.Mesh(new THREE.CapsuleGeometry(0.1, 0.22, 6, 16), M.teal);
  ph1.position.y = 0.17; ph2.position.y = -0.17; pill.add(ph1); pill.add(ph2); pill.rotation.z = 0.7; pill.position.set(-1.75, 0.5, 0.3); root.add(pill); floaters.push({ o: pill, y: 0.5, p: 2, s: 1.1 });
  var orb = new THREE.Mesh(new THREE.SphereGeometry(0.13, 20, 20), M.teal); orb.position.set(1.55, -0.3, 0.4); root.add(orb); floaters.push({ o: orb, y: -0.3, p: 4, s: 1.3 });

  /* tamaño del canvas */
  function size() {
    var w = Math.max(orbit.clientWidth, 1), h = Math.max(orbit.clientHeight, 1);
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    camera.position.z = w / h < 0.85 ? 12 : 11.5;
    camera.updateProjectionMatrix();
  }
  var cv = renderer.domElement; cv.className = "orbit__gl"; orbit.appendChild(cv); size();
  if ("ResizeObserver" in window) new ResizeObserver(size).observe(orbit); else addEventListener("resize", size);

  /* estado de animación */
  var tx = 0, ty = 0, hx = 0, hy = 0, visible = true, raf = 0, t0 = performance.now(), cheer = -10, lastBlink = 0, blinkT = -1, waveAmt = 0, cheerAmt = 0;
  if (fine && !reduced) {
    addEventListener("pointermove", function (e) { tx = (e.clientX / innerWidth - 0.5) * 2; ty = (e.clientY / innerHeight - 0.5) * 2; }, { passive: true });
  }
  window.addEventListener("fx:correct", function () { cheer = (performance.now() - t0) / 1000; if (!reduced) kick(); });

  function ease(v, a, k) { return v + (a - v) * k; }

  function frame(now) {
    raf = 0;
    var t = (now - t0) / 1000;
    if (!reduced) {
      /* respiración */
      var br = Math.sin(t * 1.8);
      body.scale.set(1 + br * 0.006, 1 + br * 0.012, 1 + br * 0.006);
      /* brazos cruzados; cada 6 s el brazo izquierdo se descruza y saluda; al acertar, celebra con los dos */
      var cycle = t % 6, wantWave = cycle < 2.4 ? 1 : 0, c = t - cheer, cheering = c >= 0 && c < 1.6;
      waveAmt = ease(waveAmt, wantWave || cheering ? 1 : 0, 0.08);
      cheerAmt = ease(cheerAmt, cheering ? 1 : 0, 0.1);
      poseArm(armW, waveAmt, Math.sin(t * 8), t);
      poseArm(armC, cheerAmt, Math.sin(t * 9), t);
      /* reloj en la muñeca que queda arriba */
      var wp = armW.W.clone().lerp(armW.E, 0.2); watch.position.set(wp.x, wp.y, wp.z + 0.13); watch.rotation.set(0, 0, 0); watch.visible = waveAmt < 0.4;
      /* salto de celebración */
      root.position.y = cheering ? Math.abs(Math.sin(c * 6.4)) * 0.38 * (1 - c / 1.6) : ease(root.position.y, 0, 0.2);
      /* parpadeo */
      if (t - lastBlink > 3.4) { lastBlink = t + Math.random() * 1.2; blinkT = t; }
      var bl = blinkT > 0 ? Math.max(0, 1 - Math.abs((t - blinkT) / 0.08 - 1)) : 0;
      eyes.forEach(function (e) { e.scale.y = 1 - bl * 0.92; });
      /* flotantes */
      floaters.forEach(function (f) { f.o.position.y = f.y + Math.sin(t * f.s + f.p) * 0.12; f.o.rotation.y = t * 0.6 + f.p; });
      ringBack.rotation.z = t * 0.1;
      /* cabeza y cuerpo siguen el mouse */
      hx = ease(hx, tx, 0.06); hy = ease(hy, ty, 0.06);
      head.rotation.y = hx * 0.55; head.rotation.x = hy * 0.3 + Math.sin(t * 1.1) * 0.015; head.rotation.z = hx * -0.05;
      body.rotation.y = hx * 0.18;
    }
    renderer.render(scene, camera);
    if (!reduced && visible && document.visibilityState === "visible") raf = requestAnimationFrame(frame);
  }
  function kick() { if (!raf) raf = requestAnimationFrame(frame); }

  frame(performance.now());
  orbit.classList.add("has-3d");
  if (reduced) { poseArm(armW, 0.9, 0, 0); frame(performance.now()); addEventListener("resize", function () { frame(performance.now()); }); return; }
  if ("IntersectionObserver" in window) new IntersectionObserver(function (e) { visible = e[0].isIntersecting; if (visible) kick(); }).observe(orbit);
  document.addEventListener("visibilitychange", kick);
  kick();
})();
