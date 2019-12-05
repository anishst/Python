path = r'C:\Users\532975\Documents\Automation\GitHub\flaskapp_main\flaskapp\static\images\picture_day\temp'
import os
for root, dirnames, filenames in os.walk(path):

    videoFiles = ['.avi', '.mp4', '.m4v','.mov']
    imgFiles = ['.jpg','.jpeg', '.png', '.gif']

    for file in filenames:
        filename, ext = os.path.splitext(file)
        if ext.lower() in imgFiles:
            print(filename, ext)
            get_year = filename.split('_')[:-1]
            print(get_year)
            # new_name = f"{year}-{new_year}_{filename}{ext}"
            # print(new_name)									
            # os.rename(os.path.join(root,file), os.path.join(root, new_name))


				


