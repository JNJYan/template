cmake_minimum_required(VERSION 3.0)

set(TEST_DIR ${CMAKE_CURRENT_SOURCE_DIR}/)
file(GLOB_RECURSE srcs ${TEST_DIR}/*.cpp)
message("this is a test")

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

# add_executable(unittest main_test.cpp)
add_executable(unittest ${srcs})
target_link_libraries(unittest ${CONAN_LIBS})

target_include_directories(unittest PUBLIC ${PROJECT_ROOT}/src)
target_include_directories(unittest PUBLIC ${TEST_DIR})
target_include_directories(unittest PUBLIC ${CMAKE_BINARY_DIR})