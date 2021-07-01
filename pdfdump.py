import fitz  # this is pymupdf

with fitz.open("1.pdf") as doc:
    text = ""
    for page in doc:
        text += page.getText()
with open('1.txt', 'w+', encoding="utf-8") as f:
    f.write(text)