# Copyright (c) 2010 Jean-Paul Calderone
# See LICENSE file for details.

from distutils.core import setup

setup(
    name="filepath",
    description="Object-oriented filesystem path representation.",
    version="0.2",
    author="Twisted Matrix Labs",
    author_email="twisted-python@twistedmatrix.com",
    url="http://twistedmatrix.com/",
    packages=["filepath", "filepath.test"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 2.4",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Filesystems",
        ])
