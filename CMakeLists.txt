cmake_minimum_required(VERSION 3.0)

option(WITH_TESTING "build all tests" ON)

set(PROJECT_NAME mytest)
set(PROJECT_ROOT ${CMAKE_CURRENT_SOURCE_DIR})
project(${PROJECT_NAME})

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/src)


add_target(common_objs
    HEADER_BASE_DIR ${RECALL_ROOT} ${RECALL_FRAMEWORK}
    SRC "${srcs}" ${framework_srcs}
    #DEPS
    #    brec_like_basis::recall_framework_all
    DEPS ${glb_deps}
    PROTOS
        ${proto_files}
)
target_compile_options(common_objs PUBLIC -mavx2 -ftree-vectorize)

add_executable(tool_test "${CMAKE_CURRENT_SOURCE_DIR}/main.cpp"
    DEPS
        -Wl,--whole-archive
        common_objs
        -Wl,--no-whole-archive
        )
# add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/src)
if(WITH_TESTING)
    enable_testing()
    add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/tests)
endif ()