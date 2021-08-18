'''
Author: JNJYan
Date: 2021-06-30 09:34:49
LastEditors: JNJYan
LastEditTime: 2021-07-01 18:04:44
Description: file content
FilePath: /template/conanfile.py
'''

from conans import ConanFile, CMake, tools
import os

version = None
in_jenkins = False

if "TAG" in os.environ:
    print("use tag %s".format(os.environ['TAG']))
    version = os.environ['TAG']

class TestConan(ConanFile):
    name = "Test"
    version = "0.0.1"
    license = "MIT"
    settings = "cppstd", "os", "compiler", "build_type", "arch"
    default_settings = "cppstd=17", "build_type=Debug"
    options = {"shared": [True, False], "testing": [True, False]}
    default_options = "shared=False", "testing=False"
    generators = "cmake"
    exports_sources = "*"
    def requirements(self):
        self.requires("gtest/1.10.0")
        # self.requires("yaml-cpp/0.6.3")
        # self.requires("benchmark/1.5.3")
        # self.requires("rapidjson/1.1.0")
        # self.requires("glog/0.5.0")
        self.requires("protobuf/3.17.1")

    def _configure_cmake(self):
        cmake = CMake(self)
        if self.options.testing:
            print("testing is true")
            cmake.definitions["WITH_TESTING"] = "ON"
        else:
            cmake.definitions["WiTH_TESTING"] = "OFF"
        cmake.configure()
        return cmake
    
    def build(self):
        cmake = self._configure_cmake()
        cmake.build()
    
    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        tools.collect_libs(self)
    

