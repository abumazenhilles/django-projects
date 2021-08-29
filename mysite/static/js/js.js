let scene = new THREE.Scene();

let camera = new THREE.PerspectiveCamera(75, 1, 0.1, 1000);

let renderer = new THREE.WebGLRenderer({
  canvas: document.getElementById("canvas"),
});

renderer.setClearColor(0x0f0408, 1);

let opaqueGeo = new THREE.SphereGeometry(5, 24, 24);

let opaqueMat = new THREE.MeshBasicMaterial({
  color: 0x0f0408,
  polygonOffset: true,
  polygonOffsetFactor: 1,
  polygonOffsetUnits: 1,
});

let opaqueSphere = new THREE.Mesh(opaqueGeo, opaqueMat);

scene.add(opaqueSphere);

var wireframeGeo = new THREE.EdgesGeometry(opaqueSphere.geometry);

var wireframeMat = new THREE.LineBasicMaterial({
  color: 0xffff55,
  linewidth: 1,
});

var wireframeSphere = new THREE.LineSegments(wireframeGeo, wireframeMat);

opaqueSphere.add(wireframeSphere);

camera.position.z = 8.5;

function animate(t) {
  requestAnimationFrame(animate);

  opaqueSphere.rotation.y += 0.01;

  renderer.render(scene, camera);
}

animate();
