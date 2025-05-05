import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfMerger, PdfReader, PdfWriter

def merge_pdfs():
    files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    if not files:
        return

    merger = PdfMerger()
    for file in files:
        merger.append(file)

    output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if output_path:
        merger.write(output_path)
        merger.close()
        messagebox.showinfo("Success", "PDFs merged successfully!")

def split_pdf():
    file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if not file:
        return

    try:
        start = int(start_entry.get())
        end = int(end_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Start and End pages must be numbers.")
        return

    reader = PdfReader(file)
    writer = PdfWriter()

    if start < 1 or end > len(reader.pages) or start > end:
        messagebox.showerror("Error", "Invalid page range.")
        return

    for i in range(start-1, end):
        writer.add_page(reader.pages[i])

    output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if output_path:
        with open(output_path, "wb") as out:
            writer.write(out)
        messagebox.showinfo("Success", "PDF split successfully!")

# GUI
root = tk.Tk()
root.title("PDF Merger & Splitter")
root.geometry("400x250")
root.resizable(False, False)

tk.Label(root, text="PDF Merger & Splitter", font=("Arial", 16)).pack(pady=10)

tk.Button(root, text="Merge PDFs", width=20, command=merge_pdfs).pack(pady=10)

tk.Label(root, text="Split PDF (Enter Page Range)").pack()
start_entry = tk.Entry(root, width=5)
start_entry.pack(side=tk.LEFT, padx=(80, 5))
start_entry.insert(0, "1")

tk.Label(root, text="to").pack(side=tk.LEFT)
end_entry = tk.Entry(root, width=5)
end_entry.pack(side=tk.LEFT, padx=5)
end_entry.insert(0, "2")

tk.Button(root, text="Split PDF", width=20, command=split_pdf).pack(pady=30)

root.mainloop()
