import pandas as pd
import tkinter as tk
from tkinter import filedialog

# --------------------
# Data Processing Functions
# --------------------

def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        selected_file_path.set(file_path)

def format_file():
    if selected_file_path.get() == "No file selected":
        print("No file selected. Please select a file first.")
        return

    df = pd.read_csv(selected_file_path.get(), delimiter=';')
    df['Transaction Amount'] = df['Transaction Amount'].str.replace(',', '.')
    df['Transaction Amount'] = df['Transaction Amount'].astype(float)
    df['Transaction Amount'] = df['Transaction Amount'].apply(lambda x: '{:,.2f}'.format(x).replace(',', 'X').replace('.', ',').replace('X', '.'))
    excel_file_path = selected_file_path.get().replace('.csv', '_formatted.xlsx')
    df.to_excel(excel_file_path, index=False)
    print(f"File formatted and saved as {excel_file_path}")

    # Update the label to show the success message and saved file path
    success_message = f"File saved to {excel_file_path}"
    selected_file_path.set(

    )

# --------------------
# UI Section
# --------------------

# Initialize the Tkinter window
root = tk.Tk()
root.title('CSV to Excel Formatter')

# Set the window size and make it non-resizable
root.geometry("500x250")
root.resizable(False, False)

# Change background color
root.configure(bg='black')

# Initialize a variable to hold the selected file path
selected_file_path = tk.StringVar()
selected_file_path.set("No file selected")

# Create and place the buttons and label
import_button = tk.Button(root, text="Select file to import", command=open_file_dialog, font=("Arial", 12), bg="white", fg="black")
import_button.pack(pady=10)
format_button = tk.Button(root, text="Format File", command=format_file, font=("Arial", 12), bg="white", fg="black")
format_button.pack(pady=10)
file_path_label = tk.Label(root, textvariable=selected_file_path, font=("Arial", 12), bg="black", fg="white")
file_path_label.pack(pady=10)


# Run the Tkinter event loop
root.mainloop()
