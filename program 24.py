import cv2
import numpy as np

# Read the image
image = cv2.imread(R"C:\Users\HI\Pictures\sukuna.jpg")

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define the value of 'A' (adjust this value as needed)
A = 1  # Change this value to control the sharpening effect

# Define the Laplacian mask
laplacian_mask = np.array([[0, -1, 0],
                           [-1, A + 4, -1],
                           [0, -1, 0]], dtype=np.float32)

# Apply the convolution with the Laplacian mask
sharpened_image = cv2.filter2D(gray_image, -1, laplacian_mask)

# Add the result of the convolution to the original image
sharpened_image = cv2.addWeighted(gray_image, 1 + A, sharpened_image, -A, 0)

# Convert the sharpened image back to BGR format
sharpened_image = cv2.cvtColor(sharpened_image, cv2.COLOR_GRAY2BGR)

# Display the original and sharpened images
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the sharpened image to a file
cv2.imwrite('sharpened_image.jpg', sharpened_image)
