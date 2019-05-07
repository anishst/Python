"""Deletes the log files under a directory that are older than
provided number of days"""
import os, time

top = r'C:\Temp\SeleniumPythonFramework'

import os
for dirpath, dirnames, filenames in os.walk(top):
	print(f"Checking Folder: {dirpath}")
	folder_path = dirpath
	file_ends_with = ".log"
	how_many_days_old_logs_to_remove = 1
	now = time.time()

	for file in os.listdir(folder_path):
	    file_full_path = os.path.join(folder_path,file)
	    if os.path.isfile(file_full_path) and file.endswith(file_ends_with):
	        #Delete files older than x days
	        if os.stat(file_full_path).st_mtime < now - how_many_days_old_logs_to_remove * 86400: 
	             os.remove(file_full_path)
	             print ("File Removed : " , file_full_path)