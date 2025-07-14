#pragma once
#include <vector>

namespace phasepack {

class Denoiser {
public:
    explicit Denoiser(int window_size = 5);
    // Скользящее среднее
    std::vector<double> filter(const std::vector<double>& signal);
private:
    int window_size_;
};

} // namespace phasepack
