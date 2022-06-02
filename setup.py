"""Install packages as defined in this file into the Python environment."""
from setuptools import setup, find_packages

setup(
    name="ColabKit",
    author="ColabKit",
    author_email="johnpaulbin+colabkit@gmail.com",
    url="https://github.com/johnpaulbin/ColabKit",
    description="Simple, importable tools to get quickly started in your colab runtime.",
    version="0.0.1",
    packages=find_packages(where=".", exclude=["tests"]),
    install_requires=[
        "setuptools>=45.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.0",
        "Topic :: Utilities",
        "Development Status :: 2 - Pre-Alpha",
    ],
)