from selenium.webdriver.common.by import By

"""
登录
"""
username_edit_text = By.ID, "username"
password_edit_text = By.ID, "pwd"
add_button = By.XPATH, "/html/body/div/form/input[3]"


"""
我的桌面
"""
click_change_password = By.XPATH, "//*[@id='LAY-system-side-menu']/li[1]/dl/dd[3]/a"
old_password = By.XPATH, "/html/body/form/div[1]/div/input"
new_password = By.XPATH, "/html/body/form/div[2]/div/input"
confirm_password = By.XPATH, "/html/body/form/div[3]/div/input"
preserve = By.XPATH, "/html/body/form/div[4]/div/button[1]"
switch_frame_password= By.XPATH, "//*[@id='LAY_app_body']/div[2]/iframe"




"""
客户管理
"""
customer_management = By.XPATH, "//*[@id='LAY-system-side-menu']/li[5]/a/cite"
the_customer_information = By.XPATH, "//*[@id='LAY-system-side-menu']/li[5]/dl/dd/a"
the_customer_registration = By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/button[3]"


"""
审批管理
"""
test_approval_management = By.XPATH, "//*[@id='LAY-system-side-menu']/li[2]/a/cite"
the_examination = By.XPATH, "//*[@id='LAY-system-side-menu']/li[2]/dl/dd[1]/a"
# iframe = By.TAG_NAME, "iframe[1]"
click_on_the_application = By.CSS_SELECTOR, "body > div.tab.layui-clear > div:nth-child(1) > div"


"""
招投标管理
"""
# 点击招投标管理
management_of_bidding_and_tendering = By.XPATH, "//*[@id='LAY-system-side-menu']/li[3]/a/cite"
# 点击业务机会
business_chance = By.XPATH, "//*[@id='LAY-system-side-menu']/li[3]/dl/dd[1]/a"
# 定位关键字元素输入框
keyword = By.XPATH, "/html/body/div[1]/div/form/div/div[1]/div/input"
select_project_manager = By.XPATH, "/html/body/div[1]/div/form/div/div[6]/button[1]"
switch_frame_id = By.ID, "layui-layer-iframe2"
check = By.XPATH, "//*[@id='test4']/div/div[1]/ul/li[1]/div/div/div"
botton = By.XPATH, "//*[@id='test4']/div/div[2]/button[1]"
submit = By.XPATH, "/html/body/div[2]/button"


"""
人员需求
"""
personnel_requirement = By.XPATH, "//*[@id='LAY-system-side-menu']/li[6]/a/cite"
personnel_requirement1 = By.XPATH, "//*[@id='LAY-system-side-menu']/li[6]/dl/dd/a"
check_the_operation = By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/table/tbody/tr[1]/td[5]/div/a"
switch_frame_operation = By.XPATH, "//*[@id='LAY_app_body']/div[4]/iframe"


"""
合同管理
"""
contract_management = By.XPATH, "//*[@id='LAY-system-side-menu']/li[4]/a/cite"
project_contract = By.XPATH, "//*[@id='LAY-system-side-menu']/li[4]/dl/dd/a"
please_enter = By.XPATH, "/html/body/div/div/form/div/div[1]/div/input"
click_inquire = By.XPATH, "/html/body/div/div/form/div/div[11]/button[1]"


"""
假期管理
"""
the_holiday_management = By.XPATH, "//*[@id='LAY-system-side-menu']/li[10]/a/cite"
ask_for_leave_record = By.XPATH, "//*[@id='LAY-system-side-menu']/li[10]/dl/dd/a"


"""
考勤管理
"""
attendance_management = By.XPATH, "//*[@id='LAY-system-side-menu']/li[11]/a/cite"
attendance_group_management = By.XPATH, "//*[@id='LAY-system-side-menu']/li[11]/dl/dd[1]/a"
flight_management = By.XPATH, "//*[@id='LAY-system-side-menu']/li[11]/dl/dd[2]/a"
attendance_check = By.XPATH, "//*[@id='LAY-system-side-menu']/li[11]/dl/dd[3]/a"
statistic = By.XPATH, "//*[@id='LAY-system-side-menu']/li[11]/dl/dd[4]/a"
monthly_statistic = By.XPATH, "//*[@id='LAY-system-side-menu']/li[11]/dl/dd[5]/a"


