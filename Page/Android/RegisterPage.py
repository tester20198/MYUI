from Page.basePage import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class registerPage(Base):
    """
    启动页+注册界面的页面元素
    """

    register_button = (By.ID, "btnSignup")  # 启动页注册按钮
    switch_mobile_register = (By.ID,'tv_menu')  # 切换手机注册
    select_nation_btn = (By.ID, "tv_select_country")  # 国家下拉框
    input_eamil = (By.ID, "et_email")  # 输入邮箱
    input_mobile = (By.ID, "et_phone_number")  # 输入手机号码
    input_login_pwd = (By.ID, "et_login_pass")  # 输入登录密码
    input_pay_pwd = (By.ID, "et_pay_password")  # 输入支付密码
    comfirm_pay_pwd = (By.ID, "et_confirm_pay_password")  # 确认支付密码
    click_verify = (By.XPATH, "//android.widget.TextView[@text='Send']")  # 点击发送验证码
    input_verify = (By.XPATH, "//android.widget.EditText[@text='Input the verification code']")  # 输入验证码
    click_confirm = (By.XPATH, "//android.widget.Button[@text='Confirm']")  # 点击注册提交
    click_service = (By.ID, 'tv_terms_sevice')  # 点击注册服务协议
    click_user = (By.ID, 'tv_terms_user')  # 点击注册用户协议
    click_Login = (By.ID, 'tv_accountLogin')  # 点击注册界面的Login跳转登陆界面
    get_Forgot_password = (By.XPATH,"//android.widget.TextView[@text='Forgot password']")  # 获取忘记密码的文本信息
    get_register_success = (By.XPATH,"//android.widget.TextView[@text='Profile']")  # 注册成功后用户信息中的头像Profile

    def click_register(self):
        """进入注册页面"""
        WebDriverWait(self.driver, 10, 0.5).until(
            EC.text_to_be_present_in_element(self.register_button, u"Sign Up"))
        self.driver.find_element(*self.register_button).click()

    def select_nation(self, nation):
        """选择国家 """
        nation_XPATH = (By.XPATH, f'//android.widget.TextView[contains(@text, "{nation}")]')  # 定位国家
        self.driver.find_element(*self.select_nation_btn).click()
        time.sleep(5)
        while not self.findElement(nation):
            self.swipeUp(duration=150)
            self.swipeUp(duration=150)
        else:
            self.driver.find_element(*nation_XPATH).click()

    def send_loginpwd_paypwd_code(self,loginpwd,paypwd,code):
        """输入登陆密码、支付密码、手机验证码"""
        self.driver.find_element(*self.input_login_pwd).send_keys(loginpwd)
        self.driver.back()
        self.driver.find_element(*self.input_pay_pwd).send_keys(paypwd)
        self.driver.find_element(*self.comfirm_pay_pwd).send_keys(paypwd)
        time.sleep(2)
        # self.Sys_back()
        self.driver.find_element(*self.click_verify).click()  # 点击发送验证码
        time.sleep(2)
        self.driver.find_element(*self.input_verify).send_keys(code)  # 验证码默认2222
        self.swipeUp(duration=1000)
        self.swipeUp(duration=1000)

    def set_payment_password(self,paypwd):
        """设置支付密码"""
        a = self.driver.find_element(*self.input_pay_pwd)
        # ActionChains创建鼠标事件,move_to_element鼠标移动到某个元素,click单击鼠标左键,send_keys发送某个键到当前焦点的元素,perform执行鼠标事件
        action_a = ActionChains(self.driver)
        action_a.move_to_element(a).click().send_keys(paypwd).perform()
        time.sleep(1)
        b = self.driver.find_element(*self.comfirm_pay_pwd)
        action_b = ActionChains(self.driver)
        action_b.move_to_element(b).click().send_keys(paypwd).perform()

    def register_by_mobile(self,nation,mobile,loginpwd,paypwd,code):
        """手机号码注册"""
        time.sleep(2)
        self.driver.find_element(*self.switch_mobile_register).click()  # 切换手机号码方式
        time.sleep(2)
        self.select_nation(nation)
        time.sleep(1)
        self.driver.find_element(*self.input_mobile).send_keys(mobile)  # 输入手机号码
        self.send_loginpwd_paypwd_code(loginpwd,paypwd,code)  # 输入登陆密码、支付密码、验证码

    def register_by_eamil(self,email,loginpwd,paypwd,code):
        """邮箱注册"""
        # self.select_nation(nation)
        time.sleep(1)
        self.driver.find_element(*self.input_eamil).send_keys(email)  # 输入邮箱
        time.sleep(1)
        self.send_loginpwd_paypwd_code(loginpwd,paypwd,code)  # 输入登陆密码、支付密码、验证码

    def click_confirm_button(self):
        """点击注册"""
        self.driver.find_element(*self.click_confirm).click()  # 点击注册
        WebDriverWait(self.driver, 10, 0.5).until(
            EC.text_to_be_present_in_element(self.get_register_success, u"Profile"))
        msg = self.driver.find_element(*self.get_register_success).text  # 注册成功跳转到设置头像界面
        return msg

    def clcik_register_Agreement(self):
        """点击注册界面的注册协议"""

        self.driver.back()
        time.sleep(3)
        self.driver.find_element(*self.click_service).click()
        time.sleep(2)
        self.driver.back()
        self.driver.find_element(*self.click_user).click()
        time.sleep(2)
        self.driver.back()
        self.driver.find_element(*self.click_Login).click()
        time.sleep(2)
        msg = self.driver.find_element(*self.get_Forgot_password).text
        return msg