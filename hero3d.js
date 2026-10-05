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
    skin: mat(0xf0c3a0, 0.62), hair: mat(0x2b1d18, 0.5), coat: mat(0xf8fcfb, 0.5), scrubs: mat(0x14b8a6, 0.5),
    dark: mat(0x1b2230, 0.35), steth: mat(0x334155, 0.4), silver: new THREE.MeshStandardMaterial({ color: 0xd8e0e8, metalness: 1, roughness: 0.25 }),
    cheek: mat(0xf29b8c, 0.8), white: mat(0xffffff, 0.4), teal: mat(0x2dd4bf, 0.4),
    glow: new THREE.MeshBasicMaterial({ color: 0x2dd4bf, transparent: true, opacity: 0.14 })
  };
  var seg = lite ? 20 : 36;

  var root = new THREE.Group(); scene.add(root);

  /* disco de luz detrás del médico */
  var disc = new THREE.Mesh(new THREE.CircleGeometry(1.75, 64), M.glow); disc.position.set(0, 0.1, -1.4); root.add(disc);
  var ringBack = new THREE.Mesh(new THREE.TorusGeometry(1.9, 0.015, 8, 96), new THREE.MeshBasicMaterial({ color: 0x2dd4bf, transparent: true, opacity: 0.45 })); ringBack.position.copy(disc.position); root.add(ringBack);

  var body = new THREE.Group(); root.add(body);

  /* bata (superficie de revolución aplanada) */
  var prof = [[0, -1.65], [0.78, -1.65], [0.97, -1.4], [0.93, -0.6], [0.8, 0.15], [0.74, 0.55], [0.55, 0.8], [0.3, 0.88], [0, 0.9]].map(function (p) { return new THREE.Vector2(p[0], p[1]); });
  var coat = new THREE.Mesh(new THREE.LatheGeometry(prof, seg), M.coat); coat.scale.z = 0.72; body.add(coat);
  var chest = new THREE.Mesh(new THREE.SphereGeometry(1, seg, 16), M.scrubs); chest.scale.set(0.3, 0.62, 0.16); chest.position.set(0, 0.12, 0.54); body.add(chest);
  function cross(size, material) {
    var g = new THREE.Group(), a = new THREE.BoxGeometry(size, size * 0.34, size * 0.3), b = new THREE.BoxGeometry(size * 0.34, size, size * 0.3);
    g.add(new THREE.Mesh(a, material)); g.add(new THREE.Mesh(b, material)); return g;
  }
  var badge = cross(0.2, M.teal); badge.position.set(-0.46, 0.16, 0.57); body.add(badge);
  var pocket = new THREE.Mesh(new THREE.BoxGeometry(0.3, 0.26, 0.04), M.coat); pocket.position.set(0.47, -0.42, 0.63); body.add(pocket);
  var pen = new THREE.Mesh(new THREE.CylinderGeometry(0.018, 0.018, 0.2, 8), M.teal); pen.position.set(0.52, -0.27, 0.66); body.add(pen);

  /* estetoscopio */
  function tube(points) { return new THREE.Mesh(new THREE.TubeGeometry(new THREE.CatmullRomCurve3(points), 40, 0.034, 8, false), M.steth); }
  body.add(tube([new THREE.Vector3(-0.36, 0.86, 0.12), new THREE.Vector3(-0.38, 0.45, 0.46), new THREE.Vector3(-0.1, -0.05, 0.62), new THREE.Vector3(0.18, -0.12, 0.64)]));
  body.add(tube([new THREE.Vector3(0.36, 0.86, 0.12), new THREE.Vector3(0.38, 0.45, 0.46), new THREE.Vector3(0.28, 0.0, 0.62), new THREE.Vector3(0.18, -0.12, 0.64)]));
  var piece = new THREE.Mesh(new THREE.CylinderGeometry(0.11, 0.11, 0.05, 24), M.silver); piece.rotation.x = Math.PI / 2; piece.position.set(0.18, -0.14, 0.66); body.add(piece);

  /* cabeza (pivota en el cuello para seguir el mouse) */
  var neck = new THREE.Mesh(new THREE.CylinderGeometry(0.17, 0.2, 0.34, 20), M.skin); neck.position.set(0, 0.98, 0); body.add(neck);
  var head = new THREE.Group(); head.position.set(0, 1.0, 0); body.add(head);
  var skull = new THREE.Mesh(new THREE.SphereGeometry(0.54, seg, seg), M.skin); skull.scale.set(1, 1.06, 0.98); skull.position.y = 0.58; head.add(skull);
  var cap = new THREE.Mesh(new THREE.SphereGeometry(0.565, seg, seg, 0, Math.PI * 2, 0, Math.PI * 0.52), M.hair); cap.scale.set(1, 1.08, 1.02); cap.position.set(0, 0.62, -0.02); cap.rotation.x = -0.28; head.add(cap);
  var fringe = new THREE.Mesh(new THREE.SphereGeometry(0.2, 20, 16), M.hair); fringe.scale.set(1.6, 0.7, 0.8); fringe.position.set(0.12, 1.0, 0.36); head.add(fringe);
  [-1, 1].forEach(function (s) { var ear = new THREE.Mesh(new THREE.SphereGeometry(0.1, 14, 14), M.skin); ear.scale.set(0.6, 1, 0.8); ear.position.set(0.55 * s, 0.56, 0); head.add(ear); });
  var eyes = [];
  [-1, 1].forEach(function (s) {
    var eye = new THREE.Mesh(new THREE.SphereGeometry(0.058, 16, 16), M.dark); eye.position.set(0.19 * s, 0.6, 0.5); head.add(eye); eyes.push(eye);
    var shine = new THREE.Mesh(new THREE.SphereGeometry(0.016, 8, 8), M.white); shine.position.set(0.012, 0.02, 0.05); eye.add(shine);
    var glass = new THREE.Mesh(new THREE.TorusGeometry(0.135, 0.016, 10, 40), M.dark); glass.position.set(0.19 * s, 0.6, 0.52); head.add(glass);
    var cheek = new THREE.Mesh(new THREE.SphereGeometry(0.075, 14, 14), M.cheek); cheek.scale.set(1, 0.6, 0.3); cheek.position.set(0.3 * s, 0.44, 0.46); head.add(cheek);
    var brow = new THREE.Mesh(new THREE.CapsuleGeometry(0.012, 0.13, 4, 8), M.hair); brow.rotation.z = Math.PI / 2 + 0.12 * s; brow.position.set(0.19 * s, 0.76, 0.5); head.add(brow);
  });
  var bridge = new THREE.Mesh(new THREE.CylinderGeometry(0.012, 0.012, 0.1, 6), M.dark); bridge.rotation.z = Math.PI / 2; bridge.position.set(0, 0.62, 0.53); head.add(bridge);
  var nose = new THREE.Mesh(new THREE.SphereGeometry(0.055, 14, 14), M.skin); nose.scale.set(0.9, 1, 1.1); nose.position.set(0, 0.5, 0.55); head.add(nose);
  var smile = new THREE.Mesh(new THREE.TorusGeometry(0.13, 0.017, 8, 24, Math.PI), M.cheek); smile.rotation.z = Math.PI; smile.position.set(0, 0.4, 0.52); head.add(smile);

  /* brazos: hombro -> codo; la mano derecha saluda, la izquierda sostiene un portapapeles */
  function arm(side) {
    var shoulder = new THREE.Group(); shoulder.position.set(0.95 * side, 0.6, 0); body.add(shoulder);
    var upper = new THREE.Mesh(new THREE.CapsuleGeometry(0.17, 0.5, 6, 16), M.coat); upper.position.y = -0.34; shoulder.add(upper);
    var elbow = new THREE.Group(); elbow.position.y = -0.66; shoulder.add(elbow);
    var fore = new THREE.Mesh(new THREE.CapsuleGeometry(0.145, 0.42, 6, 16), M.coat); fore.position.y = -0.28; elbow.add(fore);
    var cuff = new THREE.Mesh(new THREE.CylinderGeometry(0.15, 0.15, 0.09, 20), M.scrubs); cuff.position.y = -0.58; elbow.add(cuff);
    var hand = new THREE.Mesh(new THREE.SphereGeometry(0.15, 20, 20), M.skin); hand.position.y = -0.7; elbow.add(hand);
    return { shoulder: shoulder, elbow: elbow };
  }
  var armR = arm(-1), armL = arm(1); /* armR = brazo que saluda (lado izquierdo, visible); armL = sostiene el portapapeles */
  var board = new THREE.Group(); board.position.set(0.06, -0.78, 0.16); board.rotation.set(-0.1, 0.1, 0.06); armL.elbow.add(board);
  board.add(new THREE.Mesh(new THREE.BoxGeometry(0.54, 0.7, 0.05), M.teal));
  var paper = new THREE.Mesh(new THREE.BoxGeometry(0.46, 0.6, 0.02), M.white); paper.position.z = 0.03; board.add(paper);
  for (var l = 0; l < 4; l++) { var line = new THREE.Mesh(new THREE.BoxGeometry(0.32, 0.025, 0.01), M.teal); line.position.set(-0.04, 0.2 - l * 0.12, 0.045); board.add(line); }
  var clip = new THREE.Mesh(new THREE.BoxGeometry(0.2, 0.07, 0.07), M.silver); clip.position.set(0, 0.33, 0.04); board.add(clip);

  /* objetos flotantes: cruz, píldora y corazón de latido */
  var floaters = [];
  var fx1 = cross(0.42, M.teal); fx1.position.set(1.65, 1.3, 0.2); root.add(fx1); floaters.push({ o: fx1, y: 1.3, p: 0, s: 0.9 });
  var pill = new THREE.Group();
  var ph1 = new THREE.Mesh(new THREE.CapsuleGeometry(0.1, 0.22, 6, 16), M.white), ph2 = new THREE.Mesh(new THREE.CapsuleGeometry(0.1, 0.22, 6, 16), M.teal);
  ph1.position.y = 0.17; ph2.position.y = -0.17; pill.add(ph1); pill.add(ph2); pill.rotation.z = 0.7; pill.position.set(-1.7, 0.7, 0.3); root.add(pill); floaters.push({ o: pill, y: 0.7, p: 2, s: 1.1 });
  var orb = new THREE.Mesh(new THREE.SphereGeometry(0.13, 20, 20), M.teal); orb.position.set(1.55, -0.3, 0.4); root.add(orb); floaters.push({ o: orb, y: -0.3, p: 4, s: 1.3 });

  /* tamaño del canvas */
  function size() {
    var w = Math.max(orbit.clientWidth, 1), h = Math.max(orbit.clientHeight, 1);
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    camera.position.z = w / h < 0.85 ? 11.6 : 10.9;
    camera.updateProjectionMatrix();
  }
  var cv = renderer.domElement; cv.className = "orbit__gl"; orbit.appendChild(cv); size();
  if ("ResizeObserver" in window) new ResizeObserver(size).observe(orbit); else addEventListener("resize", size);

  /* estado de animación */
  var tx = 0, ty = 0, hx = 0, hy = 0, visible = true, raf = 0, t0 = performance.now(), cheer = -10, lastBlink = 0, blinkT = -1, waveAmt = 1;
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
      /* saludo: 2,4 s saludando, 3,6 s en reposo; al acertar celebra con los dos brazos */
      var cycle = t % 6, wantWave = cycle < 2.4 ? 1 : 0, c = t - cheer, cheering = c >= 0 && c < 1.6;
      waveAmt = ease(waveAmt, wantWave || cheering ? 1 : 0, 0.07);
      var raise = 0.35 + waveAmt * 1.95;
      armR.shoulder.rotation.z = ease(armR.shoulder.rotation.z, -raise, 0.12);
      armR.elbow.rotation.z = -(Math.sin(t * 7.5) * 0.42 - 0.25) * waveAmt;
      armL.shoulder.rotation.z = ease(armL.shoulder.rotation.z, cheering ? 2.3 : 0.12, 0.12);
      armL.elbow.rotation.z = cheering ? Math.sin(t * 9) * 0.35 : 0;
      /* salto de celebración */
      root.position.y = cheering ? Math.abs(Math.sin(c * 6.4)) * 0.38 * (1 - c / 1.6) : ease(root.position.y, 0, 0.2);
      /* parpadeo */
      if (t - lastBlink > 3.4) { lastBlink = t + Math.random() * 1.2; blinkT = t; }
      var bl = blinkT > 0 ? Math.max(0, 1 - Math.abs((t - blinkT) / 0.08 - 1)) : 0;
      eyes.forEach(function (e) { e.scale.y = 1 - bl * 0.9; });
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
  if (reduced) { armR.shoulder.rotation.z = -2.2; armR.elbow.rotation.z = 0.25; frame(performance.now()); addEventListener("resize", function () { frame(performance.now()); }); return; }
  if ("IntersectionObserver" in window) new IntersectionObserver(function (e) { visible = e[0].isIntersecting; if (visible) kick(); }).observe(orbit);
  document.addEventListener("visibilitychange", kick);
  kick();
})();
