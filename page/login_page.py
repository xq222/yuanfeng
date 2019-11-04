import allure
from selenium.webdriver.common.by import By
import page
from base.base_action import BaseAction
import time


class LoginPage(BaseAction):


    @allure.step(title="登录")
    def login(self, username, password):
        self.input(page.username_edit_text, username)
        self.input(page.password_edit_text, password)
        self.click(page.add_button)

    @allure.step(title="我的页面-修改密码")
    def change_password(self, old_password, new_password, confirm_password):
        self.click(page.click_change_password)
        time.sleep(2)
        self.base_switch_frame(self.find_element(page.switch_frame_password))
        time.sleep(2)
        self.input(page.old_password, old_password)
        self.input(page.new_password, new_password)
        self.input(page.confirm_password, confirm_password)
        self.click(page.preserve)
        self.base_switch_to_default_content()

    @allure.step(title="客户管理-登记客户信息")
    def register_customer_information(self):
        self.click(page.customer_management)
        self.click(page.the_customer_information)
        time.sleep(2)
        self.base_switch_frame(self.find_element(page.switch_frame_password))
        self.click(page.the_customer_registration)
        self.base_switch_to_default_content()

    @allure.step(title="审批管理-发起物资采购申请")
    def material_purchase_application(self):
        self.click(page.test_approval_management)
        self.click(page.the_examination)
        time.sleep(2)
        self.base_switch_frame(self.find_element(page.switch_frame_password))
        self.click(page.click_on_the_application)
        self.base_switch_to_default_content()

    @allure.step(title="招投标管理-业务机会-查询")
    def inquire(self, text):
        self.click(page.management_of_bidding_and_tendering)
        time.sleep(3)
        self.click(page.business_chance)
        time.sleep(3)
        self.base_switch_frame(self.find_element(page.switch_frame_password))
        self.input(page.keyword, text)
        self.click(page.select_project_manager)
        self.base_switch_to_default_content()
        # self.base_switch_frame(page.switch_frame_id)
        # self.click(page.check)
        # self.click(page.botton)
        # self.click(page.submit)

    @allure.step(title="人员需求-查看操作")
    def examine(self):
        self.click(page.personnel_requirement)
        self.click(page.personnel_requirement1)
        time.sleep(2)
        self.base_switch_frame(self.find_element(page.switch_frame_operation))
        self.click(page.check_the_operation)

    @allure.step(title="合同管理-项目合同-根据合同名称点击查询")
    def click_on_the_query(self, text):
        self.click(page.contract_management)
        self.click(page.project_contract)
        time.sleep(2)
        self.base_switch_frame(self.find_element(page.switch_frame_password))
        self.input(page.please_enter, text)
        self.click(page.click_inquire)
        self.base_switch_to_default_content()






