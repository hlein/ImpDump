#!/usr/bin/python

import glob
import os

from distutils.core import setup

PACKAGE_NAME = "ImpDump"

setup(name = PACKAGE_NAME,
      version = "0.0.1",
      description = "Parser / Decryptor for Impacket esentutl.py Output",
      url = "https://github.com/HarmJ0y/ImpDump",
      author = "HarmJ0y",
      author_email = "will@harmj0y.net",
      maintainer = "HarmJ0y",
      maintainer_email = "will@harmj0y.net",
      license = "GPLv2",
      long_description = 'Parser / Decryptor for Impacket esentutl.py Output',
      platforms = ["Unix","Windows"],
      packages = ['framework', 'framework.win32'],
      scripts = ['impdump_extract.sh', 'impdump.py'],
      data_files = [(os.path.join('share', 'doc', PACKAGE_NAME), ['README.md', 'LICENSE'])],
      requires=['impacket (>=0.9.13)'],
      )
