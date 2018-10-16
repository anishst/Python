from ATSFramework import CommonOperations
import os
sc = CommonOperations()

srcDir = r'Y:\SeleniumSetup'
flist = sc.ScanDirectory(srcDir, fileTypes=['.exe', '.txt'])

for i in flist:
	print(i)
	print(os.path.basename(i))

list_items = ['anish', 'anish', 'ligy', 'ligy', 'Ligy']

print(sc.FindDuplicates(list_items))