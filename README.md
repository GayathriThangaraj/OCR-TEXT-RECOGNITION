Install dependencies with:
pip install opencv-python pytesseract numpy
You also need to install Tesseract-OCR separately:

Download Tesseract for Windows

During installation, note the install path (e.g., C:/Program Files/Tesseract-OCR/tesseract.exe) and update this line in the script if needed:

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
How to Run
Place your image (e.g., text.png) in the same folder.

Run the script:
python main.py
