from conans import ConanFile, CMake
import os

class EASTLConan(ConanFile):
  name = "EASTL"
  version = "3.05.04"
  description = "EASTL stands for Electronic Arts Standard Template Library. It is an extensive and robust implementation that has an emphasis on high performance."
  license="Modified BSD License (3-Clause BSD license)"
  settings = "os", "compiler", "build_type", "arch"
  url = "https://github.com/pjohalloran/conan-eastl"
  options = {"build_type": ["Release", "Debug", "RelWithDebInfo", "MinSizeRel"]}
  default_options = "build_type=MinSizeRel",

  def source(self):
    self.run("git clone https://github.com/electronicarts/EASTL")
    os.chdir("EASTL")
    self.run("git checkout %s" % self.version)

  def build(self):
    os.makedirs("EASTL/build")
    os.chdir("EASTL/build")
    self.run("cmake ..")
    self.run("cmake --build . --config %s" % self.options.build_type)

  def package(self):
    self.copy("*.h", src="EASTL/test/packages/EABase/include/Common/EABase", dst="include/EABase", keep_path=True)
    self.copy("*.h", src="EASTL/include", dst="include", keep_path=True)
    self.copy("*.lib", dst="lib", keep_path=False)
    self.copy("*.a", dst="lib", keep_path=False)

  def package_info(self):
    self.cpp_info.libs = [ self.name ]
