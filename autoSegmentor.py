# coding=utf-8
import sys
import re
import os

# original directory
directory = './OTs/'
# objective directory
destination_directory = './SEGs/'
# backup directory
backup_directory = './Backup/'
if os.path.exists(directory):
    print('Loading...')
    # rescutive
    for file_or_folder in os.listdir(directory):
        # generate full file path which to be treated
        file_path = os.path.join(directory, file_or_folder)
        # generate full file path which to save the new file generated.
        destination_file_path = os.path.join(destination_directory, file_or_folder+'.seg') 
        # judge wheather one object in the directory is a file.
        if os.path.isfile(file_path):
            # execute statement.
            os.system("sh ./Stanford/segment.sh ctb " + file_path +" utf8 0 > " + destination_file_path)
            # execute backcup and clean operations
            os.system("cp " + file_path +" " + backup_directory + directory)
            os.system("cp " + destination_file_path +" " + backup_directory + destination_directory)
            os.system("rm " + file_path)
else:
    print('Wrong path!')

print('---------------------------------------')
print('Executing ...\n')
print('Congratuation, all the files in directory <OTs> have been segmented into ' + destination_directory + ' directory.')
print('---------------------------------------')
