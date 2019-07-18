from PO.basePage import Base
from selenium.webdriver.common.by import By
import time


class LoginPage(Base):
    """
    启动页+登录界面的页面元素
    """

    login = (By.ID, "btnSignIn")  # 启动页的登录按钮
    sunge = (By.ID, 'btnSignIn')
    zhuce = (By.ID, 'btnSignup')
    register = (By.ID, "btnSignup")  # 启动页的注册按钮
    help_bt = (By.ID, "tv_menu")  # help&feedback
    edit_email = (By.ID, "et_emailSignIn")  # 邮箱输入框
    edit_mobile = (By.ID, "et_login_mobile")  # 手机输入框
    edit_pwd = (By.ID, "et_login_pass")  # 登录密码输入框
    login_btn = (By.ID, "btn_login")  # 登录页的登录按钮
    switch_btn = (By.ID, "tv_switch")  # 切换登录方式按钮
    select_nation_btn = (By.ID, "tv_encrytionType")  # 国家下拉框
    back = (By.XPATH,
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageButton")  # 登录页面的返回按钮
    login_register = (By.ID, "tv_sign_up")  # 登录页面的注册按钮
    forget_pwd = (By.ID, "tv_forget_pass")  # 登录页面的忘记密码
    center = (By.ID, "iv_user_icon")  # 个人中心
    setting = (By.ID, "rl_layout_setting")  # 个人中心的设置
    logout = (By.ID, "tv_loginout")  # 退出登录
    confirm_logout = (By.ID, "button1")  # 确认退出登录

    def check_in(self):
        """
        启动页选择登录
        """

        self.driver.find_element(*self.login).click()

    def login_by_Email(self, email, pwd):
        """
        使用邮箱登录
        """

        self.driver.find_element(*self.edit_email).send_keys(email)
        self.driver.find_element(*self.edit_pwd).send_keys(pwd)
        self.log_in()

    def login_by_Mobile(self, mobile, pwd, na=None):
        """
        使用手机登录
        """

        self.switch_login()
        self.select_nation(na)  # 选择国家
        time.sleep(1)
        self.driver.find_element(*self.edit_mobile).send_keys(mobile)
        self.driver.find_element(*self.edit_pwd).send_keys(pwd)
        self.log_in()

    def log_in(self):
        """
        点击登录页面的登录按钮
        """
        self.driver.find_element(*self.login_btn).click()

    def switch_login(self):
        """
        切换登录方式
        """

        self.driver.find_element(*self.switch_btn).click()

    def select_nation(self, na):
        """
        手机登录--选择国家
        """

        nation_XPATH = (By.XPATH, f'//android.widget.TextView[contains(@text, "{na}")]')  # 定位国家

        self.driver.find_element(*self.select_nation_btn).click()
        while not self.findElement(na):
            self.swipeUp(duration=1500)
        else:
            self.driver.find_element(*nation_XPATH).click()

    def loginpage_register(self):
        """
        点击登录页面的注册按钮
        """

        self.driver.find_element(*self.register).click()

    def enter_usercenter(self):
        """
        进入个人中心
        """

        self.driver.find_element(*self.center).click()

    def log_out(self):
        """
        退出登录
        """

        self.driver.find_element(*self.center).click()
        time.sleep(3)
        self.driver.find_element(*self.setting).click()
        self.driver.find_element(*self.logout).click()
        self.driver.switch_to.alert.accept()  # 系统弹窗默认允许
        # self.driver.find_element(*self.confirm_logout).click()
