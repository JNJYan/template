cmake_minimum_required(VERSION 3.0)
project(mytest)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON) # for vscode c_cpp_pre.json

option(WITH_TESTING "build all tests" ON)

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/src)
include_directories(${CMAKE_BINARY_DIR})
include_directories(${CONAN_INCLUDE_DIRS})
add_target(common_objs
    SRC "${src}" # ${framework_srcs}
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
target_link_libraries(${PROJECT_NAME} ${CONAN_LIBS})

# add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/src)

# TEST
if(WITH_TESTING)
    enable_testing()
    add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/tests)
endif ()