import os
import shutil
import pwd
from datetime import datetime
from shutil import copyfile


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

headers = ["File Name", "Type", "Last Change", "OwnerID", "Size in Bytes", "Executable"]  # column headers
width = [20, 8, 24, 12, 20, 8]  # max width of data in each column

# ========================
#  file command
#     List file information
#     1 argument: file name
# ========================

def info_cmd(fields):
    if len(fields) > 1:
        if os.path.exists(fields[1]): #check file exists
            print(fields[1])
            print_header(len(headers))
            file_info(fields[1])
            print_file_info()
        else:
            print("File or directory does not exist")



# ========================
#    files command
#    List file and directory names
#    No arguments
# ========================
def files_cmd():

    print_header(2)
    for filename in os.listdir('.'):
        files_cmd_info(filename)
        print_file_info()

# ========================
#    delete command
#    delete the file
#    file as argument
# ========================

def delete_cmd(fields):
    if os.path.isfile(fields[1]):
        os.remove(fields[1])

# ========================
#    copy command
#    copy the file
#    source and destination as arguments
# ========================

def copy_cmd(from_file, to_file):
    copyfile(from_file, to_file)

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
    while field_num < lengthOfHeader:
        output += '{field:{fill}<{width}}'.format(field=headers[field_num], fill=' ', width=width[field_num])
        field_num += 1

    width_counter = 0
    width_sum = 0
    for x in width:
        if width_counter == lengthOfHeader:
            break
        width_sum=width_sum+x
        width_counter = width_counter+1

    print(output)
    print('-' * width_sum)

def file_info(name):
    global info
    info = []
    info.append(name)  # the file name
    info.append(file_or_directory(name))
    modified = os.stat(name).st_mtime
    info.append(datetime.fromtimestamp(modified).strftime('%b %d %Y %H:%M:%S'))
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

def files_cmd_info(name):
    global info
    info = []
    info.append(name)
    info.append(file_or_directory(name))

# ----------------------------------------------------------------------------------------------------------------------

while True:
    line = input("PShell>") 
    fields = line.split()
    # split the command into fields stored in the fields list
    # fields[0] is the command name and anything that follows (if it follows) is an argument to the command

    if fields[0] == "files":
        files_cmd()
    elif fields[0] == "info":
        info_cmd(fields)
    elif fields[0] == "delete":
        delete_cmd(fields)
    elif fields[0] == "copy":
        copy_cmd(fields[1], fields[2])
    else:
        print("Unknown command " + fields[0])

