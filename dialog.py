import tkinter as tk
from tkinter import messagebox


class RangeDialog(tk.Toplevel):
    def __init__(self, parent, f_index):
        super().__init__(parent.master)
        self.wm_iconbitmap(bitmap="res/pdftool.ico")
        self.parent_instance = parent
        self.file_index = f_index

        self.title("Update Page Range")
        self.resizable(False, False)

        # Label for starting page
        self.label_from = tk.Label(self, text="Starting page:")
        self.label_from.grid(row=0, column=0, padx=5, pady=5)

        # Entry field for starting page
        self.entry_from = tk.Entry(self, width=10)
        self.entry_from.grid(row=0, column=1, padx=5, pady=5)

        # Label for ending page
        self.label_to = tk.Label(self, text="Ending page:")
        self.label_to.grid(row=1, column=0, padx=5, pady=5)

        # Entry field for ending page
        self.entry_to = tk.Entry(self, width=10)
        self.entry_to.grid(row=1, column=1, padx=5, pady=5)

        # Button to submit the values
        self.submit_button = tk.Button(self, text="Submit", command=self.on_submit)
        self.submit_button.grid(row=2, columnspan=2, padx=5, pady=5)

    def on_submit(self):
        try:
            new_from_page = int(self.entry_from.get())
            new_to_page = int(self.entry_to.get())
            if new_from_page <= new_to_page:
                self.parent_instance.process_dialog_values(self.file_index, (new_from_page, new_to_page))
            else:
                messagebox.showwarning("Invalid Page Range", "Starting page must be less than or equal to ending page.")
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter valid integer values.")

        self.destroy()

