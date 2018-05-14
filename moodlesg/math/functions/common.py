# -*- coding: utf-8 -*-
"""
This module implement moodle math functions that are common between
grade and answer calculation.
"""

from moodlesg.math.base import Expression, mmParams


def sum(expr1, *expr2):
    """
    Returns the sum of all arguments.
    """
    expr2_el = len(expr2)
    if expr2_el > 0:
        expr2_add = mmParams.list_sep.join([str(expr) for expr in expr2])
        expr = mmParams.list_sep.join([str(expr1), expr2_add])
    else:
        expr = mmParams.list_sep.join([str(expr) for expr in expr1])
    return Expression('sum({0})'.format(expr))


def average(expr1, *expr2):
    """
    Returns the average of the values in a list of arguments.
    """
    expr2_el = len(expr2)
    if expr2_el > 0:
        expr2_add = mmParams.list_sep.join([str(expr) for expr in expr2])
        expr = mmParams.list_sep.join([str(expr1), expr2_add])
    else:
        expr = mmParams.list_sep.join([str(expr) for expr in expr1])
    return Expression('average({0})'.format(expr))


def max(expr1, *expr2):
    """
    Returns the maximum value in a list of arguments.
    """
    expr2_el = len(expr2)
    if expr2_el > 0:
        expr2_add = mmParams.list_sep.join([str(expr) for expr in expr2])
        expr = mmParams.list_sep.join([str(expr1), expr2_add])
    else:
        expr = mmParams.list_sep.join([str(expr) for expr in expr1])
    return Expression('max({0})'.format(expr))


def min(expr1, *expr2):
    """
    Returns the minimum value in a list of arguments.
    """
    expr2_el = len(expr2)
    if expr2_el > 0:
        expr2_add = mmParams.list_sep.join([str(expr) for expr in expr2])
        expr = mmParams.list_sep.join([str(expr1), expr2_add])
    else:
        expr = mmParams.list_sep.join([str(expr) for expr in expr1])
    return Expression('min({0})'.format(expr))


def floor(expr):
    """
    Maps a real number to the largest previous integer.
    """
    return Expression.__floor__(expr)


def ceil(expr):
    """
    Maps a real number to the smallest following integer.
    """
    return Expression.__ceil__(expr)


def round(expr, count):
    """
    Rounds number to count decimal digits.
    """
    return Expression.__round__(expr, count)


def abs(expr):
    """
    Absolute value.
    """
    return Expression.__abs__(expr)


def sin(expr):
    """
    Sine -- in radians!!! Convert your degree measurement to radians before you take the sin of it.
    """
    return Expression('sin({0})'.format(str(expr)))


def sinh(expr):
    """
    Hyperbolic sine -- in radians!!! Convert your degree measurement to radians before you take the sinh of it.
    """
    return Expression('sinh({0})'.format(str(expr)))


def cos(expr):
    """
    Cosine -- in radians!!! Convert your degree measurement to radians before you take the cos of it.
    """
    return Expression('cos({0})'.format(str(expr)))


def cosh(expr):
    """
    Hyperbolic cosine -- in radians!!! Convert your degree measurement to radians before you take the cosh of it.
    """
    return Expression('cosh({0})'.format(str(expr)))


def tan(expr):
    """
    Tangent -- in radians!!! Convert your degree measurement to radians before you take the tan of it.
    """
    return Expression('tan({0})'.format(str(expr)))


def tanh(expr):
    """
    Hyperbolic tangent -- in radians!!! Convert your degree measurement to radians before you take the tanh of it.
    """
    return Expression('tanh({0})'.format(str(expr)))


def asin(expr):
    """
    Arc sine -- output in radians.

    It is the same that :code:`arcsin` moodle math function.
    """
    return Expression('asin({0})'.format(str(expr)))


def asinh(expr):
    """
    Inverse hyperbolic sine.-- output in radians.

    It is the same that :code:`arcsinh` moodle math function.
    """
    return Expression('asinh({0})'.format(str(expr)))


def acos(expr):
    """
    Arc cosine -- output in radians.

    It is the same that :code:`arccos` moodle math function.
    """
    return Expression('acos({0})'.format(str(expr)))


def acosh(expr):
    """
    Inverse hyperbolic cosine -- output in radians.

    It is the same that :code:`arccosh` moodle math function.
    """
    return Expression('acosh({0})'.format(str(expr)))


def atan(expr):
    """
    Arc tangent -- output in radians.

    It is the same that :code:`arctan` moodle math function.
    """
    return Expression('atan({0})'.format(str(expr)))


def atanh(expr):
    """
    Inverse hyperbolic tangent-- output in radians.

    It is the same that :code:`arctanh` moodle math function.
    """
    return Expression('atanh({0})'.format(str(expr)))


def sqrt(expr):
    """
    Square root.
    """
    return Expression('sqrt({0})'.format(str(expr)))


def exp(expr):
    """
    Calculates the exponent of e.
    """
    return Expression('exp({0})'.format(str(expr)))
