/*
 * @Author: your name
 * @Date: 2021-04-29 08:56:52
 * @LastEditTime: 2021-04-29 16:19:13
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /conan-learn/main_test.cpp
 */
#include <iostream>
#include <gtest/gtest.h>

int main(int argc, char **argv) {
    std::cout << "this is a unit test." << std::endl;
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
