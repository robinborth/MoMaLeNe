cmake_minimum_required(VERSION 3.12)
project(sphere_rasterizer)

# Add pybind11
add_subdirectory(../../pybind11 ${CMAKE_CURRENT_BINARY_DIR}/pybind11_build)

# Create the Python module using Pybind11
pybind11_add_module(sphere_rasterizer pybind11.cpp)
