from ATSFramework import CommonOperations
import os
sc = CommonOperations()

srcDir = r'Y:\SeleniumSetup'
flist = sc.ScanDirectory(srcDir, fileTypes=['.py', '.txt'])

for i in flist:
	print(i)
	print(os.path.basename(i))