#!/usr/bin/python
# -*- coding: utf8 -*-

"""
Provides the error classes raised by the functions of the cjklib module.

@group Exceptions: *Error
"""

class ConversionError(Exception):
    """
    A ConversionError is raised on a general conversion exception (e.g. no
    mapping).
    """

class AmbiguousConversionError(ConversionError):
    """
    An AmbiguousConversionError is raised when a conversion of one entity from
    one reading to another is ambiguous.
    """

class DecompositionError(Exception):
    """
    A DecompositionError is raised on a general decomposition exception (e.g.
    reading string has a bad format).
    """

class AmbiguousDecompositionError(DecompositionError):
    """
    An AmbiguousDecompositionError is raised when decomposition of a string
    written in a reading is ambiguous.
    """

class InvalidEntityError(DecompositionError):
    """
    An InvalidEntityError is raised when a reading entity given (e.g. through
    decomposition) is invalid for the current reading.
    """

class NoInformationError(Exception):
    """
    A NoInformationError is raised when the database lacks information for the
    given lookup value.
    """

class UnsupportedError(Exception):
    """
    An UnsupportedError is raised when the given option is not supported.
    """
