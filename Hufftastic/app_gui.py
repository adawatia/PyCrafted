import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
from huffman_coding import HuffmanCoding

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hufftastic - Huffman Coding Compression Tool")
        self.file_path = tk.StringVar()  # To store selected file path
        self.create_widgets()

    def create_widgets(self):
        # Input file selection
        self.file_entry = tk.Entry(self.root, textvariable=self.file_path, width=50)
        self.file_entry.pack(side=tk.TOP, pady=5)

        self.select_button = tk.Button(self.root, text="Select File", command=self.select_file)
        self.select_button.pack(side=tk.TOP, pady=5)

        # Compress Button
        self.compress_button = tk.Button(self.root, text="Compress File", command=lambda: self.start_task(self.compress_file))
        self.compress_button.pack(side=tk.TOP, pady=5)

        # Decompress Button
        self.decompress_button = tk.Button(self.root, text="Decompress File", command=lambda: self.start_task(self.decompress_file))
        self.decompress_button.pack(side=tk.TOP, pady=5)

        # Progress Bar
        self.progress = ttk.Progressbar(self.root, orient=tk.HORIZONTAL, length=400, mode='determinate')
        self.progress.pack(side=tk.TOP, pady=10)

    def select_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_path.set(file_path)

    def start_task(self, task):
        self.progress['value'] = 0
        self.update_progress()
        threading.Thread(target=task).start()

    def update_progress(self, step=10):
        self.progress['value'] += step
        if self.progress['value'] >= 100:
            return
        self.root.after(100, self.update_progress)

    def compress_file(self):
        file_path = self.file_path.get()
        if file_path:
            huffman = HuffmanCoding(file_path)
            output_path = huffman.compress()
            self.progress['value'] = 100  # Update progress bar to full after completion
            messagebox.showinfo("Success", f"File compressed successfully!\nSaved as: {output_path}")

    def decompress_file(self):
        file_path = self.file_path.get()
        if file_path:
            huffman = HuffmanCoding(file_path)
            output_path = huffman.decompress()
            self.progress['value'] = 100  # Update progress bar to full after completion
            messagebox.showinfo("Success", f"File decompressed successfully!\nSaved as: {output_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()
