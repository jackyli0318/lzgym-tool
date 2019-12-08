import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lzgym_tool",
    version="0.0.3",
    author="Jacky Lee",
    author_email="emulezhi@gmail.com",
    description="LZGYM's Tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jackyli0318/lzgym-tool",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)