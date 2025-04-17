import cv2
import numpy as np

def add_watermark(image_path, watermark_text, output_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not read image")
        return
    
    overlay = image.copy()
    font = cv2.FONT_HERSHEY_SIMPLEX
    position = (30, 50)
    font_scale = 1
    color = (0, 0, 255)  # Red watermark
    thickness = 2
    
    cv2.putText(overlay, watermark_text, position, font, font_scale, color, thickness)
    cv2.imwrite(output_path, overlay)
    
    cv2.imshow("Watermarked Image", overlay)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    print("Watermark added successfully!")

def main():
    image_path = r"C:/Users/DELL/OneDrive/Pictures/murali painting.jpg"  
    output_path = "watermarked.jpg"
    watermark_text = "Sample Watermark"
    add_watermark(image_path, watermark_text, output_path)
    
if __name__ == "__main__":
    main()
