from PO.basePage import Base
from selenium.webdriver.common.by import By
import time


class DAPPPage(Base):
    """
   DAPP页面的元素
    """

    # DAPP页面 虚拟卡片 DAPP首页
    Virtual_BTC = "BTC"  # 虚拟卡片中的BTC
    Virtual_ETH = "ETH " #虚拟卡片中的ETH
    Virtual_Go = "virtual"  #虚拟卡片中的"更多"键

    # 虚拟卡片卡片详情页面
    Virtual_Eye = (By.ID, "tv_amout")  # 虚拟卡片中的加密按键
    Virtual_Setting = (By.ID, "iv_setting")  # 虚拟卡片片中的设置按键
    Virtual_bills = (By.ID, "iv_bills")  # 虚拟卡片中的账单按键
    Virtual_BTC_Details = "BTC"  # 虚拟卡片卡片详情中的BTC
    Virtual_ETH_Detail = "ETH "  # 虚拟卡片卡片详情中的ETH
    Virtual_NPXS_Detail = "NPXS"  # 虚拟卡片详情中的NPXS
    Virtual_BNB_Detail = "BNB"  # 虚拟卡片 卡片详情中的BNB
    Virtual_QTUM_Detail = "QTUM"  # 虚拟卡片卡片详情中的QTUM
    Virtual_XEM_Detail = "XEM"  # 虚拟卡片卡片详情中的XEM
    Virtual_NPXSXEM_Detail = "NPXSXEM"  # 虚拟卡片卡片详情中的NPXSXEM

    # 各币种详情页面
    Virtual_Receive = (By.ID, "btn_recharge")  # 查看虚拟卡片充值地址
    Virtual_transfer = (By.ID, "btn_withdraw")  # 查看虚拟卡片转账地址
    Virtual_Menu = (By.ID, "iv_menu")  # 虚拟卡片详情页面的菜单按键
    Virtual_Instructions = (By.ID, "tv_help")  # 币种详情页面菜单中的说明
    Virtual_Internal_Transfer = (By.ID, "tv_refresh")  # 虚拟卡片界面点击卡内划转
    Virtual_Back = (By.XPATH,
                    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ImageButton")  # 虚拟卡片详情页面左上角返回按钮
    Virtual_refresh = (By.ID, "iv_refresh")  # 虚拟卡片页面的二维码刷新按键
    Virtual_view_Address = (By.ID, "btn_view_recharge")  # 虚拟卡片查看充值地址，提醒页面
    Virtual_Copy_Address = (By.ID, "btn_single_copy")  # 复制虚拟卡片充值地址
    Receiving_address_close = (By.ID, "iv_close")  # 查看充值地址说明页面的关闭按键
    Receive_address_code = (By.ID, 'iv_single_qr_code') # 充值二维码

    # 转账页面
    Transfer_Address = (By.ID, "ed_receivingAddress")  # 在转账页面，输入地址
    Transfer_Scan = (By.ID, "iv_iconScan")  # 在转账页面，点击扫码
    Transfer_Amount_All = (By.ID, "tv_allCoinNumber")  # 在转账页面金额转出all
    Transfer_server = (By.ID, "tv_serviceCharge")  # 在转账页面查看手续费说明
    Transfer_KYC = (By.ID, "tv_kycVerify")  # 在转账页面点击KYV认证
    Transfer_Next = (By.ID, "btn_withdraw")  # 转账页面点击下一步
    Transfer_add_address = (By.ID,"iv_iconAddress") # 转账页面添加提现地址
    Transfer_Send_email = (By.ID, "tv_send_email_code")  # 转账页面获取Email验证码
    Transfer_input_email_code = (By.ID, "ed_email_code")    # 转账页面输入邮箱验证码
    Transfer_input_SMS = (By.ID, "ed_sms_code")     # 转账页面输入SMS验证码
    Transfer_Send_SMS = (By.ID, "tv_send_sms_code")  # 转账页面获取SMS验证码
    Transfer_Pay_password = (By.ID, "ed_pay_password")  # 转账页面输入支付密码
    Transfer_confirm = (By.ID, "btn_confirm")   # 转账页面输入验证码和密码后Confirm
    Transfer_camera_premise = (By.ID, "button1")    # 转账页面扫码时相机权限


    #BEP-2协议币种转账页面附言
    Transfer_Memo = (By.ID, "ed_transfer_msg")      #在转账页面点击Memo输入框
    transfer_Memo_Scan = (By.ID,"iv_msg_scan")       #在Memo输入时选择扫码

    #Google认证提示
    Google_Notnow =(By.ID, "btn_no")    #Google认证时，选择Not Now
    Google_confirm =(By.ID, "btn_yes")  #google认证时，选择confirm

    #添加提现地址
    Add_address_Send = (By.ID, "tv_send_email_code")    #添加地址时，发送邮箱验证码
    Add_address_Next = (By.ID, "btn_withdrawNext2")     #添加转账地址时，输入验证码后，点击下一步

    #虚拟卡片BEP-2协议币种(带附言的币种:BNB + NPXSXEM）
    Virtual_BNB_QRcode =(By.ID, "btn_many_get_address")     #BNB查看充值地址二维码
    Virtual_BNB_QRcode_close = (By.ID, "iv_close")      #BNB关闭充值地址二维码页面
    Virtual_BNB_copy_address = (By.ID, "btn_many_copy_address")     #复制BNB充值地址
    Virtual_BNB_Memo_QRcode  = (By.ID, "btn_many_get_message")      #BNB查看附言二维码
    Virtual_BNB_Memo_close = (By.ID,"rl_layout_close")      #BNB关闭附言二维码页面
    Virtual_BNB_Copy_Memo = (By.ID, "btn_many_copy_message")    #BNB 复制附言

    #虚拟卡片NPXSXEM
    Virtual_NPXEXEM_Address = (By.ID,"tv_count_down_timer")     #NPXSXEM 查看充值地址，弹出5说明提醒界面
    Virtual_NPXSXEM_agree = (By.ID, "cb_select_agree")      #NPXSXEM 查看充值地址，同意协议
    Virtual_NPXSXEM_Transfer = (By.ID, "btn_ok")        #NPXSXEM 转账弹出确认按钮

    # 内部划账
    Virtual_Internal_Transfer_entrance  = (By.ID, "tv_refresh")  # 虚拟卡片中内部划转入口
    Virtual_Internal_Transfer_back = (By.XPATH,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageButton")  # 内部划转左上角返回键
    Virtual_Internal_Transfer_change = (By.ID, "iv_exchange")  # 虚拟卡片内部划转切卡片位置
    Virtual_Internal_Transfer_FromCard = (By.ID, "tv_from_card_id")  # 内部划转选择From方卡片
    Virtual_Internal_Transfer_Tocard = (By.ID, "tv_to_card_id")  # 内部划转选择To方卡片
    Virtual_Internal_Transfer_Accoutclose = (By.ID, "ll_close")  # 内部划转在选择卡片时，点击X
    Virtual_Internal_Transfer_Accountselect = (By.ID, "rl_layout_pay_type")  # 内部划转，选择转账卡片
    Virtual_Internal_Transfer_Coin = (By.ID, "tv_cion")  # 内部划转选择点击下拉币种
    Virtual_Internal_Transfer_Coinselect = (By.ID, "rl_layout_pay_type")  # 内部划转选择币种
    Virtual_Internal_Transfer_ALl = (By.ID, "tv_available_all")  # 内部划转金额选择all
    Virtual_Internal_Transfer_Available = (By.ID, "ed_available")  # 内部划转手动输入金额
    Virtual_Internal_Transfer_Confirm = (By.ID, "btn_transfer")  # 内部划转选择确认

    #虚拟卡片卡片详情中的历史账单
    Virtual_Transition_Hisrory = (By.ID,"rl_layout_payinfo")    #虚拟卡片，卡片详情中的历史账单


    #添加XPASS卡
    Add_card =(By.ID, "ib_add_card")        #添加卡片按钮
    Add_XPASS = "XPASS"    #点击添加XPASS卡
    Add_XPASS_No = (By.ID , "ed_addCardXpassNO")       #输入XPASS卡号输入框
    Add_XPASS_Next = (By.ID, "btn_addCardNext")         #输入卡号后下一步按钮
    Add_XPASS_6pin_code = (By.ID, "ed_addCardXpassNO")      #输入6位密码
    Add_XPASS_confirm = (By.ID, "btn_addCardNext")      #最后一步确认按键

    #添加开放平台卡片
    Add_opencard = (By.ID, "item_card_tv_virtual")  #选择开放平台卡片点击区域
    Add_opencard_select_Virtual = (By.Id, "rl_virtualFlag")     #添加开放平台卡片时，选择添加虚拟卡
    Add_opencard_select_Physical =(By.ID, "rl_physicalFlag")    #添加开放平台卡片时，选择添加物理卡片

    # 开放平台卡片
    Open_Platform_Card_Pay ="Pay"   #点击开放平台卡片Pay按钮
    Open_Platform_Card_Transfer = "Transfer"  #点击开放平台卡片上的Transfer按钮
    Open_Platform_Card_Website ="Website"    #开放平台卡片上的开发者网站

    #添加开放平台APP
    open_platform_app_Add ="FamilyMart"   #添加开放平台APP
    Open_Platfrom_app = "familymart"     #点击DApp首页APP入口
    Open_Platform_app_About = "About us"   #点击DAPP首页关于入口

    def enter_dapp(self):
        """
        点击DAPP按钮
        """
        # self.driver.find_element(*self.Dapp).click()
        self.click2("DApp")
        time.sleep(2)

    def click_Virtual_BTC(self):
        """
        点击虚拟卡片上的BTC
        """
        self.click2(self.Virtual_BTC)

    def click_Virtual_ETH(self):
        """
        点击虚拟卡片上的ETH
        """
        self.click2(self.Virtual_ETH)

    def click_virtual_More(self):
        """
        点击虚拟卡片上的"更多"
        """
        self.click2(self.Virtual_Go)

    def click_eye(self):
        """
        点击虚拟卡片上的眼睛加密按键
        """
        self.click_virtual_More()
        self.driver.find_element(*self.Virtual_Eye).click()

    def click_setting(self):
        """
        点击虚拟卡片上的设置按键
        """
        self.click_virtual_More()
        self.driver.find_element(*self.Virtual_Setting).click()

    def click_bills(self):
        """
        点击虚拟卡片上的账单按钮
        """
        self.click_virtual_More()
        self.driver.find_element(*self.Virtual_bills).click()

    def click_BTC_Detail(self):
        """
        点击虚拟卡片详情上的BTC
        """
        self.click_virtual_More()
        self.driver.find_element(*self.Virtual_BTC_Details).click()

    def click_ETH_Detail(self):
        """
        点击虚拟卡片详情上的ETH
        """
        self.click_virtual_More()
        self.driver.find_element(*self.Virtual_ETH_Detail).click()

    def click_NPXS_Detail(self):
        """
        点击虚拟卡片上的NPXS
        """
        self.click_virtual_More()
        self.driver.find_element(*self.Virtual_NPXS_Detail).click()

    def click_BNB_Detail(self):
        """
        点击虚拟卡片详情上的BNB
        """
        self.click_virtual_More()
        self.driver.find_element(*self.Virtual_BNB_Detail).click()

    def click_QTUM_Detail(self):
        """
        点击虚拟卡片详情上的QTUM
        """
        self.click_virtual_More()
        self.driver.find_element(*self.Virtual_QTUM_Detail).click()

    def click_XEM_Detail(self):
        """
        点击虚拟卡片详情上的XEM
        """
        self.click_virtual_More()
        self.driver.find_element(*self.Virtual_XEM_Detail).click()

    def click_NPXSXEM_Detail(self):
        """
        点击虚拟卡片上的NPXSXEM
        """
        self.click_virtual_More()
        self.driver.find_element(*self.Virtual_NPXSXEM_Detail).click()

    def Click_Token_setting(self):
        """
        点击币种详情页面的设置菜单
        """
        self.driver.find_element(*self.Virtual_Setting).click()

    def click_instructions(self):
        """
        点击币种详情页面的说明
        """
        self.driver.find_element(*self.Virtual_Instructions).click()
        time.sleep(2)
        self.driver.find_element(*self.Virtual_Back).click2()

    def Click_refresh(self):
        """
        点击币种详情页面的二维码刷新按键
        """
        self.driver.find_element(*self.Virtual_refresh).click()

    def Click_Receice(self):
        """
        点击币种详情页面查看充值地址
        """
        self.driver.find_element(*self.Virtual_Receive).click()
        time.sleep(2)




    def click_transaction_history(self):
        """
        遍历所有的账单类型
        """
        self.click_BTC_Detail()
        time.sleep(2)
        bills = [self.Receive, self.Expenditure, self.Transfer, self.Extra, self.Distribution, self.Collection1,
                 self.Refund, self.Crypto_Gift_Sent, self.Crypto_Gift_Received, self.Crypto_Gift_Refund]
        for i in bills:
            if self.findElement(i):
                self.click2(i)
                time.sleep(2)
                self.driver.back()
            else:
                self.swipeUp()
                print('找不到该类型账单...')


    def Click_Transfer_without_Memo(self):

        """
          无Memo类型的货币，转账页面操作
        """
        self.driver.find_element(*self.Virtual_transfer).click()
        if self.findElement('Not Now'):
            self.driver.back()
        else:
            pass
        time.sleep(2)
        self.driver.find_element(*self.Transfer_Address).send_keys('midWvkgYPSXHgkYHibfW5LK7Bkqg3GVqPV')    # 转账输入BTC地址
        self.driver.find_element(*self.Transfer_Amount_All).click()     # 转账页面转全部金额
        self.driver.find_element(*self.Transfer_Next).click()       # 输入金额后点下一步



    def Send_code(self):
        """
        输入验证码和支付密码后完成
        """
        if self.findElement('@'):
            """
            查找元素如果出现@，发送Email code
            """
            self.driver.find_element(self.Transfer_Send_email).click()  # 点击发送邮箱验证码
            time.sleep(3)
            self.driver.find_element(*self.Transfer_input_email_code).send_keys("2222")     # 调起输入法，输入2222
        else:
            pass

        if self.findElement("+"):
            """
            查找元素如果出现+，发送SMS code
            """
            self.driver.find_element(self.Transfer_Send_SMS).click()
            time.sleep(3)
            self.driver.find_element(*self.Transfer_input_SMS).send_keys("2222")
        else:
            pass

        self.driver.find_element(*self.Transfer_Pay_password).send_keys("123456")   # 输入支付密码123456
        self.driver.back()      # 输入完成后，点击系统返回，显示确认菜单
        self.driver.find_element(*self.Transfer_confirm).click()


    def Add_address(self):
        """
        在转账页面添加转账地址
        """
        self.driver.find_element(*self.Virtual_transfer).click()
        if self.findElement('Not Now'):
            self.driver.back()
        else:
            pass
        time.sleep(2)
        self.driver.find_element(*self.Transfer_add_address).click()
        time.sleep(1)
        self.driver.find_element(*self.Add_Address).click()
        self.driver.find_element(*self.Input_withdrawAddress).send_keys("0x94c49f0DA296fb34D81F14511Bf4AdF557f3b708")   # 输入转账地址
        self.driver.find_element(*self.Input_note).send_keys("Token")   # 输入地址备注

    def Copy_Receive_Address(self):
        """
        无Memo的货币查看充值地址
        """
        self.driver.find_element(*self.Virtual_Receive).click()     # 点击Receving,弹出"View address"提示
        self.driver.find_element(*self.Virtual_view_Address).click()    # 复制充值地址
        self.driver.find_element(*self.Virtual_Copy_Address).click()    # 点击返回键
        self.driver.back()


    def Copy_Address_Memo(self):
        """
        有Memo的货币在充值二维码页面操作地址二维码和附言二维码
        """

        self.driver.find_element(*self.Virtual_BNB_QRcode).click()      # 点击查看充值地址二维码
        time.sleep(2)
        self.driver.find_element(self.Virtual_BNB_QRcode_close).click()     # 关闭充值二维码显示框
        time.sleep(1)
        self.driver.find_element(self.Virtual_BNB_copy_address).click()     # 点击复制BNB充值地址
        self.driver.find_element(self.Virtual_BNB_Memo_QRcode).click()      # 点击查看BNB附言二维码
        self.driver.find_element(self.Virtual_BNB_Memo_close).click()       # 点击关闭附言二维码显示框
        time.sleep(1)
        self.driver.find_element(self.Virtual_BNB_Copy_Memo).click()        # 点击copy memo
        time.sleep(1)

    def check_QR_code(self):
        """检查是否加载付款二维码是否正确"""

        if self.driver.find_element(*self.Receive_address_code).is_enabled():  # 判断充值二维码是否可用
            return True
        else:
            return False

    def Click_Transfer_with_memo(self):
        """
        有Memo的货币，在转账页面输入转账地址，金额，等操作
        """
        self.driver.find_element(*self.Virtual_transfer).click()
        if self.findElement("Not Now"):
            self.driver.back()
        else:
            pass
        time.sleep(2)
        self.driver.find_element(*self.Transfer_Scan).click()       # 转账页面点击地址扫码

        if self.findElement("camera"):
            self.driver.find_element(*self.Transfer_camera_premise).click()
        else:
            pass
        """
        判断转账点击扫码时，如果弹出获取相机权限按键，点击"Allow"
        """
        self.driver.back()
        time.sleep(1)
        self.driver.find_element(*self.Transfer_Memo_Scan).click()  # 点击扫码Memo
        time.sleep(1)
        self.driver.back()      # 在相机扫码界面点击返回
        time.sleep(1)
        self.driver.find_element(*self.Transfer_Address).send_keys("tbnb1x5n9ck6xhexwfjpxmp2ygg0ypndmrnfv9l45de")       # 拉起键盘输入转账地址
        self.driver.find_element(*self.Transfer_Amount_All).click()     # 转出金额点击All
        self.driver.find_element(*self.Transfer_Memo).send_keys("")     # 转出到外部地址，不输入附言
        self.driver.find_element(*self.Transfer_Next).click()   # 点击下一步
        time.sleep(1)



    def click_NPXSXEM_Receice(self):
        self.click_NPXSXEM_Detail()
        time.sleep(2)
        self.driver.find_element(*self.Virtual_Receive).click()
        time.sleep(7)
        self.driver.find_element(*self.Virtual_NPXSXEM_agree).click()
        time.sleep(1)
        self.driver.find_element(*self.Virtual_view_Address).click()
        self.Copy_Address_Memo()
        """
        调用在地址界面复制操作方法
        """

    def Internal_Transfer(self):
        self.click_BNB_Detail()
        self.driver.find_element(*self.Virtual_Menu).click()
        self.driver.find_element(*self.Virtual_Internal_Transfer_entrance).click()


    def check_receive_code(self):
        """检查是否加载付款二维码是否正确"""

        if self.driver.find_element(*self.Receive_address_code).is_enabled():  # 判断充值二维码是否可用
            return True
        else:
            return False








    def add_XPASS_card(self, num, pin):
        """
        添加XPASS卡
        num:XPASS卡号
        pin:卡号密码
        """

        self.driver.find_element(*self.Add_card).click()
        self.driver.find_element(*self.Add_XPASS).click()
        time.sleep(1)
        self.driver.find_element(*self.Add_XPASS_No).send_keys(num)
        self.driver.find_element(*self.Add_XPASS_Next).click()

        if self.is_toast_exist('not found'):
            print(f'卡号{num}没找到，请输入正确的卡号')
        elif self.is_toast_exist('activitied'):
            print(f'卡号{num}未被激活，请先激活...')
        else:
            self.driver.find_element(*self.Add_XPASS_6pin_code).send_keys(pin)
            self.driver.find_element(*self.Add_XPASS_confirm)
            if self.is_toast_exist('already'):
                print(f'该{num}已被添加过！')
            elif self.is_toast_exist('password'):
                print(f'卡号的密码{pin}不对')
            else:
                time.sleep(1)
                return True

    def XPASS_BTC_icon(self):
        """从XPASS卡的一级页，点击BTC icon"""

        XPASS_BTC = (By.XPATH, '//android.widget.ImageView[@resource-id="com.pundix.xwallet:id/iv_recod" and @instance=7]')
        self.driver.find_element(*XPASS_BTC).click()  # 点击XPASS卡的BTC
        time.sleep(3)

    def XPASS_ETH_icon(self):
        """从XPASS卡的一级页，点击ETH icon"""

        XPASS_ETH = (By.XPATH, '//android.widget.ImageView[@resource-id="com.pundix.xwallet:id/iv_recod" and @instance=8]')
        self.driver.find_element(*XPASS_ETH).click()  # 点击XPASS卡的ETH
        time.sleep(3)

    def into_XPASS_card(self):
        """进入XPASS card页面"""

        self.click2('black')

    def click_card_setting(self):
        """点击卡片的设置"""

        self.into_XPASS_card()
        self.driver.find_element(*self.Virtual_Setting).click()  # 点击黑卡的设置

    def click_card_bill(self):
        """点击卡片的账单"""

        self.into_XPASS_card()
        self.driver.find_element(*self.Virtual_bills).click()  # 点击黑卡的账单

    def click_card_eye(self):
        """点击卡片的眼睛，加密余额"""

        self.driver.find_element(*self.Virtual_Eye).click()

    def into_coin_detail(self, coin):

        self.click2(coin)
        time.sleep(2)

    def check_QR_code(self):
        """检查是否加载付款二维码是否正确"""

        if self.driver.find_element(*self.QR_code).is_enabled():  # 判断元素是否可用
            return True
        else:
            return False

    def click_refresh(self):
        """点击付款二维码下的刷新按钮"""

        if self.check_QR_code():
            self.driver.find_element(*self.Virtual_refresh).click()
            time.sleep(1)
        else:
            raise ConnectionError

    def click_more(self):
        """点击卡片详情页中的更多按钮"""

        self.driver.find_element(*self.Virtual_Menu).click()

    def click_card_internal_transfer(self):
        """点击卡片中的内部划转"""

        self.click_more()
        self.driver.find_element(*self.Virtual_Internal_Transfer).click()
        time.sleep(1)

    def click_card_instrucment(self):
        """点击卡片中的说明"""

        self.click_more()
        self.driver.find_element(*self.card_instrucment).click()
        time.sleep(3)

    def check_card_Receive(self):
        """
        卡片的 充值  功能
        针对：BTC ETH NPXS
        """

        self.driver.find_element(*self.Virtual_Receive).click()
        time.sleep(2)
        self.driver.find_element(*self.Virtual_view_Address).click()
        time.sleep(1)
        if self.driver.find_element(*self.receive_address).is_enabled():
            self.driver.find_element(*self.Virtual_Copy_Address).click()
            return True
        else:
            return False

    def click_card_transfer(self, switch=0):
        """
        点击卡片的 转账  功能
        针对：BTC ETH NPXS
        """

        self.driver.find_element(*self.Virtual_transfer).click()
        # 是否开启2FA，默认不开启
        if switch == 0:  # 不开启2FA
            if self.driver.find_element(*self.Google_Notnow).is_enabled():
                self.driver.find_element(*self.Google_Notnow).click()
                time.sleep(1)
            else:
                pass
        else:  # 开启2FA
            if self.driver.find_element(*self.Google_Notnow).is_enabled():
                self.driver.find_element(*self.Google_confirm).click()
                time.sleep(1)
            else:
                pass
        self.driver.find_element(*self.Virtual_transfer).click()

    def transfer(self, address, money):
        """
        输入卡片的 转账  数据
        针对：BTC ETH NPXS
        """

        self.click_card_transfer()
        time.sleep(2)
        self.driver.find_element(*self.Transfer_Address).send_keys(address)
        self.driver.find_element(*self.Transfer_money).send_keys(money)
        time.sleep(3)
        self.driver.find_element(*self.Tranfer_Next).click()



