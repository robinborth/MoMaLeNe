#include "point3d.h"
#include <pybind11/pybind11.h>

namespace py = pybind11;

PYBIND11_MODULE(sphere_rasterizer, m)
{
    py::class_<Point3D>(m, "Point3D")
        .def(py::init<float, float, float>())
        .def("set", &Point3D::set)
        .def("get", &Point3D::get)
        .def_readwrite("x", &Point3D::x)  // Expose x
        .def_readwrite("y", &Point3D::y)  // Expose y
        .def_readwrite("z", &Point3D::z); // Expose z
}
