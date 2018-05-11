from ATSFramework import CommonOperations
from PIL import Image
import os
myFramework =  CommonOperations()

thumb_size=(250,250)

srcDir = r'C:\Temp\Images'

for root, dirnames, filenames in os.walk(srcDir):
		imgFiles = ['.jpg','.jpeg', '.png', '.gif']
		for file in filenames:
			# split filename and extension
			fileName, ext = os.path.splitext(file)
			print("Resizing file {}....".format(file))
			if ext.lower() in imgFiles:
				try:
					img = Image.open(os.path.join(root,file))
					os.chdir(root)
					# print(fileName, ext)
					img.thumbnail(thumb_size)
					#  save as new file
					new_fileName = fileName + 'RESIZED' + ext
					img.save(new_fileName)
					# img.save('{}_RESIZED_{}'.format(fileName, ext))
					print("Resized file {} saved to: {}".format(new_fileName,root))
				except Exception as e:
					print("there was an issue {}".format(e))

				


