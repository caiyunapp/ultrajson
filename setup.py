
try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension
import distutils.sysconfig
import os.path
import re
import shutil
import sys

from setuptools.command.build_ext import build_ext

CLASSIFIERS = filter(None, map(str.strip,
                               """
Development Status :: 5 - Production/Stable
Intended Audience :: Developers
License :: OSI Approved :: BSD License
Programming Language :: C
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
""".splitlines()))

try:
    shutil.rmtree("./build")
except(OSError):
    pass

module1 = Extension('nujson',
                    sources=['./python/ujson.c',
                             './python/objToJSON.c',
                             './python/JSONtoObj.c',
                             './lib/ultrajsonenc.c',
                             './lib/ultrajsondec.c'],
                    include_dirs=['./python', './lib'],
                    extra_compile_args=['-D_GNU_SOURCE'])


def get_version():
    filename = os.path.join(os.path.dirname(__file__), './python/version.h')
    file = None
    try:
        file = open(filename)
        header = file.read()
    finally:
        if file:
            file.close()
    m = re.search(r'#define\s+NUJSON_VERSION\s+"(\d+\.\d+(?:\.\d+)?)"', header)
    assert m, "version.h must contain NUJSON_VERSION macro"
    return m.group(1)


f = open('README.md')
try:
    README = f.read()
finally:
    f.close()


class CustomBuildExtCommand(build_ext):
    """build_ext command for use when numpy headers are needed."""

    def run(self):

        # Import numpy here, only when headers are needed
        import numpy

        # Add numpy headers to include_dirs
        self.include_dirs.append(numpy.get_include())

        # Call original build_ext command
        build_ext.run(self)


setup(name='nujson',
      version=get_version(),
      description="Ultra fast JSON encoder and decoder for Python with NumPy support",
      long_description=README,
      long_description_content_type="text/markdown",
      keywords='numpy ujson json python3',
      project_urls={
          #   'Documentation': '',
          'Source': 'http://github.com/caiyunapp/ultrajson',
      },
      cmdclass={'build_ext': CustomBuildExtCommand},
      install_requires=['numpy>=1.16.4'],
      ext_modules=[module1],
      author="caiyunapp",
      author_email="admin@caiyunapp.com",
      download_url="http://github.com/caiyunapp/ultrajson",
      license="BSD License",
      platforms=['any'],
      url="https://caiyunapp.com",
      classifiers=CLASSIFIERS,
      )
