cmake_minimum_required(VERSION 3.0)

option(WITH_TESTING "build all tests" ON)

set(PROJECT_NAME mytest)
set(PROJECT_ROOT ${CMAKE_CURRENT_SOURCE_DIR})
project(${PROJECT_NAME})

# set(CMAKE_CXX_FLAGS "-g -Wall")

if(WITH_TESTING)
    enable_testing()
    add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/tests)
endif ()