import cv2
import numpy as np

# read images
img_1 = cv2.imread("./feature_matching/python_code/1.png", 1)
img_2 = cv2.imread("./feature_matching/python_code/2.png", 1)

sift = cv2.SIFT_create()

#find keypoints and descriptors
keypoint_1, descriptor_1 = sift.detectAndCompute(img_1, None)
keypoint_2, descriptor_2 = sift.detectAndCompute(img_2, None)

#some parameter for flann matching algorithm
index_params = dict(algorithm=1, trees=5)
search_params = dict(checks=50)

#flann matching
flann = cv2.FlannBasedMatcher(index_params, search_params)

matches = flann.knnMatch(descriptor_1, descriptor_2, k=2)

# remove bad matching
good = []
for m,n in matches:
    if m.distance < 0.4*n.distance:
        good.append(m)

if len(good) > 10:
    keypoint_good_1 = np.float32([keypoint_1[m.queryIdx].pt for m in good])
    keypoint_good_2 = np.float32([keypoint_2[m.trainIdx].pt for m in good])

    #draw just matches
    M, mask = cv2.findHomography(keypoint_good_1, keypoint_good_2, cv2.RANSAC,5.0)
    matchesMask = mask.ravel().tolist()
    draw_params = dict(matchColor = (0,255,0), singlePointColor = None, matchesMask = matchesMask, flags = 2)
    
else:
    print("not enough points")
    raise

img_out = cv2.drawMatches(img_1, keypoint_1, img_2, keypoint_2, good, None, **draw_params)

cv2.imwrite("./feature_matching/python_code/out.png", img_out)