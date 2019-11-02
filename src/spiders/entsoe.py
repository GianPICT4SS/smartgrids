import os
import time
import requests as req
from selenium import webdriver

class EntsoeSpider():
    def __init__(self, log):
        # Class init
        self.driver = webdriver.Firefox(profile)
        self.log = log
