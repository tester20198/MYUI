from PO.basePage import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class LoginPage(Base):
    """
    启动页+登录界面的页面元素
    """

    click_login = (By.ID, "btnSignIn")  # 启动页的登录按钮
    edit_email = (By.ID, "et_emailSignIn")  # 邮箱输入框
    edit_mobile = (By.ID, "et_login_mobile")  # 手机输入框
    edit_pwd = (By.ID, "et_login_pass")  # 登录密码
    login_btn = (By.ID, "btn_login")  #  登录按钮
    switch_btn = (By.ID, "tv_switch")  # 切换登录方式按钮
    select_nation_btn = (By.ID, "tv_encrytionType")  # 登陆国家下拉框
    Forgot_password_select_nation = (By.ID, 'tv_select_country')  #忘记登陆密码国家下拉框
    back = (By.ID, "//android.widget.ImageButton[@index='0']")  # 登录页面的返回按钮

    #登陆界面的Sign Up 按钮
    click_SignUp = (By.XPATH,'//android.widget.TextView[@text="Sign Up"]')  # 点击登陆界面的Sign Up跳转注册界面
    get_payment_password = (By.XPATH, "//android.widget.TextView[@text='Payment password']")  # 获取支付密码的文本信息

    #工单系统help_and_feedback
    click_help_and_feedback = (By.ID, "tv_menu")  # 点击工单系统help_and_feedback
    click_FAQ = (By.XPATH,"//android.widget.TextView[@text='FAQ']")  # 点击FAQ目录
    click_Support_and_Feedback = (By.XPATH,"//android.widget.TextView[@text='Support and Feedback']")  # 点击Support and Feedback目录
    click_Disclaimer = (By.XPATH,"//android.widget.TextView[@text='Disclaimer']")  # 点击Disclaimer目录
    get_page_title = (By.XPATH,"//android.widget.TextView[@index='1']")  # 获取点击工单目录后的页面标题

    #忘记密码流程
    click_Forgot_password = (By.XPATH, "//android.widget.TextView[@text='Forgot password']")  # 点击忘记密码
    input_Email_address = (By.XPATH, "//android.widget.EditText[@text='Input an Email address']")  # 输入邮箱
    input_Mobile_address = (By.ID, "et_phone_number")  # 输入手机号码
    click_send_verify_code = (By.XPATH, "//android.widget.TextView[@text='Send']")  # 点击发送验证码
    input_verify_code = (By.XPATH, "//android.widget.EditText[@text='Input the verification code']")  # 输入验证码
    click_Next = (By.ID, "btn_forget")  # 点击下一步
    input_login_pwd = (By.ID, "et_login_pass")  # 输入登录密码
    input_confirm_login_pwd = (By.ID, "et_login_pass_again")  # 确认登录密码
    click_ok =(By.ID,'bt_setting_pass_finish') #点击ok

    #登陆后个人中心
    get_balance_text =(By.XPATH,"//android.widget.TextView[@text='Balance']") #登陆成功后，获取Dapp页面Balance的文本信息
    center = (By.ID, "iv_user_icon")  # 个人中心
    setting = (By.ID, "rl_layout_setting")  # 个人中心的设置
    logout = (By.ID, "tv_loginout")  # 退出登录
    confirm_logout = (By.ID, "button1")  # 确认退出登录

    def check_in(self):
        """启动页选择登录"""

        WebDriverWait(self.driver, 10, 0.5).until(
            EC.text_to_be_present_in_element(self.click_login, u"LOG IN"))
        self.driver.find_element(*self.click_login).click()

    def switch_login(self):
        """切换登录方式"""

        self.driver.find_element(*self.switch_btn).click()

    def select_nation(self, na):
        """手机登录--选择国家"""

        nation_XPATH = (By.XPATH, f'//android.widget.TextView[contains(@text, "{na}")]')  # 定位国家

        self.driver.find_element(*self.select_nation_btn).click()
        time.sleep(5)
        while not self.findElement(na):
            self.swipeUp(duration=1500)
            self.swipeUp(duration=1500)
        else:
            self.driver.find_element(*nation_XPATH).click()

    def login_by_Email(self, email, pwd):
        """使用邮箱登录"""

        time.sleep(1)
        self.driver.find_element(*self.edit_email).send_keys(email)
        self.log_in(pwd)
        time.sleep(6)
        self.telegram_skip()

    def login_by_Mobile(self, mobile, pwd, na=None):
        """使用手机登录"""

        self.switch_login() #切换登录方式
        time.sleep(2)
        self.select_nation(na)  # 选择国家
        time.sleep(1)
        self.driver.find_element(*self.edit_mobile).send_keys(mobile)
        self.log_in(pwd)

    def log_in(self,pwd):
        """点击登录页面的登录按钮"""

        self.driver.find_element(*self.edit_pwd).send_keys(pwd) #输入登陆密码
        self.driver.find_element(*self.login_btn).click() #点击登陆

    def Dapp_balance_text(self):
        '''登陆成功后，获取Dapp页面Balance的文本信息'''

        time.sleep(6)
        if self.findElement("Skip"):
            self.click2('Skip')   # 登录成功后，点击红包引导界面的"跳过"按钮
            time.sleep(2)
        else:
            pass
        WebDriverWait(self.driver, 10, 0.5).until(
            EC.text_to_be_present_in_element(self.get_balance_text, u"Balance"))  # 登陆后获取Dapp页面Balance
        msg = self.driver.find_element(*self.get_balance_text).text  # 登陆后获取Dapp页面Balance
        return msg

    def enter_usercenter(self):
        """进入个人中心"""

        self.driver.find_element(*self.center).click()

    def log_out(self):
        """退出登录"""

        self.driver.find_element(*self.center).click()
        time.sleep(3)
        self.driver.find_element(*self.setting).click()
        self.driver.find_element(*self.logout).click()
        self.driver.switch_to.alert.accept()  # 系统弹窗默认允许
        # self.driver.find_element(*self.confirm_logout).click()

    def click_loginpage_SignUp(self):
        """点击登录页面的注册按钮"""

        self.driver.find_element(*self.click_SignUp).click() # 点击登陆界面的Sign Up跳转注册界面
        time.sleep(2)
        msg = self.driver.find_element(*self.get_payment_password).text  # 获取支付密码的文本信息
        return msg

    def business_forgot_password(self,text1,text2):
        '''忘记密码流程（点击发送验证码、输入验证码、下一步、新的登陆密码'''

        self.driver.find_element(*self.click_send_verify_code).click()
        time.sleep(2)
        self.driver.find_element(*self.input_verify_code).send_keys(text1)
        time.sleep(1)
        self.driver.find_element(*self.click_Next).click()
        time.sleep(1)
        self.driver.find_element(*self.input_login_pwd).send_keys(text2)
        time.sleep(1)
        self.driver.find_element(*self.input_confirm_login_pwd).send_keys(text2)
        time.sleep(1)
        self.driver.find_element(*self.click_ok).click()

    def Email_Forgot_password(self,text,text1,text2):
        '''单邮箱忘记密码，默认方式'''

        self.driver.find_element(*self.click_Forgot_password).click()
        time.sleep(3)
        self.driver.find_element(*self.input_Email_address).send_keys(text)
        time.sleep(1)
        self.business_forgot_password(text1,text2)
        time.sleep(3)
        msg = self.driver.find_element(*self.login_btn).text  # 重置成功后，获取登陆界面的Log in按钮文本信息
        return msg

    def Mobile_Forgot_password(self,text,text1,text2,na=None):
        '''单手机忘记密码'''

        self.driver.find_element(*self.click_Forgot_password).click()
        time.sleep(1)
        self.switch_login()  # 切换登录方式
        time.sleep(1)
        nation_XPATH = (By.XPATH, f'//android.widget.TextView[contains(@text, "{na}")]')  # 定位国家

        self.driver.find_element(*self.Forgot_password_select_nation).click()
        time.sleep(3)
        while not self.findElement(na):
            self.swipeUp(duration=1500)
        else:
            self.driver.find_element(*nation_XPATH).click()
        time.sleep(1)
        self.driver.find_element(*self.input_Mobile_address).send_keys(text)
        time.sleep(1)
        self.business_forgot_password(text1,text2)
        time.sleep(3)
        msg = self.driver.find_element(*self.login_btn).text  # 重置成功后，获取登陆界面的Log in按钮文本信息
        return msg

    def help_and_feedback(self):
        '''工单系统界面'''

        self.driver.find_element(*self.click_help_and_feedback).click()  # 点击工单系统help_and_feedback
        time.sleep(2)
        self.driver.find_element(*self.click_FAQ).click()  # 点击FAQ目录
        time.sleep(2)
        msg = self.driver.find_element(*self.get_page_title).text  # 获取点击工单目录后的页面标题
        self.driver.back()
        self.driver.find_element(*self.click_Support_and_Feedback).click()  # 点击Support and Feedback目录
        time.sleep(2)
        msg1 = self.driver.find_element(*self.get_page_title).text  # 获取点击工单目录后的页面标题
        self.driver.back()
        self.driver.find_element(*self.click_Disclaimer).click()  # 点击Disclaimer目录
        time.sleep(2)
        msg2 = self.driver.find_element(*self.get_page_title).text  # 获取点击工单目录后的页面标题
        self.driver.back()
        return msg,msg1,msg2  # 返回为FAQ、Support and Feedback、Disclaimer

    def telegram_skip(self):
        """关闭telegram引导图"""

        if self.findElement('Skip'):  # 关闭telegram引导图
            self.click2('Skip')
        else:
            pass
