from PO.basePage import Base
from selenium.webdriver.common.by import By
import time

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
    select_coin_npxs = (By.XPATH, "//android.widget.TextView[@text='ETH']")  # 选择ETH
    input_redpacket_amount =(By.XPATH,"//android.widget.EditText[@text='Please enter amount']") #输入红包金额
    input_redpacket_number =(By.XPATH,"//android.widget.EditText[@text='Please enter number of people']") #输入红包个数
    input_redpacket_best_wishes =(By.XPATH,"//android.widget.EditText[@text='Best wishes']") #输入红包祝福语52076
    click_send_button =(By.CLASS_NAME,'android.widget.Button') # 点击send发送
    input_pay_password =(By.ID,'ed_pwd') # 输入支付密码
    click_forgot_pay_password =(By.ID,'tv_forget_pwd') # 点击忘记支付密码
    redpacket_status =(By.XPATH,"//android.widget.TextView[@text='View']") #判断发出去的红包状态是否为View
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

    def Click_chat(self):
        # 进入Chat菜单

        self.driver.find_element(*self.click_chat).click() #点击进入Chat菜单

    def Send_redpacket_default_setting(self,text1,text2,text3):
        '''红包默认配置包括(默认金额、币种、红包祝福语)'''

        r = self.driver.find_element(*self.Search_nickname)  # 输入接收者昵称
        r.click();r.send_keys(text1)
        time.sleep(2)
        self.driver.find_element(*self.select_contacts).click()  # 搜索结果中第一个人
        time.sleep(2)
        self.driver.find_element(*self.click_enclosure).click()  # 点击附件按钮
        time.sleep(1)
        self.driver.find_element(*self.click_crypto_gift).click()  # 进入红包界面
        time.sleep(1)
        self.driver.find_element(*self.click_redpacket_coin).click()  # 点击选择币种
        time.sleep(2)
        self.driver.find_element(*self.select_coin_npxs).click()  # 选择NPXS币种
        time.sleep(1)
        self.driver.find_element(*self.input_redpacket_amount).send_keys(text2)  # 输入红包金额
        time.sleep(1)
        self.driver.find_element(*self.input_redpacket_best_wishes).send_keys(text3)  # 输入红包祝福语
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

    def Send_personal_redpacket(self,text1,text2,text3,text4='123456'):
        '''发送个人红包(小额)'''

        self.Send_redpacket_default_setting(text1,text2,text3)
        self.driver.find_element(*self.click_send_button).click()  # 点击发送红包按钮
        time.sleep(1)
        self.driver.find_element(*self.input_pay_password).send_keys(text4)  # 输入支付密码
        time.sleep(3)
        redpacket_status = self.driver.find_element(*self.redpacket_status).text  #判断发出去的红包状态是否为View
        return redpacket_status

    def Send_group_redpacket(self,text1,text2,text3,text4,text5='123456'):
        '''发送群红包(小额)'''

        self.Send_redpacket_default_setting(text1,text2,text3)
        self.driver.find_element(*self.input_redpacket_number).send_keys(text4)  # 输入红包个数
        time.sleep(1)
        self.driver.find_element(*self.click_send_button).click()  # 点击发送红包按钮
        time.sleep(1)
        self.driver.find_element(*self.input_pay_password).send_keys(text5)  # 输入支付密码
        time.sleep(1)

    def Open_group_redpacket(self):
        '''打开群红包'''

        send_redpacket_status = self.driver.find_element(*self.redpacket_status).text  # 判断发出去的红包状态是否为View
        self.driver.find_element(*self.redpacket_status).click() #点击发送的红包
        time.sleep(3)
        self.driver.find_element(*self.open_group_redpacket).click()  #打开群红包
        text = u"Saved to Virtual Card"
        while not self.findElement(text):
            time.sleep(2)
        else:
            return True
        self.driver.back()
        return send_redpacket_status

    def Send_group_big_redpacket(self,text1,text2,text3,text4,text5='123456',text6='2222',text7='222222'):
        '''发送群红包(大额)'''

        self.Send_group_redpacket(text1,text2,text3,text4,text5)
        self.business_processes_2FA(text6,text7)
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