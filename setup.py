from sys import version_info
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.rst") as f:
    readme = f.read()

if version_info < (3, 4):
    requirements = ["pathlib", "six"]
else:
    requirements = ["six"]

setup(
    name = "extended_pathlib",
    version = "0.4.1",
    description = "shell library",
    long_description = readme,
    author = "Ken Kundert",
    author_email = "extended_pathlib@nurdletech.com",
    py_modules = ["extended_pathlib"],
    url = "http://nurdletech.com/linux-utilities/extended_pathlib",
    download_url = "https://github.com/kenkundert/extended_pathlib/tarball/master",
    license = "GPLv3+",
    zip_safe = False,
    install_requires = requirements,
    setup_requires='pytest-runner>=2.0'.split(),
    tests_require='pytest'.split(),
    keywords = ["extended", "pathlib"],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Utilities",
    ],
)
