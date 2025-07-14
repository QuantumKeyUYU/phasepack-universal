import pytest
from phasepack_py import Tuner

def test_tune_empty():
    assert Tuner().tune([]) == []

def test_tune_gain_and_offset():
    sig = [0.0, 1.0, -1.0]
    t = Tuner(gain=2.0, offset=1.0)
    # x*2 + 1
    assert t.tune(sig) == [1.0, 3.0, -1.0]
