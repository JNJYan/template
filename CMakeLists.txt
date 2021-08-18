cmake_minimum_required(VERSION 3.0)
project(mytest)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON) # for vscode c_cpp_pre.json
set(CMAKE_BUILD_TYPE "Debug")
set(CMAKE_CXX_FLAGS_DEBUG "$ENV{CXXFLAGS} -O0 -Wall -g -ggdb")
set(CMAKE_CXX_FLAGS_RELEASE "ENV{CXXFLAGS} -O3 -Wall")

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

option(WITH_TESTING "build all tests" OFF)

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/src)
include_directories(${CMAKE_BINARY_DIR})
include_directories(${CONAN_INCLUDE_DIRS})
include_directories(${CMAKE_CURRENT_BINARY_DIR})

add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/proto)

add_executable(tool_test "${CMAKE_CURRENT_SOURCE_DIR}/main.cpp")
target_link_libraries(tool_test ${CONAN_LIBS} proto)

# TEST
if(WITH_TESTING)
    enable_testing()
    add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/tests)
endif ()