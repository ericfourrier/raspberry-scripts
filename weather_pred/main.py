#!/usr/bin/env python
# -*- coding: utf-8 -*-u

"""
Purpose : Get weather predition using https://developer.forecast.io/ and
the pip install python-forecastio python wrapper

Requirements
------------
* pip install python-forecastio

"""


import os
import forecastio
import datetime
import time
import RPi.GPIO as GPIO
import logging
from pprint import pprint

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("predict-weather")


api_key = os.environ.get("FORECAST_API_KEY")
paris_lat = 48.8534100
paris_lng = 2.3488000
API_RATE_LIMIT = 1000  # 1000 calls a day

# Be careful with timezone here
# current_time = datetime.datetime.now()
# print(current_time)
#
# forecast = forecastio.load_forecast(api_key, paris_lat, paris_lng, time=current_time)
#
# pred_now = forecast.currently().d


def get_weather_now(api_key=api_key, lat=paris_lat, long=paris_lng, verbose=True):
    """ Returns the weather now for a certain latitude and longitude """
    current_time = datetime.datetime.now()
    forecast = forecastio.load_forecast(
        api_key, paris_lat, paris_lng, time=current_time)
    nb_remaining_calls = API_RATE_LIMIT - int(forecast.response.headers['x-forecast-api-calls'])
    logger.debug("Pulling data from  the api forecast.io, remaining calls : {}".format(
        nb_remaining_calls))
    pred = forecast.currently().d
    if verbose:
        pprint(pred)
    return pred

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

while True:
    pred = get_weather_now()
    # light up red light if it is raining
    if pred['precipProbability'] > 90:
        GPIO.output(18, True)
    else:
        GPIO.output(18, False)
    time.sleep(60 * 30)
