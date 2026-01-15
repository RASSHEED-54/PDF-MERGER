from pypdf import PdfWriter

merger = PdfWriter()
pdfs=[]
n = int(input("Enter No of Pdf to be Merged: "))

print("Enter file names :")
print("*****---------*****")

for i in range(1,n+1):
    pdfs.append(str(input(f"Enter  PDF {i}:")))

for pdf in pdfs:
    merger.append(pdf)

merger.write("MergedPDF.pdf")

print("PDFs Merged Successfully !!!")