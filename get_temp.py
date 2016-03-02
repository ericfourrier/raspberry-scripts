#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: efourrier

Purpose : Get temperature of your rpi cluster via python
"""

import subprocess
import re


def get_temperature():
    """ Get the temperature in Celsius of your pi, execute it on the pi """
    cmd = "/opt/vc/bin/vcgencmd measure_temp"
    output = subprocess.check_output(cmd, shell=True)
    regex_number = re.compile("\d+\.\d+")
    return float(re.search(regex_number, output).group())

if __name__ == "__main__":
    print("Temperature in Celsius :{}".format(get_temperature()))
