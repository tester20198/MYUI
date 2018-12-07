from PO.basePage import Base
from selenium.webdriver.common.by import By


class LoginPage(Base):
    """
    启动页+登录界面的页面元素
    """

    login_button = (By.ID, "btnSignIn")  # 启动页的登录按钮
    edit_email = (By.ID, "et_emailSignIn")  # 邮箱输入框
    edit_pwd = (By.ID, "et_login_pass")  # 登录密码输入框
    login_btn = (By.ID, "btn_login")  # 登录页的登录按钮

    def check_in(self):
        self.driver.find_element(*self.login_button).click()

    def login_by_Email(self, email, pwd):
        self.check_in()
        self.driver.find_element(*self.edit_email).send_keys(email)
        self.driver.find_element(*self.edit_pwd).send_keys(pwd)

    def login_in(self):
        self.driver.find_element(*self.login_btn).click()

