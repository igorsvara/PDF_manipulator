import os

import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

from pdf_tool import *
from dialog import RangeDialog


class FileUI:

    def __init__(self, master):

        self.file_array = []  # Initialize the array
        self.page_ranges = {}

        self.master = master
        self.master.title("PDF TOOLS")

        # Set the window size
        self.master.geometry("700x500")

        # Frame for buttons
        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(side="top", fill="both", padx=10, pady=20)

        # Buttons for adding, removing, and moving files
        self.add_button = tk.Button(self.button_frame, text="Add Files", command=self.add_files)
        self.add_button.pack(side="left", padx=(0, 10))
        self.remove_button = tk.Button(self.button_frame, text="Remove Files", command=self.remove_files)
        self.remove_button.pack(side="left", padx=10)
        self.move_up_button = tk.Button(self.button_frame, text="Move Up", command=self.move_up)
        self.move_up_button.pack(side="left", padx=10)
        self.move_down_button = tk.Button(self.button_frame, text="Move Down", command=self.move_down)
        self.move_down_button.pack(side="left", padx=10)
        self.update_range_button = tk.Button(self.button_frame, text="Update Range", command=self.update_range)
        self.update_range_button.pack(side="left", padx=10)

        # Frame for file list
        self.file_list_frame = tk.Frame(self.master)
        self.file_list_frame.pack(fill="both", expand=True, pady=10, padx=10)  # Place file list on the right

        # Listbox to display files
        self.file_list = tk.Listbox(self.file_list_frame)
        self.file_list.pack(fill="both", expand=True)

        self.merge_button = tk.Button(self.master, text="Merge", command=self.merge_files)
        self.merge_button.pack(side="left", padx=10, pady=20)  # Place it at the bottom

    def merge_files(self):
        if len(self.file_array) < 2:
            messagebox.showwarning("No Files to Merge", "Please add at least two files to merge.")
            return
        output_path = filedialog.asksaveasfilename(
            title="Save Merged PDF", defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")]
        )

        if output_path:
            try:
                merge_pdfs(self.file_array, output_path)
                tk.messagebox.showinfo("Merge Successful", "PDFs merged successfully!")
            except Exception as e:
                tk.messagebox.showerror("Merge Error", f"An error occurred: {e}")

    def add_files(self):
        filenames = filedialog.askopenfilenames(title="Select Files")
        for filename in filenames:
            if filename.endswith(".pdf"):  # Check filename extension
                f_basename = os.path.basename(filename)
                f_npages = get_pages(filename)
                self.file_array.append(filename)
                self.page_ranges[filename] = (1, f_npages)
                f_range = f"[{self.page_ranges[filename][0]}-{self.page_ranges[filename][1]}]"
                self.file_list.insert(tk.END, f"  {f_range:<15}{f_basename}")

            else:
                messagebox.showwarning("Invalid File Type", "Only PDF files are allowed.")

    def remove_files(self):
        index = self.file_list.curselection()[0]
        self.file_list.delete(index)
        del self.page_ranges[self.file_array[index]]  # Remove from the dictionary
        del self.file_array[index]  # Remove from the array

    def move_up(self):
        index = self.file_list.curselection()[0]
        if index > 0:  # Ensure not at the top
            item = self.file_list.get(index)
            self.file_list.delete(index)
            self.file_list.insert(index - 1, item)
            self.file_list.select_set(index - 1)  # Reselect the moved item
            self.file_array.insert(index - 1, self.file_array.pop(index))  # Update array order

    def move_down(self):
        index = self.file_list.curselection()[0]
        if index < self.file_list.size() - 1:  # Ensure not at the bottom
            item = self.file_list.get(index)
            self.file_list.delete(index)
            self.file_list.insert(index + 1, item)
            self.file_list.select_set(index + 1)  # Reselect the moved item
            self.file_array.insert(index + 1, self.file_array.pop(index))  # Update array order

    def update_range(self):
        index = self.file_list.curselection()[0]

        filename = self.file_array[index]

        # dialog = RangeDialog(self.master)
        # dialog.mainloop()

        dialog = RangeDialog(self.master)  # Keep this as self.master
        r_tuple = self.master.wait_window(dialog)
        if r_tuple is not None:
            (new_from_page, new_to_page) = r_tuple

        print(f"from: {new_from_page}, to: {new_to_page}")

        if new_from_page is not None and new_to_page is not None:
            # Validate page range (ensure new_from_page <= new_to_page)
            if new_from_page <= new_to_page:
                self.page_ranges[filename] = (new_from_page, new_to_page)
                self.file_list.delete(index)
                f_range = f"[{new_from_page}-{new_to_page}]"
                self.file_list.insert(index, f"  {f_range:<15}{os.path.basename(filename)}")
            else:
                messagebox.showwarning("Invalid Page Range",
                                       "Starting page must be less than or equal to ending page.")
        else:
            messagebox.showinfo("Update Cancelled", "Update cancelled.")


if __name__ == "__main__":
    root = tk.Tk()
    ui = FileUI(root)
    root.mainloop()
