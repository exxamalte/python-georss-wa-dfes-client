from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIRES = [
    "georss_client>=0.14",
]

setup(
    name="georss_wa_dfes_client",
    version="0.3",
    author="Malte Franken",
    author_email="coding@subspace.de",
    description="A GeoRSS client library for the WA Department of Fire and Emergency Services (DFES) feed.",
    license="Apache-2.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/exxamalte/python-georss-wa-dfes-client",
    packages=find_packages(exclude=("tests*",)),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIRES,
)
