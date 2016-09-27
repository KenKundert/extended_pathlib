# pathlib -- extends system pathlib

# License {{{1
# Copyright (C) 2016 Kenneth S. Kundert
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].

__version__ = '0.0.0'

# Imports {{{1
from pathlib import Path, PosixPath
import os


# is_readable {{{1
def _is_readable(path):
    """
    Tests whether path exists and is readable.

    >>> from extended_pathlib import Path
    >>> Path('/usr/bin/python').is_readable()
    True

    """
    return os.access(str(path), os.R_OK)

PosixPath.is_readable = _is_readable

# is_writable {{{1
def _is_writable(path):
    """
    Tests whether path exists and is writable.

    >>> Path('/usr/bin/python').is_writable()
    False

    """
    return os.access(str(path), os.W_OK)

PosixPath.is_writable = _is_writable

# is_executable {{{1
def _is_executable(path):
    """
    Tests whether path exists and is executable.

    >>> Path('/usr/bin/python').is_executable()
    True

    """
    return os.access(str(path), os.X_OK)

PosixPath.is_executable = _is_executable

# is_hidden {{{1
def _is_hidden(path):
    """
    Tests whether path exists and is hidden.

    >>> Path('/usr/bin/python').is_hidden()
    False

    """
    return path.exists() and str(path).startswith('.')

PosixPath.is_hidden = _is_hidden

# path_from {{{1
def _path_from(path, start):
    """
    Returns relative path from start as a path object.
    This differs from Path.relative_to() in that relative_to() will not return a
    path that starts with '..'.

    >>> Path('.').path_from('..')
    PosixPath('tests')

    """
    return Path(os.path.relpath(str(path), str(start)))

PosixPath.path_from = _path_from

# sans_ext {{{1
def _sans_ext(path):
    """
    Removes the file extension.
    This differs from Path.stem, which returns the final path component
    stripped of its extension. This returns the full path stripped of its
    extension.

    >>> Path('a/b.c').sans_ext()
    PosixPath('a/b')

    """
    return path.parent / path.stem

PosixPath.sans_ext = _sans_ext
