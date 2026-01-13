# laniakea
LANIAKEA: Chaos Theory Particle Simulation
# LANIAKEA: Chaos Theory Simulation

### [🔴 Live Demo](https://your-username.github.io/laniakea)

**Laniakea** is a GPU-accelerated particle simulation that visualizes the formation of cosmic filaments (The Cosmic Web) using chaotic attractors and spectral turbulence. 

It renders **180,000 autonomous agents** in real-time in the browser, serving as a case study in High-Performance Computing (HPC), Emergence Theory, and WebGL optimization.

## 🚀 Key Features

* **Massive Scale:** 180,000 flow particles + 35,000 background stars rendered at 60 FPS using `THREE.Points`.
* **Emergent Physics:** No pre-defined paths. Structure arises naturally from the interaction between a radial gravity well and a Perlin-esque vector field.
* **Volumetric Core:** A particle-based singularity (8,000 points) simulating a thermodynamic accretion disk.
* **Scientific Visualization:** Includes metric plot grids and real-time variable controls.

## 🧠 The Math: "Structure from Chaos"

The simulation mimics the **Zeldovich Pancake** model of cosmological structure formation. By applying low-frequency noise interference (Turbulence) against a central attractor (Gravity), the system spontaneously generates "filaments" and "nodes" without explicit instruction.

## 🛠️ Tech Stack

* **Engine:** Three.js (WebGL 2.0)
* **Language:** JavaScript (ES6+)
* **Shaders:** Custom Fragment logic for non-attenuating starfields

## 📦 Run Locally

1.  Clone the repository:
    ```bash
    git clone [https://github.com/your-username/laniakea.git](https://github.com/your-username/laniakea.git)
    ```
2.  Open `index.html` in any browser.

---
*Built as a study in Generative Art and Complexity Theory.*
