from ATSFramework import CommonOperations
import os
sc = CommonOperations()

srcDir = r'H:\My Pictues\2008\Auto Show'
flist = sc.ScanDirectory(srcDir, fileTypes=['.jpg', '.txt'])

for i in flist:
	print(i)
	print(os.path.basename(i))

list_items = ['anish', 'anish', 'ligy', 'ligy', 'Ligy']

print(sc.FindDuplicates(list_items))