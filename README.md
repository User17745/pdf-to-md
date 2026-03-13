# PDF to Markdown Converter

A lightweight Python script to easily bulk convert PDF files into Markdown (`.md`) format.

This simple tool preserves the layout and text properties as much as possible, including tables, lists, and formatting. This makes it exceptional for transferring manual documentation into a plain text structure or feeding data into LLMs (Large Language Models).

## Prerequisites

- **Python 3.6** or higher
- The `pymupdf4llm` library

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/User17745/pdf-to-md.git
   cd pdf-to-md
   ```

2. Install the required Python packages:
   ```bash
   pip install pymupdf4llm
   ```

## Usage

Place the PDFs you'd like to convert into your current directory, then execute the script:

```bash
python convert_pdfs.py
```

### Specifying a Custom Directory

You can point the tool to explicitly target a custom directory containing your PDFs using the `--dir` flag.

```bash
python convert_pdfs.py --dir /path/to/your/pdf/folder
```

## How It Works

The script operates by locating all `.pdf` files inside your targeted directory (the current one by default) and looping through them one-by-one. Based on the filename, it cleanly generates formatted Markdown files possessing the exact same names, respectively inside the same directory structure.
