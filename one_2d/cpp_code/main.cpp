#include <iostream>
using namespace std;

#include <opencv2/core/core.hpp>
#include <opencv2/features2d/features2d.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/calib3d/calib3d.hpp>
#include <opencv2/imgproc.hpp>


int main(int argc, char **argv){

    cv::Mat img_1 = cv::imread("../base.jpg");
    cv::Mat img_2 = cv::imread("../all.jpg");

    cv::Ptr<cv::FeatureDetector> detector = cv::ORB::create();
    cv::Ptr<cv::DescriptorExtractor> descriptor = cv::ORB::create();
    cv::Ptr<cv::DescriptorMatcher> matcher = cv::DescriptorMatcher::create("BruteForce-Hamming");

    vector<cv::KeyPoint> keypoint_1, keypoint_2;
    cv::Mat descriptor_1, descriptor_2;
    vector<cv::DMatch> all_match, good_match;

    // find keypoints
    detector->detect(img_1, keypoint_1);
    detector->detect(img_2, keypoint_2);

    // calculate descriptors
    descriptor->compute(img_1, keypoint_1, descriptor_1);
    descriptor->compute(img_2, keypoint_2, descriptor_2);

    // calculate matching value, similarity
    matcher->match(descriptor_1, descriptor_2, all_match);

    // the minimum match value
    auto min_max = minmax_element(all_match.begin(), all_match.end(), 
    [](const cv::DMatch &m1, const cv::DMatch &m2){return m1.distance < m2.distance;});
    double min_dist = min_max.first->distance;

    // remove bad match points that have high distance 
    for(int i=0; i<all_match.size(); i++){
        if (all_match[i].distance < max(2*min_dist, 30.0)){
            good_match.push_back(all_match[i]);
        }
    }

    vector<cv::Point2f> keypoint_good_1, keypoint_good_2;

    if (good_match.size() > 10){
        for (int i=0; i<good_match.size(); i++){
            keypoint_good_1.push_back( keypoint_1[good_match[i].queryIdx].pt );
            keypoint_good_2.push_back( keypoint_2[good_match[i].trainIdx].pt );
        }
    }


    cv::Mat H = cv::findHomography(keypoint_good_1, keypoint_good_2, cv::RANSAC);
    // define corner points
    vector<cv::Point2f> corner_1(4), corner_2(4);
    corner_1[0] = cv::Point2f(0,0);
    corner_1[1] = cv::Point2f((float)img_1.cols, 0);
    corner_1[2] = cv::Point2f(0, (float)img_1.rows);
    corner_1[3] = cv::Point2f((float)img_1.cols, (float)img_1.rows);

    cv::perspectiveTransform(corner_1, corner_2, H);

    cv::Mat good_match_img, img_object = img_2;
    cv::drawMatches(img_1, keypoint_1, img_2, keypoint_2, good_match, good_match_img);
    cv::imwrite("../good_match.png", good_match_img);

    // draw lines between corners
    cv::line( img_object, corner_2[0], corner_2[1], cv::Scalar(0, 255, 0), 4);
    cv::line( img_object, corner_2[0], corner_2[2], cv::Scalar( 0, 255, 0), 4);
    cv::line( img_object, corner_2[2], corner_2[3], cv::Scalar( 0, 255, 0), 4);
    cv::line( img_object, corner_2[1], corner_2[3], cv::Scalar( 0, 255, 0), 4);

    cv::imwrite("../pose.png", img_object);
    

    return 0;
}