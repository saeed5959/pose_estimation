import cv2
import numpy as np

# Load the image
image = cv2.imread('2.png')

# Define the four points that represent your custom polygon (replace these with your points)
points = np.array([(10,20), (400,500), (1000,700), (800,400)], np.int32)

# Create an empty mask with the same dimensions as the image
mask = np.zeros_like(image)

# Fill the custom polygon on the mask
cv2.fillPoly(mask, [points], (255, 255, 255))  # (255, 255, 255) represents white color

# Apply the mask to the original image
result = cv2.bitwise_and(image, mask)


cv2.imwrite("./out.png", result)