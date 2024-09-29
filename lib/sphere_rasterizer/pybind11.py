import sys
from pathlib import Path
import os

# add the .so file to the current python environment
current_directory = os.path.dirname(os.path.abspath(__file__))
build_dir = Path(current_directory) / "build"
sys.path.append(str(build_dir))
# import everything from the c++ to python
import sphere_rasterizer as sr  # type: ignore


class Point3D(sr.Point3D):
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        super().__init__(x, y, z)
