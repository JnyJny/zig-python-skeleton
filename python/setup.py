"""Setup script for zigmath Python package."""

from setuptools import setup, find_packages

setup(
    name="zigmath",
    version="0.1.0",
    description="Python bindings for Zig mathematical functions",
    long_description=open("../README.md").read(),
    long_description_content_type="text/markdown",
    author="Jny",
    author_email="jny@example.com",
    py_modules=["zigmath"],
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov",
            "mypy",
            "black",
            "isort",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    include_package_data=True,
    package_data={
        "": ["*.dylib", "*.so", "*.dll"],
    },
)