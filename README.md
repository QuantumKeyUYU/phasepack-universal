````markdown
# PhasePack Universal Toolkit

**PhasePack Universal** — это универсальный набор инструментов для детекции фазы, фильтрации (de-noising) и тюнинга (усиления/смещения) сигналов. Проект состоит из:

- **C++ core** — высокопроизводительные алгоритмы на C++17  
- **Python bindings** — обёртка на pybind11  
- **CLI** — удобный интерфейс командной строки (`phasepack-universal`)  
- **Тесты** — unit- и интеграционные тесты на pytest  
- **CI/CD** — пример конвейера сборки и тестов под GitHub Actions  

---

## Содержание

1. [Особенности](#особенности)  
2. [Требования](#требования)  
3. [Установка и сборка](#установка-и-сборка)  
   1. [Клонирование репозитория](#клонирование-репозитория)  
   2. [Виртуальное окружение Python](#виртуальное-окружение-python)  
   3. [Установка зависимостей](#установка-зависимостей)  
   4. [Сборка C++ core](#сборка-c-core)  
   5. [Установка Python пакета](#установка-python-пакета)  
4. [Использование CLI](#использование-cli)  
5. [Использование Python API](#использование-python-api)  
6. [Тестирование](#тестирование)  
7. [CI/CD](#cicd)  
8. [Дорожная карта](#дорожная-карта)  
9. [Вклад](#вклад)  
10. [Лицензия](#лицензия)  

---

## Особенности

- **PhaseDetector** — оценка фазы доминирующей частоты  
- **Denoiser** — скользящее среднее для удаления шума  
- **Tuner** — масштабирование и смещение сигнала  
- **CLI** — быстрый доступ через `phasepack-universal detect|denoise|tune`  
- **Python API** — простая интеграция в скрипты и Jupyter  
- **Кроссплатформенность** — Windows, Linux, macOS  
- **Тесты** — >90% покрытия, unit и интеграционные сценарии  

---

## Требования

- **C++**: компилятор с поддержкой C++17 (MSVC 2019+, GCC 9+, Clang 10+)  
- **CMake**: версия ≥3.15  
- **Python**: версия ≥3.7  
- **pip**, **virtualenv** или встроенный `venv`  
- Опционально: **Docker** для контейнеризации  

---

## Установка и сборка

### 1. Клонирование репозитория

```bash
git clone https://github.com/yourusername/phasepack-universal.git
cd phasepack-universal
````

### 2. Виртуальное окружение Python

```powershell
# Windows PowerShell
py -3 -m venv .venv
& .\.venv\Scripts\Activate.ps1
```

или

```bash
# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Установка зависимостей

```bash
pip install --upgrade pip
pip install cmake pybind11 numpy click pytest
```

### 4. Сборка C++ core

```bash
mkdir build
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build --config Release
```

> **Примечание:** на Windows в PowerShell обязательно указывать `--config Release`.

### 5. Установка Python пакета

```bash
pip install .
```

---

## Использование CLI

### Детект фазы

```bash
phasepack-universal detect path/to/signal.csv
```

### Де-ноизинг

```bash
phasepack-universal denoise path/to/signal.csv --window-size 5
```

### Тюнинг

```bash
phasepack-universal tune path/to/signal.csv --gain 2.0 --offset 1.0
```

---

## Использование Python API

```python
from adapter import detect_phase, denoise_signal, tune_signal
import numpy as np

sig = np.sin(np.linspace(0, 2*np.pi, 200))
phase = detect_phase(sig)
print(f"Phase: {phase:.4f} rad")
denoised = denoise_signal(sig, window_size=7)
tuned = tune_signal(sig, gain=1.5, offset=-0.2)
```

---

## Тестирование

```bash
pytest -q
```

---

## CI/CD

```yaml
name: CI

on: [push, pull_request]

jobs:
  build-and-test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install cmake pybind11 numpy click pytest
      - name: Build C++ core
        run: |
          mkdir build
          cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
          cmake --build build --config Release
      - name: Install package
        run: pip install .
      - name: Run tests
        run: pytest -q
```

---

## Дорожная карта

* Улучшить алгоритм детекции: FFT-подход, адаптивные окна
* Оптимизация фильтра: гауссово взвешенное скользящее среднее
* Распараллеливание и GPU-ускорение
* Расширение CLI новыми командами (`bench`, `stats`)
* Документация Sphinx / MkDocs

---

## Вклад

1. Форкай репозиторий
2. Создай ветку `feature/your_feature`
3. Добавь тесты
4. Открой Pull Request

---

## Лицензия

MIT License. См. [LICENSE](LICENSE).

```
```
