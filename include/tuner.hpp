#pragma once
#include <vector>

namespace phasepack {

class Tuner {
public:
    Tuner(double gain = 1.0, double offset = 0.0);
    // Усиление и смещение
    std::vector<double> tune(const std::vector<double>& signal);
private:
    double gain_;
    double offset_;
};

} // namespace phasepack
