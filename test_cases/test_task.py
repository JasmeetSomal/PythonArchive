'''
Created on Feb 11, 2019

@author: singhjasmeet
'''
import unittest
from selenium import webdriver
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



class Test(unittest.TestCase):

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))#Path to chromedriver

    def setUp(self):
        self.driver = webdriver.Chrome(os.path.join(self.ROOT_DIR, 'chromedriver.exe'))
        pass

    def tearDown(self):
        self.driver.quit()
        pass

    def testName(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.element_to_be_clickable((By.ID, "button_1")).click())#business suite
        
        wait.until(EC.element_to_be_clickable((By.ID, "button_2")).click())#ip procurement
        
        wait.until(EC.element_to_be_clickable((By.ID, "button_3")).click())#project workbench
        
        self.driver.switch_to.frame(wait.until(EC.presence_of_element_located((By.ID, "page2"))))
        
        element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@id, button_4) and @value='Add']")))
        element.click()
        self.driver.switch_to.default_content()        
        pass
    
    def dropdown(self, dropdownid, dropdownvalue):
        select = Select(self.driver.find_element_by_id(dropdownid))
        select.select_by_visible_text(dropdownvalue)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()