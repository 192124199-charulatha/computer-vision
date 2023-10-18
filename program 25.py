import cv2
import numpy as np

# Load the image
image = cv2.imread(r"C:\Users\HI\Pictures\download.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Calculate the gradient using the Sobel filter
gradient_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Combine the gradient images
gradient_magnitude = cv2.magnitude(gradient_x, gradient_y)

# Normalize the gradient magnitude to the 8-bit range
gradient_magnitude = np.uint8(255 * gradient_magnitude / gradient_magnitude.max())

# Apply the gradient mask to the original image
sharpened_image = cv2.addWeighted(image, 1.5, cv2.cvtColor(gradient_magnitude, cv2.COLOR_GRAY2BGR), -0.5, 0)

# Display the original and sharpened images
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
