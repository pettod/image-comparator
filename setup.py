from setuptools import setup
from imco import __version__


setup(
    name="imco",
    version=__version__,
    description="Python package to compare images with metrics",
    url="https://github.com/pettod/imco",
    packages=["imco"],
    install_requires=open("requirements.txt").read().splitlines(),
    include_package_data=True,
    zip_safe=True,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Topic :: System :: Monitoring",
    ],
)