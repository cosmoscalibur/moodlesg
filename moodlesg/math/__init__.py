"""
Module :code:`moodlesg.math` implements a python interface to math manipulation
requiered in grade_ and answer_ moodle formulas.

You can use variable assigment, relation operators, mixing types (moodle
expressions with python data types) and commons names of functions in both type
of formulas, grade and answers.

References
----------

.. [grade] `Grade calculations <https://docs.moodle.org/34/en/Grade_calculations>`_.
            Moodle 3.4 Docs.

.. [answer] `Calculated question type <https://docs.moodle.org/34/en/Calculated_question_type>`_
             Moodle 3.4 Docs.
"""

from moodlesg.math.base import (Expression, grade_var, answer_var, moodle_var,
                                mmParams)
from moodlesg.math.constants import PI
from moodlesg.math.functions.common import (max, min, average, sum, floor,
                                            ceil, round, abs,
                                            sin, cos, tan, asin, acos, atan,
                                            sinh, cosh, tanh, asinh, acosh,
                                            atanh, sqrt, exp)
from moodlesg.math.functions.compatibility import (log, log10, mod, pow)
from moodlesg.math.functions.extended import trunc, bool
