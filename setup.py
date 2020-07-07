import setuptools
from pathlib import Path

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
        name="covin-cli",
        version=1.0,
        author="Abhishek Amralkar",
        author_email="abhishekammralkar@gmail.comm",
        description="A COVID19 India CLI package",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/abhishekamralkar/covincli",
        packages=setuptools.find_packages(exclude=["tests", "data"])
)
