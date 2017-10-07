# -*- coding: utf-8 -*-
"""

@author: Saurav Kanchan

"""
import sys
from cx_Freeze import setup, Executable
setup(
    name = "detector",
    version = "1.1",
    description = "Any Description you like",
    executables = [Executable("faces.py", base = "Win32GUI")])
