#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `moodlesg` package."""

import pytest

import moodlesg.math.base as base
import moodlesg.math.functions.common as fcommon


def test_Expression():
    """Test string format of MoodleVar."""
    a = base.Expression('[[a]]')
    assert str(a) == '[[a]]'


def test_grade_var():
    """ Test string format of GradeVar."""
    a = base.grade_var('a')
    assert str(a) == '[[a]]'


def test_AnsVar():
    """Test string format of AnsVar."""
    a = base.answer_var('a')
    assert str(a) == '{a}'

def test_add_expr():
    a = base.grade_var('a')
    b = base.grade_var('b')
    assert str(a + b) == "([[a]] + [[b]])"

def test_mul_expr():
    a = base.grade_var('a')
    b = base.grade_var('b')
    assert str(a * b) == "([[a]] * [[b]])"

def test_div_expr():
    a = base.grade_var('a')
    assert str(a / 2) == "([[a]]/2)"

def test_pow_expr():
    a = base.grade_var('a')
    assert str(3**a) == "(3 ^ [[a]])"

def test_sum_exprs():
    a = base.grade_var('a')
    b = base.grade_var('b')
    c = base.grade_var('c')
    assert str(fcommon.sum(a, b, c)) == "sum([[a]];[[b]];[[c]])"

def test_average_arrays():
    a = base.grade_var('a')
    b = base.grade_var('b')
    c = base.grade_var('c')
    abc = [a, b, c]
    assert str(fcommon.average(abc)) == "average([[a]];[[b]];[[c]])"
