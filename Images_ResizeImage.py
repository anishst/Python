from ATSFramework import CommonOperations
from PIL import Image
import os
myFramework =  CommonOperations()

thumb_size=(1000,1000)

srcDir = r'E:\My Pictues\2012'

for root, dirnames, filenames in os.walk(srcDir):
		imgFiles = ['.jpg','.jpeg', '.png', '.gif']
		for file in filenames:
			# split filename and extension
			fileName, ext = os.path.splitext(file)
			# print("Resizing file {}....".format(file))
			if ext.lower() in imgFiles:
				try:
					img = Image.open(os.path.join(root,file))
					os.chdir(root)
					# print(fileName, ext)
					img.thumbnail(thumb_size)
					#  save as new file
					new_fileName = fileName + '_RESIZED_' + ext
					img.save(new_fileName)
					print("Resized file {} saved to: {}".format(new_fileName,root))
				except Exception as e:
					print("there was an issue with {}. Details: {}".format(file,e))
				finally:
					img.close()

				


