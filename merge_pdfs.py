#  Merges PDF docs in the oflder
import os
from PyPDF2 import PdfFileMerger

path = r"<insert your path>"

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