"""Setup script for the package"""

import ast
from setuptools import setup, find_packages


with open("README.md") as readme_file:
    README = readme_file.read()


def version():
    """Return version string."""
    with open("rpn_calc/__main__.py") as input_file:
        for line in input_file:
            if line.startswith('__version__'):
                return ast.parse(line).body[0].value.s
        return "0.0.0"


setup(
    name="rpn_calc",
    version=version(),
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
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Environment :: Console",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6",
    test_suite="test",
    packages=find_packages(exclude=["test"]),
    entry_points={
        "console_scripts": [
            "pol=rpn_calc.__main__:main",
        ]
    },
    install_requires=[
        "pyyaml>=5.0",
    ]
)
