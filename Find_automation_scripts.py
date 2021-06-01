"""
This script searches for files with specified extensions and 
displays the folder name and file name and count

"""


import os
path= r"D:\GitHub\Automation"		# provide location of files
filesToFind = ['.py'] 			# provide extension to look for

filesFound = []
for root, dirnames, filenames in os.walk(path):
	for file in filenames:
		# split filename and extension
		filename, ext = os.path.splitext(file)
		if ext.lower() in filesToFind:
			print(f"Folder: {root}  \nFileName: {file}")
			filesFound.append(file)
print(f"Found {len(filesFound)} files ")

