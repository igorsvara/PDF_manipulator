import tkinter as tk

def merge_pdfs():
    print("Merge button clicked")

def copy_pdfs():
    print("Copy button clicked")

root = tk.Tk()
root.title("PDF TOOLS")

# Set the window size
root.geometry("700x500")

# Title Label at the center top
title_label = tk.Label(root, text="PDF TOOLS", font=("Helvetica", 16))
# title_label.pack(side="top", pady=20)
title_label.pack(anchor='center', pady="30")

# # Merge Button
# merge_button = tk.Button(root, text="Merge", command=merge_pdfs)
# merge_button.pack(side="bottom", anchor="center", padx=10, pady=30)
# # merge_button.grid(row=3, column=0, sticky="s", padx=10, pady=5)
#
# # Copy Button
# copy_button = tk.Button(root, text="Copy", command=copy_pdfs)
# merge_button.pack(side="bottom", anchor="center", padx=10, pady=30)
# # copy_button.grid(row=3, column=1, sticky="s", padx=10, pady=5)


# Button dimensions (adjust as needed)
button_width = 100
button_height = 50

# Main container for buttons
button_container = tk.Frame(root, bg="lightblue")
container_width = 2 * button_width + 10  # Add 10 for spacing

# Set the container width
button_container.config(width=200)
button_container.pack(side="bottom", anchor="center", fill="both")



# Left button
left_button = tk.Button(button_container, text="Left Button", command=merge_pdfs)
left_button.pack(side="left", padx=5, pady=5)

# Right button
right_button = tk.Button(button_container, text="Right Button", command=copy_pdfs)
right_button.pack(side="left", padx=5, pady=5)



# Start the Tkinter event loop
root.mainloop()