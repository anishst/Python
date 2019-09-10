"""Gets the total lines of python code in a given folder"""

def get_line_count(filename):
        """returns total number of lines in the provided text file"""
        num_lines = sum(1 for line in open(filename, 'rb'))
        print(num_lines)
        return num_lines

fileTypes = ['.py']
folder_path = r'.' # specify ur folder here
line_count = 0
import os
for root, dirnames, filenames in os.walk(folder_path):

    for file in filenames:
        filename, ext = os.path.splitext(file)
        if fileTypes != None:
            if ext.lower() in fileTypes:
                num_of_lines = get_line_count(os.path.join(root,file))
                print(f"File {file} contains {num_of_lines} of code")
                line_count += num_of_lines
        else:
            pass
print("*"*70)
print(f"Total lines of code: {line_count}")
print("*"*70)