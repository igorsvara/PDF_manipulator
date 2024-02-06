from pdf_tool import merge_pdfs
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os


class FileUI:

    def __init__(self, master):

        self.file_array = []  # Initialize the array

        self.master = master
        self.master.title("PDF TOOLS")

        # Set the window size
        self.master.geometry("700x500")

        # Frame for buttons
        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(side="top", fill="both")  # Place buttons on the left

        # Buttons for adding, removing, and moving files
        self.add_button = tk.Button(self.button_frame, text="Add Files", command=self.add_files)
        self.add_button.pack(side="left", padx=10, pady=20)  # Add padding for spacing
        self.remove_button = tk.Button(self.button_frame, text="Remove Files", command=self.remove_files)
        self.remove_button.pack(side="left", padx=10, pady=20)
        self.move_up_button = tk.Button(self.button_frame, text="Move Up", command=self.move_up)
        self.move_up_button.pack(side="left", padx=10, pady=20)
        self.move_down_button = tk.Button(self.button_frame, text="Move Down", command=self.move_down)
        self.move_down_button.pack(side="left", padx=10, pady=20)

        # Frame for file list
        self.file_list_frame = tk.Frame(self.master)
        self.file_list_frame.pack(side="right", fill="both", expand=True)  # Place file list on the right

        # Listbox to display files
        self.file_list = tk.Listbox(self.file_list_frame, selectmode="multiple")
        self.file_list.pack(fill="both", expand=True)

        self.merge_button = tk.Button(self.master, text="Merge", command=self.merge_files)
        self.merge_button.pack(side="bottom", pady=20)  # Place it at the bottom

    def merge_files(self):
        if len(self.file_array) < 2:
            messagebox.showwarning("No Files to Merge", "Please add at least two files to merge.")
            return  # Exit the function here
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
                self.file_list.insert(tk.END, os.path.basename(filename))
                self.file_array.append(filename)
            else:
                messagebox.showwarning("Invalid File Type", "Only PDF files are allowed.")

    def remove_files(self):
        selected_indices = self.file_list.curselection()
        for index in reversed(selected_indices):
            self.file_list.delete(index)
            del self.file_array[index]  # Remove from the array

    def move_up(self):
        selected_indices = self.file_list.curselection()
        for index in selected_indices[::-1]:  # Reverse order to avoid index shifts
            if index > 0:  # Ensure not at the top
                item = self.file_list.get(index)
                self.file_list.delete(index)
                self.file_list.insert(index - 1, item)
                self.file_list.select_set(index - 1)  # Reselect the moved item
                self.file_array.insert(index - 1, self.file_array.pop(index))  # Update array order

    def move_down(self):
        selected_indices = self.file_list.curselection()
        for index in selected_indices:
            if index < self.file_list.size() - 1:  # Ensure not at the bottom
                item = self.file_list.get(index)
                self.file_list.delete(index)
                self.file_list.insert(index + 1, item)
                self.file_list.select_set(index + 1)  # Reselect the moved item
                self.file_array.insert(index + 1, self.file_array.pop(index))  # Update array order

if __name__ == "__main__":
    root = tk.Tk()
    ui = FileUI(root)
    root.mainloop()
