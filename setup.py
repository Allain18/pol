"""Setup script for the package"""

from setuptools import setup, find_packages
from rpn_calculator import __version__

with open("README.md") as readme_file:
    README = readme_file.read()


setup(
    name="rpn_calc",
    version=__version__,
    description="RPN calculator",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Alain Girard",
    author_email="alaingirardvd@gmail.com",
    url="https://github.com/Allain18/pol",
    license="MIT License",
    keywords="rpn, calculator, reverse polish notation",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Environment :: Console",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6",
    test_suite="test",
    packages=find_packages(exclude=["test"]),
    entry_points={
        "console_scripts": [
            "pol=rpn_calculator.main:main",
        ]
    },
)
