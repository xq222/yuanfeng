import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://yf.a99.live/login.html")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element_by_xpath("html/body/div[1]/form/input[1]").send_keys("18055779893")
driver.find_element_by_xpath("html/body/div[1]/form/input[2]").send_keys("123456789")
driver.find_element_by_xpath("html/body/div[1]/form/input[3]").click()
driver.find_element_by_xpath("//*[@id='LAY-system-side-menu']/li[2]/a/cite").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='LAY-system-side-menu']/li[2]/dl/dd[1]/a").click()
time.sleep(3)
# iframe = driver.find_elements_by_tag_name("iframe")[1]
# driver.switch_to.frame(iframe)
driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='LAY_app_body']/div[2]/iframe"))

time.sleep(3)
driver.find_element_by_css_selector("body > div.tab.layui-clear > div:nth-child(1) > div").click()


# driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='LAY_app_body']/div[3]/iframe"))
# driver.find_element_by_xpath("/html/body/div[2]/div[1]/div").click()

# driver.find_element_by_xpath("/html/body/form/div[1]/div/input").send_keys("111")
