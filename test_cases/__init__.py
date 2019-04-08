import unittest
from elements_repo import archive_repo
from  archive_globals import webdriver,archive_common
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time
import archive_globals

def get_url(driver):
    time.sleep(3)
    return driver.current_url
#Clear than set text. Only for ID locators
def enter(self, Id, value):
    self.by.BY_ID(Id).clear()
    self.by.BY_ID(Id).send_keys(value)
    