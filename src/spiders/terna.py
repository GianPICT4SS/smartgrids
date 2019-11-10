import time
from selenium import webdriver
import logging
import logging.config

# logging.config.fileConfig('src/logging.conf')
# logger = logging.getLogger(__name__)

class TernaSpider():

    def setUp(self):
        driver= webdriver.Chrome()
        driver.set_page_load_timeout(10)
        connection = driver.get("https://www.terna.it/it/sistema-elettrico/transparency-report/actual-generation")
        time.sleep(10)
        driver.maximize_window()
        return connection


    def setElemets(self, connection):
        _input=connection.find_elements_by_xpath("/html/body/div[2]/ui-view/div/div[1]/div/div/div/div/exploration-container/exploration-container-legacy/div/div/exploration-host/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[28]/transform/div/visual-container-header-modern/div/div[1]/div/visual-container-options-menu/visual-header-item-container/div/button/i")
        time.sleep(4)
        print("Test completato")



def main():
    spider = TernaSpider()
    url=spider.setUp()
    spider.setElemets(url)


if __name__ == '__main__':
    main()


