"""Setup script for the package"""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    README = readme_file.read()


setup(
    name="rpn_calc",
    version="0.1.3",
    description="RPN calculator",
    long_description=README,
    author="Alain Girard",
    author_email="alaingirardvd@gmail.com",
    url="https://github.com/Allain18/pol",
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
        "Programming Language :: Python :: Implementation :: PyPy",
        "Environment :: Console",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6",
    test_suite="test",
    packages=find_packages(exclude=["test"]),
    entry_points={
        "console_scripts": [
            "pol=rpn_calculator.calculator:main",
        ]
    },
)
