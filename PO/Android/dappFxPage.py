from PO.basePage import Base
from selenium.webdriver.common.by import By
import time
from appium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DappFxPage(Base):
    """
    Dapp FX页面元素
    """
    text = 'FX'
    # Android#
    # -------DApp列表元素------------
    urgent_news=(By.ID,"tv_notice")#紧急消息
    Dapp = (By.XPATH,"//android.widget.TextView[@resource-id='android.widget.TextView' and @text='FX']")  # 点击卡片DApp标题
    click_dapp = (By.XPATH, "//android.widget.TextView[@text='DApp']")  # 点击dapp标题
    get_balance_text = (By.XPATH, "//android.widget.TextView[@text='Balance']")  # 获取Dapp页面Balance的文本信息
    Dapp_enter_fx_card = "FX"  # 点击fxcard
    Dapp_add_card_btn = (By.ID, "ib_add_card")  # 添加卡片按钮
    Dapp_show_amout = (By.ID, "img_show_amout")  # 加密按钮
    #uat2环境
    #fx_card_btn= (By.XPATH,"//android.widget.TextView[@text='FX' and @resource-id='com.pundix.xwallet:id/tv_balance']") #点击进入fx卡
    fx_card_btn = (By.XPATH, '//android.widget.TextView[contains(@text, "FX")]')
    #uat环境
    #fx_card_btn = (By.XPATH, "//android.widget.TextView[@text='f(x) Card']")  # 点击进入fx卡

    # ----------fx卡片主界面元素---------------
    fx_amout = (By.ID, "tv_amout")  # fx卡片里面的加密按钮
    fx_setting = (By.ID, "iv_setting")  # fx卡片里面的设置按钮
    fx_back_btn = (By.CLASS_NAME, "android.widget.ImageButton")  # fx卡片里面的左上角返回键
    fx_conversion_btn = (By.XPATH,"//android.widget.TextView[@text='Conversion']")  # 转换按钮
    fx_staking_btn = (By.XPATH,"//android.widget.TextView[@text='Staking']")  # 挖矿按钮
    fx_main_btn =(By.XPATH,"//android.widget.TextView[@text='FX' and @resource-id='com.pundix.xwallet:id/tv_currency' and @index='1']")# fx按钮
    fx_NPXS_btn = (By.XPATH,"//android.widget.TextView[@text='NPXS']")  # npxs按钮
    fx_NPXSXEM_btn = (By.XPATH,"//android.widget.TextView[@text='NPXSXEM']")  # npxsxem按钮

    # ---------转换功能界面元素-------------
    conver_option_btn = (By.ID, "rl_layout_option")  # 帮助按钮

    # ---------staking功能的界面元素-------
    staking_title=(By.XPATH,"//android.view.View[@text='f(x) Staking Terms and Conditions']")
    staking_terms=(By.ID,"cb_staking_terms")#挖矿协议界面的第一个复选框
    staking_function_token=(By.ID,"cb_function_token")#挖矿协议界面的第二个复选框
    staking_confirm_btn=(By.ID,"btn_confirm")#挖矿协议界面的确定按钮
    staking_gotoKyc=(By.XPATH,"//android.widget.Button[@resource-id='commonBigBtnKyc']")#gotokyc 按钮
    staking_closeBtn=(By.ID,"toolbar")#挖矿界面左上角的关闭按钮
    staking_option_btn = (By.ID, "option")  # 挖矿界面右上角的更多按钮
    staking_rl_layout_option=(By.ID,"rl_layout_option")#挖矿右上角的更多按钮
    staking_Guide = (By.ID, "option1")  # 挖矿界面guide按钮
    staking_history = (By.ID, "option2")  # 挖矿界面staking history按钮
    staking_startTime = (By.XPATH, "//android.view.View[@text='Start time']")  # 挖矿开始时间
    staking_endTime = (By.XPATH, "//android.view.View[@text='End Time']")  # 挖矿结束时间
    staking_startTime_cancle = (By.ID, "cancle")  # 取消时间按钮
    staking_startTime_OK = (By.ID, "tv_finish")  # 确定时间按钮
    staking_endTime_cancle = (By.XPATH, "//android.widget.TextView[@text='Cancel']")  # 取消时间按钮
    staking_endTime_OK = (By.XPATH, "//android.widget.TextView[@text='OK']")  # 确定时间按钮
    staking_option2 = (By.ID, "option")  # 挖矿帮助按钮
    staking_shart = (By.ID, "option3")  # 挖矿界面分享按钮
    staking_pwCancel = (By.ID, "tv_pwCancel")  # 取消分享按钮
    staking_cancle = (By.ID, "cancle")  # 取消按钮
    staking_withdraw=(By.XPATH,"//android.view.View[@text='Withdraw']")#提现按钮
    staking_startMining=(By.XPATH,"//android.view.View[@text='Start staking']")#开始挖矿按钮
    staking_next=(By.XPATH,"//android.widget.Button[@text='Next']")#点击下一步按钮
    staking_copy=(By.XPATH,"//android.widget.TextView[@text='Copy Link']")#点击复制链接按钮



    # -----------fx转账界面元素----------
    fx_page_transfer = (By.ID, "btn_withdraw")  # 转账按钮
    fx_type_name = (By.ID, "tv_type_name")  # 账单名称
    fx_transferAddress=(By.ID,"ed_receivingAddress")#fx转账地址
    fx_coinNumber=(By.ID,"ed_coinNumber")#输入金额框
    fx_all = (By.ID, "tv_allCoinNumber")  # all按钮
    fx_transferNext = (By.ID, "btn_withdraw")  # 第一个fx界面的下一步按钮
    fx_withdrawNext=(By.ID,"btn_withdrawNext1")   #第二个fx'转账的下一步按钮
    fx_email_code=(By.ID,"ed_email_code")#邮箱验证码
    fx_send_sms_code=(By.ID,"tv_send_sms_code")#短信验证码
    fx_ed_sms_code=(By.ID,"ed_sms_code")#短信验证码编辑框
    fx_pay_password=(By.ID,"ed_pay_password") #输入支付密码
    fx_send_emai_code=(By.ID,"tv_send_email_code")  #点击发送验证码
    fx_confirm=(By.ID,"btn_confirm") #点击确认按钮
    fx_bill=(By.XPATH,"//android.widget.TextView[@text='FX Distribution')")#fx账单名称

    #fx账单
    fx_list=(By.ID,"rv_record")
    fx_transfer_type=(By.XPATH,"//android.widget.TextView[@text='Transfer']")#fx账单的transfer
    fx_FX_Distribution=(By.XPATH,"//android.widget.TextView[@text='FX Distribution']")#fx账单
    fx_Allocation_from_Staking=(By.XPATH,"//android.widget.TextView[@text='Allocation from Staking']")#挖矿账单

    # ------------NPXS界面元素------------
    npxs_help_menu = (By.ID, "iv_menu")  # 帮助按钮
    npxs_transfer = (By.ID, "btn_transfer")  # NPXS转账
    npxs_add = (By.ID, "rl_layout_add")  # add按钮
    npxs_private = (By.ID, "ll_layout_private")  # private wallet account
    npxs_exchange = (By.ID, "iv_exchange")  # 切换按钮
    npxs_all = (By.ID, "tv_available_all")  # 全部按钮
    npxs_confirm = (By.ID, "btn_transfer")  # 确认转账按钮
    npxs_input_amount=(By.ID,"ed_available")#内部转账金额输入框
    npxs_chainAddress=(By.ID,"ed_address")#NPXS链上地址
    npxs_addressNote=(By.ID,"ed_remarks")#NPXS地址备注
    npxs_chain_confirmBtn=(By.ID,"btn_confirm")#添加npxs链上地址界面的确认按钮
    npxs_help_title=(By.XPATH,"//android.view.View[@text='How to allocate your NPXS in your XWallet to Stake for f(x) token distribution?']")#npxs帮助界面的标题

    # ---------NPXSXEM界面元素------------
    npxsxem_helpBtn = (By.ID, "iv_menu")  # 帮助按钮
    npxsxem_view = (By.ID, "btn_transfer")  # view按钮
    npxsxem_add = (By.ID, "iv_add_icon")  # add按钮
    npxsxem_account = (By.ID, "ll_layout_private")  # npxsxem account记录
    npxsxem_receive = (By.ID, "btn_recharge")  # receive按钮
    npxsxem_transfer_btn = (By.ID, "btn_withdraw")  # transfer按钮
    npxsxem_payinfo = (By.ID, "rl_layout_payinfo")  # 账单记录
    npxsxem_tv_private_account=(By.ID,"tv_private_account")#链上地址列表
    npxsxem_copy_address=(By.ID,"btn_many_copy_address")#copy address按钮
    npxsxem_select_agree = (By.ID, "cb_select_agree")  # 同意复选框
    npxsxem_view_address = (By.ID, "btn_view_recharge")  # view address按钮
    npxsxem_close = (By.ID, "iv_close")  # 关闭按钮
    npxsxem_address_QRcode = (By.ID, "btn_many_get_address")  # Address QR code按钮

    npxsxem_copy_address1= (By.ID, "btn_confirm")  # copy address按钮
    npxsxem_copy_address2=(By.ID,"btn_copy_address")#copy按钮
    npxsxem_iv_menu=(By.ID,"iv_menu")#右上角更多按钮
    npxsxem_modify_address_note=(By.ID,"tv_refresh")#modify address note按钮
    npxsxem_guide_btn=(By.ID,"tv_help")#guide按钮
    npxsxem_cancel=(By.ID,"tv_cancel")#取消按钮
    npxsxem_address_note=(By.ID,"ed_remarks")#address note输入框
    npxsxem_save_modification=(By.ID,"btn_confirm")#save modificication按钮
    npxsxem_tv_remarks=(By.ID,"tv_remarks")#address note的文本


    npxsxem_message_QRcode = (By.ID, "btn_many_get_message")  # message QR code按钮
    npxsxem_copy_message = (By.ID, "btn_many_copy_message")  # copy message按钮
    npxsxem_recipient_address = (By.ID, "ed_transferAddress")  # recipient address输入框
    npxsxem_amount = (By.ID, "ed_transferCoinNumber")  # amount输入框
    npxsxem_message = (By.ID, "ed_transfer_msg")  # message输入框
    npxsxem_transfer_next = (By.ID, "btn_transferNext")  # 下一步按钮

    npxsxem_chain_record=(By.ID,"iv_arrow")#点击链上的转账记录
    npxsxem_select_btn=(By.ID,"cb_select_agree")#npxsxem的复选框按钮
    npxsxem_transfer_confirm=(By.ID,"btn_confirm")#npxsxem确认按钮
    npxsxen_withdrawNext1=(By.ID,"btn_withdrawNext1")#点击确认转账按钮
    npxsxem_emailCode=(By.ID,"tv_send_email_code")#转账的邮箱验证码
    npxsxem_ed_email_code=(By.ID,"ed_email_code")#邮箱验证码输入框
    npxsxem_ed_pay_password=(By.ID,"ed_pay_password")#支付密码输入框
    npxsxem_btn_confirm1=(By.ID,"btn_confirm")#确认转账按钮



    #---------------npxsxem add界面元素------------------#
    npxsxem_NEM_address=(By.ID,"ed_address")#NEM输入框
    npxsxem_NEM_note=(By.ID,"ed_remarks")#备注
    npxsxem_confirm=(By.ID,"btn_confirm")#确定按钮

    def swipeFXUp(self, duration=500):
        """
        根据屏幕相对大小，向上滑动
        :return:
        """

        x, y = self.get_size()
        self.driver.swipe(x/2, y *13/100, x/2, 55/100, duration)
        print(x,y)


    def dapp_page(self):
        '''进入dapp页面'''
        WebDriverWait(self.driver, 20, 0.5).until(
            EC.text_to_be_present_in_element(self.get_balance_text, u'Balance'))  # 获取Dapp页面Balance
        self.driver.find_element(*self.click_dapp).click()  # 进入dapp页面


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
        time.sleep(3)
        if self.findElement("FX"):
            print("F(x)Card已存在，不需要添加")
            pass

        else:
            self.swipeUp(duration=1500)#滑动查找fx app
            self.swipeUp(duration=1500)  # 滑动查找fx app
            self.swipeUp(duration=1500)  # 滑动查找fx app
            time.sleep(2)
            if self.findElement("FX"):
                print("滑动后，已经找到F(x)Card")
                time.sleep(2)
            else:
                self.swipeUp(duration=800)  # 滑动查找fx app
                time.sleep(2)
                self.driver.find_element(*self.Dapp_add_card_btn).click()
                time.sleep(2)


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
        self.driver.find_element(*self.fx_conversion_btn).click()
        time.sleep(2)


    def enter_conversion(self):
        """
        进入转换的帮助按钮
        """
        time.sleep(3)
        self.driver.find_element(*self.conver_option_btn).click()
        time.sleep(3)

    def enter_staking_protocol(self):
        """进入挖矿的协议界面"""
        # el = WebDriverWait(self.driver, 10, 0.5).until(
        #        EC.text_to_be_present_in_element(self.staking_title, u"f(x) Staking Terms and Conditions"))
        #
        # if el ==True:
        if self.findElement("I have read and agreed to f(x) Staking Terms and Conditions"):
            self.swipeFXUp(duration=800)  #滑动协议界面
            self.swipeFXUp(duration=800)  # 滑动协议界面
            self.swipeFXUp(duration=1500)  # 滑动协议界面
            self.driver.find_element(*self.staking_terms).click() #点击第一个协议复选框
            time.sleep(2)
            self.driver.find_element(*self.staking_function_token).click()#点击第二个协议复选框
            time.sleep(2)
            self.driver.find_element(*self.staking_confirm_btn).click()#点击确定按钮
            time.sleep(2)
            return True
        elif self.findElement("go to kyc"):
            print("进入go to kyc界面")
            self.driver.find_element(*self.staking_gotoKyc).click()#点击go to kyc按钮
            time.sleep(2)
            return True
        elif self.findElement("Staking"):
            print("进入挖矿中的界面")
            return True
        elif self.findElement("Start staking"):
            print("进入开始挖矿界面")
            return True
        else:
            return False

    def Dapp_notice(self):
        """去掉紧急消息提示"""
        #notice=self.driver.find_element(*self.urgent_news)
        if self.findElement("tv_notice"):
            #notice.click()
            self.driver.find_element(*self.urgent_news).click()
            time.sleep(2)
            self.driver.back()
            time.sleep(1)

    def Dapp_click_fxText(self):
        """从Dapp界面进入fx转账界面"""
        #self.driver.find_element(*self.fx_card_btn).click()# 点击DAPP界面的fx按钮
        self.click2("FX")
        time.sleep(2)

    def enter_staking(self):
        """点击fx卡片的staking按钮"""
        time.sleep(2)
        self.driver.find_element(*self.fx_staking_btn).click()
        time.sleep(2)

    def enter_fx(self):
        """点击fx卡片界面的fx按钮"""
        self.driver.find_element(*self.fx_main_btn).click() #点击fx卡片的fx按钮
        time.sleep(4)

    def fx_transfer(self,text1,text2,text3,text4,text5):
        """
        fx转账
        """
        self.driver.find_element(*self.fx_page_transfer).click()  # 点击转账按钮
        time.sleep(4)
        if self.findElement('Not Now'):
            self.click2("Not Now")
            time.sleep(2)
            self.driver.find_element(*self.fx_page_transfer).click()  # 点击转账按钮
            time.sleep(4)
        else:
            pass

        fx_address = self.driver.find_element(*self.fx_transferAddress)#点击fx转账地址
        fx_address.click();fx_address.send_keys(text1) #输入转账地址
        time.sleep(2)

        fx_amount=self.driver.find_element(*self.fx_coinNumber)#点击转账金额输入框
        fx_amount.click();fx_amount.send_keys(text2)#输入金额
        #coinNumber = self.driver.find_element(*self.fx_all).click()#点击all按钮
        # coinNumber.clear()
        # coinNumber.send_keys(text1)
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.driver.find_element(*self.fx_transferNext).click()#点击第一个界面的下一步按钮
        time.sleep(3)
        self.driver.find_element(*self.fx_withdrawNext).click()#点击第二个界面的下一步按钮
        time.sleep(3)

        if self.findElement("ed_email_code"):
            self.driver.find_element(*self.fx_send_emai_code).click()  # 点击发送验证码
            time.sleep(2)
            email_code =self.driver.find_element(*self.fx_email_code)#点击邮箱验证码输入框
            email_code.click();email_code.send_keys(text3)
            time.sleep(2)

        if self.findElement("tv_send_sms_code"):
            self.driver.find_element(*self.fx_send_sms_code).click()  # 点击发送验证码
            time.sleep(2)
            sms_code=self.driver.find_element(*self.fx_ed_sms_code)#点击短信验证码输入框
            sms_code.click();sms_code.send_keys(text4)
            time.sleep(2)

        pay_password=self.driver.find_element(*self.fx_pay_password) #点击支付密码
        pay_password.click();pay_password.send_keys(text5)#输入支付密码
        time.sleep(3)
        self.driver.back()#按返回键
        time.sleep(2)
        self.driver.find_element(*self.fx_confirm).click()#点击确认转账按钮
        time.sleep(1)

        if self.is_toast_exist("Transfer successful"):
            print("转账成功")
            return True

        elif self.is_toast_exist("Insufficient balance"):
            print("余额不足")
            return True


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
        helpBtn=self.driver.find_element(*self.npxs_help_title)
        if helpBtn:
            print("已进入npxs帮助说明界面")
            return True
        else:
            print("未进入npxs帮助说明界面")
            return False


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
        time.sleep(2)

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

        self.driver.back()#按返回键
        time.sleep(1)
        self.driver.find_element(*self.npxs_confirm).click()#点击确认按钮
        if self.is_toast_exist("Insufficient balance"):
            print("钱包金额不足")
            return True
        elif self.is_toast_exist("Transfer successful"):
            print("内部划转成功")
            return True


    def click_npxs_add(self):
        """点击NPXS的ADD按钮"""
        self.driver.find_element(*self.npxs_add).click()
        time.sleep(2)

    def Add_NPXSchain_address(self,text,text1):
        """添加npxs链上地址"""
        self.driver.find_element(*self.npxs_chainAddress).click()#点击npxs地址输入框
        time.sleep(2)
        npxsChainAddress=self.driver.find_element(*self.npxs_chainAddress)
        npxsChainAddress.click();npxsChainAddress.send_keys(text)#输入npxs链上地址
        time.sleep(2)

        self.driver.find_element(*self.npxs_addressNote).click()#点击npxs地址备注
        npxsAddressNote =self.driver.find_element(*self.npxs_addressNote)#输入备注
        time.sleep(2)
        npxsAddressNote.click();npxsAddressNote.send_keys(text1)#输入备注
        time.sleep(2)

        self.driver.find_element(*self.npxs_chain_confirmBtn).click()#点击确认按钮
        time.sleep(4)


    def click_tv_private_account(self,text1):
        """点击npxsxem的列表记录"""
        self.driver.find_element(*self.npxsxem_tv_private_account).click()#点击列表数据
        time.sleep(2)

        if self.findElement("btn_confirm"):
            self.driver.find_element(*self.npxsxem_copy_address1).click()  # 点击copy address按钮
            time.sleep(1)

        self.driver.find_element(*self.npxsxem_iv_menu).click()#点击右上角的更多按钮
        time.sleep(2)

        if self.findElement("tv_refresh"):

            self.driver.find_element(*self.npxsxem_modify_address_note).click()#点击modify address note按钮
            time.sleep(2)

            self.driver.find_element(*self.npxsxem_address_note).click()#点击address note输入框
            address_note = self.driver.find_element(*self.npxsxem_address_note)
            address_note.click();address_note.send_keys(text1)
            msg = self.driver.find_element(*self.npxsxem_address_note).text
            time.sleep(2)
            self.driver.find_element(*self.npxsxem_save_modification).click() #点击save modification按钮
            time.sleep(2)
            msg1 = self.driver.find_element(*self.npxsxem_tv_remarks).text
            self.driver.find_element(*self.npxsxem_iv_menu).click()#点击右上角的更多按钮
            time.sleep(2)
            self.driver.find_element(*self.npxsxem_guide_btn).click()#点击帮助说明
            if self.findElement('Guide'):
                time.sleep(2)
                self.driver.back()
            time.sleep(1)
            self.driver.find_element(*self.npxsxem_iv_menu).click()#点击右上角的更多按钮
            time.sleep(2)
            self.driver.find_element(*self.npxsxem_cancel).click()#点击取消按钮
            time.sleep(1)
            #return msg,msg1
        else:
            print("进入帮助界面")
        #     self.driver.find_element(*self.npxsxem_copy_address2).click()  # 点击copy address按钮
        #     self.is_toast_exist("Copied successfully ")
        #     time.sleep(1)
        #     print("无更多按钮点击，成功进入npxsxem界面")
        #     return True

    def click_npxsxem_helpBtn(self):
        """点击npxsxem界面的帮助按钮"""
        self.driver.find_element(*self.npxsxem_helpBtn).click()
        time.sleep(2)

    def click_npxsxem_viewBtn(self):
        """点击npxsxem界面的view按钮"""

        time.sleep(2)
        self.driver.find_element(*self.npxsxem_view).click()
        time.sleep(1)

    def click_npxsxem_receive(self):
        """点击npxsxem界面的received按钮"""
        self.driver.find_element(*self.npxsxem_receive).click()
        time.sleep(1)

    def click_npxsxem_receiveCountdown(self):
        """点击npxsxem充值界面的倒计时"""
        time.sleep(9)#等待充值倒计时9秒
        self.driver.find_element(*self.npxsxem_select_agree).click()#点击同意按钮
        time.sleep(2)
        self.driver.find_element(*self.npxsxem_view_address).click()#点击view address按钮
        time.sleep(2)
        self.driver.find_element(*self.npxsxem_address_QRcode).click()#点击address QRcode按钮
        time.sleep(2)
        self.driver.find_element(*self.npxsxem_close).click()#点击关闭按钮
        time.sleep(2)
        self.driver.find_element(*self.npxsxem_copy_address).click()#点击copy address按钮
        time.sleep(2)
        self.driver.find_element(*self.npxsxem_message_QRcode).click()#点击message QRcode按钮
        time.sleep(2)
        self.driver.find_element(*self.npxsxem_close).click()  # 点击关闭按钮
        time.sleep(1)
        self.driver.find_element(*self.npxsxem_copy_message).click()#点击copy message按钮
        time.sleep(2)

    def click_npxsxem_transfer(self):
        """点击npxsxem界面的转账按钮"""
        self.driver.find_element(*self.npxsxem_transfer_btn).click()
        time.sleep(2)

    def npxsxem_transfer(self,text,text1,text2,text3,text4):
        """npxsxem转账"""
        #第一步：输入转账地址
        self.driver.find_element(*self.npxsxem_recipient_address).click()#点击Recipient's Address输入框
        time.sleep(1)
        ecipient_address=self.driver.find_element(*self.npxsxem_recipient_address)
        ecipient_address.click();ecipient_address.send_keys(text)#输入npxsxem地址
        time.sleep(2)

        #第二步：输入转账金额
        self.driver.find_element(*self.npxsxem_amount).click()#点击amount按钮
        npxsxem_amount= self.driver.find_element(*self.npxsxem_amount)
        npxsxem_amount.click();npxsxem_amount.send_keys(text1)#输入转账金额
        time.sleep(2)
        self.driver.back()#按返回键
        time.sleep(1)

        #第三步：输入附言
        self.driver.find_element(*self.npxsxem_message).click()#点击message按钮
        time.sleep(1)
        npxsxem_message=self.driver.find_element(*self.npxsxem_message)
        npxsxem_message.click();npxsxem_message.send_keys(text2)#输入附言
        time.sleep(2)
        self.driver.back()#按返回键
        time.sleep(1)

        self.swipeUp()#往上滑动到下一步按钮
        time.sleep(2)

        #第四步：点击下一步按钮
        self.driver.find_element(*self.npxsxem_transfer_next).click()#点击下一步按钮
        time.sleep(2)

        if self.is_toast_exist("The withdrawal amount cannot be larger than the maximum allowed limit"):
            return True
        else:

            time.sleep(6)#倒计时5秒

            self.driver.find_element(*self.npxsxem_select_btn).click()#点击复选框勾选按钮
            time.sleep(2)

            self.driver.find_element(*self.npxsxem_transfer_confirm).click()#点击协议确定按钮
            time.sleep(2)

            #点击确认转账
            self.driver.find_element(*self.npxsxen_withdrawNext1).click()
            time.sleep(2)

            #第五步：输入支付密码确认转账
            self.driver.find_element(*self.npxsxem_emailCode).click()#发送验证码
            time.sleep(2)
            self.driver.find_element(*self.npxsxem_ed_email_code).click()#点击邮箱输入框
            time.sleep(2)
            npxsxem_email_code=self.driver.find_element(*self.npxsxem_ed_email_code)
            npxsxem_email_code.click();npxsxem_email_code.send_keys(text3)#输入邮箱验证码
            time.sleep(2)

            self.driver.find_element(*self.npxsxem_ed_pay_password).click()#点击支付密码输入框
            time.sleep(2)
            npxsxem_payPassword =self.driver.find_element(*self.npxsxem_ed_pay_password)
            npxsxem_payPassword.click();npxsxem_payPassword.send_keys(text4)#输入支付密码
            time.sleep(2)

            self.driver.back()#按返回键
            time.sleep(2)

            self.driver.find_element(*self.npxsxem_btn_confirm1).click()#确认转账
            if self.is_toast_exist("Transfer successful"):
                return True




    def click_npxsxem_add(self):
        """点击npxsxem的add按钮"""
        self.driver.find_element(*self.npxsxem_add).click()
        time.sleep(2)

    def add_npxsxem_chain_address(self,text,text1):
        """添加npxsxem链上地址"""

        #第一步：输入地址
        self.driver.find_element(*self.npxsxem_NEM_address).click()#点击NEM address的输入框
        time.sleep(2)
        NEM_address=self.driver.find_element(*self.npxsxem_NEM_address)
        NEM_address.click();NEM_address.send_keys(text)#输入NEM的地址
        time.sleep(2)

        #第二步：输入备注
        self.driver.find_element(*self.npxsxem_NEM_note).click()#点击备注输入框
        time.sleep(1)
        NEM_note=self.driver.find_element(*self.npxsxem_NEM_note)
        NEM_note.click();NEM_note.send_keys(text1)#输入备注
        time.sleep(2)

        #第三步：点击确定按钮
        self.driver.find_element(*self.npxsxem_confirm).click()#点击确定按钮
        time.sleep(1)

    def click_npxsxem_chainRecord(self):
        """点击NEM转账记录"""
        self.driver.find_element(*self.npxsxem_chain_record).click()
        time.sleep(2)

    def click_start_staking(self):
        """点击开启挖矿按钮"""
        if self.findElement("Start staking"):
            self.driver.find_element(*self.staking_startMining).click() #点击开始挖矿按钮
            time.sleep(5)
        elif self.findElement("Withdraw"):
            time.sleep(2)
            self.driver.find_element(*self.staking_withdraw).click()#点击提现按钮
            time.sleep(2)
            self.driver.find_element(*self.staking_next).click()#点击下一步按钮
            time.sleep(2)
            self.driver.find_element(*self.staking_copy).click()#点击复制按钮

    def click_staking_setting(self):
        """点击挖矿界面右上角的更多按钮"""
        time.sleep(2)
        self.driver.find_element(*self.staking_rl_layout_option).click()
        time.sleep(2)

    def click_staking_history(self):
        """点击挖矿历史界面"""
        self.driver.find_element(*self.staking_history).click()#点击挖矿历史按钮
        time.sleep(3)

        #开始时间功能
        self.driver.find_element(*self.staking_startTime).click()#点击开始时间
        time.sleep(2)
        self.driver.find_element(*self.staking_startTime_cancle).click()#点击取消按钮
        time.sleep(2)
        self.driver.find_element(*self.staking_startTime).click()  # 点击开始时间
        time.sleep(2)
        self.driver.find_element(*self.staking_startTime_OK).click()#点击ok按钮
        time.sleep(2)

        #结束时间功能
        self.driver.find_element(*self.staking_endTime).click()#点击结束时间按钮
        time.sleep(3)
        self.driver.find_element(*self.staking_endTime_cancle).click()#点击取消按钮
        time.sleep(2)
        self.driver.find_element(*self.staking_endTime).click()#点击结束时间按钮
        time.sleep(2)
        self.driver.find_element(*self.staking_endTime_OK).click()#点击确定按钮
        time.sleep(2)

        #帮助说明按钮
        self.driver.find_element(*self.staking_option2).click()#点击挖矿的帮助按钮
        time.sleep(2)
        if self.findElement("STAKING GUIDE"):
            print("进入帮助界面成功")
            pass


    def click_staking_shareTo(self):
        """点击分享按钮"""
        self.driver.find_element(*self.staking_shart).click()
        time.sleep(2)

    def click_staking_guide(self):
        """点击挖矿说明"""
        self.driver.find_element(*self.staking_Guide).click()
        time.sleep(2)

    def fresh_staking(self):
        """下拉刷新挖矿界面"""
        time.sleep(3)
        self.swipeDown()
