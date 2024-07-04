import cv2 as cv

image_file = "scr1.jpg"
img = cv.imread(image_file)

# preprocessing

# gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imwrite("index_gray.jpg", gray)

# blur
blur = cv.GaussianBlur(gray, (9,9), 0)
cv.imwrite("index_blur.jpg", gray)

# thresholding
thresh = cv.threshold(blur,50,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)[1]
cv.imwrite("index_thresh.jpg", thresh)

# kernels
kernel = cv.getStructuringElement(cv.MORPH_RECT, (40,10))

# dilation
dilate = cv.dilate(thresh, kernel, iterations=5)
cv.imwrite("index_dilate.jpg", dilate)

# creating contours
cnts = cv.findContours(dilate, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
cnts = sorted(cnts, key=lambda x: cv.boundingRect(x)[0])

# eliminate the contours that are too small
# goes from bottom to top
for c in cnts:
	x, y, w, h = cv.boundingRect(c)
	if w > 400 and h < 300:
		# save each piece in an roi
		roi = img[y:y+h, x:x+w]
		cv.imwrite("saved.jpg", roi)
		break
		cv.rectangle(img, (x, y), (x+w, y+h), (36, 255, 12), 2)
cv.imwrite("index_bbox.jpg", img)

