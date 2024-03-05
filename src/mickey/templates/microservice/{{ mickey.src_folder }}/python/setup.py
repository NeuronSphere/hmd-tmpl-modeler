from setuptools import setup, find_packages
import pathlib

repo_dir = pathlib.Path(__file__).absolute().parent.parent.parent
version_file = repo_dir / "meta-data" / "VERSION"

with open(version_file, "r") as vfl:
    version = vfl.read().strip()

setup(
    name="{{ vars.package_name }}",
    version=version,
    license="unlicensed",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
)
