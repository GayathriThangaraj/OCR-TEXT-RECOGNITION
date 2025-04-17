import cv2
import pytesseract
import numpy as np

# Set Tesseract OCR Path
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

# Load Image
image_path = "text.png"  # Ensure the image is in the same directory
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Could not load image at {image_path}. Check file path and format.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Resize image to improve OCR accuracy
scale_factor = 2  # Increase size by 2x
gray = cv2.resize(gray, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)

# Denoise using Gaussian Blur
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Adaptive Thresholding (better for uneven lighting)
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                               cv2.THRESH_BINARY, 11, 2)

# Morphological Operations (Dilation and Erosion) to improve text clarity
kernel = np.ones((2, 2), np.uint8)
thresh = cv2.dilate(thresh, kernel, iterations=1)
thresh = cv2.erode(thresh, kernel, iterations=1)

# Improve contrast using Histogram Equalization
thresh = cv2.equalizeHist(thresh)

# OCR Configuration
custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

# Use image_to_data() for better spacing
ocr_data = pytesseract.image_to_data(thresh, config=custom_config, output_type=pytesseract.Output.DICT)

# Extract text with spacing
extracted_text = ""
for i in range(len(ocr_data['text'])):
    if int(ocr_data['conf'][i]) > 60:  # Confidence threshold
        extracted_text += ocr_data['text'][i] + " "  # Add spaces between words

print("Extracted Text:\n", extracted_text)

# Save Extracted Text to a File
with open("extracted_text.txt", "w", encoding="utf-8") as file:
    file.write(extracted_text)

# Draw Bounding Boxes around Detected Text
for i in range(len(ocr_data['text'])):
    if int(ocr_data['conf'][i]) > 60:  # Confidence filter
        (x, y, w, h) = (ocr_data["left"][i], ocr_data["top"][i], ocr_data["width"][i], ocr_data["height"][i])
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Show Processed Image and Detected Text
cv2.imshow("Processed Image", thresh)
cv2.imshow("Text Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
