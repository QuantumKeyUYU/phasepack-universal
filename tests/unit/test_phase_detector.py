import math
import pytest
from phasepack_py import PhaseDetector

def test_detect_empty_signal():
    pd = PhaseDetector()
    assert pd.detect([]) == 0.0

def test_detect_constant_signal():
    sig = [1.0] * 16
    phase = PhaseDetector().detect(sig)
    # постоянный сигнал ≈ нулевая фаза
    assert pytest.approx(0.0, abs=1e-6) == phase

def test_detect_sine_wave():
    N = 128
    sig = [math.sin(2*math.pi*i/N) for i in range(N)]
    phase = PhaseDetector().detect(sig)
    # синус опережает косинус на π/2
    assert pytest.approx(math.pi/2, rel=1e-2) == phase
