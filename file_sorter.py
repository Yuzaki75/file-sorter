import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def sort_files(folder_path):
    # File type categories
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
        "Videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv"],
        "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Music": [".mp3", ".wav", ".aac", ".flac"],
        "Code": [".py", ".js", ".html", ".css", ".cpp", ".java", ".c"],
    }

    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)

        if os.path.isdir(full_path):
            continue

        file_ext = os.path.splitext(file)[1].lower()
        moved = False

        for folder_name, extensions in file_types.items():
            if file_ext in extensions:
                dest_folder = os.path.join(folder_path, folder_name)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(full_path, os.path.join(dest_folder, file))
                moved = True
                break

        if not moved:
            other_folder = os.path.join(folder_path, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(full_path, os.path.join(other_folder, file))

def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_path_var.set(folder)

def start_sorting():
    folder_path = folder_path_var.get()

    if not folder_path:
        messagebox.showerror("Error", "Please select a folder first!")
        return

    try:
        sort_files(folder_path)
        messagebox.showinfo("Success", "Files sorted successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

# GUI Setup
root = tk.Tk()
root.title("Python File Sorter")
root.geometry("400x200")
root.resizable(False, False)

folder_path_var = tk.StringVar()

title_label = tk.Label(root, text="File Sorter", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

path_entry = tk.Entry(root, textvariable=folder_path_var, width=40)
path_entry.pack()

browse_btn = tk.Button(root, text="Browse Folder", command=select_folder)
browse_btn.pack(pady=5)

sort_btn = tk.Button(root, text="Start Sorting", command=start_sorting, bg="#4CAF50", fg="white")
sort_btn.pack(pady=10)

root.mainloop()
