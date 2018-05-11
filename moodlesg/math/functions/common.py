# -*- coding: utf-8 -*-

"""
This module implement moodle math functions that are common between
grade and answer calculation.
"""

from moodlesg.math.base import Expression
from moodlesg.math.settings import list_sep


def sum(expr1, *expr2):
    """
    Returns the sum of all arguments.
    """
    expr2_el = len(expr2)
    if expr2_el > 0:
        expr2_add = list_sep.join([str(expr) for expr in expr2])
        expr = list_sep.join([str(expr1), expr2_add])
    else:
        expr = list_sep.join([str(expr) for expr in expr1])
    return Expression('sum({0})'.format(expr))


def average(expr1, *expr2):
    """
    Returns the average of the values in a list of arguments.
    """
    expr2_el = len(expr2)
    if expr2_el > 0:
        expr2_add = list_sep.join([str(expr) for expr in expr2])
        expr = list_sep.join([str(expr1), expr2_add])
    else:
        expr = list_sep.join([str(expr) for expr in expr1])
    return Expression('average({0})'.format(expr))


def max(expr1, *expr2):
    """
    Returns the maximum value in a list of arguments.
    """
    expr2_el = len(expr2)
    if expr2_el > 0:
        expr2_add = list_sep.join([str(expr) for expr in expr2])
        expr = list_sep.join([str(expr1), expr2_add])
    else:
        expr = list_sep.join([str(expr) for expr in expr1])
    return Expression('max({0})'.format(expr))


def min(expr1, *expr2):
    """
    Returns the minimum value in a list of arguments.
    """
    expr2_el = len(expr2)
    if expr2_el > 0:
        expr2_add = list_sep.join([str(expr) for expr in expr2])
        expr = list_sep.join([str(expr1), expr2_add])
    else:
        expr = list_sep.join([str(expr) for expr in expr1])
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


def power(expr1, expr2):
    """
    Raises a number to the power of another.
    """
    return Expression('power({0}{1}{2})'.format(str(expr1), list_sep, str(expr2)))


def mod(expr1, expr2):
    """
    Calculates the remainder of a division.
    """
    return Expression.__mod__(expr1, expr2)


def abs(expr):
    """
    Absolute value.
    """
    return Expression.__abs__(expr)

"""
    sin()
    sinh()
    asin() <- arcsin()
    asinh() <- arcsinh()
    cos()
    cosh()
    acos() <- arccos()
    acosh() <- arccosh()
    tan()
    tanh()
    atan() <- arctan()
    atanh() <- arctanh()
    sqrt()
    ln() -> log
    log() -> log10
    exp()
"""
