import pytest
import allure
from selenium import webdriver
# from base.base_analyze import analyze_data
# from base.base_driver import init_driver
# from base.base_page import Page


@allure.title("登录")
def test_login():
    driver = webdriver.Chrome()
    driver.get("http://yf.a99.live/")
    driver.find_element_by_id("username").send_keys("18055779893")
    driver.find_element_by_id("pwd").send_keys("123456789")
    driver.find_element_by_xpath("/html/body/div/form/input[3]").click()


@allure.title("我的桌面")
def test_home():
    assert True


@allure.title("审批管理")
def test_approval_management():
    assert True


@allure.title("招投标管理")
def test_management_of_bidding_and_tendering():
    assert False


@allure.title("合同管理")
def test_contract_management():
    assert True


@allure.title("客户管理2")
def test_customer_management():
    assert True