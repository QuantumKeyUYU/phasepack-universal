cmake_minimum_required(VERSION 3.15)
project(phasepack-universal VERSION 0.1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# Подключаем pybind11 через FetchContent
include(FetchContent)
FetchContent_Declare(
  pybind11
  GIT_REPOSITORY https://github.com/pybind/pybind11.git
  GIT_TAG        v2.11.1
)
FetchContent_MakeAvailable(pybind11)

# Библиотека core
add_library(phasepack
    src/phase_detector.cpp
    src/denoise.cpp
    src/tuner.cpp
)
target_include_directories(phasepack PUBLIC include)

# Python-модуль
pybind11_add_module(phasepack_py src/filter_api.cpp)
target_link_libraries(phasepack_py PRIVATE phasepack)
