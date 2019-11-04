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

