from PyPDF2 import PdfReader
pdf_file = open('sample.pdf', 'rb')
pdf_reader = PdfReader(pdf_file)
num_pages = len(pdf_reader.pages)
data = ''
for page_number in range(num_pages):
    page = pdf_reader.pages[page_number]
    text = page.extract_text()
    data += text

with open('sample.txt', 'w', encoding='utf-8') as file:
    file.write(data)


file.close()
pdf_file.close()

