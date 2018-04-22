ncdu-dropbox
============

Generates `ncdu <http://dev.yorhel.nl/ncdu>`__ compatible JSON file for
Dropbox.

You can use this script (with ncdu) to visualize which files and folders
are taking up all the space in your dropbox.

Usage
=====

First, generate an oauth token from Dropbox's `app
console <http://dropbox.com/developers/apps>`__.

.. code:: bash

    $ ncdu-dropbox --token $TOKEN -o dropbox.json
    $ ncdu -f dropbox.json

Caution: Due to limitations in Dropbox API, it takes about 10s to fetch
the information of ~5,000 files and folders. So, if you have millions of
files in your Dropbox, this script may be running for hours.

Related projects
================

See `ncdu-s3 <https://github.com/EverythingMe/ncdu-s3>`__.
