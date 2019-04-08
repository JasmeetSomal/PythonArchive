
from selenium import webdriver
import sys
from pathlib import Path

home = str(Path.home())
download_dir = home


def startDriver():
    browser = 'Firefox'#sys.argv[2]
    if 'BrowserStack' in browser:
        print ('Argument List:', str(sys.argv))
        user = sys.argv[3]
        pswd = sys.argv[4]#os.environ["BROWSERSTACK_PASSWORD"]#os.environ.get('BROWSERSTACK_PASSWORD', 'VhnyxJGRzp9X6pfzqdk')
        print(user+"=========="+pswd)
        driver = webdriver.Remote(
        command_executor="http://" + user + ":" + pswd + "@hub.browserstack.com:80/wd/hub",
        desired_capabilities={ 'browser': 'Firefox', 'browser_version': '46.0',
                        'os': 'Windows', 'os_version': '7',
                        'resolution': '1024x768'})
        return driver
    options = webdriver.ChromeOptions()
    profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}], # Disable Chrome's PDF Viewer
               "download.default_directory": download_dir , "download.extensions_to_open": "applications/pdf"}
    options.add_experimental_option("prefs", profile)
    driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)  # Optional argument, if not specified will search path.
    return driver
    
class  BY:
    
    
    def meet(self, driver):
        self.BY_ID = driver.find_element_by_id
        self.BYS_ID = driver.find_elements_by_id
        self.BY_XPATH = driver.find_element_by_xpath
        self.BYS_XPATH = driver.find_elements_by_xpath
        self.BY_LINK = driver.find_element_by_link_text
        self.BY_CLASS = driver.find_element_by_class_name
        self.BY_CSS = driver.find_element_by_css_selector
        self.BYS_CSS = driver.find_elements_by_css_selector
        self.BY_NAME = driver.find_element_by_name
        self.BY_PARTIAL_LINK = driver.find_element_by_partial_link_text
        self.BY_TAG = driver.find_element_by_tag_name
        self.BYS_TAG = driver.find_elements_by_tag_name
        return self