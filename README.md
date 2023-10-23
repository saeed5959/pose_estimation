# pose estimation

## [1 - finding one object in 2D](/one_2d/)
For one base image we should find it in another image and draw a 2d pose of object

    1-find keypoints with FAST algorithm or SIFT
    2-calculating descriptor with ORB/BRIEF algorithm
    3-matching keypoints with FLANN algorithm
    4-calculate transformation matrix with RANSAC: R,T
    5-transform corner of object to second image

### base image
<img src="/one_2d/python_code/base.jpg" width="250" height="200" border="10" title="model">

### second image
<img src="/one_2d/python_code/all.jpg" width="250" height="200" border="10" title="model">

### matching
<img src="/one_2d/python_code/match.png" width="250" height="200" border="10" title="model">

### matching
<img src="/one_2d/python_code/pose.png" width="250" height="200" border="10" title="model">
    

## finding multiple object in 2D

## finding one object in 3D