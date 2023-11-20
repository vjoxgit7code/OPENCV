from tkinter import font
import cv2

image = cv2.imread("lena.jpg", 1)

# Define rectangle coordinates
rect_width = 300
rect_height = 120
center_x = image.shape[1] // 2
center_y = image.shape[0] // 2
top_left = (center_x - rect_width // 2, center_y - rect_height // 2)
bottom_right = (center_x + rect_width // 2, center_y + rect_height // 2)

# Draw lines connecting the corners for the envelope
cv2.line(image, top_left, (top_left[0], bottom_right[1]), (255, 0, 0), 2)  # Top-left to bottom-left
cv2.line(image, top_left, (bottom_right[0], top_left[1]), (255, 0, 0), 2)  # Top-left to top-right
cv2.line(image, (bottom_right[0], top_left[1]), bottom_right, (255, 0, 0), 2)  # Top-right to bottom-right
cv2.line(image, (top_left[0], bottom_right[1]), bottom_right, (255, 0, 0), 2)  # Bottom-left to bottom-right

# Add circles at corners
cv2.circle(image, (50, 50), 40, (0, 255, 255), -1)  # Top-left corner (yellow)
cv2.circle(image, (image.shape[0]-50, 50), 40, (0, 255, 255), -1)  # Top-right corner (yellow)
cv2.circle(image, (50, image.shape[1]-50), 40, (0, 255, 255), -1)  # Bottom-left corner (yellow)
cv2.circle(image, (image.shape[1]-50, image.shape[1]-50), 40, (0, 255, 255), -1)  # Bottom-right corner (blue)

# Draw a centered rectangle
cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), 2)

# Add text
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image, "Hello ", (center_x - 80, center_y + 20), font, 2, (0, 255, 0), 3)

# Display the modified image
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
