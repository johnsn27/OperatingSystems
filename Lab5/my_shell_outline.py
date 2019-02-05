import os
import shutil
import pwd
from datetime import datetime


# Simple shell
# COMMANDS          ERRORS CHECKED
# 1. info XX         - check file/dir exists
# 2. files
# 3. delete  XX      - check file exists and delete succeeds
# 4. copy XX YY      - XX exists, YY does not exist copy succeeds
# 5. where
# 6. down DD         - check directory exists and change succeeds
# 7. up              - check not at the top of the directory tree - can't go up from root
# 8. finish

headers = ["File Name", "Last Change", "Type", "OwnerID", "Size in Bytes", "Executable"]  # column headers
width = [20, 24, 8, 12, 20, 8]  # max width of data in each column

# ========================
#  file command
#     List file information
#     1 argument: file name
# ========================

def info_cmd(fields):
    info = []
    print_header(len(headers))
    for filename in os.listdir('.'): # move this to function and also call print_file_info from fileInfo2 from lab 4
        file_info(filename)
        print_file_info()



# ========================
#    files command
#    List file and directory names
#    No arguments
# ========================
def files_cmd(fields):
    print_header(2)
    files = []
    for filename in os.listdir('.'):
        print(filename)
        print(file_or_directory(filename))
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

def print_header(lengthOfHeader):
    field_num = 0
    output = ''
    while field_num < len(headers):
        output += '{field:{fill}<{width}}'.format(field=headers[field_num], fill=' ', width=width[field_num])
        field_num += 1

    print(output)
    length = sum(width)
    print('-' * length)

def file_info(name):
    global info
    info = []
    info.append(name)  # the file name
    modified = os.stat(name).st_mtime
    info.append(datetime.fromtimestamp(modified).strftime('%b %d %Y %H:%M:%S'))
    info.append(file_or_directory(name))
    info.append(os.stat(name).st_uid)
    if os.path.isfile(name):
        info.append(os.stat(name).st_size)
        if os.access(name, os.X_OK):
            info.append('Yes')
        else:
            info.append('No')

def print_file_info():
    global info
    fieldNum = 0
    output = ''
    while fieldNum < len(info):
        output += '{field:{fill}<{width}}'.format(field=info[fieldNum], fill=' ', width=width[fieldNum])
        fieldNum += 1
    print(output)

def file_or_directory(name):
    if os.path.isdir(name):
        return "dir"
    else:
        return "file"

# ----------------------------------------------------------------------------------------------------------------------

while True:
    line = raw_input("PShell>")  # NOTE! This is only for python 2. Should be 'input' for python 3
    fields = line.split()
    # split the command into fields stored in the fields list
    # fields[0] is the command name and anything that follows (if it follows) is an argument to the command

    if fields[0] == "files":
        files_cmd(fields)
    elif fields[0] == "info":
        info_cmd(fields)
    else:
        print("Unknown command " + fields[0])

