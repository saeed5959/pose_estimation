import cv2
import numpy as np

def mask_apply(pts, image):
    mask = np.ones_like(image) * 255
    points = np.array([(pts[0,0,0],pts[0,0,1]), (pts[1,0,0],pts[1,0,1]), (pts[2,0,0],pts[2,0,1]), (pts[3,0,0],pts[3,0,1])], np.int32)
    # Fill the polygon (rectangle) on the mask
    cv2.fillPoly(mask, [points], (0,0,0))  # (255, 255, 255) represents white color

    # Apply the mask to the original image
    result = cv2.bitwise_and(image, mask)

    return result

# read images
img_1 = cv2.imread("./1.png", 0)
img_2 = cv2.imread("./2.png", 0)

sift = cv2.SIFT_create()

#find keypoints and descriptors
keypoint_1, descriptor_1 = sift.detectAndCompute(img_1, None)

orb = cv2.ORB_create()
#orb = cv2.ORB_create()

# find the keypoints and descriptors with SIFT
# keypoint_1, descriptor_1 = orb.detectAndCompute(img_1, None)


#some parameter for flann matching algorithm
index_params = dict(algorithm=1, trees=5)
search_params = dict(checks=50)

#flann matching
flann = cv2.FlannBasedMatcher(index_params, search_params)
bf = cv2.BFMatcher()

# find corners of book in second image for pose estimation
h,w = img_1.shape[0], img_1.shape[1]
pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)

img_object = cv2.imread("./2.png", 1)
i = 0
while(True):
    keypoint_2, descriptor_2 = sift.detectAndCompute(img_2, None)
    # keypoint_2, descriptor_2 = orb.detectAndCompute(img_2, None)
    matches = flann.knnMatch(descriptor_1, descriptor_2, k=2)
    # matches = bf.knnMatch(descriptor_1, descriptor_2, k=2)
    # remove bad matching
    good = []
    for m,n in matches:
        if m.distance < 0.4*n.distance:
            good.append(m)

    if len(good) > 2:
        print(len(good))
        keypoint_good_1 = np.float32([keypoint_1[m.queryIdx].pt for m in good])
        keypoint_good_2 = np.float32([keypoint_2[m.trainIdx].pt for m in good])

        #draw just matches
        M, mask = cv2.findHomography(keypoint_good_1, keypoint_good_2, cv2.RANSAC,5.0,)
        matchesMask = mask.ravel().tolist()
        draw_params = dict(matchColor = (0,255,0), singlePointColor = None, matchesMask = matchesMask, flags = 2)
        img_match = cv2.drawMatches(img_1, keypoint_1, img_2, keypoint_2, good, None, **draw_params)
        cv2.imwrite(f"./match_{i}.png", img_match)

        dst = cv2.perspectiveTransform(pts,M)
        img_object = cv2.polylines(img_object,[np.int32(dst)],True,255,3, cv2.LINE_AA)
        print(dst)
        img_2 = mask_apply(dst, img_2)
        i += 1 

    else:
        print("not enough points")
        break


cv2.imwrite("./pose.png", img_object)