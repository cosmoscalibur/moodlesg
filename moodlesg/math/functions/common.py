# -*- coding: utf-8 -*-

"""
This module implement moodle math functions that are common between
grade and answer calculation.
"""

from moodlesg.math.base import Expression
from moodlesg.math.settings import list_sep


def sum(expr1, *expr2):
    expr2_el = len(expr2)
    if expr2_el > 0:
        expr2_add = list_sep.join([str(expr) for expr in expr2])
        expr = list_sep.join([str(expr1), expr2_add])
    else:
        expr = list_sep.join([str(expr) for expr in expr1])
    return Expression('sum({})'.format(expr))


def average(expr1, *expr2):
    expr2_el = len(expr2)
    if expr2_el > 0:
        expr2_add = list_sep.join([str(expr) for expr in expr2])
        expr = list_sep.join([str(expr1), expr2_add])
    else:
        expr = list_sep.join([str(expr) for expr in expr1])
    return Expression('average({})'.format(expr))


def max(expr1, *expr2):
    expr2_el = len(expr2)
    if expr2_el > 0:
        expr2_add = list_sep.join([str(expr) for expr in expr2])
        expr = list_sep.join([str(expr1), expr2_add])
    else:
        expr = list_sep.join([str(expr) for expr in expr1])
    return Expression('max({})'.format(expr))


def min(expr1, *expr2):
    expr2_el = len(expr2)
    if expr2_el > 0:
        expr2_add = list_sep.join([str(expr) for expr in expr2])
        expr = list_sep.join([str(expr1), expr2_add])
    else:
        expr = list_sep.join([str(expr) for expr in expr1])
    return Expression('min({})'.format(expr))


def floor(expr):
    return Expression.__floor__(expr)


def ceil(expr):
    return Expression.__ceil__(expr)


def round(expr, count):
    return Expression.__round__(expr, count)
