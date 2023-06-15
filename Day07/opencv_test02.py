import cv2

# 01. Original Image
img = cv2.imread('./Day07/test.jpg')
# cv2.imshow('Original', img)

# 02. Gray Image
# img = cv2.imread('./Day07/test.jpg', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('Gray', img)

# 03. Resize Image
img_small = cv2.resize(img, (200, 90))
# cv2.imshow('Small', img_small)

# 04. Add Gray Image Without Chagning Original 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Original', img)
# cv2.imshow('Gray', gray)

# 05. Cut Image
height, width, channel = img.shape
# print(height, width, channel)
img_crop = img[:, :int(width/2)]
gray_crop = gray[:, :int(width/2)]
# cv2.imshow('Original_half', img_crop)
# cv2.imshow('Gray_half', gray_crop)

# 06. Blur Image
img_blur = cv2.blur(img_crop, (10,10)) # more num more blur
cv2.imshow('Blur half',img_blur)


cv2.waitKey(0)
cv2.destroyAllWindows()