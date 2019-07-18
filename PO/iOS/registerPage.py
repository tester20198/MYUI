from PO.basePage import Base
from selenium.webdriver.common.by import By
import time


class registerPage(Base):
    """
    启动页+注册界面的页面元素
    """

    register_button = (By.ID, "SIGN UP")  # 启动页注册按钮
    select_nation_btn = (By.ID, "tv_encrytionType")  # 国家下拉框
    send_mobile = (By.ID, "et_phone_number")  # 注册手机号码
    next_step = (By.ID, "btn_signUp")  # 注册第一步
    mobile_code = (By.ID, "et_mobile_code")  # 手机验证码
    verify_code = (By.ID, "bt_moblie_code_verify_next")  # 注册第二步
    register_pwd = (By.ID, "et_register_pass")  # 登录密码
    comfirm_pwd = (By.ID, "et_register_pass_again")  # 确认登录密码
    comfirm_btn = (By.ID, "btn_completeRegistration")  # 注册第三步
    pay_pwd = (By.ID, "et_register_pass")  # 支付密码
    comfirm_pay_pwd = (By.ID, "et_register_pass_again")  # 确认支付密码
    complete = (By.ID, "btn_completeRegistration")  # 完成
    tt = (By.ID, "tv_mobile_verify_time")  # 倒计时
    switch_email = (By.ID, "tv_switch")

    def click_register(self):
        """
        初始页面的注册按钮
        :return:
        """
        self.driver.find_element(*self.register_button).click()

    def register_by_mobile(self, nation, mobile):
        """
        1.选择国家
        2.手机号码注册
        """

        self.select_nation(nation)
        time.sleep(1)
        self.driver.find_element(*self.send_mobile).send_keys(mobile)
        self.driver.find_element(*self.next_step).click()
        time.sleep(2)

    def select_nation(self, na):
        """
        选择国家
        :return:
        """
        nation_XPATH = (By.XPATH, f'//android.widget.TextView[contains(@text, "{na}")]')# 定位国家

        self.driver.find_element(*self.select_nation_btn).click()
        while not self.findElement(na):
            self.swipeUp(duration=1500)
        else:
            self.driver.find_element(*nation_XPATH).click()

    def verify(self, code=2222):
        """输入手机验证码"""

        self.driver.find_element(*self.mobile_code).send_keys(code)  # 测试环境默认2222
        self.driver.find_element(*self.verify_code).click()  # 第二步
        time.sleep(2)

    def send_pwd(self, pwd='Aa123456'):
        """
        注册时输入账号密码
        :return:
        """

        self.driver.find_element(*self.register_pwd).send_keys(pwd)
        self.driver.find_element(*self.comfirm_pwd).send_keys(pwd)
        self.Sys_back()  # 缩下键盘
        self.driver.find_element(*self.comfirm_btn).click()  # 第三步
        time.sleep(1)

    def send_pay_pwd(self, p='123456'):
        """
        注册时输入支付密码
        :return:
        """

        self.driver.find_element(*self.pay_pwd).send_keys(p)
        self.driver.find_element(*self.comfirm_pay_pwd).send_keys(p)
        self.driver.find_element(*self.complete).click()  # 完成
        time.sleep(2)
