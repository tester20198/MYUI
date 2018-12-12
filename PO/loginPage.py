from PO.basePage import Base
from selenium.webdriver.common.by import By
import time


class LoginPage(Base):
    """
    启动页+登录界面的页面元素
    """

    login_button = (By.ID, "btnSignIn")  # 启动页的登录按钮
    edit_email = (By.ID, "et_emailSignIn")  # 邮箱输入框
    edit_mobile = (By.ID, "et_login_mobile")
    edit_pwd = (By.ID, "et_login_pass")  # 登录密码输入框
    login_btn = (By.ID, "btn_login")  # 登录页的登录按钮
    switch_btn = (By.ID, "tv_switch")  # 切换登录方式按钮(默认：手机)
    select_nation_btn = (By.ID, "tv_encrytionType")  # 国家下拉框
    nation = 'Venezuela'
    nation_XPATH = (By.XPATH, "//android.widget.TextView[contains(@text, 'Venezuela')]")

    def check_in(self):
        """
        初始页面的登录按钮
        :return:
        """
        self.driver.find_element(*self.login_button).click()

    def login_by_Email(self, email, pwd):
        """
        使用邮箱登录
        :return:
        """
        self.check_in()
        self.switch_login()  # 切换为邮箱登录模式
        self.driver.find_element(*self.edit_email).send_keys(email)
        self.driver.find_element(*self.edit_pwd).send_keys(pwd)
        self.Sys_back()  # 把键盘缩下去
        time.sleep(1)

    def login_by_Mobile(self, mobile, pwd):
        """
        使用手机登录
        :return:
        """
        self.check_in()
        self.select_nation(self.nation)  # 选择国家
        self.driver.find_element(*self.edit_mobile).send_keys(mobile)
        self.driver.find_element(*self.edit_pwd).send_keys(pwd)
        if self.findElement('注册'):
            pass
        else:
            self.Sys_back()

    def login_in(self):
        """
        登录页面的登录按钮
        :return:
        """
        self.driver.find_element(*self.login_btn).click()

    def switch_login(self):
        """
        切换登录方式
        :return:
        """
        self.driver.find_element(*self.switch_btn).click()  # 切换为登录模式

    def select_nation(self, na):
        """
        选择国家
        :return:
        """

        self.driver.find_element(*self.select_nation_btn).click()
        while not self.findElement(na):
            self.swipeUp(duration=1500)
        else:
            self.driver.find_element(*self.nation_XPATH).click()


