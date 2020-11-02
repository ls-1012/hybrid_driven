#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# File:         Capture.py
# Author:       ls
# Date:         2020/10/23 16:43
#-------------------------------------------------------------------------------
from PIL import ImageGrab
from Util.Dir import make_time_dir
from Util.DateAndTime import *
import os
import traceback

def capture():
    try:
        im = ImageGrab.grab()
        png_path=os.path.join(make_time_dir(),TimeUtil().get_chinesedatetime()+".png")
        # print(png_path)
        # im.show()
        im.save(png_path)
    except Exception:
        traceback.print_exc()


capture()