# setup.py
from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension, build_ext
import os

here = os.path.abspath(os.path.dirname(__file__))
include_dir = os.path.join(here, "include")

ext_modules = [
    Pybind11Extension(
        "phasepack_py",
        [
            "src/filter_api.cpp",
            "src/phase_detector.cpp",
            "src/denoise.cpp",
            "src/tuner.cpp",
        ],
        include_dirs=[include_dir],
        language="c++",
    ),
]

setup(
    name="phasepack-universal",
    version="0.1.0",
    description="Universal phase detection & denoise toolkit",
    author="Your Name",
    author_email="you@example.com",

    # Устанавливаем эти файлы из папки py/ как топ-левел модули
    py_modules=["cli", "adapter"],
    package_dir={"": "py"},

    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},

    install_requires=[
        "numpy",
        "click",
    ],
    python_requires=">=3.7",

    entry_points={
        "console_scripts": [
            "phasepack-universal=cli:cli",
        ],
    },
)
