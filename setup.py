# setup.py

from setuptools import setup, find_packages

setup(
    name="market-regime-detection",
    version="0.1.0",
    description="A toolkit for market regime detection using various methods",
    author="James Crowley",
    author_email="james.crowley.to@gmail.com",
    packages=find_packages(where="src"),
        package_dir={"": "src"},
        install_requires=[
            "numpy",
            "pandas",
            "scipy",
            "pyyaml",
            "matplotlib",
            "seaborn",
            "scikit-learn",
            "hmmlearn",
            "jupyter",
            "jupyterlab",
            "ruptures"
        ],
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent"
        ],
        python_requires=">=3.10"
)