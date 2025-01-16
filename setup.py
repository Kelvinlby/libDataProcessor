from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize

sourceFiles = ["libDataProcessor/lib.py"]

extensions = cythonize(
    Extension(
        name="libDataProcessor.so",
        sources = sourceFiles,
    ),
    compiler_directives={"language_level": "3"},
)

kwargs = {
    "name": "libDataProcessor",
    "packages": find_packages(),
    "ext_modules": extensions,
}

setup(**kwargs)
