from PO.basePage import Base
from selenium.webdriver.common.by import By
import time


class LoginPage(Base):
    """
    启动页+登录界面的页面元素
    """

    login = (By.ID, "LOG IN")  # 启动页的登录按钮
    register = (By.ID, "SIGN UP")  # 启动页的注册按钮
    edit_email = (By.ID, 'login_email')  # 邮箱输入框
    edit_mobile = (By.ID, "login_phone")  # 手机输入框
    edit_pwd = (By.ID, 'login_password')  # 登录密码输入框
    login_btn = (By.ID, 'login_submit')  # 登录页的登录按钮
    switch_btn = (By.NAME, "Phone No.")  # 切换登录方式按钮
    back = (By.ID, "btn back")  # 登录页面的返回按钮
    help_btn = (By.ID, 'Help&Feedback')
    register_btn = (By.ID, 'Sign Up')  # 登录页的注册按钮
    forget_pwd = (By.ID, 'Forgot Password')  # 登录页的忘记登录密码按钮
    select_nation_btn = (By.ID, "Rectangle")  # 国家下拉框
    center = (By.ID, 'ic user home')  # 个人中心
    setting = (By.ID, 'Account Settings')  # 个人中心的设置
    logout = (By.ID, 'Log Out')
    confirm_logout = (By.ID, 'Confirm')

    def check_in(self):
        """初始页面的登录按钮"""

        self.driver.find_element(*self.login).click()

    def login_by_Email(self, email, pwd):
        """
        使用邮箱登录
        """

        self.driver.find_element(*self.edit_email).send_keys(email)
        self.driver.find_element(*self.edit_pwd).send_keys(pwd)
        self.login_in()

    def login_by_Mobile(self, mobile, pwd, na=None):
        """
        使用手机登录
        """

        self.switch_login()
        # self.select_nation(na)  # 选择国家
        self.driver.find_element(*self.edit_mobile).send_keys(mobile)
        self.driver.find_element(*self.edit_pwd).send_keys(pwd)
        self.login_in()

    def login_in(self):
        """登录页面的登录按钮"""

        self.driver.find_element(*self.login_btn).click()

    def switch_login(self):
        """切换登录方式"""

        self.driver.find_element(*self.switch_btn).click()

    def select_nation(self, na):
        """选择国家"""

        nation_PATH = (By.ID, na)  # 定位国家
        self.driver.find_element(*self.select_nation_btn).click()
        while not self.findElement(na):
            self.ios_swipeUP()
        else:
            self.driver.find_element(*nation_PATH).click()

    def loginpage_register(self):
        """登录页面的注册按钮"""

        self.driver.find_element(*self.register).click()

    def log_out(self):
        """
        退出登录
        """

        self.driver.find_element(*self.center).click()
        time.sleep(5)
        self.ios_swipeUP()
        self.driver.find_element(*self.setting).click()
        self.driver.find_element(*self.logout).click()
        self.driver.find_element(*self.confirm_logout).click()
