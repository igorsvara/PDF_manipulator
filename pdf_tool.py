from PyPDF2 import PdfReader, PdfWriter
import sys

def merge_pdfs(paths, output):
    pdf_writer = PdfWriter()

    for path in paths:
        pdf_reader = PdfReader(path)
        for page in range(len(pdf_reader.pages)):
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

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python pdf_tool.py [merge/copy] file1.pdf file2.pdf ... [output.pdf/page_range]")
        sys.exit(1)

    operation = sys.argv[1].lower()
    input_files = sys.argv[2:-1]
    output_file = sys.argv[-1]

    if operation == 'merge':
        merge_pdfs(input_files, output_file)
        print(f'Merged PDFs: {input_files} into {output_file}')
    elif operation == 'copy':
        # Specify the page range as the last argument
        try:
            start, end = map(int, output_file.split('-'))
        except ValueError:
            print("Invalid page range. Provide a valid page range like '1-5'.")
            sys.exit(1)

        for input_file in input_files:
            copy_range(input_file, start-1, end-1, name_of_copy=input_file.split('\\')[-1].split('.')[0])
            print(f'Copied {input_file} from page {start} to {end}')
    else:
        print("Invalid operation. Use 'merge' or 'copy'.")
