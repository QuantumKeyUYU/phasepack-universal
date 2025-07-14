#define _USE_MATH_DEFINES
#include "phase_detector.hpp"
#include <cmath>

namespace phasepack {

    // Явная реализация конструктора
    PhaseDetector::PhaseDetector() {}

    double PhaseDetector::detect(const std::vector<double>& signal) {
        if (signal.empty()) {
            return 0.0;
        }
        size_t N = signal.size();
        double re = 0.0, im = 0.0;

        // Собираем компоненты на первой гармонике
        for (size_t i = 0; i < N; ++i) {
            double angle = 2.0 * M_PI * static_cast<double>(i) / static_cast<double>(N);
            re += signal[i] * std::cos(angle);
            im += signal[i] * std::sin(angle);
        }

        // Если амплитуда почти нулевая — постоянный или пустой сигнал
        double magnitude = std::sqrt(re * re + im * im);
        if (magnitude < 1e-8) {
            return 0.0;
        }

        // Иначе возвращаем фазу
        return std::atan2(im, re);
    }

} // namespace phasepack
