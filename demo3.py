from selenium import webdriver
import time
import allure


@ allure.title("登录")
def test_01():
    # 调起Chrome
    driver = webdriver.Chrome()
    driver.get("http://yf.a99.live/")
    # 最大化
    driver.maximize_window()

    # 获取当前页面title
    title = driver.title
    print("当前页面的title是：", title, "\n")
    # 登录
    driver.find_element_by_id("username").send_keys("18055779893")
    driver.find_element_by_id("pwd").send_keys("123456789")
    driver.find_element_by_xpath("/html/body/div/form/input[3]").click()
    time.sleep(2)

    # 获取当前页面title
    title = driver.title
    print("当前页面的title是：", title, "\n")

    # 断言
    if "元丰监理后台管理模板系统" == driver.title:
        print('登陆成功.')
    else:
        print('登录失败')