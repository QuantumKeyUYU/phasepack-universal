#pragma once
#include <vector>

namespace phasepack {

class PhaseDetector {
public:
    PhaseDetector();  // теперь объявлен явно, реализация ниже
    // Возвращает фазу сигнала (в радианах)
    double detect(const std::vector<double>& signal);
};

} // namespace phasepack
