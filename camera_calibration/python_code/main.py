import cv2
import numpy as np
import glob


CHECKBOARD = (6,9)
criteria = (cv2.TermCriteria_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

object_points = []
image_points = []

# define 3d coordinate of chessboard points. chessboard is in center coordinate and camera moving around it 
# we consider every square in chessboard as 1 unit
objp = np.zeros((1,CHECKBOARD[0]*CHECKBOARD[1], 3), np.float32)
objp[0,:,:2] = np.mgrid[0:CHECKBOARD[0], 0:CHECKBOARD[1]].T.reshape(-1, 2)
prev_img_shape = None
 
# read images
images = glob.glob("./camera_calibration/data/*.jpg")
for img_path in images:
    img = cv2.imread(img_path, 0)

    #find chessboard points
    ret, corners = cv2.findChessboardCorners(img, CHECKBOARD, cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_FAST_CHECK + cv2.CALIB_CB_NORMALIZE_IMAGE)
    #if you find
    if ret==True:
        object_points.append(objp)
        #make a accurate chessboard points
        corners_accurate = cv2.cornerSubPix(img, corners, (11,11),(-1,-1), criteria)
        image_points.append(corners_accurate)
 
h, w = img.shape[:2]
#calculate intrinsic matrix and distortion and translation and rotation in every frame
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(object_points, image_points, img.shape[::-1], None, None)
 
print("Camera matrix : \n")
print(mtx , "\n")
print(f"focal length : {mtx[0,0]}, \n")
print("distortion : \n")
print(dist)
