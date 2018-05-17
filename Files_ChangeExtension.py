import os,sys
folder = r'\\192.168.0.50\LinuxShare\FlaskApp_Personal\static\image_gallery'
for filename in os.listdir(folder):
	infilename = os.path.join(folder,filename)
	if not os.path.isfile(infilename): continue
	oldbase = os.path.splitext(filename)
	newname = infilename.replace('.JPG', '.jpg')
	output = os.rename(infilename, newname)
	print("Processing finished for{}".format(filename))

