from Page.basePage import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class DappOpenCardPage(Base):
    """
    Dapp-开放平台卡片
    """
    click_dapp = (By.XPATH, "//android.widget.TextView[@text='DApp']")  # 点击dapp标题
    get_balance_text = (By.XPATH, "//android.widget.TextView[@text='Balance']")  #获取Dapp页面Balance的文本信息
    add_card = (By.ID, "ib_add_card")  # 添加卡片按钮

    # 添加开放平台卡片、app
    add_open_card = (By.XPATH, "//android.widget.TextView[@text='Virtual Card']")  # 添加开放平台卡片
    select_Virtual_card = (By.ID, "btnVirtual")  # 添加开放平台卡片时，选择添加虚拟卡
    select_Physical_card = (By.ID, "btnPhysical")  # 添加开放平台卡片时，选择添加物理卡片
    #实体卡
    Add_XPASS_No = (By.ID, "ed_addCardXpassNO")  # 输入XPASS卡号输入框
    Add_XPASS_Next = (By.ID, "btn_addCardNext")  # 输入卡号后下一步按钮
    Add_XPASS_6pin_code = (By.ID, "ed_cardBackPassword")  # 输入6位密码
    Add_XPASS_confirm = (By.ID, "btn_cardPwFinish")  # 最后一步确认按键

    click_open_card_Pay = (By.XPATH,"//android.widget.TextView[@text='Pay']")  # 点击Pay按钮
    click_open_card_Transfer = (By.XPATH,"//android.widget.TextView[@text='Transfer']")  # 点击Transfer按钮

    # 卡片详情页面
    click_eye = (By.ID, "tv_amout")  # 加密按钮
    click_setting = (By.ID, "iv_setting")  # 设置按键
    get_card_setting_title = (By.ID, "tv_title")  # 获取标题文本
    click_bills = (By.ID, "iv_bills")  # 账单按键
    # click_open_card_Pay1 = (By.XPATH, "//android.widget.TextView[@text='XEM']")  # 点击进入卡片详情页面
    click_open_card_token = (By.ID, "tv_currency")  # 卡片详情页面点击币种
    click_Website = (By.XPATH, "//android.widget.TextView[@text='Website']")  # 点击开发者网站

    click_Menu = (By.XPATH, "//android.widget.ImageView[@resource-id='com.pundix.xwallet:id/iv_menu']")  # 点击付款码界面右上角的说明入口
    click_Internal_Transfer = (By.ID, "tv_refresh")  # 点击内部划转
    click_Instructions = (By.ID, "tv_help")  # 点击帮助说明
    click_Cancel = (By.ID, "tv_cancel")  # 点击取消

    # Google认证提示
    Google_Notnow = (By.ID, "btn_no")  # Google认证时，选择Not Now
    Google_confirm = (By.ID, "btn_yes")  # google认证时，选择confirm

    Payment_code = (By.ID, "iv_qr_code")  # 二维码
    click_receive = (By.ID, "btn_recharge")  # Receive充值地址
    click_transfer = (By.ID, "btn_withdraw")  # Transfer转账地址
    click_refresh = (By.ID, "iv_refresh")  # Refresh二维码刷新按键
    click_Transaction_history = (By.ID, "rl_layout_payinfo")  # 账单中第一条记录
    history = (By.XPATH, "//android.widget.TextView[@resource-id='com.pundix.xwallet:id/tv_hint_text']")

    click_view_Address = (By.ID, "btn_view_recharge")  # 查看充值地址，提醒页面
    Receiving_address_close = (By.ID, "iv_close")  # 查看充值地址说明页面的关闭按钮
    click_copy_address = (By.ID, "btn_single_copy")  # 复制充值地址
    receive_address_code = (By.ID, "iv_single_qr_code")  # 复制充值地址

    #转账
    input_transfer_Address = (By.ID, "ed_receivingAddress")  # 输入转账地址
    input_amount = (By.ID, "ed_coinNumber")  # 输入金额框
    click_all = (By.ID, "tv_allCoinNumber")  # all按钮
    click_next= (By.ID, "btn_withdraw")  # 第一个界面下一步按钮
    click_next2 = (By.ID, "btn_withdrawNext1")  # 第二个界面转账的下一步按钮
    send_email_code = (By.ID, "ed_email_code")  # 发送邮箱验证码
    input_email_code = (By.ID, "tv_send_email_code")  # 输入邮箱验证码
    input_pay_password = (By.ID, "ed_pay_password")  # 输入支付密码
    click_confirm = (By.ID, "btn_confirm")  # 点击确认按钮
    get_bill = (By.XPATH, "//android.widget.TextView[contains(@text,'Distribution')")  # fx账单名称

    #内部划转
    click_Internal_Transfer_all =(By.ID,'tv_available_all')
    click_Internal_Transfer_Confirm =(By.ID,'btn_transfer')

    def dapp_page(self):
        '''进入dapp页面'''

        WebDriverWait(self.driver, 10, 0.5).until(EC.text_to_be_present_in_element(self.get_balance_text,u'Balance'))  #获取Dapp页面Balance
        self.driver.find_element(*self.click_dapp).click()  # 进入dapp页面

    def add_card_buisess(self,cardname):
        '''添加卡片流程'''

        self.swipeUp(duration=1500)
        self.swipeUp(duration=1500)
        self.driver.find_element(*self.add_card).click()  # 点击添加按钮
        time.sleep(2)
        Virtual_Card = (By.XPATH, f'//android.widget.TextView[contains(@text, "{cardname}")]')  # 进入添加卡片列表界面定位虚拟卡
        while not self.findElement(cardname):
            self.swipeUp(duration=1500)
            self.swipeUp(duration=1500)
        else:
            self.driver.find_element(*Virtual_Card).click()

    def add_virtual_card(self):
        '''添加虚拟卡'''

        time.sleep(3)
        self.swipeUp()
        if self.driver.find_element(*self.select_Virtual_card).is_enabled():  # 添加虚拟卡
            self.driver.find_element(*self.select_Virtual_card).click()
            msg = self.is_toast_exist(u'Added successfully', 10, 0.5)
            return msg
        else:
            pass

    def add_physical_card(self,num,pin):
        '''添加实体卡'''

        time.sleep(1)
        self.driver.find_element(*self.Add_XPASS_No).send_keys(num)
        time.sleep(1)
        self.driver.find_element(*self.Add_XPASS_Next).click()
        if self.is_toast_exist('not found'):
            print(f'卡号{num}没找到，请输入正确的卡号')
        elif self.is_toast_exist('activitied'):
            print(f'卡号{num}未被激活，请先激活...')
        else:
            self.driver.find_element(*self.Add_XPASS_6pin_code).send_keys(pin)
            print(pin)
            self.driver.find_element(*self.Add_XPASS_confirm)
            if self.is_toast_exist('already'):
                print(f'该{num}已被添加过！')
            elif self.is_toast_exist('password'):
                print(f'卡号的密码{pin}不对')
            else:
                time.sleep(1)
                return True

    def card_details(self,cardname):
        '''卡片详情界面'''
        self.swipeDown(duration=1000)
        time.sleep(2)
        self.click2(cardname) # 进入卡片详情
        time.sleep(1)
        self.driver.find_element(*self.click_open_card_token).click()
        time.sleep(4)

    def card_details_page(self,cardname):
        '''卡片详情页面——加密、设置按钮、账单、开发者网站'''

        self.swipeDown(duration=1500)
        time.sleep(2)
        self.click2(cardname)
        time.sleep(1)
        # self.driver.find_element(*self.click_open_card_Pay1).click() #进入卡片详情
        self.driver.find_element(*self.click_eye).click() #点击加密按钮
        self.driver.find_element(*self.click_setting).click() #点击设置按钮
        time.sleep(2)
        msg = self.driver.find_element(*self.get_card_setting_title).text #获取标题文本
        self.driver.back()
        self.driver.find_element(*self.click_bills).click() #点击账单按键
        time.sleep(2)
        msg1 = self.driver.find_element(*self.get_card_setting_title).text  # 获取标题文本
        self.driver.back()
        self.driver.find_element(*self.click_Website).click()  # 点击开发者网站
        time.sleep(3)
        msg2 = self.driver.find_element(*self.get_card_setting_title).text  # 获取标题文本
        return msg,msg1,msg2  #返回的标题为msg = Card Settings;msg1 = Transactions

    def click_pay_button(self):
        '''进入二维码界面'''

        self.driver.find_element(*self.click_open_card_Pay).click()  # 进入二维码界面

    def check_receive_code(self):
        """检查是否加载付款二维码是否正确"""

        time.sleep(2)
        if self.driver.find_element(*self.Payment_code).is_enabled():  # 判断充值二维码是否可用
            return True
        else:
            return False

    def check_receive_address(self):
        """查看充值地址"""

        self.driver.find_element(*self.click_receive).click()  # 点击Receving
        time.sleep(2)
        self.driver.find_element(*self.click_view_Address).click()  # 弹出"View address"提示
        time.sleep(2)
        self.driver.find_element(*self.click_copy_address).click()  # 复制充值地址
        if self.driver.find_element(*self.receive_address_code).is_enabled():  # 判断充值二维码是否可用
            return True
        else:
            return False

    def transfer_buisess(self,text,text1,text2,text3,cardname):
        '''转账流程'''

        self.driver.find_element(*self.click_transfer).click()
        time.sleep(3)
        # 首次点击转账，弹出是否开启2FA，默认不开启
        switch = 0
        if switch == 0:  # 不开启2FA
            if self.findElement('Not Now'):
                self.driver.find_element(*self.Google_Notnow).click()
                time.sleep(1)
            else:
                pass
        else:  # 开启2FA
            if self.findElement('Not Now'):
                self.driver.find_element(*self.Google_confirm).click()
                time.sleep(2)
            else:
                pass
        time.sleep(1)
        self.driver.find_element(*self.click_transfer).click()
        time.sleep(4)
        self.driver.find_element(*self.input_transfer_Address).send_keys(text)
        self.driver.find_element(*self.input_amount).send_keys(text1)
        time.sleep(1)
        self.driver.find_element(*self.click_next).click()
        if self.is_toast_exist(f'Max. transfer amount0.00000000{cardname}'):
            return True
        else:
            self.driver.find_element(*self.click_next2).click()
            time.sleep(2)
            self.driver.find_element(*self.send_email_code).click()
            time.sleep(2)
            self.driver.find_element(*self.input_email_code).send_keys(text2)
            time.sleep(2)
            self.driver.find_element(*self.input_pay_password).send_keys(text3)
            self.driver.find_element(*self.click_confirm).click()
            time.sleep(2)
            msg1 = self.is_toast_exist(u'Transfer successful')
            return msg1

    def Internal_Transfer(self):
        '''内部划转'''

        self.driver.find_element(*self.click_Menu).click()
        time.sleep(1)
        self.driver.find_element(*self.click_Internal_Transfer).click()
        time.sleep(4)
        self.driver.find_element(*self.click_Internal_Transfer_all).click()
        time.sleep(1)
        self.driver.find_element(*self.click_Internal_Transfer_Confirm).click()
        time.sleep(1)
        return self.is_toast_exist("Please enter correct amount" or "Recipient's card does not support this coin")

    def click_help(self):
        '''帮助说明、取消'''

        self.driver.find_element(*self.click_Menu).click()
        time.sleep(1)
        self.driver.find_element(*self.click_Instructions).click()
        time.sleep(1)
        msg = self.driver.find_element(*self.get_card_setting_title).text  # 获取标题文本
        self.driver.back()
        self.driver.find_element(*self.click_Menu).click()
        time.sleep(1)
        self.driver.find_element(*self.click_Cancel).click()
        return msg

    def Transaction_history(self):
        '''账单历史记录'''

        self.swipeUp()
        if self.findElement('No data'):
            pass
        else:
            self.driver.find_element(*self.click_Transaction_history).click()
            time.sleep(3)

