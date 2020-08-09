import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setuptools.setup(
    name="prohosting24api",
    version="0.1.1",
    author="AdriBloober",
    author_email="adrianbloober@gmail.com",
    description="Communicate with the ProHosting24 internal api.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AdriBloober/Python_ProHosting24API",
    packages=["prohosting24"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
)
