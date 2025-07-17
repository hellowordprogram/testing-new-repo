import tkinter as tk
from tkinter import filedialog, messagebox

# --- Functions ---
def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, content)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            content = text_area.get(1.0, tk.END)
            file.write(content)
        messagebox.showinfo("Saved", "File saved successfully!")

# --- Main UI ---
root = tk.Tk()
root.title("Notepad ✨")
root.geometry("800x500")
root.config(bg="#2c3e50")

# --- Sidebar ---
side_frame = tk.Frame(root, width=120, bg="#34495e")
side_frame.pack(side=tk.LEFT, fill=tk.Y)

tk.Label(side_frame, text="Options", font=("Helvetica", 14, "bold"), bg="#34495e", fg="white").pack(pady=(30, 10))

btn_style = {"font": ("Helvetica", 12, "bold"), "bg": "#1abc9c", "fg": "white", "bd": 0, "activebackground": "#16a085"}

tk.Button(side_frame, text="Open File", command=open_file, **btn_style, height=2, width=12).pack(pady=10)
tk.Button(side_frame, text="Save File", command=save_file, **btn_style, height=2, width=12).pack(pady=10)

# --- Text Area ---
text_area = tk.Text(root, wrap="word", font=("Consolas", 14), bg="#ecf0f1", fg="#2c3e50", padx=10, pady=10, undo=True)
text_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Scrollbar
scrollbar = tk.Scrollbar(text_area)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_area.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_area.yview)

root.mainloop()
