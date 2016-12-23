from conans import ConanFile, CMake

class EASTLConan(ConanFile):
  name = "EASTL"
  version = "3.05.00"
  description = "EASTL stands for Electronic Arts Standard Template Library. It is an extensive and robust implementation that has an emphasis on high performance."
  license="Modified BSD License (3-Clause BSD license)"
  settings = "os", "compiler", "build_type", "arch"
  url = "https://github.com/pjohalloran/conan-eastl"
  options = {"build_type": ["Release", "Debug", "RelWithDebInfo", "MinSizeRel"]}
  default_options = "build_type=MinSizeRel",

  def source(self):
    self.run("git clone https://github.com/electronicarts/EASTL")
    os.chdir("EASTL")
    self.run("git checkout 3.05.00")

  def build(self):
    os.makedirs("build")
    os.chdir("build")
    self.run("cmake ..")
    self.run("cmake --build . --config %s" % self.options.build_type)

  def package(self):
    self.copy("build/*.lib", dst="lib", keep_path=False)
    self.copy("build/*.a", dst="lib", keep_path=False)
