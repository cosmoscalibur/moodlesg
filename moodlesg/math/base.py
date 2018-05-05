#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module :code:`_base` contains definitions required for building
moodle mathematical expressions.
"""


class Expression():
    """
    Implement a generic mathematical expression in moodle format.

    :param expression: Math moodle expression.
    :type expression: str
    """

    def __init__(self, expression):
        self.root = expression

    def __str__(self):
        return self.root

    def __repr__(self):
        return 'Expression({})'.format(self.root)

    # Numeric type operations

    def __add__(self, expression):
        return Expression('({} + {})'.format(self.root, expression.root))

    def __sub__(self, expression):
        return Expression('({} - {})'.format(self.root, expression.root))

    def __mul__(self, expression):
        return Expression('({} * {})'.format(self.root, expression.root))

    def __truediv__(self, expression):
        return Expression('({} / {})'.format(self.root, expression.root))

    def __floordiv__(self, expression):
        return Expression('floor{}'.format(self.root / expression.root))

    def __mod__(self, expression):
        return Expression('mod({}, {})'.format(self.root, expression.root))

    def __pow__(self, expression):
        return Expression('({} ^ {})'.format(self.root, expression.root))

    def __neg__(self):
        return Expression('-{}'.format(self.root))

    def __abs__(self):
        return Expression('abs{}'.format(self.root))

    # Container type operations

    def __contains__(self, expression):
        return expression.root in self.root


def grade_var(id_activity):
    """
    Implement a moodle variable specific for using in grade calculation.

    :param id_activity: Moodle ID of the activity.
    :type id_activity: str
    :return: Moodle ID ready for grade calculation.
    :rtype: Expression


    We can create a moodle variable as follow:

    >>> from moodlesg.math import base
    >>> a = base.grade_var('a')

    And we obtain:

    >>> print(a)
    [[a]]

    .. seealso:: :class:`Expression`, :func:`answer_var`.
    """
    return Expression('[[{}]]'.format(id_activity))


def answer_var(answer_variable):
    """
    Implement a moodle variable specific for using in correct answer
    calculation.

    .. seealso:: :class:`Expression`, :func:`grade_var`.
    """
    return Expression('{{ {} }}'.format(answer_variable))
