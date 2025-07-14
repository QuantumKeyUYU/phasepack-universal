#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "phase_detector.hpp"
#include "denoise.hpp"
#include "tuner.hpp"

namespace py = pybind11;

PYBIND11_MODULE(phasepack_py, m) {
    m.doc() = "Python bindings for phasepack-universal";

    py::class_<phasepack::Denoiser>(m, "Denoiser")
        .def(py::init<int>(), py::arg("window_size") = 5)
        .def("filter", &phasepack::Denoiser::filter);

    py::class_<phasepack::PhaseDetector>(m, "PhaseDetector")
        .def(py::init<>())
        .def("detect", &phasepack::PhaseDetector::detect);

    py::class_<phasepack::Tuner>(m, "Tuner")
        .def(py::init<double, double>(),
            py::arg("gain") = 1.0, py::arg("offset") = 0.0)
        .def("tune", &phasepack::Tuner::tune);
}
