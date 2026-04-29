## rbyrct-cad

Parametric CAD and geometry definitions for the Ray-by-Ray Computed Tomography (RBYRCT) system.

```
geometry JSON → Python generator → CAD/Blender/Fusion/Houdini outputs
```

### Overview

This repository defines the **geometric foundation** of the RBYRCT architecture, including:

* Source–detector configuration
* Beam steering geometry
* Janus layer representations
* Parametric system definitions

The goal is to maintain **consistent geometry across:**

* CAD models (Fusion 360)
* Monte Carlo simulation (TOPAS / Geant4)
* Reconstruction pipelines
* Research figures and diagrams

---

### Core Concepts

* **Parametric geometry**: All critical dimensions and angles are defined in JSON
* **Single coordinate system**: Shared across all modules
* **Modular design**: Source, steering, detection, and patient subsystems

---

### Getting Started

1. Open CAD model:

   ```
   cad/fusion360/rbyrct_master.f3d
   ```

2. Modify parameters:

   ```
   params/default_geometry.json
   ```

3. Export geometry for simulation:

   ```
   python scripts/export_for_topas.py
   ```

---

### Repository Structure

---

### Future Work

* Procedural geometry generation
* Integration with reconstruction pipelines
* XR-based visualization

```
rbyrct-cad/
│
├── README.md
├── LICENSE
│
├── docs/
│   ├── geometry_spec.md
│   ├── coordinate_system.md
│   ├── figures.md
│
├── cad/
│   ├── fusion360/
│   │   ├── rbyrct_master.f3d
│   │   └── exports/
│   │       ├── step/
│   │       └── stl/
│
├── params/
│   ├── default_geometry.json
│   ├── configs/
│   │   ├── compact_system.json
│   │   ├── wide_detector.json
│
├── scripts/
│   ├── generate_geometry.py
│   ├── export_for_topas.py
│   └── visualize_rays.py
│
├── figures/
│   ├── system_overview/
│   ├── beam_steering/
│   ├── detector_geometry/
│
├── houdini/
│   ├── hip/
│   └── vex/
│
└── integration/
    ├── topas/
    ├── reconstruction/
```
