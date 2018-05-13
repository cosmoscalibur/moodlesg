#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module :code:`base` contains definitions required for building
moodle mathematical expressions.
"""

from moodlesg.math.settings import decimal_sep, list_sep, math_type
from math import ceil, floor


def _add(expr1, expr2):
    return Expression('({0} + {1})'.format(str(expr1), str(expr2)))


def _sub(expr1, expr2):
    return Expression('({0} - {1})'.format(str(expr1), str(expr2)))


def _mul(expr1, expr2):
    return Expression('({0} * {1})'.format(str(expr1), str(expr2)))


def _div(expr1, expr2):
    return Expression('({0}/{1})'.format(str(expr1), str(expr2)))


def _mod(expr1, expr2):
    return Expression('mod({0}{1}{2})'.format(
        str(expr1), list_sep, str(expr2)))


def _pow(expr1, expr2):
    return Expression('({0} ^ {1})'.format(str(expr1), str(expr2)))


def _bool(expr):
    return ceil(abs(expr) / (1 + abs(expr)))


def _not(expr):
    return abs(expr - 1)


class Expression():
    """Implement a generic mathematical expression in moodle format.

    Args:
        expression (str): Math moodle expression.

    Returns:
        :obj:`Expression`: Moodle math object.

    Examples:
        >>> str(mm.Expression('a'))
        a

        >>> a = mm.Expression('a')
        >>> b = mm.Expression('b')

        >>> str(a + b)
        (a + b)
        >>> str(a + 1)
        (a + 1)
    """

    def __init__(self, expression):

        self.root = expression

    # String type methods
    def __str__(self):
        return self.root

    def __repr__(self):
        return "Expression('{0}')".format(str(self))

    # Math type methods
    def __round__(self, count):
        return Expression('round({0}{1}{2})'.format(
            str(self), list_sep, str(count)))

    def __ceil__(self):
        return Expression('ceil({0})'.format(str(self)))

    def __floor__(self):
        return Expression('floor({0})'.format(str(self)))

    def __trunc__(self):
        return (self < 0) * ceil(self) + (self >= 0) * floor(self)

    # Numeric type operations

    def __add__(self, expression):
        return _add(self, expression)

    def __radd__(self, expression):
        return _add(expression, self)

    def __sub__(self, expression):
        return _sub(self, expression)

    def __rsub__(self, expression):
        return _sub(expression, self)

    def __mul__(self, expression):
        return _mul(self, expression)

    def __rmul__(self, expression):
        return _mul(expression, self)

    def __truediv__(self, expression):
        return _div(self, expression)

    def __rtruediv__(self, expression):
        return _div(expression, self)

    def __floordiv__(self, expression):
        return floor(self / expression)

    def __rfloordiv__(self, expression):
        return floor(expression / self)

    def __mod__(self, expression):
        return _mod(self, expression)

    def __rmod__(self, expression):
        return _mod(expression, self)

    def __pow__(self, expression):
        return _pow(self, expression)

    def __rpow__(self, expression):
        return _pow(expression, self)

    def __neg__(self):
        return Expression('-({0})'.format(str(self)))

    def __pos__(self):
        return Expression(str(self))

    def __abs__(self):
        return Expression('abs({0})'.format(str(self)))

    # Relational operators
    def __ne__(self, expression):
        return _bool(self - expression)

    def __eq__(self, expression):
        return _not(self != expression)

    def __lt__(self, expression):
        diff = expression - self
        return _bool(diff + abs(diff))

    def __gt__(self, expression):
        diff = expression - self
        return _bool(diff - abs(diff))

    def __le__(self, expression):
        return _not(self > expression)

    def __ge__(self, expression):
        return _not(self < expression)

    # Bitwise operators (input must be 0 or 1)
    def __and__(self, expression):
        return self * expression

    def __or__(self, expression):
        return self + expression

    def __xor__(self, expression):
        return (self | expression) & (_not(self) | _not(expression))

    # Container type operations
    def __contains__(self, expression):
        return str(expression) in str(self)


def grade_var(id_activity):
    """Implement a moodle variable for using in grade calculation.

    Args:
        id_activity (str): Moodle ID of the activity.

    Returns:
        :obj:`Expression`: Moodle ID ready for grade calculation.

    Examples:
        We can create a moodle id activity for calculation as follow:

        >>> a = mm.grade_var('a')
        >>> str(a)
        [[a]]
        >>> str(a + 1)
        ([[a]] + 1)

    See Also:
        :class:`Expression`
        :func:`answer_var`

    """
    return Expression('[[{}]]'.format(id_activity))


def answer_var(answer_variable):
    """Implement a moodle variable for using in correct answer calculation.

    Args:
        answer_variable (str): Variable name string.

    Returns:
        :obj:`Expression`: Moodle variable ready for calculations.

    Examples:
        We can create a moodle answer variable for calculation as follow:

        >>> a = mm.answer_var('a')
        >>> str(a)
        {a}

    See Also:
        :class:`Expression`
        :func:`grade_var`.
    """
    return Expression('{{{}}}'.format(answer_variable))
