#!/usr/bin/python

from distutils.core import setup

setup(
    name="Poor-Mans-Spotify",
    version="0.16.10",
    description="Search, Stream and Download MP3",
    keywords=["MP3", "music", "audio", "search", "stream", "download"],
    author="nagev",
    author_email="np1nagev@gmail.com",
    url="http://github.com/np1/pms/",
    download_url="https://github.com/np1/pms/tarball/master",
    scripts=['pms'],
    package_data={"": ["LICENSE", "README.md"]},
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Environment :: Console",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "Topic :: Multimedia :: Sound/Audio :: Players",
        "Topic :: Internet :: WWW/HTTP"],
    long_description="""

.. image::http://badge.fury.io/py/Poor-Mans-Spotify.png
.. image::https://pypip.in/d/Poor-Mans-Spotify/badge.png

Description
-----------

This is a console based application and requires mplayer to be installed to
perform the streaming.  It's interactive so no arguments are needed, although
you can optionally add the search term as an argument. Eg: `pms beethovens 5th`

To install:

::

    sudo pip install Poor-Mans-Spotify

To run:

::

    pms


Screenshot
----------

.. image:: http://i.imgur.com/Oqyz5vk.png

"""
)
