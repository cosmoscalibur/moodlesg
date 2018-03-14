=======================
Moodle String Generator
=======================


.. image:: https://img.shields.io/pypi/v/moodlesg.svg
        :target: https://pypi.python.org/pypi/moodlesg

.. image:: https://img.shields.io/travis/cosmoscalibur/moodlesg.svg
        :target: https://travis-ci.org/cosmoscalibur/moodlesg

.. image:: https://readthedocs.org/projects/moodlesg/badge/?version=latest
        :target: https://moodlesg.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/cosmoscalibur/moodlesg/shield.svg
     :target: https://pyup.io/repos/github/cosmoscalibur/moodlesg/
     :alt: Updates


Python package to generate common strings used in moodle for users (not admin level) and manage exported files from moodle and generate files for import.


* Free software: MIT license
* Documentation: https://moodlesg.readthedocs.io.


Description
-----------

MoodleSG (Moodle String Generator) is a python package with the purpose of help to generate common strings using for users (not admin level) when manage a course in moodle, e.g. answer formulas, grade formulas and question generation in markdown or XML.

This package is not intended to use as admin level and is developed because management of some formulas are very uncomfortable because not variable is available as user level (some universities has very strange methods for grade calculation and vary each semester or some math problems has many substitutions). So, you finish with a longer formula with pattern repetitions that you add manually and many brackets and then your math expression for grade or answer formula is very susceptible to fail.

Also, you can think in some automatic question generation that Moodle not support but you can create and export as a question database of questions (not calculated questions that support numeric or text variables only -not both in the same question-) or import from a question database backup and modify that.

Features
--------

* [ ] String generation of moodle math formulas.

  * [ ] `Grade calculations <https://docs.moodle.org/33/en/Grade_calculations#Calculation_functions>`_.
  * [ ] `Calculated question <https://docs.moodle.org/33/en/Calculated_question_type#Available_functions>`_.
* [ ] String generation of questions for text plain moodle editor (not XML nor HTML).
* [ ] String manipulation of question bank.

  * [ ] Export of question strings to moodle supported `question import formats <https://docs.moodle.org/33/en/Import_questions>`_.
  * [ ] Import of question strings from moodle `question export formats <https://docs.moodle.org/33/en/Export_questions>`_.
  * [ ] Management `question bank <https://docs.moodle.org/33/en/Question_bank>`_ locally and generate from collections of question strings.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
