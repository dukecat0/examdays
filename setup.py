from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="examdays",
    version="0.0.3",
    author="meowmeowcat",
    author_email="",
    description="A module that helps you to calculate how many days will you have for preparing your exam.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["exam"],
    python_requires=">=3.6",
    install_requires=[
        "pendulum"
    ],
    
)