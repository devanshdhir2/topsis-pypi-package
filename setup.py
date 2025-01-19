from setuptools import setup, find_packages

setup(
    name="Topsis-Devansh-102203449",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
    ],
    author="Devansh Dhir",
    author_email="dhir.devansh@gmail.com",
    description="A TOPSIS implementation package for Multiple Criteria Decision Making",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/devanshdhir2/topsis-pypi-package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'topsis=topsis.topsis:main',
        ],
    },
)