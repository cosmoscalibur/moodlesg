#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module :code:`classes` contains basic classes required for building
moodle mathematical expressions.

Created on Tue Mar 13 09:01:57 2018

@author: cosmoscalibur
"""


class Expression():
    """
    Implement a generic mathematical expression in moodle format.
    """

    def __init__(self, expression):
        self.root = expression

    def __repr__(self):
        return type(self).__name__ + '({})'.format(self.root)


class MoodleVar(Expression):
    """
    Implement a generic variable for Moodle derived from :class:`Expression`.

    :param varname: Name of the moodle variable.
    :type varname: str
    :param ldelim: Left delimiter of the moodle variable.
    :type ldelim: str
    :param rdelim: Right delimiter of the moodle variable.

    We can create a moodle variable as follow::

    >>> from moodlesg.math import classes
    >>> a = classes.MoodleVar('a', '[[', ']]')

    We can obtain:

    >>> print(a)
    [[a]]

    .. seealso:: :class:`GradeVar`, :class:`AnsVar`.
    """
    def __init__(self, varname, ldelim, rdelim):
        """
        Constructor of :class:`MoodleVar`.
        """
        self.root = varname
        self.ldelim = ldelim
        self.rdelim = rdelim

    def __str__(self):
        """
        Concatenate delimiters with name of moodle variable.
        """
        return self.ldelim + self.root + self.rdelim


class GradeVar(MoodleVar):
    """
    Implement a moodle variable specific for using in grade calculation.

    :param varname: Moodle ID Number of the activity.
    :type varname: str

    We can create a moodle variable as follow:

    >>> from moodlesg.math import classes
    >>> a = classes.GradeVar('a')

    And we obtain:

    >>> print(a)
    [[a]]

    .. seealso:: :class:`MoodleVar`, :class:`AnsVar`.
    """
    def __init__(self, varname):
        """
        Constructor of :class:`GradeVar`.
        """
        self.root = varname
        self.ldelim = "[["
        self.rdelim = "]]"


class AnsVar(MoodleVar):
    """
    Implement a moodle variable specific for using in correct answer
    calculation.

    .. seealso:: :class:`MoodleVar`, :class:`GradeVar`.
    """
    def __init__(self, varname):
        self.root = varname
        self.ldelim = "\{"
        self.rdelim = "\}"
