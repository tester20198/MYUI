from Page.basePage import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Public.other import create_address
import time

Best_wishes = create_address() #随机生成红包祝福语

class ChatPage(Base):
    """
    进入Chat页面
    """

    click_chat = (By.XPATH,"//android.widget.TextView[@text='Chat']") #点击Chat菜单

    Search_nickname =(By.XPATH,"//android.widget.EditText[@text='xSearch']") #首页点击搜索联系人昵称
    select_contacts =(By.XPATH,"//android.view.ViewGroup[@index='0']") #搜索结果中第一人
    input_message =(By.XPATH,"//android.widget.EditText[@index='1']") #输入信息框
    click_enclosure =(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.ImageView') #点击附件按钮
    click_emjoy =(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.ImageView') #点击表情按钮
    click_26_emjoy =(By.XPATH,"//android.widget.ImageView[@index='26']") #选择第26个表情
    click_send_message = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ImageView") # 点击发送信息按钮
    click_send_message1 = (By.CLASS_NAME, "//android.widget.ImageView")  # 点击发送信息按钮
    click_crypto_gift = (By.XPATH, "//android.widget.TextView[@text='Crypto Gift']")  # 点击Crypto Gift进入发红包界面
    click_redpacket_coin =(By.XPATH,"//android.widget.TextView[@index='1']") #点击选择币种
    select_coin_btc = (By.XPATH, "//android.widget.TextView[@text='BTC']")  # 选择BTC
    select_coin_eth = (By.XPATH, "//android.widget.TextView[@text='ETH']")  # 选择ETH
    select_coin_npxs = (By.XPATH, "//android.widget.TextView[@text='NPXS']")  # 选择NPXS
    select_coin_bnb = (By.XPATH, "//android.widget.TextView[@text='BNB']")  # 选择BNB
    input_redpacket_amount =(By.XPATH,"//android.widget.EditText[@text='Please enter amount']") #输入红包金额
    input_redpacket_number =(By.XPATH,"//android.widget.EditText[@text='Please enter number of people']") #输入红包个数
    input_redpacket_best_wishes =(By.XPATH,"//android.widget.EditText[@text='Best wishes']") #输入红包祝福语
    click_send_button =(By.CLASS_NAME,'android.widget.Button') # 点击send发送
    input_pay_password =(By.ID,'ed_pwd') # 输入支付密码
    click_forgot_pay_password =(By.ID,'tv_forget_pwd') # 点击忘记支付密码
    redpacket_status =(By.XPATH,"//android.widget.TextView[@text='View']") #判断发出去的红包状态是否为View
    # open_redpacket =(By.XPATH,"//android.widget.TextView[@text='测试拆红包']") #打开群红包
    open_group_redpacket =(By.XPATH,"//android.widget.Button[@text='Open']") #打开群红包

    #大额红包绑定2FA流程
    click_google_authenticator =(By.XPATH,"//android.widget.Switch[@resource-id='com.pundix.xwallet:id/switch_google_authen']") # 点击谷歌验证器开关
    click_google_confirm =(By.XPATH,"//android.widget.Button[@text='Confirm']") # 确认开启谷歌验证器
    click_send_code =(By.ID,'com.pundix.xwallet:id/tv_send_email_code') # 点击发送验证码
    input_verification_code =(By.XPATH,"//android.widget.EditText[@text='Input the verification code']") # 输入验证码
    click_confirm_button =(By.XPATH,"//android.widget.Button[@text='Confirm']") # 点击提交按钮
    click_backed_up_my_key =(By.ID,'btn_confirm') # 点击I have backed up my key
    input_2FA_verification_code =(By.ID,'et_2fa_code') # 输入2FA谷歌验证码
    click_2FA_paste =(By.ID,'tv_paste') # 点击2FA页面粘贴按钮
    click_2FA_confirm =(By.ID,'btn_confirm') # 点击2FA页面提交按钮Confirm

    #忘记密码流程
    Click_forgot_password =(By.XPATH,"//android.widget.TextView[@text='Forgot payment password?']") #点击忘记密码
    Click_send_email =(By.XPATH,"//android.widget.TextView[@resource-id='com.pundix.xwallet:id/tv_send_email_code']") #点击发送邮箱验证码
    input_email_code =(By.ID,"ed_email_code") #输入邮箱验证码
    Click_send_mobile =(By.ID,"tv_send_sms_code']") #点击发送手机验证码
    input_mobile_code =(By.ID,"ed_sms_code']") #输入手机验证码
    Click_Confirm_button = (By.XPATH, "//android.widget.Button[@text='Confirm']")  # 点击提交按钮
    input_pay_pwd = (By.XPATH, "//android.widget.TextView[@text='Set a 6-digit payment password']")  # 输入支付密码
    input_confirmpay_pwd = (By.XPATH, "//android.widget.TextView[@text='Confirm the payment password']")  # 确认支付密码
    button_confirmpay_pwd = (By.XPATH, "//android.widget.Button[@text='Confirm']")  # 提交

    def Click_chat(self):
        # 进入Chat菜单

        self.driver.find_element(*self.click_chat).click() #点击进入Chat菜单

    def Send_redpacket_default_setting(self,text1,text2):
        '''红包默认配置包括(默认金额、币种、红包祝福语)'''

        r = self.driver.find_element(*self.Search_nickname)  # 输入接收者昵称
        r.click();r.clear();r.send_keys(text1)
        time.sleep(2)
        self.driver.find_element(*self.select_contacts).click()  # 搜索结果中第一个人
        time.sleep(3)
        self.driver.find_element(*self.click_enclosure).click()  # 点击附件按钮
        time.sleep(2)
        self.driver.find_element(*self.click_crypto_gift).click()  # 进入红包界面
        time.sleep(2)
        self.driver.find_element(*self.input_redpacket_amount).send_keys(text2)  # 输入红包金额
        time.sleep(1)
        self.driver.find_element(*self.input_redpacket_best_wishes).send_keys(Best_wishes)  # 输入红包祝福语
        time.sleep(1)

    def Select_redpacket_coin_BTC(self):
        '''选择支付的BTC币种'''

        self.driver.find_element(*self.click_redpacket_coin).click()  # 点击选择币种
        time.sleep(2)
        self.driver.find_element(*self.select_coin_btc).click()  # 选择BTC币种
        time.sleep(1)

    def Select_redpacket_coin_ETH(self):
        '''选择支付的ETH币种'''

        self.driver.find_element(*self.click_redpacket_coin).click()  # 点击选择币种
        time.sleep(2)
        self.driver.find_element(*self.select_coin_eth).click()  # 选择ETH币种
        time.sleep(1)

    def Select_redpacket_coin_NPXS(self):
        '''选择支付的NPXS币种'''

        self.driver.find_element(*self.click_redpacket_coin).click()  # 点击选择币种
        time.sleep(2)
        self.driver.find_element(*self.select_coin_npxs).click()  # 选择NPXS币种
        time.sleep(1)

    def Select_redpacket_coin_BNB(self):
        '''选择支付的BNB币种'''

        self.driver.find_element(*self.click_redpacket_coin).click()  # 点击选择币种
        time.sleep(2)
        self.driver.find_element(*self.select_coin_bnb).click()  # 选择BNB币种
        time.sleep(1)

    def business_processes_2FA(self,text1='2222',text2='222222'):
        '''绑定2FA的流程'''

        self.driver.switch_to.alert.accept()  # 系统弹窗默认允许跳转开启2FA界面
        time.sleep(2)
        self.driver.find_element(*self.click_google_authenticator).click()
        time.sleep(1)
        self.driver.find_element(*self.click_google_confirm).click()
        time.sleep(1)
        self.driver.find_element(*self.click_send_code).click()
        time.sleep(1)
        self.driver.find_element(*self.input_verification_code).send_keys(text1)
        time.sleep(1)
        self.driver.find_element(*self.click_confirm_button).click()
        time.sleep(1)
        self.driver.find_element(*self.click_backed_up_my_key).click()
        time.sleep(1)
        self.driver.find_element(*self.click_2FA_paste).click()
        time.sleep(1)
        self.driver.find_element(*self.input_2FA_verification_code).send_code(text2)
        time.sleep(1)
        self.driver.find_element(*self.click_2FA_confirm).click()

    def business_forgot_payment_password(self,text,text1):
        '''忘记密码支付密码流程'''

        self.driver.find_element(*self.click_send_button).click()  # 点击发送红包按钮
        time.sleep(1)
        self.driver.find_element(*self.Click_forgot_password).click()
        time.sleep(2)
        self.driver.find_element(*self.Click_send_email).click()
        time.sleep(3)
        self.driver.find_element(*self.input_email_code).send_keys(text)
        time.sleep(1)
        self.driver.find_element(*self.Click_Confirm_button).click()
        time.sleep(2)
        a = self.driver.find_element(*self.input_pay_pwd)
        # ActionChains创建鼠标事件,move_to_element鼠标移动到某个元素,click单击鼠标左键,send_keys发送某个键到当前焦点的元素,perform执行鼠标事件
        action_a = ActionChains(self.driver)
        action_a.move_to_element(a).click().send_keys(text1).perform()
        time.sleep(2)
        b = self.driver.find_element(*self.input_confirmpay_pwd)
        action_b = ActionChains(self.driver)
        action_b.move_to_element(b).click().send_keys(text1).perform()
        time.sleep(1)
        self.driver.find_element(*self.button_confirmpay_pwd).click()
        time.sleep(1)

    def Click_Send_redpacket(self,text):
        '''点击发送按钮和输入支付密码'''

        self.driver.find_element(*self.click_send_button).click()  # 点击发送红包按钮
        time.sleep(4)
        self.driver.find_element(*self.input_pay_password).send_keys(text)  # 输入支付密码
        time.sleep(3)

    def judge_redpacket_status(self):
        '''判断发出去的红包状态是否为View'''

        time.sleep(2)
        redpacket_status = self.driver.find_element(*self.redpacket_status).text  #判断发出去的红包状态是否为View
        return redpacket_status

    def Send_personal_redpacket(self,text1,text2):
        '''发送个人红包(小额)'''

        self.Send_redpacket_default_setting(text1,text2)

    def Send_group_redpacket(self,text1,text2,text4):
        '''发送群红包(小额)'''

        self.Send_redpacket_default_setting(text1,text2)
        self.driver.find_element(*self.input_redpacket_number).send_keys(text4)  # 输入红包个数
        time.sleep(1)

    def Open_group_redpacket(self):
        '''打开群红包'''

        # self.driver.find_element(*self.open_redpacket).click() #点击发送的红包
        if self.findElement(Best_wishes):
            self.click2(Best_wishes)
        else:
            self.swipeUp(duration=10000)
        time.sleep(3)
        self.driver.find_element(*self.open_group_redpacket).click()  #打开群红包
        time.sleep(3)
        text = u"Saved to"
        while not self.findElement(text):
            time.sleep(10)
        else:
            return True

    def Send_group_big_redpacket(self,text1,text2,text3,text5='2222',text6='222222'):
        '''发送群红包(大额)'''

        self.Send_group_redpacket(text1,text2,text3)
        self.business_processes_2FA(text5,text6)
        send_redpacket_status = self.driver.find_element(*self.redpacket_status).text  #判断发出去的红包状态是否为View
        return send_redpacket_status

    def Send_group_emjoy_message(self,text1,text2):
        '''发送表情、文字信息'''

        r = self.driver.find_element(*self.Search_nickname)  # 输入接收者昵称
        r.click();r.send_keys(text1)
        time.sleep(2)
        self.driver.find_element(*self.select_contacts).click()  # 搜索结果中第一个人
        time.sleep(1)
        self.driver.find_element(*self.input_message).send_keys(text2) #输入需要发送的文字信息
        time.sleep(1)
        self.driver.find_element(*self.click_send_message1).click()  #发送信息
        time.sleep(1)
        self.driver.find_element(*self.click_emjoy).click()  # 输入需要发送的文字信息
        time.sleep(1)
        self.driver.find_element(*self.click_26_emjoy).click()  # 发送信息
        time.sleep(1)
        self.driver.find_element(*self.click_send_message).click()  # 发送信息
