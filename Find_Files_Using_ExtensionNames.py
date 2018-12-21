
path= r"Y:\Automation 2.0\ALM\Regression"

filesToFind = ['.usr'] # provide extension to look for

import os

scriptNames = []
for root, dirnames, filenames in os.walk(path):

	for file in filenames:
		# split filename and extension
		filename, ext = os.path.splitext(file)
		if ext.lower() in filesToFind:
			# print(f"{root}\t {file}") 
			# print(f"FileName: {file}")
			print(file)
			scriptNames.append(file)

print(f"Found {len(scriptNames)} scripts ")
