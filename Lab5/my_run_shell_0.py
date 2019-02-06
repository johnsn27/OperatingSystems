#! /usr/bin/env python
import subprocess
import os, sys
import shutil
from datetime import datetime
# The purpose of this script is to give you simple functions for locating an executable program in common locations in the Linux path

# Simple shell
# COMMANDS          ERRORS CHECKED
# 1. info XX         - check file/dir exists
# 2. files
# ... omitted for simplicity
# 8. Default is to run the program


# Here the path is hardcoded, but you can easily optionally get your PATH environ variable
# by using: path = os.environ['PATH'] and then splitting based on ':' such as the_path = path.split(':')
THE_PATH = ["/bin/", "/usr/bin/", "/usr/local/bin/", "./"]

# ========================
#    Run command
#    Run an executable somewhere on the path
#    Any number of arguments
# ========================
def runCmd(fields):
  global PID, THE_PATH

  cmd = fields[0]
  cnt = 0
  args = []
  while cnt < len(fields):
      args.append(fields[cnt])
      cnt += 1

  execname = add_path(cmd, THE_PATH)

  # run the executable
  if not execname:
      print('Executable file ' + str(cmd) +' not found')
  else:
    # execute the command
    print(execname)

  # execv executes a new program, replacing the current process; on success, it does not return. 
  # On Unix, the new executable is loaded into  the current process, and will have the same process id as the caller.
  try:	
    os.execv(execname, args)
  except :
    print('Something went wrong there')
    os._exit(0)

# ========================
#    Constructs the full path used to run the external command
#    Checks to see if the file is executable
# ========================
def add_path(cmd, path):
    if cmd[0] not in ['/', '.']:
        for d in path:
            execname = d + cmd
            if os.path.isfile(execname) and os.access(execname, os.X_OK):
                return execname
        return False
    else:
        return cmd

# ========================
#    files command
#    List file and directory names
#    No arguments
# ========================
def filesCmd(fields):
    print('Nothing here yet. Use your files command from part A')


# ========================
#  info command
#     List file information
#     1 argument: file name
# ========================
def infoCmd(fields):
    print('Nothing here yet. Use your info command from part A')

# ----------------------
# Other functions
# ----------------------
def checkArgs(fields, num):
    numArgs = len(fields) - 1
    if numArgs == num:
        return True
    if numArgs > num:
        print("  Unexpected argument " + fields[num+1] + "for command " + fields[0])
    else:
        print("  Missing argument for command " + fields[0])

    return False

# ----------------------------------------------------------------------------------------------------------------------

while True:
    line = input("PShell>")
    fields = line.split()
    
    if fields[0] == "files":
        filesCmd(fields)
    elif fields[0] == "info":
        infoCmd(fields)
    else:
        runCmd(fields)
