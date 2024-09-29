cmake_minimum_required(VERSION 3.12)
project(point3d)

# Find the Python executable
find_package(Python COMPONENTS Interpreter Development REQUIRED)

# Use the found Python executable
message(STATUS "Using Python executable: ${Python_EXECUTABLE}")

# Define the module
set(pybind11_DIR "/opt/homebrew/Caskroom/miniforge/base/envs/momalene/lib/python3.10/site-packages/pybind11/share/cmake/pybind11")
find_package(pybind11 REQUIRED)

# Create the Python module
pybind11_add_module(point3d point3d.cpp)
