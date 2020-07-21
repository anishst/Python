# Author: Anish Sebastian
# Functions to work with Python Modules
# =============================================================================================
import csv
import os
import time
from datetime import datetime

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import *


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
        r = requests.get(url, verify=False)
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

    def SecretKeyGenerator(self,len):
        """Returns random text in hexadecimal format"""
        import secrets
        return secrets.token_hex(len)
    # *******************************************************************************************************************
    # Utility functions
    # *******************************************************************************************************************

    def get_line_count(self, filename):
        """returns total number of lines in the provided text file"""
        num_lines = sum(1 for line in open(filename, 'rb'))
        return num_lines

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

    def ScanDirectory(self, srcDir, fileTypes=None):
        """Scans given directory and returns file paths
        if fileTypes provideds applies that filter"""
        
        import os
        fileList = []
        for root, dirnames, filenames in os.walk(srcDir):

            for file in filenames:
                filename, ext = os.path.splitext(file)
                if fileTypes != None:
                    if ext.lower() in fileTypes:
                        fileList.append(os.path.join(root,file))
                else:
                    fileList.append(os.path.join(root,file))

        return fileList                  
        
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

    def FindDuplicates(self, listItems):
        """This list accepts a list and returns duplicate values in the list"""
        duplicates = []
        duplicates = set([x for x in listItems if listItems.count(x) > 1])
        return list(duplicates)



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

class EmailFL:
    """Email related methods"""

    @staticmethod
    def send_email_gmail(recipients, subject, message):
        """
        This function emails the message provided using provided parameter values - UNDER DEV
        :param recipients: list of email addresses
        :param subject: email subject
        :param message: email message in HTML format
        :return: None
        """
        try:
            import smtplib
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText

            # GMAIL user info
            GMAIL_USER =  os.getenv('GMAIL_ID')
            GMAIL_PASS = os.getenv('GMAIL_PWD')
            SMTP_SERVER = 'smtp.gmail.com'
            SMTP_PORT = 587
            msg = MIMEMultipart()
            msg['Subject'] = subject
            msg['From'] = GMAIL_USER
            msg['To'] = ", ".join(recipients)
            body = message
            msg.attach(MIMEText(body, 'html'))
            smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            smtpserver.starttls()
            smtpserver.login(GMAIL_USER, GMAIL_PASS)
            print("Logged in")
            smtpserver.send_message(msg)
            smtpserver.close()
            print(f"Email has been sent successfully to {recipients}")
        except Exception as e:
            print(f"There was an issue with emailing results: {e}")



TIME_OUT = 30

