'''
THIS SCRIPT TAKES EITHER TWO COMPLETELY NEW DICTIONARIES (ON THE FIRST RUN) OR TWO PREVIOUSLY CREATED ONES.
IT THEN READS THE NEW CLEAN CSV FILE CREATED WITH cleaning.py AND SORTS THE INFORMATION IN THE CORRESPONDING
DICTIONARIES. LAST, IT REMOVES ALL INSTANCES IN WHICH THE INFORMATION IS TOO OLD, BE IT 5 YEARS IN THE CASE OF
Labs, OR TWO YEARS IN Courses.
'''



import json
import os
import os.path


def add.tutor(sub):
  '''
  THIS FUNCTION TAKES AS AN ARGUMENT A LIST WHICH REPRESENTS THE ELEMENTS OF A CSV LINE.
  IT THEN ADDS THE APPROPRIATE PARTS OF THE LINE TO THE Labs.
  '''
  area = sub[a][18]
  tut = sub[a][16]
  year = ceil(float(sub[a][3]/2)
  year = int(year)
  if area not in Labs.keys():
    Labs[area] = {tut: {year: {"Calidad": (sub[a][19], sub[a][0]), "Dedicacion": (sub[a][20], sub[a][0]), "Ambiente": (sub[a][21], sub[a][0]), "Aprendizaje": (sub[a][22], sub[a][0]), "Trato": (sub[a][23], sub[a][0])}}}
  elif tut not in Labs[area].keys():
   Labs[area][tut] = {year: {"Calidad": (sub[a][19], sub[a][0]), "Dedicacion": (sub[a][20], sub[a][0]), "Ambiente": (sub[a][21], sub[a][0]), "Aprendizaje": (sub[a][22], sub[a][0]), "Trato": (sub[a][23], sub[a][0])}}
  elif year not in Labs[area][tut].keys():
    Labs[area][tut][year] = {"Calidad": (sub[a][19], sub[a][0]), "Dedicacion": (sub[a][20], sub[a][0]), "Ambiente": (sub[a][21], sub[a][0]), "Aprendizaje": (sub[a][22], sub[a][0]), "Trato": (sub[a][23], sub[a][0])}
  else:
    Labs[area][tut][year]["Calidad"].append((sub[a][19], sub[a][0]))
    Labs[area][tut][year]["Dedicacion"].append((sub[a][20], sub[a][0]))
    Labs[area][tut][year]["Ambiente"].append((sub[a][21], sub[a][0]))
    Labs[area][tut][year]["Aprendizaje"].append((sub[a][22], sub[a][0]))
    Labs[area][tut][year]["Trato"].append((sub[a][23], sub[a][0]))





files = []
Path = os.listdir(".")                      ### I NEED A WAY TO MAKE SURE THAT THE PATH IS ALWAYS THE SAME. MAYBE CREATE A NEW PATH WITH THE PROGRAM ITSELF? ###
for path in Path:
  path = os.path.abspath(path)
  if os.path.isfile(path):
    files.append(path.split("\\")[-1])

if "output_json.csv" not in files:
  Courses = {}
  Labs = {}
else:
  source = json.load("output_json.csv")
  Courses = source[0]
  Labs = source[1]


f = open(handle_del_curado, "r")
lines = f.readlines()
for a in range(len(lines()):
  lines[a] = lines[a].split("\t")
  for b in range(len(lines[a])):
    try:
      lines[a][b] = float(lines[a][b])
     except:
      continue
      
      
#######################################################
### SET OF COORDINATES FOR INFORMATION IN EACH LINE ###
### TIMESTAMP: 0                                    ###
### E-MAIL: 1                                       ###
### ID: 2                                           ###
### SEMESTER: 3                                     ###
### MATERIA 1: [4:10]                               ###
###   NAME: 4                                       ###
###   TEACHER: 5                                    ###
###   CLARITY: 6                                    ###
###   DEDICATION: 7                                 ###
###   COURSE PLAN: 8                                ###
###   COVERAGE: 9                                   ###
### MATERIA 2: [10:16]                              ###
###   NAME: 10                                      ###
###   TEACHER: 11                                   ###
###   CLARITY: 12                                   ###
###   DEDICATION: 13                                ###
###   COURSE PLAN: 14                               ###
###   COVERAGE: 15                                  ###
### ROTACION: [16:]                                 ###
###   TUTOR: 16                                     ###
###   LOCATION: 17                                  ###
###   AREA: 18                                      ###
###   QUALITY: 19                                   ###
###   DEDICATION: 20                                ###
###   AMBIENT: 21                                   ###
###   QUALITY: 22                                   ###
###   TREATMENT: 23                                 ###
#######################################################




### I PROBABLY NEED TO CHANGE THIS INTO A FUNCTION ###
for a in range(1, len(lines)):
  add.tutor(lines[a])
  ### I STILL NEED SOMETHING SIMILAR FOR Courses ###
 

 
 
 
 
