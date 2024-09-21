import os
from setuptools import setup, find_packages

# Project metadata
PROJECT_NAME = "OmniaCore"
VERSION = "1.0.0"
AUTHOR = "KOSASIH"
EMAIL = "kosasihg88@gmail.com"

# Dependencies
DEPENDENCIES = [
    "numpy==1.21.2",
    "pytest==6.2.5",
    "django==3.2.9",
]

# Setup script
setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    packages=find_packages(),
    install_requires=DEPENDENCIES,
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "omnia_core=omnia_core.__main__:main",
        ],
    },
)
