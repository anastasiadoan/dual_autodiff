# dual_autodiff_x/setup.py
from setuptools import setup, Extension
from Cython.Build import cythonize
import os

# Identify all .pyx files in dual_autodiff_x
# If you have multiple files, list them or find them automatically.

# Point to the renamed dual.pyx
extensions = [
    Extension("dual_autodiff_x.dual", ["dual.pyx"]),
]


setup(
    name="dual_autodiff_x",
    version="0.1.0",
    package_dir={"": "."},
    ext_modules=cythonize(extensions, 
    compiler_directives={'language_level': "3"}),
    # If needed, add install_requires or other metadata here.

    packages=["dual_autodiff_x"],
    package_data={"dual_autodiff_x": ["*.so", "*.pyd"]},  # Include compiled files
    exclude_package_data={"dual_autodiff_x": ["*.pyx", "*.py"]},  # Exclude source files
    )
