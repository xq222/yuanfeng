from page.login_page import LoginPage


class PageIn():

    # page_index 页面
    def login_page(self, driver):
        return LoginPage(driver)

