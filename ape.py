import cv2
import pytesseract
import pandas as pd

# Load the image containing the table
image = cv2.imread('scr1.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform thresholding to convert the image to binary
_, binary_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)

# Perform OCR on the binary image
text = pytesseract.image_to_string(binary_image)

# Split the OCR text into lines
lines = text.split('\n')

# Extract the text into a tabular form with three columns: module, coe, and grade
data = []
for line in lines:
    if line.strip() and len(line.split()) >= 3:
        parts = line.split()
        module = ' '.join(parts[:-2])
        coe = parts[-2]
        grade = parts[-1]
        data.append([module, coe, grade])

# Create a DataFrame from the extracted data
df = pd.DataFrame(data, columns=['Module', 'COE', 'Grade'])

# Display the tabular data with three columns
print(df)

