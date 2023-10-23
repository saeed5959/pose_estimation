import cv2
import numpy as np

# read images
img_1 = cv2.imread("./1_4.jpg", 0)
img_2 = cv2.imread("./2_4.jpg", 0)

sift = cv2.SIFT_create()

#find keypoints and descriptors
keypoint_1, descriptor_1 = sift.detectAndCompute(img_1, None)
keypoint_2, descriptor_2 = sift.detectAndCompute(img_2, None)

orb = cv2.ORB_create()
#orb = cv2.ORB_create()

# find the keypoints and descriptors with SIFT
keypoint_1, descriptor_1 = orb.detectAndCompute(img_1, None)
keypoint_2, descriptor_2 = orb.detectAndCompute(img_2, None)

#some parameter for flann matching algorithm
index_params = dict(algorithm=0, trees=5)
search_params = dict(checks=50)

#flann matching
flann = cv2.FlannBasedMatcher(index_params, search_params)

# matches = flann.knnMatch(descriptor_1, descriptor_2, k=2)
bf = cv2.BFMatcher()
matches = bf.knnMatch(descriptor_1, descriptor_2, k=2)
# remove bad matching
good = []
for m,n in matches:
    if m.distance < 0.9*n.distance:
        good.append(m)

if len(good) > 10:
    keypoint_good_1 = np.float32([keypoint_1[m.queryIdx].pt for m in good])
    keypoint_good_2 = np.float32([keypoint_2[m.trainIdx].pt for m in good])

    #draw just matches
    M, mask = cv2.findHomography(keypoint_good_1, keypoint_good_2, cv2.RANSAC,5.0)
    matchesMask = mask.ravel().tolist()
    draw_params = dict(matchColor = (0,255,0), singlePointColor = None, matchesMask = matchesMask, flags = 2)
    img_match = cv2.drawMatches(img_1, keypoint_1, img_2, keypoint_2, good, None, **draw_params)
    
else:
    img_match = cv2.drawMatches(img_1, keypoint_1, img_2, keypoint_2, good, None)
    cv2.imwrite("./match.png", img_match)
    print("not enough points")
    raise

# find corners of book in second image for pose estimation
h,w = img_1.shape[0], img_1.shape[1]
pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
print(f"q1 = {pts[0]}")
print(f"q2 = {pts[1]}")
print(f"q3 = {pts[2]}")
print(f"q4 = {pts[3]}")
dst = cv2.perspectiveTransform(pts,M)
print(f"p1 = {dst[0]}")
print(f"p2 = {dst[1]}")
print(f"p3 = {dst[2]}")
print(f"p4 = {dst[3]}")
img_object  = cv2.polylines(img_2,[np.int32(dst)],True,255,3, cv2.LINE_AA,)


cv2.imwrite("./match.png", img_match)
cv2.imwrite("./pose.png", img_object)