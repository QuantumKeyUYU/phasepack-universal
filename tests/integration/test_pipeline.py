import math
import pytest
from phasepack_py import Denoiser, Tuner, PhaseDetector

def test_full_pipeline_preserves_phase():
    N = 256
    # чистый синус
    sig = [math.sin(2*math.pi*i/N) for i in range(N)]

    # 1) убираем шум (хотя его нет)
    filtered = Denoiser(window_size=5).filter(sig)
    # 2) настраиваем усиление и смещение
    tuned = Tuner(gain=0.5, offset=0.2).tune(filtered)
    # 3) детектируем фазу
    phase = PhaseDetector().detect(tuned)

    # gain/offset не меняют фазу, она всё так же π/2
    assert pytest.approx(math.pi/2, rel=1e-2) == phase
