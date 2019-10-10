"""Gets the total lines in a file for given folder and file type"""


import os


def get_line_count(filename):
    """returns total number of lines in the provided text file"""
    num_lines = sum(1 for line in open(filename, 'rb'))
    return num_lines


file_types = ['.py']
total_line_count = 0
file_list = []
root_folder = r'.'

# traverse project root directory to find python filesd
for root, dirnames, filenames in os.walk(root_folder):
    for file in filenames:
        filename, ext = os.path.splitext(file)
        if file_types != None:
            if ext.lower() in file_types:
                num_of_lines = get_line_count(os.path.join(root, file))
                total_line_count += num_of_lines
                file_list.append([file, num_of_lines])
        else:
            pass
# print out results
print("-" * 78)
print("{:<60}{:>15}".format(("FILE NAME"), ("LINE COUNT")))
print("-" * 78)
# sort file list by number of lines and sort in desc order
file_list.sort(key=lambda item: item[1], reverse=True)

for file in file_list:
    print("{:<60}{:>15}".format((file[0]), (file[1])))
    print("-" * 78)
print(f"LOCATION: {root_folder}")
print(f"TOTAL PYTHON FILES: {len(file_list):>55}")
print(f"TOTAL LINES OF CODE: {total_line_count:>55}")
print("=" * 78)
