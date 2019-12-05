# https://stackoverflow.com/questions/225735/batch-renaming-of-files-in-a-directory
folder = r'C:\Users\532975\Documents\Automation\GitHub\flaskapp_main\flaskapp\static\images\picture_day'

import glob, os

def rename(dir, pattern, titlePattern):
    for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        print(pattern, titlePattern)
        os.rename(pathAndFilename, os.path.join(dir, titlePattern % title + ext))
# using
rename(folder, r'*.jpg', r'new(%s)')
