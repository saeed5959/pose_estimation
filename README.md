# computer vision


## [1 - feature matching](/feature_matching/)

    1-finding keypoints with ORB/FAST algorithm 
    2-calculating descriptor with ORB/BRIEF algorithm
    3-matching keypoints with FLANN algorithm

### left image
<img src="/feature_matching/python_code/1.png" width="250" height="200" border="10" title="model">

### right image
<img src="/feature_matching/python_code/2.png" width="250" height="200" border="10" title="model">

### matching
<img src="/feature_matching/python_code/out.png" width="500" height="200" border="10" title="model">


## [2 - camera calibration](/camera_calibration/)

    1-consider (6,9) corner points of chessboard with 3d points
    2-find corners points of chessboard in image
    3-calculate intrinsic matrix : focal length, ox, oy
    4-calculate distortion parameters : (k1, k2, p1, p2, k3)


### chessboard
<img src="/camera_calibration/data/image_2.jpg" width="350" height="200" border="10" title="model">

### calibration result
<img src="/camera_calibration/data/result.png" width="350" height="200" border="10" title="model">
