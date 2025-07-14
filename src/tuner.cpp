#include "tuner.hpp"

namespace phasepack {

    Tuner::Tuner(double gain, double offset)
        : gain_(gain), offset_(offset) {
    }

    std::vector<double> Tuner::tune(const std::vector<double>& signal) {
        std::vector<double> result;
        result.reserve(signal.size());
        for (double x : signal) {
            result.push_back(x * gain_ + offset_);
        }
        return result;
    }

} // namespace phasepack
