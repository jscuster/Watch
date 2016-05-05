#!/usr/bin/python

# Copyright 2016, Jason Custer.
# Released under the MIT license.


from os import path
import os
from time import sleep
from sys import argv
from subprocess import call

# confirm inputs and print help message if need be
if len(argv) <= 3:
 print "To run this script, type " + argv[0] + " <path-to-watch> <command-to-run> ext1 [ext2] [ext3] ... \n\n where ext[N} = extension to watch. If the command is in quotes, [\"], you can use %f to indicate where the filename should be substituted. For example: " + argv[0] + " . \"gcc %f\" txt\n\n*** if %f is not included in the command argument, the file will be added to the end of the command."
print "The output of the command will be saved as [filename]_result.txt.
 exit(1)

# collect variables from argv
watchPath = path.abspath(argv[1])
cmd = argv[2]
#we have to have %f to know where to insert the file.
# Find it or add it to the end of the command.
if cmd.find("%f") < 0:
 cmd = cmd + " %f"
extlst = ["." + i.lower() for i in argv[3:]]

# print starting message, confirming user input.
print "Watching " + watchPath + " and running " + cmd + " on any new or changed files with extensions " + ", ".join(extlst) + " where %f = the name of the new or changed files."

#create hash for database
files = {}

# function to run the command on a newly added/changed file.
def runCommand(file):
 # create the command, replacing %f with the filename.
 newCmd = cmd.replace("%f", file) 
 newCmd += " > " + path.basename(path.splitext(file)[0]) + "_results.txt"
 # tell user and run command.
 print "Running " + newCmd + " now."
 call([newCmd], shell=True)

# check to see if a file exists.
def checkFile(f, noRun = False):
 #get the modified time of the file.
 mt = path.getmtime(f)
 #get extension
 x = path.splitext(f)[1].lower()
 #make sure it's a file extension we're watching.
 if x in extlst:
  #see if it's already in the database.
  if files.has_key(f):
   #compare times and update.
   if files[f] != mt:
    files[f] = mt
    print "The file " + f + " has changed."
    if not noRun:
     runCommand(f)
  else:
   #it's a new file, add it to the database and run command.
   files[f] = mt
   print "The file " + f + " was added to the folder."
   if not noRun:
    runCommand(f)

# scan the path for files we should process.
def scanPath(noRun = False):
 #creat a lost of files, absolute paths.
 ls = [path.join(watchPath, i) for i in os.listdir(watchPath)]
 #remove subdirectorys.
 ls = [i for i in ls if path.isfile(i)]
 # go through this list, check if we should process.
 for i in ls:
  checkFile(i, noRun)

# remove files that are deleted.
def removeDeadFiles():
 # get the list of all dead files from the keys of the database.
 dead = [i for i in files.keys() if not path.exists(i)]
 #remove dead files from the database.
 for i in dead:
  print "File " + i + " has been deleted."
  del files[i]

#start processing.
print "Initializing database."
scanPath(True) #add files, don't run commands on existing files.
print "Database initialized: watching for new files now. Press control+c to stop."
#main loop.
while (True):
 sleep(10)
 scanPath()
 removeDeadFiles()
