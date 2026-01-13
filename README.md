
# LANIAKEA: Chaos Theory Simulation

**Laniakea** is a GPU-accelerated particle simulation that visualizes the formation of cosmic filaments (The Cosmic Web) using chaotic attractors and spectral turbulence. 
Renders **180,000 autonomous agents** in real-time in the browser, serving as a visualizer in Chaos Theory, as well as a light application of Python, JavaScript, and HTML.

## Key Features
* **Particulate Scale:** 180,000 flow particles + 35,000 background stars rendered at 60 FPS using `THREE.Points`.
* **Emergent Physics:** No pre-defined paths. Structure arises naturally from the interaction between a radial gravity well and a Perlin-esque vector field.
* **Volumetric Core:** A particle-based singularity (8,000 points) simulating a thermodynamic accretion disk of a spinning black hole.

## Order from Chaos
The simulation mimics the **Zeldovich Pancake** model of cosmological structure formation. By applying low-frequency noise interference (referenced as turbulence) against a central attractor (Gravity), the system spontaneously generates "filaments" and "nodes" without explicit instruction or hardcoding of any kind. Each pass will generate an entirely new flow of particles.

## Stack
* **Engine:** Three.js (WebGL 2.0)
* **Language:** JavaScript (ES6+)
* **Shaders:** Custom Fragment logic for non-attenuating starfields

## To Run
1.  Clone repo:
    ```bash
    git clone [https://github.com/your-username/laniakea.git](https://github.com/your-username/laniakea.git)
    ```
2.  Open `index.html` in any browser.

