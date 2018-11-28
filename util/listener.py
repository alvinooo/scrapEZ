from sys import maxsize

from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver, AbstractEventListener
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchWindowException

import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from constants import PROJECT_BASE_DIRECTORY

class ElementListener(AbstractEventListener):
    def after_click(self, element, driver):
        print(f'<element>\t{element}\t</element>')

    def after_navigate_to(self, url, driver):
    	print(f'url: {url}')

class BrowserState:
	def __call__(self, driver):
		try:
			driver.title
			return False
		except NoSuchWindowException:
			return True

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    print('browser opened')
    driver = webdriver.Chrome(f'{PROJECT_BASE_DIRECTORY}/chromedriver', chrome_options=options)
    event_driver = EventFiringWebDriver(driver, ElementListener())
    event_driver.get('https://www.google.com')

    # Wait until user closes browser
    wait = WebDriverWait(event_driver, maxsize)
    wait.until(BrowserState())
    print('browser closed')
    driver.quit()