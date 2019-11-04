import unittest

import pytest
import allure
from selenium import webdriver
from page.pege_in import PageIn


class TestAdmin(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://yf.a99.live/")
        self.driver.maximize_window()
        self.login_page = PageIn().login_page(self.driver)
        self.login_page.login("18055779893", "123456789")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    @allure.title("我的桌面-修改密码")
    def test_change_password(self):
        self.login_page.change_password("123456789", "123456789", "123456789")

    @allure.title("审批管理")
    def test_approval_management(self):
        self.login_page.material_purchase_application()

    @allure.title("招投标管理")
    def test_management_of_bidding_and_tendering(self):
        self.login_page.inquire("111")

    @allure.title("合同管理")
    def test_contract_management(self):
        self.login_page.click_on_the_query("1111")

    @allure.title("客户管理")
    def test_customer_management(self):
        self.login_page.register_customer_information()

    @allure.title("人员需求")
    def test_personnel_requirement(self):
        self.login_page.examine()

    @allure.title("调度派遣管理")
    def test_dispatch_management(self):
        assert True

    @allure.title("员工档案")
    def test_staff_record(self):
        assert True

    @allure.title("资质管理")
    def test_qualification_management(self):
        assert True
