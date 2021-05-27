#  Merges PDF docs in the oflder
import os
import re
import fitz
from PyPDF2 import PdfFileMerger, PdfFileReader


def pdf_parse_using_pypdf2(path=None, search_text=None):
    files_to_process = ['.pdf']
    for root, dirnames, filenames in os.walk(path):
        for file in filenames:
            fileName, ext = os.path.splitext(file)
            if ext.lower() in files_to_process:
                print(f"Processing {file}... ")
                pdf = PdfFileReader(file, 'rb')
                number_of_pages = pdf.getNumPages()
                print(number_of_pages)
                page = pdf.getPage(1)
                print(page.extractText())
                if search_text:
                    page_content = page.extractText()
                    print(page_content)
                    if search_text in page_content:
                        print(f"Found {search_text} in PDF!")


def merge_pdfs(path=None):
    """
    merges all pdfs in given folder
    """
    merged_pdf_name = 'merged_doc.pdf'
    merger = PdfFileMerger()
    files_to_process = ['.pdf']
    for root, dirnames, filenames in os.walk(path):
         for file in filenames:
            fileName, ext = os.path.splitext(file)
            if ext.lower() in files_to_process:
                try:
                    print(f"Processing {file}...")
                    merger.append(os.path.join(root,file))
                except:
                    print(f"Issue with {file}...skipping")
    print("Merging...")
    # save merged file to path provided
    merger.write(os.path.join(path, merged_pdf_name))
    merger.close()
    print("Merging Complete!")

def get_pdf_data(parent_folder=None):
    for dirName, subdirs, fileList in os.walk(parent_folder):
        print('Scanning %s...' % dirName)
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(dirName, filename)
            print(f"Searching file: {path}...")

            with fitz.open(path) as doc:
                for page in doc:
                    text = page.getText()
                    print(text)

def parse_pdf_using_regex(parent_folder=None, pattern=None):
    # https://pymupdf.readthedocs.io/en/latest/tutorial.html
    # pip install PyMuPDF
    # https://github.com/pymupdf/PyMuPDF/tree/master/tests

    match_list = []
    # loop thru each folder
    for dirName, subdirs, fileList in os.walk(parent_folder):
        print('Scanning %s...' % dirName)
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(dirName, filename)
            print(f"Searching file: {path}...")

            with fitz.open(path) as doc:
                for page in doc:
                    text = page.getText()
                    #  using match
                    matches = re.findall(pattern, text, re.DOTALL)
                    # add matches to main list
                    [match_list.append(item) for item in matches]

    print(f"Found total of {len(match_list)} items with pattern {pattern}")
    print(match_list)
    return  match_list
# function calls
# merge_pdfs(path = r"<insert your path>")
# parse_pdf_using_regex(parent_folder=r'C:\temp',
#                       pattern=r'[\$]{1}[\d,]+\.?\d{0,2}')
get_pdf_data(parent_folder=r'C:\temp')