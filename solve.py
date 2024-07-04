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

# Extract the text into a tabular form
data = []
for line in lines:
    row = line.split('\t')
    data.append(row)

# Create a DataFrame from the extracted data
df = pd.DataFrame(data)

# Display the tabular data
print(df)

