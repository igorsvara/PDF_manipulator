# PDF Tool

This Python script provides simple functionalities for manipulating PDF files. It currently supports merging multiple PDFs into a single file (`merge` operation) and copying a specific range of pages from one or more PDFs into new files (`copy` operation).

## Prerequisites

- Python 3.x
- PyPDF2 library

Install the required library using:

```bash
pip install PyPDF2
```

## Usage

### Merging PDFs

To merge multiple PDF files into one, use the following command:

```bash
python pdf_tool.py merge file1.pdf file2.pdf ... output.pdf
```

Example:

```bash
python pdf_tool.py merge document1.pdf document2.pdf merged_output.pdf
```

<br>

### Copying Page Ranges
To copy a specific range of pages from one PDF, use the following command:

```bash
python pdf_tool.py copy file1.pdf ... start_page-end_page
```

Example:

```bash
python pdf_tool.py copy document.pdf 15-50
```

---

## Notes
- For the copy operation, the script copies the specified page range (inclusive) from each input PDF into a new file with a name derived from the original file's name.
- Ensure that the specified page range is within the total number of pages in the input PDF(s).
- For the copy operation, the output file is named as original_filename_copy.pdf.

Feel free to explore and modify the script based on your specific use case.