#include <iostream>

#include <opencv2/core/core.hpp>
#include <opencv2/features2d/features2d.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/calib3d/calib3d.hpp>


using namespace std;


int main(int argc, char **argv){

    // read images
    cv::Mat img_1 = cv::imread("../1.png", 1);
    cv::Mat img_2 = cv::imread("../2.png", 1);

    cv::Ptr<cv::FeatureDetector> detector = cv::ORB::create();
    cv::Ptr<cv::DescriptorExtractor> descriptor = cv::ORB::create();
    cv::Ptr<cv::DescriptorMatcher> matcher = cv::DescriptorMatcher::create("BruteForce-Hamming");

    vector<cv::KeyPoint> keypoint_1, keypoint_2;
    cv::Mat descriptor_1, descriptor_2;
    vector<cv::DMatch> all_match;
    vector<cv::DMatch> good_match;

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


    cv::Mat out_all_point;
    cv::drawKeypoints(img_1, keypoint_1, out_all_point);
    cv::imwrite("../img1_keypoints.png", out_all_point);

    cv::Mat all_match_img;
    cv::Mat good_match_img;
    cv::drawMatches(img_1, keypoint_1, img_2, keypoint_2, all_match, all_match_img);
    cv::drawMatches(img_1, keypoint_1, img_2, keypoint_2, good_match, good_match_img);
    cv::imwrite("../all_match.png", all_match_img);
    cv::imwrite("../good_match.png", good_match_img);


    return 0;
}