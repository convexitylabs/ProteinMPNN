#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name="proteinmpnn",
    version="1.0.0",
    description="ProteinMPNN: Robust deep learning-based protein sequence design",
    author="J. Dauparas, I. Anishchenko, N. Bennett, H. Bai, R. J. Ragotte, L. F. Milles, B. I. M. Wicky, A. Courbet, R. J. de Haas, N. Bethel, P. J. Y. Leung, T. F. Huddy, S. Pellock, D. Tischer, F. Chan, B. Koepnick, H. Nguyen, A. Kang, B. Sankaran, A. K. Bera, N. P. King, D. Baker",
    author_email="",
    url="https://github.com/dauparas/ProteinMPNN",
    packages=find_packages(),
    py_modules=[
        "protein_mpnn_run",
        "protein_mpnn_utils",
    ],
    python_requires=">=3.6",
    install_requires=[
        "torch",
        "numpy",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    include_package_data=True,
    package_data={
        "": ["*.pt", "*.pth", "*.ckpt"],
        "proteinmpnn": [
            "ca_model_weights/*.pt",
            "vanilla_model_weights/*.pt", 
            "soluble_model_weights/*.pt",
        ],
    },
)