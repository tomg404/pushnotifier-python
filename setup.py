import setuptools
import pushnotifier

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name=pushnotifier.__name__,
    version=pushnotifier.__version__,
    author="Tom Gaimann",
    author_email="tom.gaimann@outlook.com",
    description="A python package for an easy use of the service from https://pushnotifier.de/",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tomg404/pushnotifier-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
