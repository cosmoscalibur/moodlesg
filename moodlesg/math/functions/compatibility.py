"""
This module create a common interface to call math functions of grade and
answer calculation. Some functions in moodle version has different names and
other cases has no equivalent (grade calculation support less functions).

Examples
--------

In Moodle you can evaluate a natural logarithm in both, grade and answer
calculation, but the function has different name. If you need to evaluate
in grade calculation :code:`ln` is the function but in answer calculation
is :code:`log`. With MoodleSG both cases are covered with :func:`log`
(common convention in programming languages).

>>> mm.mmParams.grade()
>>> a = mm.moodle_var('a')
>>> mm.log(a)
Expression('ln([[a]])')

>>> mm.mmParams.answer()
>>> b = mm.moodle_var('b')
>>> mm.log(b)
Expression('log({b})')
"""
from moodlesg.math.base import Expression, mmParams

def log(expr):
    """
    Return natural logarithm of a expression.
    """
    if mmParams.math_type == 'grade':
        fun_string = "ln"
    else:
        fun_string = "log"
    return Expression("{0}({1})".format(fun_string, str(expr)))

def log10(expr):
    """
    Return base-10 logarithm of a expression.
    """
    if mmParams.math_type == 'grade':
        fun_string = "log"
    else:
        fun_string = "log10"
    return Expression("{0}({1})".format(fun_string, str(expr)))

def mod(expr1, expr2):
    """
    Calculates the remainder of a division.

    Also supported in the builtin :code:`%` (modulus) operator.
    """
    return Expression.__mod__(expr1, expr2)

def pow(expr1, expr2):
    """
    Exponential expression. Raises a number to the power of another.
    """
    if mmParams.math_type == 'grade':
        fun_string = "power"
    else:
        fun_string = "pow"
    return Expression("{0}({1}{2}{3})".format(fun_string, str(expr1), \
                        mmParams.list_sep, str(expr2)))


"""
atan2 	Arc tangent of two variables -- pass in two values like (y, x), and you'll get the atan(y/x), adjusted to the proper quadrant. (Note: The variables are in the reverse order to atan2(x,y) in Excel) Output is radians.
bindec 	Binary to decimal
decbin 	Decimal to binary
decoct 	Decimal to octal
deg2rad 	Converts the number in degrees to the radian equivalent
expm1 	Returns exp(number) - 1, computed in a way that is accurate even when the value of number is close to zero
is_finite 	Finds whether a value is a legal finite number
is_infinite 	Finds whether a value is infinite
is_nan 	Finds whether a value is not a number
log1p 	Returns log(1 + number), computed in a way that is accurate even when the value of number is close to zero
octdec 	Octal to decimal
rad2deg 	Converts the radian number to the equivalent number in degrees
rand 	Generate a random integer
"""
