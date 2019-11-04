from appium.webdriver.webdriver import WebDriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Base():

    # 初始化驱动
    def __init__(self,driver):
        self.driver = driver

    # 元素定位
    def base_element(self,loc):
        return WebDriverWait(self.driver, 5, 0.2).until(lambda x: x.find_element(*loc))


    """
        鼠标操作
    """

    # 鼠标悬浮
    def base_move_to_element(self,loc):
        ActionChains(self.driver).move_to_element(self.base_element(loc)).perform()

    # 鼠标左键单击
    def base_click(self,loc):
        self.base_element(loc).click()

    # 鼠标右键单击
    def base_context_click(self,loc):
        ActionChains(self.driver).context_click(self.base_element(loc)).perform()

    # 鼠标左键双击
    def base_double_click(self,loc):
        ActionChains(self.driver).double_click(self.base_element(loc)).perform()

    # 鼠标拖动|loc_left左侧,loc_right右侧
    def base_drag_and_drop(self,loc_left,loc_right):
        ActionChains(self.driver).drag_and_drop(self.base_element(loc_left),self.base_element(loc_right)).perform()


    """
        键盘操作
    """

    # 输入框输入
    def base_send_keys(self,loc,text):
        self.base_element(loc).clear()
        self.base_element(loc).send_keys(text)

    # 键盘"退格"操作
    def base_drop(self,loc):
        self.base_element(loc).send_keys(Keys.BACK_SPACE)

    # 键盘"全选"操作
    def base_ctrl_a(self,loc):
        self.base_element(loc).send_keys(Keys.CONTROL, 'a')

    # 键盘"复制"操作
    def base_ctrl_c(self,loc):
        self.base_element(loc).send_keys(Keys.CONTROL, 'c')

    # 键盘"粘贴"操作
    def base_ctrl_(self,loc):
        self.base_element(loc).send_keys(Keys.CONTROL, 'v')


    """
        警告弹窗处理
    """

    # 弹窗单击确定
    def base_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    # 弹窗单击取消
    def base_confirm(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()

    # 弹窗输入点击确定
    def base_prompt_yes(self,text):
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()

    # 弹窗输入点击取消
    def base_prompt_no(self,text):
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        alert.dismiss()


    """
        下拉选择框处理
    """

    # 根据索引指定下拉框,索引定位从0开始
    def select_by_index(self,loc,number):
        select = Select(self.base_element(loc))
        select.select_by_index(number)

    # 根据value值定位
    def select_by_value(self,loc,text):
        select = Select(self.base_element(loc))
        select.select_by_value(text)

    # 根据所显示下拉框内容定位
    def select_by_visible_text(self,loc,text):
        select = Select(self.base_element(loc))
        select.select_by_visible_text(text)

    """
        frame切换
    """

    # 切换至name或id为text的frame模块
    def base_switch_frame(self,text):
        self.driver.switch_to.frame(text)

    # 切换至原页面
    def base_switch_to_default_content(self):
        self.driver.switch_to.default_content()