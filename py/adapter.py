"""
adapter.py — обёртки над C++-модулями phasepack_py
"""

from typing import List, Union

import numpy as np
from phasepack_py import Denoiser, PhaseDetector, Tuner

Signal = Union[List[float], np.ndarray]


def detect_phase(signal: Signal) -> float:
    """
    Детектирует фазу сигнала (в радианах)
    :param signal: list или numpy.ndarray с отсчетами
    :return: фаза в радианах
    """
    # конвертим в список float
    sig = signal.tolist() if hasattr(signal, "tolist") else list(signal)
    return PhaseDetector().detect(sig)


def denoise_signal(signal: Signal, window_size: int = 5) -> List[float]:
    """
    Применяет скользящее среднее для удаления шума
    :param signal: входной сигнал
    :param window_size: размер окна фильтра
    :return: отфильтрованный сигнал как list[float]
    """
    sig = signal.tolist() if hasattr(signal, "tolist") else list(signal)
    return Denoiser(window_size).filter(sig)


def tune_signal(signal: Signal, gain: float = 1.0, offset: float = 0.0) -> List[float]:
    """
    Применяет усиление и смещение к сигналу
    :param signal: входной сигнал
    :param gain: множитель
    :param offset: смещение
    :return: откорректированный сигнал как list[float]
    """
    sig = signal.tolist() if hasattr(signal, "tolist") else list(signal)
    return Tuner(gain, offset).tune(sig)
