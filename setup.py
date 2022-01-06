import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="robedbeauvile001",
    version="0.0.1",
    author="Robed Beauvile",
    author_email="robedbeauvil@gmail.com",
    description="A python package that retrieves a matrix dimensions, it's trace, and performs matrix addition, subtraction, multiplication.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/beauvilerobed/py-matrix",
    packages=setuptools.find_packages()
)