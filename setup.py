import setuptools
from pathlib import Path

setuptools.setup(
        name="covincli",
        version=1.0,
        long_description_content_type=Path("README.md").read_text(),
        packages=setuptools.find_packages(exclude=["tests", "data"])
)
