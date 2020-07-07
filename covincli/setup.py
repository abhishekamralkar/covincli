import setuptools
from pathlib import Path

setuptools.setup(
        name="covincli",
        version=1.0,
        long_description=Path("README.org").read_text(),
        packages=setuptools.find_packages(exclude=["tests", "data"])
)