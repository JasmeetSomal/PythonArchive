'''
Created on Aug 30, 2018

@author: singhjasmeet
'''
import time
import random
from selenium import webdriver

import poplib
from elements_repo import archive_repo


verify_message = list()
def login(driver, username, password):
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("submit").click()
 
def verify(condition, message):
    global verify_message
    if(condition is False):
        print("Verification failed due to: "+message)
        verify_message += [message]
    return verify_message

def verify_all():
    global verify_message
    if verify_message:
        message = "Following Verifications are failed in testcase"
        i=1;
        for msg in verify_message:
            message += " :  (" + str(i) +") " + msg
            i = i+1
        verify_message = list()
        assert 0, message
    return verify_message      


def uniqueNo(digit_count = 3):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890&@*!#`~-/\[]<>:?|^"
    if (digit_count == 1):
        return random.choice(chars)
    else:
        return  random.choice(chars) + uniqueNo(digit_count-1)
    