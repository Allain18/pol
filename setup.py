"""Setup script for the package"""

from setuptools import setup

with open("README.md") as readme_file:
    README = readme_file.read()


setup(
    name="rpn calculator",
    version="0.1.0",
    description="RPN calculator",
    long_description=README,
    author="Alain Girard",
    author_email="alaingirardvd@gmail.com",
    url="https://github.com/Allain18/rpncal",
    license="MIT License",
    keywords="rpn, calculator, reverse polish notation",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Environment :: Console",
        "Operating System :: OS Independent"
    ],
    test_suite="test",
    entry_points={
        "console_scripts": [
            "pol=calculator.calculator:main",
        ]
    },
)
