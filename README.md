# PDF Merger & Splitter

## Overview

PDF Merger & Splitter is a Python-based desktop GUI tool that allows users to merge and split PDF files effortlessly.  
The tool is built with **Tkinter** for the interface and **pypdf** for PDF manipulation, providing a seamless experience for managing PDFs.

---

## 🧰 Technology Stack

| Component     | Purpose                                         | External Install Required?        |
|---------------|-------------------------------------------------|-----------------------------------|
| **Python 3.x**| Programming logic                               | ✅ Yes                            |
| **Tkinter**   | GUI framework (comes with Python)               | ❌ No                             |
| **pypdf**     | PDF merging/splitting functions                 | ✅ Yes (`pip install pypdf`)      |
| **PyInstaller**| Packaging the app as a Windows executable (.exe) | ✅ Yes                            |

---

## ✅ Key Features

- **Merge** multiple PDFs into a single file.
- **Split** PDFs into separate individual files.
- **User-friendly** desktop GUI for easy interaction.
- **Completely offline** – no internet connection required.
- **Windows Packaging** – Optionally packaged into a `.exe` for easy distribution.

---

## 🛠️ Installation Instructions

1. Clone this repository:

    ```bash
    git clone https://github.com/vlaprogrammer3534/pdf-merger-splitter.git
    ```

2. Install the required Python libraries:

    ```bash
    pip install pypdf
    ```

3. (Optional) To create a Windows executable, use **PyInstaller**:

    ```bash
    pip install pyinstaller
    pyinstaller --onefile yourscript.py
    ```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Developed By

Mudassir Ijaz  
For: Desktop PDF Utility  
Stack: Python, Tkinter, pypdf  
📅 April 2025
