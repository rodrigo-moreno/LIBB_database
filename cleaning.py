from math import ceil
import json

### FUNCTIONS ###
def rewrite_line(l):
  '''
  A FUNCTION THAT WILL REMOVE ALL WHITESPACE
  AT THE END AND BEGINING OF LINES AND REWRITE IT WITH 
  TAB DELIMITERS.
  '''
  l = l.decode("utf-8")
  l = l.strip()
  l = l.upper()
  l = l.split('\",\"')
# -*- utf-8 -*-
#  print l[len(l)-1]
  for pos in range(len(l)):
    l[pos] = l[pos].strip()
    l[pos] = l[pos].replace('\"', "")
  l = "\t".join(l)
  l = l.encode("utf-8")
  return l



### VARIABLES ###
Courses = {}       ### THIS WILL CONTAIN THE INFORMATION ABOUT THE COURSES
Labs = {}          ### THIS WILL CONTAIN THE INFORMATION ABOUT THE LABS


### MAIN ###


### OBTAIN ALL LINES OF THE .CSV FILE AND PUT THEM IN A TAB SEPARATED FORMAT, IN ALL-CAPS, WITH NO QUOTATION MARKS ###
f = raw_input("Enter file to clean:\t")
fo = open(f, "r")

lines = fo.readlines()
for a in range(0, len(lines)):
  lines[a] = rewrite_line(lines[a])

fo.close()


### OPEN NEW FILE AND WRITE THE NEW TABLE ON IT, WITH AN APPENDIX TO THE NAME IN THE FORM OF _new.csv ###
new_file = f.replace(".csv", "_new.csv")
fo = open(new_file, "w")
for i in range(len(lines)):
  if i < len(lines)-1:
    fo.write(lines[i] + "\n")
  else:
    fo.write(lines[i])
fo.close()

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

for a in range(len(lines)):
#  lines[a] = lines[a].decode("utf-8")
  lines[a] = lines[a].split("\t")
  for b in range(len(lines[a])):
    try:
      lines[a][b] = float(lines[a][b])
    except:
      continue


### THE PROPOSED FORM OF THE LABS DICTIONARY IS Labs{area1: {Doctor1: {Semester1: {Grades}, Semester2{Grades}}, Doctor2: {...}}, area2: {...}}
### THE PROPOSED FORM OF THE COURSES DICTIONARY IS Courses
for a in range(1, len(lines)):
  area = lines[a][18]
  tut = lines[a][16]
  year = ceil(float(lines[a][3])/2)
  year = int(year)
  if area not in Labs.keys():
    Labs[area] = {tut: {year: {"Calidad": lines[a][19], "Dedicacion": lines[a][20], "Ambiente": lines[a][21], "Aprendizaje": lines[a][22], "Trato": lines[a][23]}}}
  elif tut not in Labs[area].keys():
    Labs[area][tut] = {year: {"Calidad": lines[a][19], "Dedicacion": lines[a][20], "Ambiente": lines[a][21], "Aprendizaje": lines[a][22], "Trato": lines[a][23]}}
  elif year not in Labs[area][tut].keys():
    Labs[area][tut][year] = {"Calidad": lines[a][19], "Dedicacion": lines[a][20], "Ambiente": lines[a][21], "Aprendizaje": lines[a][22], "Trato": lines[a][23]}
  else:
    Labs[area][tut][year]["Calidad"].append(lines[a][19])
    Labs[area][tut][year]["Dedicacion"].append(lines[a][20])
    Labs[area][tut][year]["Ambiente"].append(lines[a][21])
    Labs[area][tut][year]["Aprendizaje"].append(lines[a][22])
    Labs[area][tut][year]["Trato"].append(lines[a][23])
    
  
for a in Labs.keys():
  print a, Labs[a]
    
json.dump(Labs, open("output_json.csv", "w"))       ### THE COUNTERPART TO READ THIS IS json.load(filehandle). IT CAN BE ASSIGNED AS A VARIABLE
### THIS IS THE LINK WHERE I FOUND THE ABOVE: http://stackoverflow.com/questions/11026959/writing-a-dict-to-txt-file-and-reading-it-back#11027021 ###
