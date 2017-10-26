# MoodleSG

MoodleSG (Moodle String Generator) is a python package with the purpose of help to generate common strings using for users (not admin level) when manage a course in moodle, e.g. answer formulas, grade formulas and question generation in markdown or XML.  

This package is not intended to use as admin level and is developed because management of some formulas are very uncomfortable because not variable is available as user level (some universities has very strange methods for grade calculation and vary each semester or some math problems has many substitutions). So, you finish with a longer formula with pattern repetitions that you add manually and many brackets and then your math expression for grade or answer formula is very susceptible to fail.  

Also, you can think in some automatic question generation that Moodle not support but you can create and export as a question database of questions (not calculated questions that support numeric or text variables only -not both in the same question-) or import from a question database backup and modify that.  

## Features and RoadMap

- [ ] String generation of moodle math formulas.  
  - [ ] [Grade calculations](https://docs.moodle.org/33/en/Grade_calculations#Calculation_functions).  
  - [ ] [Calculated question](https://docs.moodle.org/33/en/Calculated_question_type#Available_functions).  
- [ ] String generation of questions for text plain moodle editor (not XML nor HTML).  
- [ ] Export of question strings to moodle supported [question import formats](https://docs.moodle.org/33/en/Import_questions).  
- [ ] Import of question strings from moodle [question export formats](https://docs.moodle.org/33/en/Export_questions).  
- [ ] Management [question bank](https://docs.moodle.org/33/en/Question_bank) locally and generate from collections of question strings.  
