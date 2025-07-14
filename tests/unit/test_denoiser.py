import pytest
from phasepack_py import Denoiser

def test_filter_empty():
    assert Denoiser().filter([]) == []

def test_filter_window_1_leaves_signal():
    sig = [10, 20, 30]
    out = Denoiser(window_size=1).filter(sig)
    assert out == sig

def test_filter_moving_average():
    sig = [1.0, 2.0, 3.0, 4.0, 5.0]
    d = Denoiser(window_size=3)
    out = d.filter(sig)
    # ручной расчёт:
    # индекс 0: (1+2)/2 = 1.5
    # индекс 1: (1+2+3)/3 = 2.0
    # индекс 2: (2+3+4)/3 = 3.0
    # индекс 3: (3+4+5)/3 = 4.0
    # индекс 4: (4+5)/2 = 4.5
    expected = [1.5, 2.0, 3.0, 4.0, 4.5]
    for e, o in zip(expected, out):
        assert pytest.approx(e, rel=1e-6) == o
