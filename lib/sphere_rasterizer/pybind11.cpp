#include "point3d.h"
#include <pybind11/pybind11.h>

namespace py = pybind11;

PYBIND11_MODULE(sphere_rasterizer, m)
{
    py::class_<Point3D>(m, "Point3D")
        .def(py::init<float, float, float>())
        .def("set", &Point3D::set)
        .def("get", &Point3D::get)
        .def("distance", &Point3D::distanceTo) // Bind distanceTo function
        .def("normalize", &Point3D::normalize) // Bind normalize function
        .def_property("x", [](const Point3D &p)
                      { return p.point.x; }, [](Point3D &p, float x)
                      { p.point.x = x; }) // Expose x
        .def_property("y", [](const Point3D &p)
                      { return p.point.y; }, [](Point3D &p, float y)
                      { p.point.y = y; }) // Expose y
        .def_property("z", [](const Point3D &p)
                      { return p.point.z; }, [](Point3D &p, float z)
                      { p.point.z = z; }); // Expose z
}