#PDF Merger Example

from PyPDF2 import PdfMerger

# create merger object
merger = PdfMerger()

# add pdf files
pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]

for pdf in pdf_files:
    merger.append(pdf)

# output file
merger.write("merged.pdf")

merger.close()

print("PDF files merged successfully")

'''
output:-

PDF files merged successfully

(merged.pdf file created containing file1 + file2 + file3)
'''