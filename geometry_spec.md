# RBYRCT Geometry Specification

## Purpose

This document defines the canonical geometry standard for the RBYRCT CAD system.

The goal is to keep the geometry consistent across:

- CAD models
- ray/path visualization
- TOPAS / Geant4 simulations
- reconstruction pipelines
- patent and manuscript figures

---

## Coordinate System

### Origin

## Detector Architecture: Adaptive Sparse Panels

The baseline detector configuration uses sparse, modular detector panels rather than a continuous full detector ring.

Each detector panel is defined by:

- panel index
- angular position
- radial distance from imaging center
- panel width
- panel height
- active/inactive state

This supports adaptive ray sampling and targeted acquisition strategies for RBYRCT reconstruction.

The origin is defined as the center of the imaging volume:

```text
(0, 0, 0)
````

### Axes

```text
+X = patient left/right direction
+Y = source-detector depth direction
+Z = vertical direction
```

The imaging target is centered at the origin unless otherwise specified.

---

## Primary Geometry Parameters

| Parameter                  | Meaning                                       |   Units | Default |
| -------------------------- | --------------------------------------------- | ------: | ------: |
| `R_detector`               | Detector arc/ring radius from origin          |      mm |     500 |
| `D_source_to_center`       | Distance from source emission point to origin |      mm |     300 |
| `theta_max`                | Maximum beam steering angle                   | degrees |      15 |
| `N_detectors`              | Number of detector segments                   |   count |      64 |
| `detector_arc_angle`       | Total detector angular coverage               | degrees |     120 |
| `table_height`             | Patient table height relative to origin       |      mm |    -120 |
| `janus_layers`             | Number of Janus steering layers               |   count |      11 |
| `janus_elements_per_layer` | Elements per Janus layer                      |   count |      24 |
| `janus_layer_spacing`      | Spacing between Janus layers                  |      mm |       2 |
| `janus_module_distance`    | Distance from source to Janus module center   |      mm |      80 |

---

## System Modules

The RBYRCT geometry is divided into four major modules:

1. **Source Assembly**
2. **Steering / Janus Module**
3. **Detector Assembly**
4. **Patient / Imaging Volume**

Each module should be modeled as a separate CAD component.

---

## Source Assembly

The source assembly defines the nominal X-ray emission point and orientation.

### Source Position

Default source position:

```text
(0, -D_source_to_center, 0)
```

### Source Direction

The default beam direction points toward the origin:

```text
+Y direction
```

### Source Parameters

| Parameter               | Meaning                         |
| ----------------------- | ------------------------------- |
| `source_radius`         | Visual radius of source housing |
| `source_length`         | Length of source housing        |
| `source_emission_point` | Point from which rays originate |

---

## Janus Steering Module

The Janus module represents the conceptual beam-steering region.

### Default Position

The Janus module is placed between the source and imaging volume:

```text
(0, -D_source_to_center + janus_module_distance, 0)
```

### Function

The Janus module should visually communicate:

* layered beam interaction
* steering or deflection region
* structured element array

### Modeling Guidance

For early CAD versions, the Janus module may be represented as:

* layered slabs
* spherical array elements
* ring-like element groups
* simplified material zones

The purpose is conceptual clarity, not manufacturing precision.

---

## Detector Assembly

The detector assembly is centered around the imaging volume.

### Detector Radius

Detector elements lie approximately on a circular arc:

```text
radius = R_detector
```

### Detector Arc

The detector arc is centered opposite the source unless otherwise specified.

Default angular coverage:

```text
detector_arc_angle = 120 degrees
```

### Detector Segmentation

Detector panels should be indexed:

```text
detector_000
detector_001
...
detector_N
```

Each detector element should have:

* angular position
* radial distance
* panel width
* panel height

---

## Imaging Volume

The imaging volume is centered at the origin.

For early CAD versions, represent this as a transparent cylinder or box.

### Default Bounding Volume

| Parameter               | Meaning                 | Units |
| ----------------------- | ----------------------- | ----: |
| `imaging_volume_radius` | Radius of target region |    mm |
| `imaging_volume_height` | Height of target region |    mm |

---

## Beam Path Convention

Beam paths should be represented as lines or curves from:

```text
source → Janus module → imaging volume → detector
```

### Beam Types

| Beam Type              | Meaning                                       |
| ---------------------- | --------------------------------------------- |
| `nominal_ray`          | Central undeflected ray                       |
| `steered_ray_positive` | Ray steered toward positive angular direction |
| `steered_ray_negative` | Ray steered toward negative angular direction |
| `sample_ray`           | Representative ray used for visualization     |

---

## Parameter File

The canonical parameter file is:

```text
params/default_geometry.json
```

Example:

```json
{
  "units": "mm",
  "R_detector": 500,
  "D_source_to_center": 300,
  "theta_max_deg": 15,
  "N_detectors": 64,
  "detector_arc_angle_deg": 120,
  "table_height": -120,
  "janus_layers": 11,
  "janus_elements_per_layer": 24,
  "janus_layer_spacing": 2,
  "janus_module_distance": 80
}
```

---

## Naming Conventions

### CAD Components

Use clear module prefixes:

```text
SRC_source_housing
JAN_layer_00
JAN_element_00_00
DET_panel_000
PAT_imaging_volume
SYS_reference_axes
```

### Parameters

Use lowercase snake case in JSON:

```text
r_detector
theta_max_deg
n_detectors
```

Use readable names in Fusion 360 where needed:

```text
R_detector
theta_max
N_detectors
```

---

## Geometry Constraints

Initial geometry should satisfy:

```text
D_source_to_center < R_detector
theta_max_deg > 0
N_detectors >= 1
janus_layers >= 1
```

Recommended constraints:

```text
R_detector >= 2 * D_source_to_center
detector_arc_angle_deg >= 2 * theta_max_deg
janus_module_distance < D_source_to_center
```

---

## Versioning

Each major geometry update should include:

* updated `default_geometry.json`
* updated exported CAD file
* changelog entry
* figure regeneration if geometry changed visually

Suggested version format:

```text
geometry_v0.1
geometry_v0.2
geometry_v1.0
```

---

## Export Targets

CAD geometry may be exported to:

```text
STEP    - CAD exchange
STL     - mesh visualization
OBJ     - rendering / Blender / Houdini
JSON    - simulation parameter exchange
CSV     - detector and ray positions
```

---

## Notes

This specification is not intended to define a final manufacturable device.

It defines a shared geometric language for:

* design exploration
* visualization
* simulation alignment
* manuscript and patent preparation

