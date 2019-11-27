import pytest
import allure
from selenium import webdriver
from page.pege_in import PageIn
import unittest


class TestAdmin():

    # @classmethod
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://yf.a99.live/")
        self.driver.maximize_window()
        self.login_page = PageIn().login_page(self.driver)
        self.login_page.login("18055779893", "123456789")

    # @classmethod
    def teardown(self):
        self.driver.quit()

    @pytest.mark.run(order=1)
    @allure.title("我的桌面-修改密码")
    def test_change_password(self):
        print("1")
        self.login_page.change_password("123456789", "123456789", "123456789")


    @pytest.mark.run(order=2)
    @allure.title("审批管理")
    def test_approval_management(self):
        print("2")
        self.login_page.material_purchase_application()


    @pytest.mark.run(order=3)
    @allure.title("招投标管理")
    def test_management_of_bidding_and_tendering(self):
        print("3")
        self.login_page.inquire("111")



    @allure.title("合同管理")
    def test_contract_management(self):
        print("4")
        self.login_page.click_on_the_query("1111")



    @allure.title("客户管理")
    def test_customer_management(self):
        self.login_page.register_customer_information()

    @allure.title("人员需求")
    def test_personnel_requirement(self):
        self.login_page.examine()

    @allure.title("调度派遣管理")
    def test_dispatch_management(self):
        print("7")
        assert True

    @allure.title("员工档案")
    def test_staff_record(self):
        assert True

    @allure.title("资质管理")
    def test_qualification_management(self):
        assert True

    @allure.title("假期管理")
    def test_the_holiday_management(self):
        self.login_page.leave()

    @allure.title("考勤管理")
    def test_attendance_management(self):
        self.login_page.group_of_check_on_work_attendance()
        self.login_page.classes()
        self.login_page.sign_in_to_query()
        self.login_page.statistics()
        self.login_page.monthly_statistics()

    @allure.title("人员进出")
    def test_personnel_in_and_out(self):
        self.login_page.apply_for()
        self.login_page.staff_regularization()
        self.login_page.personnel_transfer()
        self.login_page.dimission_management()

    @allure.title("培训管理")
    def test_training_management(self):
        self.login_page.training_program()
        self.login_page.internal_training()
        self.login_page.external_training()
        self.login_page.training_record_statistics()

    @allure.title("考核管理")
    def test_appraisal_management(self):
        self.login_page.appraisal_managements()
        self.login_page.coefficient_setting()

    @allure.title("社保管理")
    def test_management_of_social_security(self):
        self.login_page.employees_social_security()
        self.login_page.share_the_summary()
        self.login_page.cardinality()

    @allure.title("薪资管理")
    def test_salary_management(self):
        self.login_page.monthly_salary_management()
        self.login_page.attendance_salary_accounting()
        self.login_page.actual_salary_accounting()
        self.login_page.wage_statistics()
        self.login_page.deductions_rules()
        self.login_page.the_amount_of_tax_payable_is_set()

    @allure.title("项目管理")
    def test_project_management(self):
        self.login_page.project_startup()
        self.login_page.project_monitoring()
        self.login_page.report_form_statistics()

    @allure.title("资料库管理")
    def test_database_management(self):
        self.login_page.data_bank()
        self.login_page.norm()
        self.login_page.template()
        self.login_page.system_document()

    @allure.title("投标保证金管理")
    def test_bid_security_management(self):
        self.login_page.pay_deposit()

    @allure.title("合同履约金管理")
    def test_contract_performance_fund_management(self):
        self.login_page.performance_management_tax_payment()

    @allure.title("合同质保金管理")
    def test_contract_management_quality_retention_money(self):
        self.login_page.contract_quality_retention_money_payment_and_recovery()

    @allure.title("监理费管理")
    def test_supervision_fee_management(self):
        self.login_page.supervision_fee_settlement_application()
        self.login_page.deductions_settlement()
        self.login_page.standing_book()

    @allure.title("盖章管理")
    def test_seal_management(self):
        self.login_page.category_management()
        self.login_page.stamp_to_apply()

    @allure.title("企业证书管理")
    def test_enterprise_certificate_management(self):
        self.login_page.enterprise_certificate_management()

    @allure.title("日程管理")
    def test_schedule_management(self):
        self.login_page.schedule_management()

    @allure.title("公司证书管理")
    def test_company_certificate_management(self):
        self.login_page.corporation_charter()
        self.login_page.certificate_to_borrow()
        self.login_page.standing_book_borrowed()

    @allure.title("票务管理")
    def test_ticket_management(self):
        self.login_page.apply_for()
        self.login_page.standing_books()

    @allure.title("活动管理")
    def test_publication_of_activity(self):
        self.login_page.publication_of_activity()

    @allure.title("新闻管理")
    def test_news_management(self):
        self.login_page.material_collection()
        self.login_page.news()
        self.login_page.news_list()

    @allure.title("公告通知")
    def test_the_announcement_to_inform(self):
        self.login_page.inform()
        self.login_page.bulletin_reading_statistics()

    @allure.title("会议管理")
    def test_meeting_management(self):
        self.login_page.conference_room()
        self.login_page.make_an_appointment_to_statistics()
        self.login_page.meeting_summary()

    @allure.title("物资管理")
    def test_materials_management(self):
        self.login_page.materials_put_in_storage()
        self.login_page.supplies_to_allocate()
        self.login_page.borrow_and_return()
        self.login_page.supplies_cleaning()
        self.login_page.material_parameter()

    @allure.title("车辆管理")
    def test_vehicle_management(self):
        self.login_page.information_management()
        self.login_page.annual_verification()
        self.login_page.automobile_insurance()

    @allure.title("统计管理")
    def test_statistical_management(self):
        self.login_page.report_forms()
        self.login_page.tabulate_statistics()
        self.login_page.technical_department_report()

    @allure.title("数据字典管理")
    def test_the_dictionary_management(self):
        self.login_page.the_dictionary_management()

    @allure.title("系统管理")
    def test_system_management(self):
        self.login_page.role_management()
        self.login_page.division_management()
        self.login_page.post_management()
        self.login_page.user_management()















