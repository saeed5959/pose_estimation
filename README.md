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
    

## [2 - finding multiple object in 2D](/multiple_2d/)
For one base image we should find all objects in another image and draw a 2d pose of object

    1-find keypoints with FAST algorithm or SIFT
    2-calculating descriptor with ORB/BRIEF algorithm
    3-matching keypoints with FLANN algorithm
    4-calculate transformation matrix(projective) with RANSAC: R,T
    5-transform corner of object to second image
    6-mask that area and repeat 1-5

### base image
<img src="/multiple_2d/1.png" width="250" height="200" border="10" title="model">

### second image
<img src="/multiple_2d/2.png" width="250" height="200" border="10" title="model">

### matching 1
<img src="/multiple_2d/match_0.png" width="250" height="200" border="10" title="model">

### matching 2 after mask
<img src="/multiple_2d/match_1.png" width="250" height="200" border="10" title="model">
 
### pose
<img src="/multiple_2d/pose.png" width="250" height="200" border="10" title="model">
 

##  [3 - finding 3d object](/pose3d/)
For one base 3d image we should find 3d pose of object in another image and draw a 3d pose of object

    1-find keypoints with FAST algorithm or SIFT
    2-calculating descriptor with ORB/BRIEF algorithm
    3-matching keypoints with FLANN algorithm
    4-calculate transformation matrix from 3d to 2d with PnP with RANSAC: R,T
    5-transform corner of object to second image
    6-use Linear Kalman Filter for bad poses rejection

### base image
<img src="/pose3d/Data/1.JPG" width="250" height="200" border="10" title="model">

### second image
<img src="/pose3d/Data/2.png" width="250" height="200" border="10" title="model">

### 3d pose
<img src="/pose3d/Data/pose.png" width="250" height="200" border="10" title="model">
