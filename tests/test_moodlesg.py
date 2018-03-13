#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `moodlesg` package."""

import pytest

import moodlesg.math.classes as classes


def test_MoodleVar():
    """Test string format of MoodleVar."""
    a = classes.MoodleVar('a', '[[', ']]')
    assert str(a) == '[[a]]'


def test_GradeVar():
    """ Test string format of GradeVar."""
    a = classes.GradeVar('a')
    assert str(a) == '[[a]]'


def test_AnsVar():
    """Test string format of AnsVar."""
    a = classes.AnsVar('a')
    assert str(a) == '\{a\}'