class SeleniumFL:
    """Selenium related """

    def __init__(self, driver):
        """Initializes the base page class and inherits from Selenium driver and Util class"""
        self.driver = driver


    def get_title(self):
        """Returns title of the current page"""
        return self.driver.title

    def get_current_url(self):
        """Returns URL of the current page"""
        return self.driver.current_url

    def get_element(self, locatorType, locator):
        """ Returns the element using provided locator and locatorytype"""
        element = None
        try:
            element = WebDriverWait(self.driver, TIME_OUT).until(EC.element_to_be_clickable((locatorType, locator)))
            self.log.info(f"Element found with locator: {locator}")
            return element
        except Exception as e:
            self.log.error(f"Element was not found with locator: {locator}. Exception: {e}")

    def get_elements(self, locatorType, locator):
        """ Returns list of elements using provided locator and locatorytype"""
        elements = None
        try:
            elements = WebDriverWait(self.driver, TIME_OUT).until(
                EC.presence_of_all_elements_located((locatorType, locator)))
            self.log.info(f" {len(elements)} Elements found with locator: {locator}")
            return elements
        except Exception as e:
            self.log.error(f"Elements was not found with locator: {locator}. Exception: {e}")
            return None

    def get_text(self, locatorType, locator):
        """ Returns the text of the element provided locator and locatorytype"""
        element = None
        try:
            self.util.sleep(1)
            element = WebDriverWait(self.driver, TIME_OUT).until(EC.presence_of_element_located((locatorType, locator)))
            self.log.info(f"Element found with locator: {locator} with text {element.text}")

            return element.text
        except Exception as e:
            self.log.error(f"Element was not found with locator: {locator}. Exception: {e}")
            return None

    def element_click(self, locatorType, locator):
        """
		clicks on the element using locator and locatorytype values provided
		"""
        try:
            element = self.get_element(locatorType, locator)
            # adding a wait before clicking on elements to resolve issues seen with chrome driver
            self.util.sleep(1, "before clicking on element")
            element.click()
            self.log.info(f"Clicked on element with locator: {locator} and locatorType: {locatorType}")
        except Exception as e:
            self.log.error(
                f"Cannot click on element with locator: {locator} and locatorType: {locatorType}. Exception: {e}")

    def sendKeys(self, data, locatorType, locator, clearField=True):
        """this function will send data provided to a field using  locator and locatoryType values; clearField = optional field;
		By default, it will clear the fields before sending data
		"""
        try:
            element = self.get_element(locatorType, locator)
            if clearField:
                element.clear()
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
        except Exception as e:
            self.log.error("Cannot send data on element with " + locator + " locatorType: " + locatorType + str(e))

    def is_element_visible(self, locatorType, locator):
        """
		Return the visibility state of an element; True if visible; False if not visible
		"""
        try:
            element = WebDriverWait(self.driver, TIME_OUT).until(
                EC.visibility_of_element_located((locatorType, locator)))
            if element is not None:
                self.log.info(f"Element: {locator} is visible")
                return True
            else:
                self.log.error(f"Element: {locator}is NOT visible")
                return False
        except Exception as e:
            self.log.info(f"Element: {locator} is NOT visible; Error Details {e}")
            return False

    def is_element_clickable(self, locatorType, locator):
        """
        Return the clickability state of an element; True if clickable; False if not clickable
        """
        try:
            element = WebDriverWait(self.driver, TIME_OUT).until(
                EC.element_to_be_clickable((locatorType, locator)))
            if element is not None:
                self.log.info(f"Element: {locator} is clickable")
                return True
            else:
                self.log.error(f"Element: {locator}is NOT clickable")
                return False
        except Exception as e:
            self.log.info(f"Element: {locator} is NOT clickable; Error Details {e}")
            return False

    def wait_for_element(self, locatorType, locator, timeout=TIME_OUT, poll_frequency=0.5):
        """wait for element; currently not being used"""
        element = None
        try:
            byType = self.getByType(locatorType)
            print("Waiting for a maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, TIME_OUT, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType,
                                                             locator)))

            print("Element appeared on the web page")
        except:
            print("Element did not appear on the web page!")
        return element

    def verify_element_is_enabled(self, locatorType, locator):
        """
        @summary:  This function checks to see if an element is enabled
        @param locatorType: type of locator
        @param locator: locator value
        @return: boolean
        """

        try:
            elm = self.get_element(locatorType, locator)
            if elm.is_enabled() == True:
                self.log.info(f"Element: {locator} is Enabled")
                return True
            else:
                self.log.info(f"Element: {locator} is NOT Enabled")
                return False
        except:
            self.log.info(f"Element: {locator} is NOT Enabled")
            return False

    def take_screenshot(self, resultMessage):
        """
		This functions takes a screenshot of the current open page and saves it in screenshots folder
		"""
        fileName = f"{self.driver.name}_{resultMessage}.{time.strftime('%m%d%Y%H%M%S')}.png"
        screenShotDirectory = "../screenshots/"
        relativeFileName = screenShotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)  # gives the file directory
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenShotDirectory)
        try:
            # if screenshots folder doesn't exist, create it
            if not os.path.exists(destinationDirectory):
                print(f"{destinationDirectory} was not found. Creating....")
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info(f"Screenshot saved to directory: {destinationFile}")
        except Exception as e:
            self.log.error(f"An exception occured while trying to save screenshot: {e}")
            print_stack()

    #  Dropdown methods
    def get_dropdown_list_values(self, locatorType, locator):
        """
		This function returns a list with values of a dropdown
		"""
        try:
            drop_down_element = Select(self.get_element(locatorType, locator))
            dropdown_list_values = [option.text for option in drop_down_element.options]
            return dropdown_list_values
        except Exception as e:
            self.log.error(f"There was issue with getting dropdown values using {locatorType} and {locator}: {e}")

    def select_dropdown_list_value(self, value_to_select, locatorType, locator):
        """
		This function selects the value provide in a dropdown
		"""
        try:
            drop_down_element = Select(self.get_element(locatorType, locator))
            drop_down_element.select_by_visible_text(value_to_select)
            self.is_element_visible(locatorType, locator)
            drop_down_element = Select(self.get_element(locatorType, locator))
            self.log.info(f"Selected dropdown value: {str(drop_down_element.first_selected_option.text)}")
        except Exception as e:
            self.log.error(f"There was issue with selecting dropdown value using using {locatorType} and {locator}: {e}")

    def select_dropdown_list_value_using_index(self, locatorType, locator, index_num=0):
        """
        This function selects the value provide in a dropdown using index numbers
        """
        try:
            drop_down_element = Select(self.get_element(locatorType, locator))
            drop_down_element.select_by_index(index_num)
            self.is_element_visible(locatorType, locator)
            drop_down_element = Select(self.get_element(locatorType, locator))
            self.log.info(f"Selected dropdown value: {str(drop_down_element.first_selected_option.text)}")
        except Exception as e:
            self.log.error(
                f"There was issue with selecting dropdown value using using {locatorType} and {locator}: {e}")


    def get_dropdown_list_length(self, locatorType, locator):
        """
        This function returns the number of items in a dropdown element
        """
        try:
            drop_down_element = Select(self.get_element(locatorType, locator))
            dd_length = len(drop_down_element.options)
            self.log.info(f"Found { dd_length} items in dropdown  using {locatorType} and {locator}")
            return dd_length
        except Exception as e:
            self.log.error(f"UNABLE to find length of items in dropdown  using {locatorType} and {locator}")
            return None

    def get_dropdown_list_value_selected(self,locatorType, locator):

        """
        This function returns the value currently selected in a dropdown
        @param locatorType: type of locator
        @param locator: locator value
        @return: selected dropdown list value
        """
        try:
            drop_down_element = Select(self.get_element(locatorType, locator))
            current_selection = str(drop_down_element.first_selected_option.text)
            self.log.info(f"Current selected dropdown value is: {current_selection}")
            return current_selection
        except Exception as e:
            self.log.error(
                f"There was issue with getting dropdown value using using {locatorType} and {locator}: {e}")
            return None

    def select_random_dropdown_list_value(self, locatorType, locator, start_index=0):
        """
        This function selects a random value of a given dropdown
        """
        try:
            drop_down_element = Select(self.get_element(locatorType, locator))
            import random
            random_option = random.randrange(start_index, len(drop_down_element.options))
            drop_down_element.select_by_index(random_option)
            self.util.sleep(2)
            drop_down_element = Select(self.get_element(locatorType, locator))
            self.log.info(f"Selected random dropdown value: {str(drop_down_element.first_selected_option.text)}")
        except Exception as e:
            self.log.error(f"There was issue with selecting random dropdown value using using {locatorType} and {locator}: {e}")

    def select_radio_button(self, locatorType, locator):
        """
		This function selects the radio element passed in
		"""
        elm = self.get_element(locatorType, locator)
        if elm.is_selected() == False:
            elm.click()

    def deselect_radio_button(self, locatorType, locator):
        """
		This function deselects the radio element passed in
		"""
        elm = self.get_element(locatorType, locator)
        if elm.is_selected() == True:
            elm.click()

    def verify_checkbox_is_enabled(self, locatorType, locator):
        """
		This function selects the checkbox element passed in
		"""
        elm = self.get_element(locatorType, locator)
        if elm.is_selected() == True:
            return True
        else:
            return False

    def verify_checkbox_is_disable(self, locatorType, locator):
        """
        This function verifies the checkbox is disabled
        """
        elm = self.get_element(locatorType, locator)
        if elm.is_selected() == False:
            return True
        else:
            return False

    def select_checkbox(self, locatorType, locator):
        """
		This function selects the checkbox element passed in
		"""
        try:
            elm = self.get_element(locatorType, locator)
            if elm.is_selected() == False:
                elm.click()
            self.log.info(f"checkbox was selected using {locatorType} and {locator}")
        except:
            self.log.error(f"There was an issue with selecting checkbox using {locatorType} and {locator}")

    def deselect_checkbox(self, locatorType, locator):
        """
		This function deselects the checkbox element passed in
		"""
        try:
            elm = self.get_element(locatorType, locator)
            if elm.is_selected() == True:
                elm.click()
            self.log.info(f"checkbox was deselected using {locatorType} and {locator}")
        except:
            self.log.error(f"There was an issue with deselecting checkbox using {locatorType} and {locator}")

    def alert_dialog_confirm(self):
        """
		This function Accepts confirmation dialog box
		"""
        try:
            WebDriverWait(self.driver, TIME_OUT).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
            self.log.info("alert accepted")
        except TimeoutException:
            self.log.error("alert was not found")

    def alert_dialog_dismiss(self):
        """
		This function Dismisses confirmation dialog box
		"""
        try:
            WebDriverWait(self.driver, TIME_OUT).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.dismiss()
            self.log.info("alert dismissed")
        except TimeoutException:
            self.log.error("alert was not found")

    def verify_radio_button_is_enabled(self, locatorType, locator):
        """
        This function verifies the radio button is enabled
        :param locatorType:
        :param locator:
        """
        elm = self.get_element(locatorType, locator)
        if elm.is_selected() == True:
            return True
        else:
            return False

    def verify_radio_button_is_disabled(self, locatorType, locator):
        """
        This function verifies the radio button is disabled
        :param locatorType:
        :param locator:
        """
        elm = self.get_elements(locatorType, locator)
        if elm.is_selected() == False:
            return True
        else:
            return False

    def verify_dropdown_listbox_is_enabled(self, locatorType, locator):
        """
        This function verifies the dropdown list box is enabled
        :param locatorType:
        :param locator:
        """
        elm = self.get_element(locatorType, locator)
        if elm.is_selected() == True:
            return True
        else:
            return False

    def verify_dropdown_listbox_is_disabled(self, locatorType, locator):
        """
        This function verifies the dropdown list box is disabled
        :param locatorType:
        :param locator:
        """
        elm = self.get_element(locatorType, locator)
        if elm.is_selected() == False:
            return True
        else:
            return False

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #                                           TABLE Related Methods
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    def table_get_row_count(self, locatorType, locator):
        """ This will return the number of rows for the provided table"""
        try:
            table = self.get_element(locatorType, locator)
            row_count = len(table.find_elements(By.TAG_NAME, 'tr'))
            self.log.info(f"Found {row_count} rows of for {locator}")
            return row_count

        except Exception as e:
            self.log.error(f"There was error getting the table row count for {locator}: Error Details: {e}")
            return None

    def table_get_column_count(self, locatorType, locator):
        """ This will return the number of columns for the provided table"""
        try:
            th_xpath = locator + "/*/tr[1]/th"
            td_xpath = locator + "/*/tr[1]/td"
            if len(self.get_elements(locatorType, th_xpath)) is not None:
                column_count = len(self.get_elements(locatorType, th_xpath))
            else:
                column_count = len(self.get_elements(locatorType, td_xpath))
            self.log.info(f"Found {column_count} columns of for {locator}")
            return column_count

        except Exception as e:
            self.log.error(f"There was error getting the table column count for {locator}: Error Details: {e}")
            return None

    def table_get_row_data_using_rownumber(self, locatorType, locator, row_number):
        """ This will return the row data for the given row number in list format; Parameter expected is row_number;
		Row number should start at 1"""
        try:
            for rows in self.get_elements(locatorType, locator + "/*/tr[" + str(row_number) + "]"):
                #TODO: use table data function method
                return [td.text.strip() for td in rows.find_elements_by_xpath('td')
                        or rows.find_elements_by_xpath('th')]
            self.log.info(f"Returned row # {row_number} data for {locator}")
        except Exception as e:
            self.log.error(f"Unable to return row {row_number}  for table {locator} : Error Details: {e}")

    def table_get_column_data_using_colnumber(self, locatorType, locator, col_number):
        """ This will return the column data for the given column number in list format; Parameter expected is col_number;
		Col number should start at 1"""

        try:
            col_data = []
            for rows in self.get_elements(locatorType, locator + "/*/tr"):
                # TODO: use table data function method
                data = [td.text.strip() for td in rows.find_elements_by_xpath("td[" + str(col_number) + "]") or
                        rows.find_elements_by_xpath("th[" + str(col_number) + "]")]
                for item in data:
                    col_data.append(item)
            self.log.info(f"Returned column # {col_number} data for {locator}")
            return col_data

        except Exception as e:
            self.log.error(f"Unable to return column {col_number}  for table {locator} : Error Details: {e}")


    def table_save_data(self, locatorType, locator, file_name):
        """ This will return write the data for the table to the provided file in csv format"""
        try:
            table = self.get_element(locatorType, locator)
            with open(file_name, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                for rows in table.find_elements_by_css_selector('tr'):
                    csv_writer.writerow([td.text.strip() for td in rows.find_elements(
                        By.XPATH, ".//*[local-name(.)='th' or local-name(.)='td']")])
                self.log.info(f"Wrote table data for table {locator} to file: {file_name}")
                print(table.text)
        except Exception as e:
            self.log.error(f"There was error writing table data for {locator} to file: {file_name}: Error Details: {e}")
