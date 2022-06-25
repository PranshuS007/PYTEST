import time
import pytest
from selenium.webdriver.chrome import webdriver

driver = None
from selenium import webdriver


@pytest.fixture
def start():
    print("Start Browser")
    global driver
    driver = webdriver.Chrome("D:\chromedriver.exe")
    driver.maximize_window()


@pytest.mark.skip
def test_1(start):
    driver.get("https://www.jetbrains.com/pycharm/")
    print('test 1 passed')


@pytest.mark.parametrize('userName, password',
                         [
                             ('usingxyz', "qwertyUIOP12@"),

                         ]
                         )
def test_2(start, userName, password):
    driver.get("https://demoqa.com/login")

    driver.find_element_by_xpath("//input[@id='userName']").send_keys(userName)
    time.sleep(2)
    driver.find_element_by_xpath("//input[@id='password']").send_keys(password)
    time.sleep(2)
    driver.find_element_by_xpath("//button[@id='login']").click()


