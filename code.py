import numpy as np
import cv2

# Load the Haar cascades
face_cascade = cv2.CascadeClassifier('D:/A/Face Detection In Images/dataSet/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('D:/A/Face Detection In Images/dataSet/haarcascade_eye.xml')

# Read the image
img = cv2.imread(r"D:/A/Face Detection In Images/img/barack-obama.jpg")  # nama_file(.jpg)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Draw rectangles around detected faces and eyes
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

# Display the output image
cv2.imshow("img", img)

# Wait for the user to press a key
while True:
    # If 'e' is pressed, exit the program
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

# Clean up and close windows
cv2.destroyAllWindows()
