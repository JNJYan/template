'''
Author: your name
Date: 2021-04-29 10:10:09
LastEditTime: 2021-04-29 14:45:14
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /conan-learn/conanfile.py
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
    default_settings = "cppstd=17"
    options = {"shared": [True, False], "testing": [True, False]}
    default_options = "shared=False", "testing=True"
    generators = "cmake"
    exports_sources = "*"

    def requirements(self):
        self.requires("gtest/1.8.1")

    def _configure_cmake(self):
        print("testing is false")
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
    

