"""Setup script."""
from setuptools import find_packages, setup

setup(
    name="lisdf_models",
    version="0.0.0",
    packages=find_packages(include=["lisdf_models"]),
    package_data={"lisdf_models": ["lisdf_models/**"]},  # mypy and model files
)
