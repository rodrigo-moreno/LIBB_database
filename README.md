# LIBB_database
A database for the information on the labs and courses taken by the students in the Licenciatura en Investigación Biomédica Básica.
For now, the single script that I have takes no argument. The file asks for a CSV to read, which will be input. This can probably be changed to a command-line argument later on. The script reads the CSV, changes the separator to tabs, and writes a new file with the "clean" information. It then adds entries to two dictionaries:

      1) Labs: Contains the information on the labs where the students have been in. For now, it takes all that information,
      without considering WHEN they were taken. As the grade given is in tuple form (grade, timestamp), this feature can be
      added later on. In this case, the time of 5 years has been proposed.

      2) Courses: Similar as the previous dictionary, but with the classes. The time of 2 years is proposed.
      
The "shape" of the dictionaries is as follows:
      Labs{area1: {Doctor1: {Year1: {Grade1: (float, timestamp), Grade2:(),...}, Year2{...}}, Doctor2: {...}}, area2: {...}}
      The shape for Courses is not yet clear.
      
The last part of the script writes a JSON file that saves both dictionaries to a file. A new feature needs to be added in which the script looks for previously saved JSON files.
