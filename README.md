# PDF Tool
Welcome to the PDF Tool – a versatile Python script that empowers you to manipulate PDF files with unique features.

## Features

### 1. Effortless PDF Merging:
- Merge PDF files seamlessly, allowing customized merge orders.
- Define specific page ranges for each file during the merging process.
- Extract a subset of pages from a PDF by merging with a designated page range.

### 2. Dynamic Page Management:
- Easily rearrange PDF files within the interface to control the merge sequence.
- Update page ranges for individual files effortlessly, providing granular control.
- Streamline PDF extraction by merging with a chosen subset of pages.

### 3. User-Friendly Interface:
- Intuitive graphical interface designed for straightforward navigation.
- Select, remove, and reorder PDF files effortlessly with a list on the right.
- Visual feedback on actions and errors ensures enhanced usability.


## Prerequisites

- Python 3.x
- PyPDF2 library

Install the required library using:
```bash
pip install PyPDF2
```

## Usage

### Run the GUI:
```bash
python pdf_tool_gui.py
```
The graphical interface will appear, allowing you to intuitively perform operations.

### Merge PDFs with Precision:
- Click "Add Files" to select PDFs.
- Use the list on the right to select, reorder, and update individual files.
- Click "Update Range" to modify page ranges for selected files.
- Press "Merge" to combine PDFs into a single file.

### Reorganize and Remove:
- Select a file from the list on the right.
- Use "Move Up" and "Move Down" to reorder files.
- Click "Remove Files" to delete the selected file.

### Additional Information
- Ensure that all selected files have the ".pdf" extension.
- The tool displays warnings for invalid file types.
- Any errors during the merge operation are presented in a popup dialog.
- The script automatically handles file naming during the copy operation.

Feel empowered to explore and adapt the script to your specific needs. The ability to reorder and define subsets of pages makes this PDF Tool a unique and powerful solution for your document manipulation tasks. Happy merging!