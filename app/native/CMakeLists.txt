cmake_minimum_required(VERSION 3.16)
project(addlib C)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)

add_library(add SHARED
    src/add.c
)

target_include_directories(add
    PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include
)

set_target_properties(add PROPERTIES
    OUTPUT_NAME "add"
)