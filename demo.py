from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://yf.a99.live/")
driver.maximize_window()
driver.find_element_by_id("username").send_keys("18055779893")
driver.find_element_by_id("pwd").send_keys("123456789")
driver.find_element_by_xpath("/html/body/div/form/input[3]").click()

time.sleep(3)
# driver.find_element_by_xpath("//*[@id='LAY-system-side-menu']/li[1]/dl/dd[3]/a").click()
time.sleep(3)
# 切换"环境"
# iframe = driver.find_elements_by_tag_name("iframe")[0]
# driver.switch_to.frame("iframe")

# driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='LAY_app_body']/div[2]/iframe"))
#
# driver.find_element_by_xpath("/html/body/form/div[1]/div/input").send_keys("111")
# driver.find_element_by_xpath("/html/body/form/div[2]/div/input").send_keys("111")
# driver.find_element_by_xpath("/html/body/form/div[3]/div/input").send_keys("111")
# time.sleep(3)
# driver.find_element_by_xpath("/html/body/form/div[4]/div/button[1]").click()
#
# # 回到原始的"环境"
# driver.switch_to.default_content()

# 客户管理
driver.find_element_by_xpath("//*[@id='LAY-system-side-menu']/li[5]/a/cite").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='LAY-system-side-menu']/li[5]/dl/dd/a").click()
# 切换"环境"
driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='LAY_app_body']/div[2]/iframe"))


# iframe = driver.find_elements_by_tag_name("iframe")[0]
# driver.switch_to.frame(iframe)
time.sleep(10)
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/button[3]").click()
