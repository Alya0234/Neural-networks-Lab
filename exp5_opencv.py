import cv2

img = cv2.imread("image1.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

resized = cv2.resize(img, (300, 300))

blur = cv2.GaussianBlur(img, (5, 5), 0)

edges = cv2.Canny(img, 100, 200)

cv2.imwrite("gray.jpg", gray)
cv2.imwrite("resized.jpg", resized)
cv2.imwrite("blur.jpg", blur)
cv2.imwrite("edges.jpg", edges)

print("Images processed and saved")