"""
人员进出
"""
personnel_in_and_out = By.XPATH, "//*[@id='LAY-system-side-menu']/li[12]/a/cite"
application_of_choose_and_employ_persons = By.XPATH, "//*[@id='LAY-system-side-menu']/li[12]/dl/dd[1]/a"
become_a_full_member = By.XPATH, "//*[@id='LAY-system-side-menu']/li[12]/dl/dd[2]/a"
remove = By.XPATH, "//*[@id='LAY-system-side-menu']/li[12]/dl/dd[3]/a"
dimission = By.XPATH, "//*[@id='LAY-system-side-menu']/li[12]/dl/dd[4]/a"


"""
培训管理
"""
training_management = By.XPATH, "//*[@id='LAY-system-side-menu']/li[13]/a/cite"
plan = By.XPATH, "//*[@id='LAY-system-side-menu']/li[13]/dl/dd[1]/a"
internal = By.XPATH, "//*[@id='LAY-system-side-menu']/li[13]/dl/dd[2]/a"
external = By.XPATH, "//*[@id='LAY-system-side-menu']/li[13]/dl/dd[3]/a"
record_statistical = By.XPATH, "//*[@id='LAY-system-side-menu']/li[13]/dl/dd[4]/a"


"""
考核管理
"""
appraisal = By.XPATH, "//*[@id='LAY-system-side-menu']/li[14]/a/cite"
appraisals = By.XPATH, "//*[@id='LAY-system-side-menu']/li[14]/dl/dd[1]/a"
coefficient =By.XPATH, "//*[@id='LAY-system-side-menu']/li[14]/dl/dd[2]/a"


"""
社保管理
"""
management_of_social_security = By.XPATH, "//*[@id='LAY-system-side-menu']/li[15]/a/cite"
social_security = By.XPATH, "//*[@id='LAY-system-side-menu']/li[15]/dl/dd[1]/a"
share = By.XPATH, "//*[@id='LAY-system-side-menu']/li[15]/dl/dd[2]/a"
set = By.XPATH, "//*[@id='LAY-system-side-menu']/li[15]/dl/dd[3]/a"


"""
薪资管理
"""
salary_management = By.XPATH, "//*[@id='LAY-system-side-menu']/li[16]/a/cite"
the_monthly_salary = By.XPATH, "//*[@id='LAY-system-side-menu']/li[16]/dl/dd[1]/a"
payroll_processing = By.XPATH, "//*[@id='LAY-system-side-menu']/li[16]/dl/dd[2]/a"
actual_salary_accounting = By.XPATH, "//*[@id='LAY-system-side-menu']/li[16]/dl/dd[3]/a"
wage_statistic = By.XPATH, "//*[@id='LAY-system-side-menu']/li[16]/dl/dd[4]/a"
deductions = By.XPATH, "//*[@id='LAY-system-side-menu']/li[16]/dl/dd[5]/a"
tax_amount_payable = By.XPATH, "//*[@id='LAY-system-side-menu']/li[16]/dl/dd[6]/a"


"""
项目管理
"""
project_management = By.XPATH, "//*[@id='LAY-system-side-menu']/li[17]/a/cite"
project_startups = By.XPATH, "//*[@id='LAY-system-side-menu']/li[17]/dl/dd[1]/a"
monitoring = By.XPATH, "//*[@id='LAY-system-side-menu']/li[17]/dl/dd[2]/a"
statistics = By.XPATH, "//*[@id='LAY-system-side-menu']/li[17]/dl/dd[3]/a"


