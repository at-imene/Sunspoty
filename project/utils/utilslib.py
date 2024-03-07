
import cv2
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import DBSCAN

def croppeImage(img):

    # # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Threshold the image
    m, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # Find contours
    contours, r = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find contour with the largest area (assumed to be the sun)
    cnt = max(contours, key=cv2.contourArea)

    # Create bounding box around contour
    x, y, w, h = cv2.boundingRect(cnt)

    # Crop image to bounding box
    cropped = gray[y:y+h, x:x+w]

    return cropped

def find_contours(img, sensitivity=70, sobel_kernel=3):
    image = img.copy()
    # Apply Gaussian blur to reduce noise (optional)
    image_blur = cv2.GaussianBlur(image, (5, 5), 2)
    # Define the kernel for dilation
    # kernel = np.ones((3, 3), np.uint8)  # You can adjust the size and shape of the kernel as needed
    # image_blur = cv2.erode(image_blur, kernel, iterations=1)
    # # Perform dilation on the image
    # image_blur = cv2.dilate(image_blur, kernel, iterations=1)

    # Apply Sobel edge detection
    sobel_x = cv2.Sobel(image_blur, cv2.CV_64F, 1, 0, ksize=sobel_kernel)
    sobel_y = cv2.Sobel(image_blur, cv2.CV_64F, 0, 1, ksize=sobel_kernel)
    gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

    # Normalize the gradient magnitude
    gradient_magnitude_normalized = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    # Threshold the gradient magnitude to create a binary image
    threshold_value = sensitivity  # Adjust this value to control the sensitivity
    _, binary_image = cv2.threshold(gradient_magnitude_normalized, threshold_value, 255, cv2.THRESH_BINARY)

    # Find contours of sunspots
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return contours

def getContoursFeatures(contours):
    sunspots_contours = []
    # all_contours = []
    filters_contours = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area <700 and area>2 :
            # Calculate the centroid of the contour
            moments = cv2.moments(contour)
            cx = int(moments['m10'] / moments['m00'])
            cy = int(moments['m01'] / moments['m00'])
            sunspots_contours.append((cx, cy, area))
            filters_contours.append(np.squeeze(contour))

    # Convert the list of sunspots to a numpy array
    sunspots_contours = np.array(sunspots_contours)
    return sunspots_contours, filters_contours

def apply_DBSCAN(data, eps=40 , min_samples=1):
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)

    # Run DBSCAN clustering
    dbscan.fit(data[:, :2])

    # Get the cluster labels assigned to each data point
    labels = dbscan.labels_

    return labels


def get_img_contours(cropped, dist, filtered_contours, num_clusters, labels):
    image_with_contours = cv2.cvtColor(cropped, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(image_with_contours, filtered_contours, -1,
                     (255, 0, 255), 1)  # Red color for contours
    for i in range(num_clusters):
        points_of_cluster = dist[labels == i, :]
        # Compute the minimum and maximum coordinates
        min_x = int(np.min(points_of_cluster[:, 0]) - 10)
        max_x = int(np.max(points_of_cluster[:, 0]) + 10)
        min_y = int(np.min(points_of_cluster[:, 1]) - 10)
        max_y = int(np.max(points_of_cluster[:, 1]) + 10)

        cv2.rectangle(image_with_contours, (min_x, min_y),
                      (max_x, max_y), (0, 0, 255), 2)

    return image_with_contours
    
