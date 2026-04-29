import json
import math
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

with open(ROOT / "params" / "default_geometry.json", "r") as f:
    cfg = json.load(f)

radius = cfg["detectors"]["radius"]
angles = cfg["detectors"]["angles_deg"]

out_dir = ROOT / "outputs"
out_dir.mkdir(exist_ok=True)

with open(out_dir / "detector_panels.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "angle_deg", "x", "y", "z"])

    for i, angle in enumerate(angles):
        theta = math.radians(angle)

        x = radius * math.sin(theta)
        y = radius * math.cos(theta)
        z = 0

        writer.writerow([i, angle, x, y, z])
