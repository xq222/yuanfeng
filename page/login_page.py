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
        # time.sleep(2)
        # self.base_switch_frame(self.find_element(page.switch_frame_operation))
        # self.click(page.check_the_operation)
        # self.base_switch_to_default_content()

    @allure.step(title="合同管理-项目合同-根据合同名称点击查询")
    def click_on_the_query(self, text):
        self.click(page.contract_management)
        self.click(page.project_contract)
        time.sleep(2)
        self.base_switch_frame(self.find_element(page.switch_frame_password))
        self.input(page.please_enter, text)
        self.click(page.click_inquire)
        self.base_switch_to_default_content()

    @allure.step(title= "假期管理-请假记录")
    def leave(self):
        self.click(page.the_holiday_management)
        self.click(page.ask_for_leave_record)

    @allure.step(title= "考勤管理-考勤组管理")
    def group_of_check_on_work_attendance(self):
        self.click(page.attendance_management)
        self.click(page.attendance_group_management)

    @allure.step(title= "考勤管理-班次管理")
    def classes(self):
        # self.click(page.attendance_management)
        self.click(page.flight_management)

    @allure.step(title="考勤管理-考勤签到查询")
    def sign_in_to_query(self):
        # self.click(page.attendance_management)
        self.click(page.attendance_check)

    @allure.step(title="考勤管理-考勤每日统计")
    def statistics(self):
        # self.click(page.attendance_management)
        self.click(page.statistic)

    @allure.step(title="考勤管理-考勤每月统计")
    def monthly_statistics(self):
        # self.click(page.attendance_management)
        self.click(page.monthly_statistic)

    @allure.step(title="人员进出-用人申请")
    def employ_persons_application(self):
        self.click(page.personnel_in_and_out)
        self.click(page.application_of_choose_and_employ_persons)

    @allure.step(title="人员进出-员工转正")
    def staff_regularization(self):
        # self.click(page.personnel_in_and_out)
        self.click(page.become_a_full_member)

    @allure.step(title="人员进出-人事调动")
    def personnel_transfer(self):
        # self.click(page.personnel_in_and_out)
        self.click(page.remove)

    @allure.step(title="人员进出-离职管理")
    def dimission_management(self):
        # self.click(page.personnel_in_and_out)
        self.click(page.dimission)

    @allure.step(title="培训管理-培训计划")
    def training_program(self):
        self.click(page.training_management)
        self.click(page.plan)

    @allure.step(title="培训管理-内部培训")
    def internal_training(self):
        # self.click(page.training_management)
        self.click(page.internal)

    @allure.step(title="培训管理-外部培训")
    def external_training(self):
        # self.click(page.training_management)
        self.click(page.external)

    @allure.step(title="培训管理-培训记录统计")
    def training_record_statistics(self):
        # self.click(page.training_management)
        self.click(page.record_statistical)

    @allure.step(title="考核管理-考核管理")
    def appraisal_managements(self):
        self.click(page.appraisal)
        self.click(page.appraisals)

    @allure.step(title="考核管理-考核系数设置")
    def coefficient_setting(self):
        # self.click(page.appraisal)
        self.click(page.coefficient)

    @allure.step(title="社保管理-员工社保")
    def employees_social_security(self):
        self.click(page.management_of_social_security)
        self.click(page.social_security)

    @allure.step(title="社保管理—员工项目分摊汇总表")
    def share_the_summary(self):
        # self.click(page.management_of_social_security)
        self.click(page.share)

    @allure.step(title="社保管理-社保基数设置")
    def cardinality(self):
        # self.click(page.management_of_social_security)
        self.click(page.set)

    @allure.step(title="薪资管理-员工每月薪资管理")
    def monthly_salary_management(self):
        self.click(page.salary_management)
        self.click(page.the_monthly_salary)

    @allure.step(title="薪资管理-员工每月出勤薪资核算")
    def attendance_salary_accounting(self):
        # self.click(page.salary_management)
        self.click(page.payroll_processing)

    @allure.step(title="薪资管理-员工每月薪资实发核算")
    def actual_salary_accounting(self):
        # self.click(page.salary_management)
        self.click(page.actual_salary_accounting)

    @allure.step(title="薪资管理-应付工资统计")
    def wage_statistics(self):
        # self.click(page.salary_management)
        self.click(page.wage_statistic)

    @allure.step(title="薪资管理-薪资扣款规则设置")
    def deductions_rules(self):
        # self.click(page.salary_management)
        self.click(page.deductions)

    @allure.step(title="薪资管理-应纳税额设置")
    def the_amount_of_tax_payable_is_set(self):
        # self.click(page.salary_management)
        self.click(page. tax_amount_payable)

    @allure.step(title="项目管理-项目启动")
    def project_startup(self):
        self.click(page.project_management)
        self.click(page.project_startups)

    @allure.step(title="项目管理-项目监控")
    def project_monitoring(self):
        # self.click(page.project_management)
        self.click(page.monitoring)

    @allure.step(title="项目管理-报表统计")
    def report_form_statistics(self):
        # self.click(page.project_management)
        self.click(page.statistics)

    @allure.step(title="资料库管理-资料库")
    def data_bank(self):
        self.click(page.library_management)
        self.click(page.bank)

    @allure.step(title="资料库管理-规范")
    def norm(self):
        # self.click(page.library_management)
        self.click(page.norms)

    @allure.step(title="资料库管理-模板")
    def template(self):
        # self.click(page.library_management)
        self.click(page.templates)

    @allure.step(title="资料库管理-公司制度文件")
    def system_document(self):
        # self.click(page.library_management)
        self.click(page.document)

    @allure.step(title="投标保证金管理-投标保证金缴纳")
    def pay_deposit(self):
        self.click(page.bid_security_management)
        self.click(page.deposit)

    @allure.step(title="合同履约金管理-合同履约金管理纳税")
    def performance_management_tax_payment(self):
        self.click(page.contract_performance_fund_management)
        self.click(page.management_tax_payment)

    @allure.step(title="合同质保金管理-合同质保金缴纳及收回")
    def contract_quality_retention_money_payment_and_recovery(self):
        self.click(page.quality_retention_money_management)
        self.click(page.payment_and_recovery)

    @allure.step(title="监理费管理-监理费结算申请")
    def supervision_fee_settlement_application(self):
        self.click(page.supervision_fee_management)
        self.click(page.settle_apply_for)

    @allure.step(title="监理费管理-监理结算扣款结算")
    def deductions_settlement(self):
        # self.click(page.supervision_fee_management)
        self.click(page.deductions_settlements)

    @allure.step(title="监理费管理-扣费汇总台账")
    def standing_book(self):
        # self.click(page.supervision_fee_management)
        self.click(page.standing_books)

    @allure.step(title="盖章管理-盖章资料类别管理")
    def category_management(self):
        self.click(page.seal_management)
        self.click(page.category_managements)

    @allure.step(title="盖章管理-盖章申请")
    def stamp_to_apply(self):
        # self.click(page.seal_management)
        self.click(page.stamp_to_applys)

    @allure.step(title="企业证书管理")
    def enterprise_certificate_management(self):
        self.click(page.enterprise_certificate)
        self.click(page.enterprise_certificates)

    @allure.step(title="日程管理")
    def schedule_management(self):
        self.click(page.schedule)
        self.click(page.schedules)

    @allure.step(title="公司证书管理-公司证书")
    def corporation_charter(self):
        self.click(page.certificate_management)
        self.click(page.corporation_charters)

    @allure.step(title="公司证书管理-公司证书借用")
    def certificate_to_borrow(self):
        # self.click(page.certificate_management)
        self.click(page.certificate_to_borrows)

    @allure.step(title="公司证书管理-公司证书借还台账")
    def standing_book_borrowed(self):
        # self.click(page.certificate_management)
        self.click(page.standing_book_borroweds)

    @allure.step(title="票务管理-票务申请")
    def apply_for(self):
        self.click(page.Ticket_management)
        self.click(page.apply_fors)

    @allure.step(title="票务管理-票务台账")
    def standing_books(self):
        # self.click(page.Ticket_management)
        self.click(page.standing_book)

    @allure.step(title="活动管理-发布活动")
    def publication_of_activity(self):
        self.click(page.activities_management)
        self.click(page.publication_activity)

    @allure.step(title="新闻管理-素材收集")
    def material_collection(self):
        self.click(page.news_management)
        self.click(page.Material_collection)

    @allure.step(title="新闻管理-新闻栏目")
    def news(self):
        # self.click(page.news_management)
        self.click(page.newss)

    @allure.step(title="新闻管理-新闻列表")
    def news_list(self):
        # self.click(page.news_management)
        self.click(page.News_list)

    @allure.step(title="公告通知-公告通知")
    def inform(self):
        self.click(page.The_announcement_to_inform)
        self.click(page.the_announcement_to_inform)

    @allure.step(title="公告通知-公告阅读统计")
    def bulletin_reading_statistics(self):
        # self.click(page.The_announcement_to_inform)
        self.click(page.reading)

    @allure.step(title="会议管理-会议室")
    def conference_room(self):
        self.click(page.meeting_management)
        self.click(page.conference_rooms)

    @allure.step(title="会议室管理-会议室预约统计")
    def make_an_appointment_to_statistics(self):
        # self.click(page.meeting_management)
        self.click(page.statisticss)

    @allure.step(title="会议室管理-会议纪要")
    def meeting_summary(self):
        # self.click(page.meeting_management)
        self.click(page.meeting_summarys)

    @allure.step(title="物资管理-物资入库")
    def materials_put_in_storage(self):
        self.click(page.materials_management)
        self.click(page.materials_put_in_storages)

    @allure.step(title="物资管理-物资调拨")
    def supplies_to_allocate(self):
        # self.click(page.materials_management)
        self.click(page.supplies_to_allocates)

    @allure.step(title="物资管理-物资借用与归还")
    def borrow_and_return(self):
        # self.click(page.materials_management)
        self.click(page.borrow_and_returns)

    @allure.step(title="物资管理-物资清理")
    def supplies_cleaning(self):
        # self.click(page.materials_management)
        self.click(page.supplies_cleanings)

    @allure.step(title="物资管理-物资台账")
    def material_parameter(self):
        # self.click(page.materials_management)
        self.click(page.material_parameters)

    @allure.step(title="车辆管理-车辆信息管理")
    def information_management(self):
        self.click(page.vehicle_management)
        self.click(page.information_managements)

    @allure.step(title="车辆信息-车辆年审")
    def annual_verification(self):
        # self.click(page.vehicle_management)
        self.click(page.annual_verifications)

    @allure.step(title="车辆信息-车辆保险")
    def automobile_insurance(self):
        # self.click(page.vehicle_management)
        self.click(page.automobile_insurances)

    @allure.step(title="统计管理-建设工程监理项目产值报表")
    def report_forms(self):
        self.click(page.statistical_management)
        self.click(page.report_formss)

    @allure.step(title="统计管理-建设工程监理项目每月项目情况汇总统计")
    def tabulate_statistics(self):
        # self.click(page.statistical_management)
        self.click(page.tabulate_statisticss)

    @allure.step(title="统计管理-技术部报表")
    def technical_department_report(self):
        # self.click(page.statistical_management)
        self.click(page.technical_department_reports)

    @allure.step(title="数据字典管理-数据字典管理")
    def the_dictionary_management(self):
        self.click(page.The_dictionary_management)
        self.click(page.the_dictionary_managements)

    @allure.step(title="系统管理-角色管理")
    def role_management(self):
        self.click(page.system_management)
        self.click(page.role_managements)

    @allure.step(title="系统管理-部门管理")
    def division_management(self):
        # self.click(page.system_management)
        self.click(page.division_managements)

    @allure.step(title="系统管理-岗位管理")
    def post_management(self):
        # self.click(page.system_management)
        self.click(page.post_managements)

    @allure.step(title="系统管理-用户管理")
    def user_management(self):
        # self.click(page.system_management) 注释
        self.click(page.user_managements)
























