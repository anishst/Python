import os,sys
import shutil


def change_extension():
	folder = r'\\192.168.0.50\LinuxShare\FlaskApp_Personal\static\image_gallery'
	for filename in os.listdir(folder):
		infilename = os.path.join(folder,filename)
		if not os.path.isfile(infilename): continue
		oldbase = os.path.splitext(filename)
		newname = infilename.replace('.JPG', '.jpg')
		output = os.rename(infilename, newname)
		print("Processing finished for{}".format(filename))

def copy_files(copy_from, copy_to):
	"""
	copies files from src_path to provided dir copy_to_path
	"""

	filesToFind = ['.m4v', '.mp4', '.mov']  # provide extension to look for

	filesFound = []
	for root, dirnames, filenames in os.walk(copy_from):
		for file in filenames:
			# split filename and extension
			filename, ext = os.path.splitext(file)
			if ext.lower() in filesToFind:
				abs_path = os.path.join(root, file)
				print(f"Copying {abs_path}...")
				shutil.copy(abs_path, copy_to)


#

copy_files(copy_from=r"D:\Pictures", copy_to=r'D:\TEMP\Videos')


