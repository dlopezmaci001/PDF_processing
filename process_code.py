# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 12:39:56 2019

@author: daniel.lopez
"""

# Merging PDF's

# Merging Multiple PDF Documents with Python 3.7 and PyPDF2
import glob
from PyPDF2 import PdfFileWriter, PdfFileReader

def merger(output_path, input_paths):
    """ 
    Creates a function that combines pdf files in a given folder
    """
    pdf_writer = PdfFileWriter()
    for path in input_paths:
            pdf_reader = PdfFileReader(path)
            for page in range(pdf_reader.getNumPages()):
                    pdf_writer.addPage(pdf_reader.getPage(page))
                    with open(output_path, 'wb') as fh:
                        pdf_writer.write(fh)
                        
                        

# Set the directorty where to look for the files
if __name__ == '__main__':
    paths = glob.glob('PATH/R*.pdf')

"""
In this case we are going to merge all files starting with the letter R
"""

paths.sort()

# Merge the PDF's to the location with the given name
merger('PATHf/PAD_NAME.pdf', paths)


# Splitting PDF files into multiple files

import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def pdf_splitter(path):
    """
    Function to splid PDF files into pages and save them in the given repository
    """
    fname = os.path.splitext(os.path.basename(path))[0]
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        output_filename = 'PATH/{}_page_{}.pdf'.format(fname, page+1)
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)
            print('Created: {}'.format(output_filename))

if __name__ == '__main__':
    path = "PATH/PDF_NAME.pdf"

pdf_splitter(path)

# Extract text from PDF

from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import BytesIO

def pdf_to_text(path):
    manager = PDFResourceManager()
    retstr = BytesIO()
    layout = LAParams(all_texts=True)
    device = TextConverter(manager, retstr, laparams=layout)
    filepath = open(path, 'rb')
    interpreter = PDFPageInterpreter(manager, device)
    for page in PDFPage.get_pages(filepath, check_extractable=True):
        interpreter.process_page(page)
        text = retstr.getvalue()
        filepath.close()
        device.close()
        retstr.close()
        return text

if __name__ == "__main__":
    text = pdf_to_text("PATH/PAD_NAME.pdf")

print(text)

from io import StringIO
import pandas as pd

t = str(text,'utf-8')

data = StringIO(t)

df = pd.read_csv(data, delimiter = '\n')
