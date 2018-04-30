from ATSFramework import CommonOperations

myFramework =  CommonOperations()

import os
from datetime import datetime
import time

#  Get exif data
from PIL import Image
from PIL.ExifTags import TAGS
def get_exif(fn):
    ret = {}
    try:
        i = Image.open(fn)
        print(fn)
        info = i._getexif()
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            ret[decoded] = value
        return ret
    except Exception:
        return False


path = r'E:\My Pictues\Tony'
for root, dirnames, filenames in os.walk(path):

		videoFiles = ['.avi', '.mp4', '.m4v','.mov']
		imgFiles = ['.jpg','.jpeg', '.png', '.gif']
		
		for file in filenames:
			filename, ext = os.path.splitext(file)
			if ext.lower() in imgFiles:
				try:
					# get directory name it title format and remove spaces
					dirname = root.split(os.path.sep)[-1].title().replace(' ',"") 
					imgMetaData = get_exif(os.path.join(root,file))
					
					#  get created date and strip out space, comma and colon
					dateTaken =  imgMetaData['DateTimeOriginal'].strip().replace(':',"").replace(' ',"_")
					print(dateTaken)
					new_name = '{}{}{}{}'.format(dateTaken,"_",dirname,ext)		
					print(new_name)									
					os.rename(os.path.join(root,file), os.path.join(root, new_name))
				except Exception as e:
					print("no metadata found {}".format(e))
					new_name = '{}{}{}{}{}'.format(time.strftime('%Y%m%d',time.gmtime(os.path.getmtime(os.path.join(root,file)))),"_",dirname,myFramework.RandomNumber(2,1100),ext)
					print(new_name)
					os.rename(os.path.join(root,file), os.path.join(root, new_name))
			elif ext.lower() in videoFiles:
				try:
					filename, ext = os.path.splitext(file)
					# get directory name it title format and remove spaces
					dirname = root.split(os.path.sep)[-1].title().replace(' ',"")					
					new_name = '{}{}{}{}{}'.format(time.strftime('%Y%m%d',time.gmtime(os.path.getmtime(os.path.join(root,file)))),"_",dirname,myFramework.RandomNumber(2,1100),ext)
					os.rename(os.path.join(root,file), os.path.join(root, new_name))
				except Exception as e:
					print("There was an issue with {}{}".format(file,e))
				


