#define GLM_ENABLE_EXPERIMENTAL
#include <glm/glm.hpp>
#include <glm/gtx/norm.hpp> // For distance functions
#include <tuple>

class Point3D
{
public:
    glm::vec3 point;

    // Constructor using glm::vec3
    Point3D(float x, float y, float z) : point(x, y, z) {}

    // Set new coordinates
    void set(float new_x, float new_y, float new_z)
    {
        point = glm::vec3(new_x, new_y, new_z);
    }

    // Get the coordinates as a tuple
    std::tuple<float, float, float> get() const
    {
        return std::make_tuple(point.x, point.y, point.z);
    }

    // Calculate distance to another Point3D
    float distanceTo(const Point3D &other) const
    {
        return glm::distance(point, other.point);
    }

    // Normalize the point and return a new Point3D
    Point3D normalize() const
    {
        glm::vec3 normalized_vec = glm::normalize(point);
        return Point3D(normalized_vec.x, normalized_vec.y, normalized_vec.z);
    }
};