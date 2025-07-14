"""
cli.py — командная утилита для phasepack-universal
"""

import click
import numpy as np

from adapter import detect_phase, denoise_signal, tune_signal


@click.group()
def cli():
    """PhasePack Universal Toolkit CLI."""
    pass


@cli.command()
@click.argument("input_file", type=click.Path(exists=True))
@click.option(
    "--window-size", "-w", default=5, show_default=True,
    help="Размер окна для фильтра скользящего среднего"
)
def denoise(input_file: str, window_size: int):
    """
    Де-ноизинг сигнала из CSV-файла (один столбец)
    """
    data = np.loadtxt(input_file, delimiter=",")
    filtered = denoise_signal(data, window_size)
    out_file = input_file + ".denoised.csv"
    np.savetxt(out_file, filtered, delimiter=",")
    click.echo(f"[✔] Де-ноизинг завершен, результат в {out_file}")


@cli.command()
@click.argument("input_file", type=click.Path(exists=True))
@click.option(
    "--gain", "-g", default=1.0, show_default=True,
    help="Коэффициент усиления"
)
@click.option(
    "--offset", "-o", default=0.0, show_default=True,
    help="Аддитивное смещение"
)
def tune(input_file: str, gain: float, offset: float):
    """
    Настройка сигнала: умножение на gain и прибавление offset
    """
    data = np.loadtxt(input_file, delimiter=",")
    tuned = tune_signal(data, gain, offset)
    out_file = input_file + ".tuned.csv"
    np.savetxt(out_file, tuned, delimiter=",")
    click.echo(f"[✔] Настройка завершена, результат в {out_file}")


@cli.command(name="detect")
@click.argument("input_file", type=click.Path(exists=True))
def _detect(input_file: str):
    """
    Детект фазы сигнала из CSV-файла
    """
    data = np.loadtxt(input_file, delimiter=",")
    phase = detect_phase(data)
    click.echo(f"[✔] Обнаруженная фаза: {phase:.6f} rad")


if __name__ == "__main__":
    cli()
