import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

import logging
import logging.config
import requests as req

# logging.config.fileConfig('src/logging.conf')
# logger = logging.getLogger(__name__)

class TernaSpider():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.set_page_load_timeout(10)

    def clickGraph(self):
        self.driver.get("https://www.terna.it/it/sistema-elettrico/transparency-report/actual-generation")
        self.driver.switch_to.frame(self.driver.find_element_by_id("iframeActualGen"))

        try:
            myElem = wait(self.driver, 10).until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, '/html/body/div/iframe')))
        except TimeoutError:
            time.sleep(2)
            
        got = False
        while not got:
            try:       
                btn = self.driver.find_element_by_class_name('vcMenuBtn')
                self.driver.execute_script('arguments[0].click();', btn)
                btn = self.driver.find_element_by_xpath("/html/body/div[9]/drop-down-list/ng-transclude/ng-repeat[1]/drop-down-list-item/ng-transclude/ng-switch/div")
                self.driver.execute_script('arguments[0].click();', btn)
                got=True
            except TimeoutException:
                print('Timeout')
                time.sleep(1)
            except NoSuchElementException:
                print('Try Again')
                time.sleep(2)

if __name__ == '__main__':
    spider = TernaSpider()
    spider.clickGraph()

