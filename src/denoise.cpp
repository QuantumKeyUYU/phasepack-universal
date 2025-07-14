#include "denoise.hpp"
#include <algorithm>

namespace phasepack {

    Denoiser::Denoiser(int window_size)
        : window_size_(window_size > 0 ? window_size : 1) {
    }

    std::vector<double> Denoiser::filter(const std::vector<double>& signal) {
        size_t N = signal.size();
        std::vector<double> result(N, 0.0);
        if (N == 0) return result;

        int ws = window_size_;
        int half = ws / 2;
        for (size_t i = 0; i < N; ++i) {
            int start = std::max<int>((int)i - half, 0);
            int end = std::min<int>((int)i + half, (int)N - 1);
            double sum = 0.0;
            for (int j = start; j <= end; ++j) {
                sum += signal[j];
            }
            result[i] = sum / static_cast<double>(end - start + 1);
        }
        return result;
    }

} // namespace phasepack
