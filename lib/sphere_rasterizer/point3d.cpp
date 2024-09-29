#include <pybind11/pybind11.h>

struct Point3D
{
    double x, y, z;

    Point3D(double x_, double y_, double z_) : x(x_), y(y_), z(z_) {}

    Point3D add(const Point3D &other) const
    {
        return Point3D(x + other.x, y + other.y, z + other.z);
    }
};

// Binding code
namespace py = pybind11;

PYBIND11_MODULE(point3d, m)
{
    py::class_<Point3D>(m, "Point3D")
        .def(py::init<double, double, double>()) // Constructor
        .def("add", &Point3D::add)               // Add function
        .def_readwrite("x", &Point3D::x)         // Expose x, y, z attributes
        .def_readwrite("y", &Point3D::y)
        .def_readwrite("z", &Point3D::z);
}