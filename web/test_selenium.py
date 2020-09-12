import  selenium
from selenium import webdriver


def test_selenium():

    driver = webdriver.Chrome()
    # driver = webdriver.Chrome("/Users/zenghuan/software/chromedriver")
    driver.get("https://www.baidu.com/")