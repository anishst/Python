"""Deletes the files with provided extensions under a directory that are older than
provided number of days"""
import os, time

root = r'C:\Temp\SeleniumPythonFramework'
file_extensions_to_remove = ('.log', '.png') # tuple
how_many_days_old_logs_to_remove = 1
removed_files = []


for dirpath, dirnames, filenames in os.walk(root):
	print(f"Checking Folder: {dirpath}")
	folder_path = dirpath

	now = time.time()

	for file in os.listdir(folder_path):
	    file_full_path = os.path.join(folder_path,file)
	    if os.path.isfile(file_full_path) and file.endswith(file_extensions_to_remove):
	        #Delete files older than x days
	        if os.stat(file_full_path).st_mtime < now - how_many_days_old_logs_to_remove * 86400: 
	             os.remove(file_full_path)
	             print ("File Removed : " , file_full_path)
	             removed_files.append(file_full_path)

print(f"{len(removed_files)} files were removed from {root}")
print(removed_files)