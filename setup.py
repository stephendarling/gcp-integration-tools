import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="gcp-integration-tools",
    version="0.0.1",
    description="Integration toolset for Google Cloud Platform",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/stephendarling/gcp-integration-tools",
    author="Stephen Darling",
    author_email="stephen.darling@outlook.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
)