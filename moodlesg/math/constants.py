"""
Module :code:`constants` define common math moodle constants between grade and
answer calculations.

In Moodle, actually there is no predefined constant that is allowed other than
pi() as a function without parameter. With this module, is posible use
:math:`\\pi` as a constant (not call to a function) and define others
constants.
"""
from moodlesg.math.base import Expression

__all__ = ['PI']

PI = Expression("pi()")
"""
Define :math:`\\pi`.
"""
