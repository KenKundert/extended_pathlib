Extended PathLib
================

This package monkey-patches some useful extensions on to pathlib from the Python 
standard library. These extensions are only supported on Posix systems.

Once installed, you can simply import Path from extended_pathlib just as you 
would from pathlib, and use the new functionality::

    >>> from extended_pathlib import Path

    >>> tmp = Path('/tmp')
    >>> tmp.is_readable()
    True


Installation
------------

Use 'pip3 install extended_pathlib' to install. Requires Python2.7 or Python3.3 
or better.

.. image:: https://travis-ci.org/KenKundert/extended_pathlib.svg?branch=master
    :target: https://travis-ci.org/KenKundert/extended_pathlib


File Types
----------

is_readable
~~~~~~~~~~~

Returns True if the given path points to an existing file or directory that is 
readable.

   >>> Path('/usr/bin/python').is_readable()
   True

is_writable
~~~~~~~~~~~

Returns True if the given path points to an existing file or directory that is 
writable.

   >>> Path('/usr/bin/python').is_writable()
   False

is_executable
~~~~~~~~~~~~~

Returns True if the given path points to an existing file or directory that is 
executable.

   >>> Path('/usr/bin/python').is_executable()
   True

is_hidden
~~~~~~~~~

Returns True if the given path points to an existing file or directory that is 
hidden (starts with '.').

   >>> Path('/usr/bin/python').is_hidden()
   False


path_from
~~~~~~~~~

Returns relative path from start as a path object.
This differs from Path.relative_to() in that relative_to() will not return
a path that starts with '..'.

    >>> cwd = Path('.')
    >>> cwd.path_from('..')
    PosixPath('tests')


sans_ext
~~~~~~~~

Removes the file extension.
This differs from Path.stem, which returns the final path component
stripped of its extension. This returns the full path stripped
of its extension.

    >>> Path('a/b.c').sans_ext()
    PosixPath('a/b')


write_bytes
~~~~~~~~~~~

Writes a binary file.
This is the standard pathlib write_bytes() that was introduced in Python3.5, but 
back-ported to earlier versions.


write_text
~~~~~~~~~~

Reads a binary file.
This is the standard pathlib write_text() that was introduced in Python3.5, but 
back-ported to earlier versions.


read_bytes
~~~~~~~~~~

Reads a binary file.
This is the standard pathlib read_bytes() that was introduced in Python3.5, but 
back-ported to earlier versions.


read_text
~~~~~~~~~

Reads a text file.
This is the standard pathlib read_text() that was introduced in Python3.5, but 
back-ported to earlier versions.


expanduser
~~~~~~~~~~

Expand leading tilde (~) in paths.
