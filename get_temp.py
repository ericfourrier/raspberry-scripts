#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: efourrier

Purpose : Get temperature of your rpi cluster via python
"""

import subprocess
import re
import logging
import time

# logging.getLogger(type(self).__name__) if you have a lot of class
logger = logging.getLogger("temperature")  # 'root' Logger
console = logging.StreamHandler()  # logging to console
template_log = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
console.setFormatter(logging.Formatter(template_log))
logger.addHandler(console)  # prints to console.
logger.setLevel(logging.INFO)  # DEBUG or above


def get_temperature():
    """ Get the temperature in Celsius of your pi, execute it on the pi """
    cmd = "/opt/vc/bin/vcgencmd measure_temp"
    output = subprocess.check_output(cmd, shell=True)
    regex_number = re.compile("\d+\.\d+")
    return float(re.search(regex_number, output).group())


def log_temperature(interval=0.5):
    """ print Logs of temperature every 'interval' seconds """
    while True:
        temp = get_temperature()
        logger.info("Temperature of the pi in Celsius : {}".format(temp))
        time.sleep(interval)


if __name__ == "__main__":
    log_temperature()
