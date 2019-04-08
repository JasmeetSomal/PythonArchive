'''
Created on Aug 30, 2018

@author: singhjasmeet
'''
from test_cases import *
from elements_repo import archive_repo
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import os


class Search(unittest.TestCase):
            
    def setUp(self):
        self.driver = webdriver.startDriver()
        self.driver.implicitly_wait(40)
        self.by = webdriver.BY.meet(self, self.driver)
        self.url = archive_repo.home_url
        self.driver.get(self.url)
        self.by.BY_XPATH(archive_repo.sign_in_btn).click()
        archive_common.login(self.driver,
                               archive_repo.email, archive_repo.password)
        
    def test_trail(self):
        time.sleep(5)
        before = os.listdir(webdriver.download_dir)
        self.by.BY_ID(archive_repo.home_search).send_keys("Goody Two Shoes alyson")
        self.by.BY_XPATH(archive_repo.home_search_btn).click()
        self.by.BY_XPATH(archive_repo.book_new_link).click()
        iframe_element = self.by.BY_XPATH(archive_repo.iframe_book)
        self.driver.switch_to.frame(iframe_element)
        self.by.BY_XPATH(archive_repo.turn_page).click()
        time.sleep(3)
        self.by.BY_XPATH(archive_repo.turn_again).click()
        self.driver.switch_to.default_content()
        self.by.BY_XPATH(archive_repo.search_inside).click()
        self.by.BY_CSS(archive_repo.flip_right_btn).click()
        self.by.BY_CSS(archive_repo.flip_right_btn).click()
        self.by.BY_CSS(archive_repo.pdf_epub_link).click()
        self.by.BY_LINK(archive_repo.pdf_format_link).click()
        time.sleep(20)
        after = os.listdir(webdriver.download_dir)
        change = set(after) - set(before)
        if len(change)==1:
            file_name = change.pop()
            os.chdir(webdriver.download_dir)
            bool_var = os.path.isfile(file_name)
            self.assertTrue(bool_var, "File downloaded successfully")
            os.remove(file_name)
        
        else:
            self.assertTrue(False, "Book could not be downloaded")
        print("Test Passed")
    
    
    def tearDown(self):
        time.sleep(5)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
