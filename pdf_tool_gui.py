import os

import tkinter as tk
from tkinter import filedialog, messagebox

from pdf_tool import *
from dialog import RangeDialog


class PDFgui:

    def __init__(self, master):

        master.wm_iconbitmap(bitmap="res/pdftool.ico")

        self.file_array = []  # Initialize the array
        self.page_ranges = {}
        self.total_page_count = 0

        self.master = master
        self.master.title("PDF TOOLS")

        # Set the window size
        self.master.geometry("700x500")

        # Left side container
        self.left_frame = tk.Frame(self.master)
        self.left_frame.pack(side="left", fill="y", padx=10, pady=10)

        # Top container within left side
        self.button_frame = tk.Frame(self.left_frame)
        self.button_frame.pack(side="top", fill="x", pady=(0, 10))

        # Buttons in the top left container
        self.add_button = tk.Button(self.button_frame, text="Add Files", command=self.add_files)
        self.add_button.pack(side="top", pady=5)
        self.add_button.config(width=10, bg="green", fg="white")

        self.remove_button = tk.Button(self.button_frame, text="Remove Files", command=self.remove_files)
        self.remove_button.pack(side="top", pady=5)
        self.remove_button.config(width=10, bg="red", fg="white")

        self.update_range_button = tk.Button(self.button_frame, text="Update Range", command=self.update_range)
        self.update_range_button.pack(side="top", pady=5)
        self.update_range_button.config(width=10, bg="blue", fg="white")

        # Middle container within left side
        self.move_frame = tk.Frame(self.left_frame)
        self.move_frame.pack(fill="both", expand=True, pady=(50, 0))

        # Buttons in the middle left container
        self.move_up_button = tk.Button(self.move_frame, text="Move Up", command=self.move_up)
        self.move_up_button.pack(side="top", pady=2)
        self.move_up_button.config(width=10)
        self.move_down_button = tk.Button(self.move_frame, text="Move Down", command=self.move_down)
        self.move_down_button.pack(side="top", pady=2)
        self.move_down_button.config(width=10)

        # Bottom container within left side
        self.merge_frame = tk.Frame(self.left_frame)
        self.merge_frame.pack(side="bottom", fill="x", pady=(10, 0))

        # Merge button in the bottom left container
        self.merge_button = tk.Button(self.merge_frame, text="Merge", command=self.merge_files)
        self.merge_button.pack(fill="both", expand=True)

        # Right side container
        self.file_list_frame = tk.Frame(self.master)
        self.file_list_frame.pack(side="right", fill="both", expand=True, padx=(0, 10), pady=10)

        # Listbox to display files in the right container
        self.file_list = tk.Listbox(self.file_list_frame)
        self.file_list.pack(fill="both", expand=True)

        self.total_page_label = tk.Label(self.file_list_frame, text="Total Pages: 0")
        self.total_page_label.pack(side="left", padx=(5, 0), pady=(12, 2))

    def merge_files(self):
        output_path = filedialog.asksaveasfilename(
            title="Save Merged PDF", defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")]
        )

        if output_path:
            try:
                merge_pdfs(self.file_array, self.page_ranges, output_path)
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
                self.total_page_count += f_npages
                self.update_page_count()
                f_range = f"[{self.page_ranges[filename][0]}-{self.page_ranges[filename][1]}]"
                self.file_list.insert(tk.END, f"  {f_range:<15}{f_basename}")

            else:
                messagebox.showwarning("Invalid File Type", "Only PDF files are allowed.")

    def remove_files(self):
        index = self.file_list.curselection()[0]

        p_range = self.page_ranges[self.file_array[index]]

        self.total_page_count -= p_range[1] - p_range[0] + 1
        self.update_page_count()

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
        try:
            f_index = self.file_list.curselection()[0]
        except IndexError:
            messagebox.showwarning("Invalid Selection", "Please select a file.")
            return
        dialog = RangeDialog(self, f_index)  # Keep this as self.master
        dialog.transient(self.master)  # Makes dialog modal
        self.master.wait_window(dialog)

    def process_dialog_values(self, f_index, p_range):
        filename = self.file_array[f_index]

        new_from_page = p_range[0]
        new_to_page = p_range[1]
        if new_from_page is None or new_to_page is None:
            messagebox.showinfo("Update Cancelled", "Range can't be None.")
            return
        if new_from_page < 1 or new_to_page > get_pages(filename):
            messagebox.showwarning("Update Cancelled", "Range not valid.")
            return
        if new_from_page <= new_to_page:
            old_p_range = self.page_ranges[filename]
            self.page_ranges[filename] = p_range

            self.file_list.delete(f_index)
            f_range = f"[{new_from_page}-{new_to_page}]"
            self.file_list.insert(f_index, f"  {f_range:<15}{os.path.basename(filename)}")

            self.total_page_count -= old_p_range[1] - old_p_range[0] + 1
            self.total_page_count += p_range[1] - p_range[0] + 1

            self.update_page_count()
        else:
            messagebox.showwarning("Invalid Page Range",
                                   "Starting page must be less than or equal to ending page.")

    def update_page_count(self):
        self.total_page_label.config(text=f"Total Pages: {self.total_page_count}")

if __name__ == "__main__":
    root = tk.Tk()
    ui = PDFgui(root)
    root.mainloop()


# TODO: Dialog box dovrebbe apparire al centro dello schermo
# TODO: Scrivi quante pagine avra' il file combinato
# TODO: Risolvi problema di collonne diasallineate
