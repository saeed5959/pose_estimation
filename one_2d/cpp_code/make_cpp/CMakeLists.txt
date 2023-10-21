cmake_minimum_required(VERSION 3.0)

project(my_project)

find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})


add_executable(run ../main.cpp)
target_link_libraries(run ${OpenCV_LIBS})