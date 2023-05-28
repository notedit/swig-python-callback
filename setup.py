

from setuptools import setup, Extension
import os
import platform

extra_link_args = []
libraries = []
library_dirs = []
extra_compile_args = []


extra_compile_args = ['-std=c++11']

example_module = Extension('_example',
                           sources=[
                               'example_wrap.cxx',
                               'example.cxx'
                           ],
                           include_dirs=['include', '.'],
                           extra_link_args=extra_link_args,
                           libraries=libraries,
                           library_dirs=library_dirs,
                           extra_compile_args=extra_compile_args
                           )

setup(name='example',
      version='1.0.0',
      author="test",
      description="example",
      ext_modules=[example_module],
      py_modules=["example"],
      package_dir={'': '.'},
      classifiers=[
           "Programming Language :: Python :: 3",
           "Development Status :: 4 - Beta",
           "License :: OSI Approved :: MIT License",
           "Operating System :: MacOS",
          "Operating System :: Microsoft :: Windows",
          "Topic :: Scientific/Engineering",
          "Topic :: Software Development :: Libraries",
          "Topic :: Multimedia :: Video",
          "Topic :: Multimedia :: Video :: Capture",
          "Programming Language :: C++",
      ],
      python_requires='>=3.6',
      )
