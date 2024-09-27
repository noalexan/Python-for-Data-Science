from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ft_package",
    version="0.1.0",
    author="Noah Alexandre",
    author_email="noalexan@student.42.fr",
    description="A short description of my package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/noalexan/Python-for-Data-Science",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
