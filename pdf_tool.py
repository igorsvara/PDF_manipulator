from PyPDF2 import PdfReader, PdfWriter


def merge_pdfs(paths, ranges, output):
    pdf_writer = PdfWriter()

    for path in paths:
        f_range = ranges[path]
        pdf_reader = PdfReader(path)
        for page in range(f_range[0]-1, f_range[1]):
            pdf_writer.add_page(pdf_reader.pages[page])

    with open(output, 'wb') as out:
        pdf_writer.write(out)


def copy_range(path, start_page, end_page, name_of_copy):
    pdf = PdfReader(path)

    # Validate page range
    if end_page >= len(pdf.pages):
        end_page = len(pdf.pages) - 1

    pdf_writer = PdfWriter()
    for page in range(start_page, end_page + 1):
        pdf_writer.add_page(pdf.pages[page])

    output = f'{name_of_copy}_copy.pdf'
    with open(output, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)


def get_pages(path):
    pdf = PdfReader(path)
    return len(pdf.pages)