"""
资料库管理
"""
library_management = By.XPATH, "//*[@id='LAY-system-side-menu']/li[18]/a/cite"
bank = By.XPATH, "//*[@id='LAY-system-side-menu']/li[18]/dl/dd[1]/a"
norms = By.XPATH, "//*[@id='LAY-system-side-menu']/li[18]/dl/dd[2]/a"
templates = By.XPATH, "//*[@id='LAY-system-side-menu']/li[18]/dl/dd[3]/a"
document = By.XPATH, "//*[@id='LAY-system-side-menu']/li[18]/dl/dd[4]/a"


"""
投标保证金管理
"""
bid_security_management = By.XPATH, "//*[@id='LAY-system-side-menu']/li[19]/a/cite"
deposit = By.XPATH, "//*[@id='LAY-system-side-menu']/li[19]/dl/dd/a"


"""
合同履约金管理
"""
contract_performance_fund_management = By.XPATH, "//*[@id='LAY-system-side-menu']/li[20]/a/cite"
management_tax_payment = By.XPATH, '//*[@id="LAY-system-side-menu"]/li[20]/dl/dd/a'


"""
合同质保金管理
"""
quality_retention_money_management = By.XPATH, "//*[@id='LAY-system-side-menu']/li[21]/a/cite"
payment_and_recovery = By.XPATH, "//*[@id='LAY-system-side-menu']/li[21]/dl/dd/a"


"""
监理费管理
"""
supervision_fee_management = By.XPATH, "//*[@id='LAY-system-side-menu']/li[22]/a/cite"
settle_apply_for = By.XPATH, "//*[@id='LAY-system-side-menu']/li[22]/dl/dd[1]/a"
deductions_settlements = By.XPATH, "//*[@id='LAY-system-side-menu']/li[22]/dl/dd[2]/a"
standing_books = By.XPATH, "//*[@id='LAY-system-side-menu']/li[22]/dl/dd[3]/a"


"""
盖章管理
"""
seal_management = By.XPATH, "//*[@id='LAY-system-side-menu']/li[23]/a/cite"
category_managements = By.XPATH, "//*[@id='LAY-system-side-menu']/li[23]/dl/dd[1]/a"
stamp_to_applys = By.XPATH, "//*[@id='LAY-system-side-menu']/li[23]/dl/dd[2]/a"


"""
企业证书管理
"""
enterprise_certificate = By.XPATH, "//*[@id='LAY-system-side-menu']/li[24]/a/cite"
enterprise_certificates = By.XPATH, "//*[@id='LAY-system-side-menu']/li[24]/dl/dd/a"


"""
日程管理
"""
schedule = By.XPATH, "//*[@id='LAY-system-side-menu']/li[25]/a/cite"
schedules = By.XPATH, "//*[@id='LAY-system-side-menu']/li[25]/dl/dd/a"


"""
公司证书管理
"""
certificate_management = By.XPATH, "//*[@id='LAY-system-side-menu']/li[26]/a/cite"
corporation_charters = By.XPATH, "//*[@id='LAY-system-side-menu']/li[26]/dl/dd[1]/a"
certificate_to_borrows = By.XPATH, "//*[@id='LAY-system-side-menu']/li[26]/dl/dd[2]/a"
standing_book_borroweds = By.XPATH, "//*[@id='LAY-system-side-menu']/li[26]/dl/dd[3]/a"


"""
票务管理
"""
Ticket_management = By.XPATH, "//*[@id='LAY-system-side-menu']/li[27]/a/cite"
apply_fors = By.XPATH, "//*[@id='LAY-system-side-menu']/li[27]/dl/dd[1]/a"
standing_book = By.XPATH, "//*[@id='LAY-system-side-menu']/li[27]/dl/dd[2]/a"


"""
活动管理
"""
activities_management = By.XPATH, "//*[@id='LAY-system-side-menu']/li[28]/a/cite"
publication_activity = By.XPATH, "//*[@id='LAY-system-side-menu']/li[28]/dl/dd/a"


