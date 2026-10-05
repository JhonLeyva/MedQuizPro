/* MedQuizPlus — objeto 3D del hero (Three.js, WebGL). Si algo falla, quedan los anillos CSS de pro.css. */
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
  renderer.toneMappingExposure = 1.15;
  renderer.domElement.setAttribute("aria-hidden", "true");

  var scene = new THREE.Scene();
  var pmrem = new THREE.PMREMGenerator(renderer);
  scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture;

  var camera = new THREE.PerspectiveCamera(32, 1, 0.1, 50);
  camera.position.set(0, 0, 7);

  /* luces tintadas con los colores de la marca */
  var teal = new THREE.PointLight(0x2dd4bf, 38, 14); teal.position.set(-3, 2, 3); scene.add(teal);
  var blue = new THREE.PointLight(0x4f6bff, 42, 14); blue.position.set(3.2, -2, 2.5); scene.add(blue);

  var glass = lite
    ? new THREE.MeshStandardMaterial({ color: 0xcfe9ff, metalness: 0.85, roughness: 0.18, envMapIntensity: 1.4 })
    : new THREE.MeshPhysicalMaterial({
        color: 0xd6f2f4, metalness: 0, roughness: 0.05, transmission: 1, thickness: 0.9, ior: 1.45,
        iridescence: 1, iridescenceIOR: 1.3, clearcoat: 1, envMapIntensity: 1.7,
        attenuationColor: new THREE.Color(0x8ff0e4), attenuationDistance: 3.2
      });

  var group = new THREE.Group(); group.position.set(0.3, 0.1, 0); scene.add(group);
  function ring(R, r, rx, ry, rz) {
    var m = new THREE.Mesh(new THREE.TorusGeometry(R, r, lite ? 32 : 64, lite ? 120 : 220), glass);
    m.rotation.set(rx, ry, rz); group.add(m); return m;
  }
  var r1 = ring(1.55, 0.115, 1.15, 0.15, 0);
  var r2 = ring(1.2, 0.075, 0.35, 0.95, 0.4);
  var r3 = ring(1.95, 0.035, 1.4, -0.5, 0.2);

  /* esferas luminosas: dan algo que refractar dentro del vidrio */
  var core = new THREE.Mesh(new THREE.SphereGeometry(0.34, 32, 32), new THREE.MeshBasicMaterial({ color: 0x2dd4bf }));
  var orb = new THREE.Mesh(new THREE.SphereGeometry(0.2, 24, 24), new THREE.MeshBasicMaterial({ color: 0x6d7dff }));
  group.add(core); group.add(orb);

  function size() {
    var w = Math.max(orbit.clientWidth, 1), h = Math.max(orbit.clientHeight, 1);
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    camera.position.z = w / h < 1 ? 8.4 : 7;
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
      tx = (e.clientX / innerWidth - 0.5) * 0.6; ty = (e.clientY / innerHeight - 0.5) * 0.4;
    }, { passive: true });
  }

  function frame(now) {
    raf = 0;
    var t = (now - t0) / 1000;
    if (!reduced) {
      r1.rotation.z = t * 0.22; r2.rotation.z = -t * 0.3; r3.rotation.z = t * 0.12;
      orb.position.set(Math.cos(t * 0.9) * 1.55, Math.sin(t * 0.9) * 0.55, Math.sin(t * 0.9) * 1.1);
      core.scale.setScalar(1 + Math.sin(t * 1.6) * 0.06); /* pulso suave, como un latido */
    }
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
