#include <tuple>

class Point3D
{
public:
    float x, y, z;

    Point3D(float x, float y, float z) : x(x), y(y), z(z) {}

    void set(float new_x, float new_y, float new_z)
    {
        x = new_x;
        y = new_y;
        z = new_z;
    }

    std::tuple<float, float, float> get() const
    {
        return std::make_tuple(x, y, z);
    }
};