"""
新闻管理
"""
news_management = By.XPATH, "//*[@id='LAY-system-side-menu']/li[29]/a/cite"
Material_collection = By.XPATH, "//*[@id='LAY-system-side-menu']/li[29]/dl/dd[1]/a"
newss = By.XPATH, "//*[@id='LAY-system-side-menu']/li[29]/dl/dd[2]/a"
News_list = By.XPATH, "//*[@id='LAY-system-side-menu']/li[29]/dl/dd[3]/a"


"""
公告通知
"""
The_announcement_to_inform = By.XPATH, "//*[@id='LAY-system-side-menu']/li[30]/a/cite"
the_announcement_to_inform = By.XPATH, "//*[@id='LAY-system-side-menu']/li[30]/dl/dd[1]/a"
reading = By.XPATH, "//*[@id='LAY-system-side-menu']/li[30]/dl/dd[2]/a"


"""
会议管理
"""
meeting_management = By.XPATH, "//*[@id='LAY-system-side-menu']/li[31]/a/cite"
conference_rooms = By.XPATH, "//*[@id='LAY-system-side-menu']/li[31]/dl/dd[1]/a"
statisticss = By.XPATH, "//*[@id='LAY-system-side-menu']/li[31]/dl/dd[2]/a"
meeting_summarys = By.XPATH, "//*[@id='LAY-system-side-menu']/li[31]/dl/dd[3]/a"


"""
物资管理
"""
materials_management = By.XPATH, "//*[@id='LAY-system-side-menu']/li[32]/a/cite"
materials_put_in_storages = By.XPATH, "//*[@id='LAY-system-side-menu']/li[32]/dl/dd[1]/a"
supplies_to_allocates = By.XPATH, "//*[@id='LAY-system-side-menu']/li[32]/dl/dd[2]/a"
borrow_and_returns = By.XPATH, "//*[@id='LAY-system-side-menu']/li[32]/dl/dd[3]/a"
supplies_cleanings = By.XPATH, "//*[@id='LAY-system-side-menu']/li[32]/dl/dd[4]/a"
material_parameters = By.XPATH, "//*[@id='LAY-system-side-menu']/li[32]/dl/dd[5]/a"


"""
车俩管理
"""
vehicle_management = By.XPATH, "//*[@id='LAY-system-side-menu']/li[33]/a/cite"
information_managements = By.XPATH, "//*[@id='LAY-system-side-menu']/li[33]/dl/dd[1]/a"
annual_verifications = By.XPATH, "//*[@id='LAY-system-side-menu']/li[33]/dl/dd[2]/a"
automobile_insurances = By.XPATH, "//*[@id='LAY-system-side-menu']/li[33]/dl/dd[3]/a"


"""
统计管理
"""
statistical_management = By.XPATH, "//*[@id='LAY-system-side-menu']/li[34]/a/cite"
report_formss = By.XPATH, "//*[@id='LAY-system-side-menu']/li[34]/dl/dd[1]/a"
tabulate_statisticss = By.XPATH, "//*[@id='LAY-system-side-menu']/li[34]/dl/dd[2]/a"
technical_department_reports = By.XPATH, "//*[@id='LAY-system-side-menu']/li[34]/dl/dd[3]/a"


"""
数据字典管理
"""
The_dictionary_management = By.XPATH, "//*[@id='LAY-system-side-menu']/li[35]/a/cite"
the_dictionary_managements = By.XPATH, "//*[@id='LAY-system-side-menu']/li[35]/dl/dd/a"


"""
系统管理
"""
system_management = By.XPATH, "//*[@id='LAY-system-side-menu']/li[36]/a/cite"
role_managements = By.XPATH, "//*[@id='LAY-system-side-menu']/li[36]/dl/dd[1]/a"
division_managements = By.XPATH, "//*[@id='LAY-system-side-menu']/li[36]/dl/dd[2]/a"
post_managements = By.XPATH, "//*[@id='LAY-system-side-menu']/li[36]/dl/dd[3]/a"
user_managements = By.XPATH, "//*[@id='LAY-system-side-menu']/li[36]/dl/dd[4]/a"


111


