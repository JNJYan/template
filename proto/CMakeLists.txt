find_package(Protobuf REQUIRED)
FILE(GLOB protofiles test.proto)
message(STATUS ${protofiles})
protobuf_generate_cpp(PROTO_SRCS PROTO_HDRS ${protofiles})
message(STATUS ${PROTO_SRCS})
add_library(proto STATIC ${PROTO_SRCS} ${PROTO_HDRS})
target_link_libraries(proto protobuf)
target_include_directories(proto PUBLIC ${CMAKE_CURRENT_BINARY_DIR})