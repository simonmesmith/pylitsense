import os

from setuptools import find_packages, setup

setup(
    name="pylitsense",
    version=os.environ.get("PACKAGE_VERSION", "0.1"),
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="Simon Smith",
    author_email="simon@simonsmith.ca",
    description="Unofficial Python wrapper for the NCBI LitSense API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
