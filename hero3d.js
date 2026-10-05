/* MedQuizPlus — hélice de ADN 3D del hero (Three.js, WebGL). Si algo falla, quedan los anillos CSS de pro.css. */
import * as THREE from "three";
import { RoomEnvironment } from "three/addons/environments/RoomEnvironment.js";

(function () {
  "use strict";
  var orbit = document.querySelector(".hero .orbit");
  if (!orbit) return;

  var reduced = false, fine = false;
  try { reduced = matchMedia("(prefers-reduced-motion: reduce)").matches; } catch (e) {}
  try { fine = matchMedia("(hover: hover) and (pointer: fine)").matches; } catch (e) {}
  var lite = innerWidth < 768 || (navigator.hardwareConcurrency || 4) < 4; /* material más barato en móviles / equipos modestos */

  var renderer;
  try {
    renderer = new THREE.WebGLRenderer({ antialias: !lite, alpha: true, powerPreference: "high-performance" });
  } catch (e) { return; }
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, lite ? 1.5 : 2));
  renderer.setClearColor(0x000000, 0);
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.1;
  renderer.domElement.setAttribute("aria-hidden", "true");

  var scene = new THREE.Scene();
  var pmrem = new THREE.PMREMGenerator(renderer);
  scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture;

  var camera = new THREE.PerspectiveCamera(30, 1, 0.1, 60);
  camera.position.set(0, 0, 15);

  /* luces tintadas: verde clínico y blanco cálido (sin azules) */
  var mint = new THREE.PointLight(0x34d399, 40, 20); mint.position.set(-4, 3, 4); scene.add(mint);
  var warm = new THREE.PointLight(0xfff3df, 32, 20); warm.position.set(4, -3, 4); scene.add(warm);

  var glass = lite
    ? new THREE.MeshStandardMaterial({ color: 0xd9f7ea, metalness: 0.8, roughness: 0.2, envMapIntensity: 1.4 })
    : new THREE.MeshPhysicalMaterial({
        color: 0xe4fbf1, metalness: 0, roughness: 0.06, transmission: 1, thickness: 0.7, ior: 1.45,
        iridescence: 0.6, iridescenceIOR: 1.25, clearcoat: 1, envMapIntensity: 1.7,
        attenuationColor: new THREE.Color(0x9bf0c6), attenuationDistance: 3
      });
  var glowMint = new THREE.MeshBasicMaterial({ color: 0x34d399 });
  var glowWhite = new THREE.MeshBasicMaterial({ color: 0xf0fff8 });

  /* doble hélice: dos hebras de vidrio, nodos luminosos y peldaños */
  var helix = new THREE.Group();
  var TURNS = 2.6, HEIGHT = 7.2, RADIUS = 1.15, PAIRS = 26, SEG = lite ? 90 : 160;
  function strand(phase) {
    var pts = [];
    for (var i = 0; i <= SEG; i++) {
      var u = i / SEG, a = phase + u * TURNS * Math.PI * 2;
      pts.push(new THREE.Vector3(Math.cos(a) * RADIUS, (u - 0.5) * HEIGHT, Math.sin(a) * RADIUS));
    }
    return new THREE.Mesh(new THREE.TubeGeometry(new THREE.CatmullRomCurve3(pts), SEG * 2, 0.07, lite ? 8 : 14, false), glass);
  }
  helix.add(strand(0)); helix.add(strand(Math.PI));

  var nodeGeo = new THREE.SphereGeometry(0.15, lite ? 14 : 24, lite ? 14 : 24);
  var rungGeo = new THREE.CylinderGeometry(0.03, 0.03, 1, 10);
  var up = new THREE.Vector3(0, 1, 0);
  for (var k = 0; k < PAIRS; k++) {
    var u = (k + 0.5) / PAIRS, a = u * TURNS * Math.PI * 2, y = (u - 0.5) * HEIGHT;
    var A = new THREE.Vector3(Math.cos(a) * RADIUS, y, Math.sin(a) * RADIUS);
    var B = new THREE.Vector3(Math.cos(a + Math.PI) * RADIUS, y, Math.sin(a + Math.PI) * RADIUS);
    var nA = new THREE.Mesh(nodeGeo, glowMint); nA.position.copy(A); helix.add(nA);
    var nB = new THREE.Mesh(nodeGeo, glowWhite); nB.position.copy(B); helix.add(nB);
    var rung = new THREE.Mesh(rungGeo, glass);
    var dir = new THREE.Vector3().subVectors(B, A), len = dir.length();
    rung.position.copy(A).addScaledVector(dir, 0.5); rung.scale.set(1, len, 1);
    rung.quaternion.setFromUnitVectors(up, dir.normalize());
    helix.add(rung);
  }
  helix.rotation.z = 0.42; /* inclinada, como en una ilustración */
  var group = new THREE.Group(); group.position.set(0.2, 0, 0); group.add(helix); scene.add(group);

  function size() {
    var w = Math.max(orbit.clientWidth, 1), h = Math.max(orbit.clientHeight, 1);
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    camera.position.z = w / h < 1 ? 17 : 15;
    camera.updateProjectionMatrix();
  }
  var cv = renderer.domElement;
  cv.className = "orbit__gl";
  orbit.appendChild(cv);
  size();
  if ("ResizeObserver" in window) new ResizeObserver(size).observe(orbit); else addEventListener("resize", size);

  var tx = 0, ty = 0, cx = 0, cy = 0, visible = true, raf = 0, t0 = performance.now();
  if (fine && !reduced) {
    addEventListener("pointermove", function (e) {
      tx = (e.clientX / innerWidth - 0.5) * 0.5; ty = (e.clientY / innerHeight - 0.5) * 0.3;
    }, { passive: true });
  }

  function frame(now) {
    raf = 0;
    var t = (now - t0) / 1000;
    if (!reduced) helix.rotation.y = t * 0.35;
    cx += (tx - cx) * 0.05; cy += (ty - cy) * 0.05;
    group.rotation.y = cx; group.rotation.x = cy;
    renderer.render(scene, camera);
    if (!reduced && visible && document.visibilityState === "visible") raf = requestAnimationFrame(frame);
  }
  function kick() { if (!raf) raf = requestAnimationFrame(frame); }

  frame(performance.now());
  orbit.classList.add("has-3d");
  if (reduced) { addEventListener("resize", function () { frame(performance.now()); }); return; }
  if ("IntersectionObserver" in window) new IntersectionObserver(function (e) { visible = e[0].isIntersecting; if (visible) kick(); }).observe(orbit);
  document.addEventListener("visibilitychange", kick);
  kick();
})();
