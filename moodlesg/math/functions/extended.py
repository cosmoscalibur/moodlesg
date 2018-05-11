from moodlesg.math.base import Expression, _bool


def trunc(expr):
    return Expression.__trunc__(expr)


def bool(expr):
    """
    Implement truth value testing.

    Expression is considered true if its result is nonzero.
    """
    return _bool(expr)
