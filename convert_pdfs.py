import os
import argparse
from pathlib import Path

try:
    import pymupdf4llm
except ImportError:
    print("Error: Required package 'pymupdf4llm' is not installed.")
    print("Please install it by running: pip install pymupdf4llm")
    exit(1)

def convert_pdfs_to_md(directory="."):
    """
    Finds all PDF files in the specified directory and converts them to Markdown.
    It uses pymupdf4llm to preserve as much information (like tables and formatting) as possible.
    """
    pdf_dir = Path(directory)
    pdf_files = list(pdf_dir.glob("*.pdf"))
    
    if not pdf_files:
        print(f"No PDF files found in '{pdf_dir.absolute()}'")
        return

    print(f"Found {len(pdf_files)} PDF file(s). Starting conversion...")

    success_count = 0
    for pdf_path in pdf_files:
        md_path = pdf_path.with_suffix(".md")
        print(f"\nProcessing: {pdf_path.name} -> {md_path.name}")
        
        try:
            # Convert the PDF file to Markdown text format
            md_text = pymupdf4llm.to_markdown(str(pdf_path))
            
            # Write the markdown text to the new .md file
            md_path.write_text(md_text, encoding="utf-8")
            print(f"✔ Successfully saved {md_path.name}")
            success_count += 1
        except Exception as e:
            print(f"✖ Error converting {pdf_path.name}: {e}")

    print(f"\nConversion complete! Successfully converted {success_count} out of {len(pdf_files)} files.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bulk convert all PDF files in a directory to Markdown format.")
    parser.add_argument(
        "--dir", 
        type=str, 
        default=".", 
        help="The directory containing the PDF files (default is the current directory)."
    )
    
    args = parser.parse_args()
    convert_pdfs_to_md(args.dir)
