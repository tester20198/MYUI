from PO.basePage import Base
from selenium.webdriver.common.by import By
import time


class DappFxPage(Base):
    """
    Dapp FX页面元素
    """


    # Android#
    # -------DApp列表元素------------
    Dapp = "DApp"  # 点击卡片DApp标题
    Dapp_enter_fx_card = "FX"  # 点击fxcard
    Dapp_add_card_btn = (By.ID, "ib_add_card")  # 添加卡片按钮
    Dapp_show_amout = (By.ID, "img_show_amout")  # 加密按钮
    fx_card_btn= (By.XPATH,"//android.widget.LinearLayout[@resource-id='com.pundix.xwallet:id/ll_layout_balance']") #点击进入fx卡

    # ----------fx卡片主界面元素---------------
    fx_amout = (By.ID, "tv_amout")  # fx卡片里面的加密按钮
    fx_setting = (By.ID, "iv_setting")  # fx卡片里面的设置按钮
    fx_back_btn = (By.CLASS_NAME, "android.widget.ImageButton")  # fx卡片里面的左上角返回键
    fx_conversion_btn = "Conversion"  # 转换按钮
    fx_staking_btn = "Staking"  # 挖矿按钮
    fx_main_btn =(By.XPATH,"//android.widget.TextView[@text='FX']")# fx按钮
    fx_NPXS_btn = (By.XPATH,"//android.widget.TextView[@text='NPXS']")  # npxs按钮
    fx_NPXSXEM_btn = (By.XPATH,"//android.widget.TextView[@text='NPXSXEM']")  # npxsxem按钮

    # ---------转换功能界面元素-------------
    conver_option_btn = (By.ID, "option")  # 帮助按钮

    # ---------staking功能的界面元素-------
    staking_option_btn = (By.ID, "option")  # 挖矿界面右上角的更多按钮
    staking_Guide = (By.ID, "option1")  # 挖矿界面guide按钮
    staking_history = (By.ID, "option2")  # 挖矿界面staking history按钮
    staking_startTime = (By.ID, "startTime")  # 挖矿开始时间
    staking_endTime = (By.ID, "endTime")  # 挖矿结束时间
    staking_startTime_cancle = (By.ID, "cancle")  # 取消时间按钮
    staking_finish = (By.ID, "tv_finish")  # 确定时间按钮
    staking_option2 = (By.ID, "option")  # 挖矿帮助按钮
    staking_shart = (By.ID, "option3")  # 挖矿界面分享按钮
    staking_pwCancel = (By.ID, "tv_pwCancel")  # 取消分享按钮
    staking_cancle = (By.ID, "cancle")  # 取消按钮

    # -----------fx转账界面元素----------
    fx_page_transfer = (By.ID, "btn_withdraw")  # 转账按钮
    fx_type_name = (By.ID, "tv_type_name")  # 账单名称
    fx_transferAddress=(By.ID,"ed_transferAddress")#fx转账地址
    fx_coinNumber=(By.ID,"ed_transferCoinNumber")#输入金额框
    # 扫码按钮
    fx_sacn = (By.XPATH,
               "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.ImageView")
    fx_all = (By.ID, "tv_allCoinNumber")  # all按钮
    fx_transferNext = (By.ID, "btn_transferNext")  # 第一个fx界面的下一步按钮
    fx_withdrawNext=(By.ID,"btn_withdrawNext1")   #第二个fx'转账的下一步按钮
    fx_email_code=(By.ID,"ed_email_code")#邮箱验证码
    fx_pay_password=(By.ID,"ed_pay_password") #输入支付密码
    fx_send_emai_code=(By.ID,"tv_send_email_code")  #点击发送验证码
    fx_confirm=(By.ID,"btn_confirm") #点击确认按钮
    fx_bill=(By.XPATH,"//android.widget.TextView[contains(@text,'Distribution')")#fx账单名称

    # ------------NPXS界面元素------------
    npxs_help_menu = (By.ID, "iv_menu")  # 帮助按钮
    npxs_transfer = (By.ID, "btn_transfer")  # NPXS转账
    npxs_add = (By.ID, "rl_layout_add")  # add按钮
    npxs_private = (By.ID, "ll_layout_private")  # private wallet account
    npxs_exchange = (By.ID, "iv_exchange")  # 切换按钮
    npxs_all = (By.ID, "tv_available_all")  # 全部按钮
    npxs_confirm = (By.ID, "btn_transfer")  # 确认转账按钮
    npxs_input_amount=(By.ID,"ed_available")#内部转账金额输入框

    # ---------NPXSXEM界面元素------------
    npxsxem_menu = (By.ID, "iv_menu")  # 帮助按钮
    npxsxem_view = (By.ID, "btn_transfer")  # view按钮
    npxsxem_add = (By.ID, "iv_add_icon")  # add按钮
    npxsxem_account = (By.ID, "ll_layout_private")  # npxsxem account记录
    npxsxem_receive = (By.ID, "btn_recharge")  # receive按钮
    npxsxem_transfer = (By.ID, "btn_withdraw")  # transfer按钮
    npxsxem_payinfo = (By.ID, "rl_layout_payinfo")  # 账单记录
    npxsxem_select_agree = (By.ID, "cb_select_agree")  # 同意复选框
    npxsxem_view_address = (By.ID, "btn_view_recharge")  # view address按钮
    npxsxem_close = (By.ID, "iv_close")  # 关闭按钮
    npxsxem_address_QRcode = (By.ID, "btn_many_get_address")  # Address QR code按钮
    npxsxem_copy_address = (By.ID, "btn_many_copy_address")  # copy address按钮
    npxsxem_message_QRcode = (By.ID, "btn_many_get_message")  # message QR code按钮
    npxsxem_copy_message = (By.ID, "btn_many_copy_message")  # copy message按钮
    npxsxem_recipient_address = (By.ID, "ed_transferAddress")  # recipient address输入框
    npxsxem_amount = (By.ID, "ed_transferCoinNumber")  # amount输入框
    npxsxem_message = (By.ID, "ed_transfer_msg")  # message输入框
    npxsxem_transfer_next = (By.ID, "btn_transferNext")  # 下一步按钮


    def enter_dapp(self):
        """
        点击DAPP按钮
        """
        # self.driver.find_element(*self.Dapp).click()
        self.click2("DApp")
        time.sleep(2)

    def add_fxcard(self):
        """
        添加fx卡片
        """
        card_btn = self.driver.find_element(*self.Dapp_add_card_btn)
        print("131232131231231231232")
        while not self.findElement(card_btn):
            print("131232131231231231232")
            self.swipeDown(duration=1000)
            time.sleep(2)

        else:
            self.driver.find_element(*self.Dapp_add_card_btn).click()

    def enter_fx_setting(self):
        """
        点击fx卡片的设置按钮
        """
        self.driver.find_element(*self.fx_setting).click()
        time.sleep(2)

    def click_fx_text(self):
        """
        点击转换按钮
        :return:
        """
        self.driver.find_element(*self.fx_conversion_btn)

    def enter_conversion(self):
        """
        进入转换的帮助按钮
        """
        self.driver.find_element(*self.fx_conversion_btn).click()

    def Dapp_enter_fx(self):
        """从Dapp界面进入fx转账界面"""

        self.driver.find_element(*self.fx_card_btn).click()  # 点击DAPP界面的fx按钮
        time.sleep(2)
    def enter_fx(self):
        """点击fx卡片界面的fx按钮"""
        self.driver.find_element(*self.fx_main_btn).click() #点击fx卡片的fx按钮
        time.sleep(2)

    def fx_transfer(self,text,text2,text3,text4):
        """
        fx转账
        """
        self.driver.find_element(*self.fx_page_transfer).click()#点击转账按钮
        time.sleep(2)

        fx_address = self.driver.find_element(*self.fx_transferAddress)#点击fx转账地址
        fx_address.click();time.sleep(2);fx_address.send_keys(text) #输入转账地址
        time.sleep(2)

        fx_amount=self.driver.find_element(*self.fx_coinNumber)#点击转账金额输入框
        fx_amount.click();fx_amount.send_keys(text2)#输入金额
        #coinNumber = self.driver.find_element(*self.fx_all).click()#点击all按钮
        # coinNumber.clear()
        # coinNumber.send_keys(text1)
        time.sleep(2)
        self.driver.back()
        time.sleep(1)
        self.driver.find_element(*self.fx_transferNext).click()#点击第一个界面的下一步按钮
        time.sleep(2)
        self.driver.find_element(*self.fx_withdrawNext).click()#点击第二个界面的下一步按钮
        time.sleep(2)
        self.driver.find_element(*self.fx_send_emai_code).click()#点击发送验证码
        time.sleep(2)
        email_code =self.driver.find_element(*self.fx_email_code)#点击邮箱验证码输入框
        email_code.click();email_code.send_keys(text3)
        time.sleep(2)

        pay_password=self.driver.find_element(*self.fx_pay_password) #点击支付密码
        pay_password.click();pay_password.send_keys(text4)#输入支付密码
        time.sleep(3)
        self.driver.find_element(*self.fx_confirm).click()#点击确认转账按钮
        time.sleep(2)

    def enter_fx_bill(self):
        """进入fx账单界面"""
        self.driver.page_source()
        msg = self.driver.find_element(*self.fx_bill).text
        #webdriver.Remote().find_element_by_id().is


        print(msg.get_attribute)
        print(msg.page_source)
        time.sleep(1)
        return msg

    def enter_NPXSPage(self):
        """进入npxs界面"""
        self.driver.find_element(*self.fx_NPXS_btn).click()
        time.sleep(2)

    def enter_NPXSXEMPage(self):
        """进入npxsxem界面"""
        self.driver.find_element(*self.fx_NPXSXEM_btn).click()
        time.sleep(2)

    def enter_NPXS_helpBtn(self):
        """进入npxs界面的帮助按钮"""
        self.driver.find_element(*self.npxs_help_menu).click()
        time.sleep(2)

    def enter_NPXS_transfer(self):
        """点击npxs界面的transfer按钮"""
        self.driver.find_element(*self.npxs_transfer).click()
        time.sleep(2)

    def enter_NPXS_Add(self):
        """点击npxs界面的add按钮"""
        self.driver.find_element(*self.npxs_add).click()

    def click_transfer_exchange(self):
        """点击npxs内部划转的切换按钮"""
        self.driver.find_element(*self.npxs_exchange).click()
        time.sleep(1)

    def click_all_Internal_transfer(self):
        """点击内部转账的all按钮"""
        self.driver.find_element(*self.npxs_all).click()
        time.sleep(1)

    def input_Internal_transfer_amount(self,text):
        """输入内部划转金额"""
        self.driver.find_element(*self.npxs_input_amount).click()
        time.sleep(2)

        npxs_amount=self.driver.find_element(*self.npxs_input_amount)#在内部转账界面输入金额
        npxs_amount.click();npxs_amount.send_keys(text)#输入金额
        time.sleep(2)

        self.driver.find_element(*self.npxs_confirm).click()#点击确认按钮
        time.sleep(1)
