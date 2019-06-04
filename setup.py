import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="pushnotifier",
    version="1.1.0",
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
