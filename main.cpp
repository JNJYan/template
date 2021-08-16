/*
 * @Author: JNJYan
 * @Date: 2021-07-01 21:01:55
 * @LastEditors: JNJYan
 * @LastEditTime: 2021-07-01 21:03:07
 * @Description: file content
 * @FilePath: /template/main.cpp
 */
#include <iostream>
#include "proto/test.pb.h"
#include "google/protobuf/arena.h"


int main() {
    google::protobuf::Arena arena;
    auto user_info = google::protobuf::Arena::CreateMessage<jnjyan::pb3::test::UserInfo>(&arena);
    *user_info->mutable_name() = "JNJYan";
    return 0;
}