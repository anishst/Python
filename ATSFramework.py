# Author: Anish Sebastian
# Functions to work with Python Modules
# =============================================================================================
class HtmlFL:
    """ This class contains methods to deal with formatting output in HTML"""
    def __init__(self):
    	pass
 
    def makebold(self, txt):
        return "<strong>" + txt + "</strong>"

    def makeitalics(self,txt):
        return "<i>" + txt + "</i>"

    def HTMLTemplate(self, pageTitle,bodyTxt): # FINAL - 11-21-17
        """This function will return an html page with the given page title and body content"""
        
        #  C style method formatting
        # template = """<!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-8"> <title>%s</title> </head> <body>%s</body> </html>"""
        # template = template % (pageTitle,bodyTxt)
        
        # new format method
        template = """<!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-8"> <title>{}</title> </head> <body>{}</body> </html>""".format(pageTitle,bodyTxt)
        return template

    def GetHTML(self, url):
        import requests
        from bs4 import BeautifulSoup
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        return soup.prettify()

class CommonOperations:
    import datetime
    """ This class contains methods to deal with formatting string"""
    def __init__(self):
        pass

    # Time formatting methods
    @staticmethod
    def Timestamp():
        """"Returns timestamp in YYYY-MM-DD HH:MM:SS format """
        ts = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        return ts        
 
    @staticmethod
    def PrintDate():
        """"Returns date in YYYY-MM-DD format """
        import datetime
        dt = '%s' % datetime.date.today()
        return dt   

    def getTodayDate(self):
        """Returns today's date in MM/DD/YYYY format"""
        import datetime
        today = (datetime.date.today()).strftime("%m/%d/%Y")
        return today

    def SubtractDaysfromDate(self,days):
        """Subtracts # days provided from today's date and 
        returns new date in MM/DD/YYYY format"""
        import datetime
        from datetime import timedelta
        newdate = (datetime.date.today() - timedelta(days=days)).strftime("%m/%d/%Y")
        return newdate

    def AddDaysfromDate(self,days):
        """Adds # days provided to today's date and 
        returns new date in MM/DD/YYYY format"""
        import datetime
        from datetime import timedelta
        newdate = (datetime.date.today() + timedelta(days=days)).strftime("%m/%d/%Y")
        return newdate

    def RandomText(self,len):
        """Returns random text string for the given length of chars"""
        import string, random
        char_set = string.ascii_letters
        text = ''.join(random.sample(char_set*len, len))
        return text  

    def RandomNumber(self,lowNum,highNum):
        """Returns random text string for the given length of chars"""
        import random
        return random.randrange(lowNum,highNum)

    # *******************************************************************************************************************
    # Utility functions
    # *******************************************************************************************************************

    def AppendToTextFile(self,filename, value):
        """This functin writes data to an existing file."""
        f = open(filename,"a") 
        f.write(value)
        f.close()

    def WritetoNewTextFile(self,filename, value):
        "This functin creates writes to a new file. If file exits it will be overwritten"
        f = open(filename,"w") 
        f.write(value)
        f.close()

    def ReadFullTextFile(self,filename):
        "This function return the entire file results in a string"
        txtFile = open(filename,'r') 
        txtFileContents = txtFile.read()
        return txtFileContents
        txtFile.close()

    def ReadCSVFile(self,filename):     
        with open(filename, "r") as CSVFile:    
            CSVFileReader = csv.reader(CSVFile)
            CSVFileList = []
            for row in CSVFileReader:
                if len(row) != 0:
                    CSVFileList = CSVFileList + [row]
        return CSVFileList

    def WritetoCSVFile(self, filename, value):
        """this function writes to a CSV file"""
        import csv
        with open(filename, 'w', newline='') as csvfile:
            outputfile = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            outputfile.writerow([value])
    
    def Backup(self, source, dest):
        """Backup function
        recursively copy the entire directory tree rooted at src to dest. 
        dest must not already exist. 
        """
        import os, shutil
        from datetime import datetime
        print("Backing up {} to {}............".format(source,dest))
        backupDir = os.path.join(dest, datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
        shutil.copytree(source, backupDir)
        print("Backup is complete!")
        
    # *******************************************************************************************************************
    # Text Search Functions
    # *******************************************************************************************************************
    def FindTextUsingRegEx_Match(self,pattern, text):
        import re
        match  = re.search(pattern, text)
        if match:
            return match.group() # here is the match
        else:
            return "no match found"

    def FindTextUsingRegEx_FindAll(self,pattern, text):
        import re
        match  = re.findall(pattern, text, flags=re.IGNORECASE)
        if match:
            return match # here is the match
        else:
            return "no match found"        

    # *******************************************************************************************************************
    # Directory Opearations
    # *******************************************************************************************************************
    def FindSpecialFilesUsingRegExp(self,pattern, src):
        """ This function takes a Regular expression pattern and source
        example call: t.FindSpecialFilesUsingRegExp(pattern, src))
        """
        import re, os
        files = [file for file in os.listdir(src) if re.search(pattern, file, re.IGNORECASE)]
        if files:
            return files
        else:
            return "No files found"

    @staticmethod
    def GetFileInfo(start_path):
        """This function prints out information about the files
        in the given path""" 

        import os
        #Import math and time module
        import math,time

        #Set listing start location
        dir_count = 0
        file_count = 0

        #Traverse directory tree
        for (path,dirs,files) in os.walk(start_path):
            # print('Directory: {:s}'.format(path))
            dir_count += 1
            #Repeat for each file in directory
            for file in files:
                fstat = os.stat(os.path.join(path,file))
                # Convert file size to MB, KB or Bytes
                if (fstat.st_size > 1024 * 1024):
                    fsize = math.ceil(fstat.st_size / (1024 * 1024))
                    unit = "MB"
                elif (fstat.st_size > 1024):
                    fsize = math.ceil(fstat.st_size / 1024)
                    unit = "KB"
                else:
                    fsize = fstat.st_size
                    unit = "B"

                mtime = time.strftime("%X %x", time.localtime(fstat.st_mtime))
                
                 # Print file attributes
                print('\t{:46.46s}\t{:8d}\t {:2s}\t {:18s}'.format(file,fsize,unit,mtime))
                # print('\t{}\t{:8d}\t {:2s}\t {:18s}'.format(file,fsize,unit,mtime))
                file_count += 1

         # Print total files and directory count
        print('\nFound {} files in {} directories.'.format(file_count,dir_count)) 

class ImageFormatting:
    """ This class contains methods to deal with images

    TO DO: class for image formatting; image rotate; change to black and white
    """
    def __init__(self):
        pass

    def Image_AddWaterMark(self, imgsrc, watermarkText):
        """This function takes in a a text string and applies that to the image provided"""
        from PIL import Image, ImageDraw, ImageFont
         
        image = Image.open(imgsrc)
        width, height = image.size
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('arial.ttf', 56)
        textwidth, textheight = draw.textsize(watermarkText, font)
         # calculate the x,y coordinates of the text
        margin = 100
        x = width - textwidth - margin
        y = height - textheight - margin
        # draw watermark in the bottom right corner
        draw.text((x, y), watermarkText, font=font)
        image.save(imgsrc)
        image.show()

    def Image_Thumbnail(self, srcdir, thumb_size=(300,300)):
        """This function resizes the images provided to the given size
        Inputs: source directory (required), thumb_size(optional)
        """
        from PIL import Image
        import os

        for file in os.listdir(srcdir):
            if file.endswith('.jpg') and os.path.isfile(os.path.join(srcdir, file)):
                img = Image.open(os.path.join(srcdir,file))
                # split filename and extension
                fileName, fileExt  = os.path.splitext(file)
                print(fileName, fileExt)
                img.thumbnail(thumb_size)
                img.save('{}{}_THUMBNAIL{}'.format(srcdir,fileName, fileExt))


    def Image_Crop(self, imgsrc, size):
        """This function crops the  image provided
        Inputs: image src, size in tuple
        """
        from PIL import Image
        # box = (100, 100, 400, 400)
        box = size
        im = Image.open(imgsrc)
        region = im.crop(box)
        # region.show()
        image = region.save(imgsrc) 
        return image

    def Image_GetImageFiles(self, src):
        """returns images """
        import glob
        image_list = []
        print(src)
        for file in glob.glob('images/*.[jpeg][png][jpg]*'):
            image_list.append(file)
        return image_list

    def Image_PrintDetails(self, imageList): 
        """This program prints out details of the image to the screeen """
        for imagename in imageList:
            from PIL import Image
            image = Image.open(imagename)
            print(image)
            print(image.format)
            print(image.size) # 2-tubel(width, height)
            print(image.width)
            print(image.height)
            print(image.filename)
            print(image.info)
            #  display image
            # image.show()                    

class PandasFL:
    """ This class contains methods to deal with panda data analysis library
    https://pandas.pydata.org/
    """
    def __init__(self):
        pass
