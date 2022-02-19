from setuptools import setup
from Cython.Build import cythonize


setup(
    name='qt5.py',
    ext_modules=cythonize(
        "qt5.py",
        nthreads=4,
        ),
    zip_safe=False,
)