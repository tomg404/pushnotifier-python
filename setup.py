import setuptools
import pushnotifier

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name=pushnotifier.__name__,
    version=pushnotifier.__version__,
    author="Tom Gaimann",
    author_email="tom.gaimann+pushnotifier@outlook.com",
    description="A python package for easy interaction with https://pushnotifier.de/",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tomg404/pushnotifier-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
