from PO.basePage import Base
from selenium.webdriver.common.by import By
import time


class CardPage(Base):
    """
    虚拟卡+黑卡的页面元素，以及操作
    """

    # DAPP页面 虚拟卡片 DAPP首页
    Virtual_BTC = "BTC"  # 虚拟卡片中的BTC
    Virtual_ETH = "ETH " #虚拟卡片中的ETH
    Virtual_Go = "virtual"  #虚拟卡片中的"更多"键

    #卡片详情页面
    Virtual_Eye = (By.ID, "tv_amout")  #虚拟卡片中的加密按键
    Virtual_Setting = (By.ID, "iv_setting")  #虚拟卡片片中的设置按键
    Virtual_bills =(By.ID, "iv_bills")  #虚拟卡片中的账单按键
    Virtual_Receive =(By.ID, "btn_recharge")  #查看虚拟卡片充值地址
    Virtual_transfer =(By.ID, "btn_withdraw")  #查看虚拟卡片转账地址
    Virtual_Menu =(By.ID, "iv_menu")    #虚拟卡片详情页面的菜单按键
    Virtual_Internal_Transfer = (By.ID, "tv_refresh")   #虚拟卡片界面点击卡内划转
    Virtual_Back =(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ImageButton")    #虚拟卡片详情页面左上角返回按钮

    Virtual_refresh =(By.ID, "iv_refresh") #虚拟卡片页面的二维码刷新按键
    Virtual_view_Address = (By.ID, "btn_view_recharge")  #虚拟卡片查看充值地址，提醒页面
    receive_address = (By.ID, 'iv_single_qr_code')  # 充值地址
    Virtual_Copy_Address = (By.ID, "btn_single_copy") #复制虚拟卡片充值地址
    Receiving_address_close =(By.ID, "iv_close") #查看充值地址说明页面的关闭按键
    QR_code = (By.ID, 'iv_qr_code')  # 付款码
    card_instrucment = (By.ID, 'tv_help')

     # 转账页面
    Transfer_Address=(By.ID,"ed_receivingAddress")  #在转账页面，选择添加地址
    Transfer_money = (By.ID, 'ed_coinNumber')  # 充值金额
    Transfer_Scan =(By.ID, "iv_iconScan")      #在转账页面，点击扫码
    Transfer_Amount_All =(By.ID, "tv_allCoinNumber")    #在转账页面金额转出all
    Transfer_server =(By.ID, "tv_serviceCharge")    #在转账页面查看手续费说明
    Transfer_KYC =(By.ID, "tv_kycVerify")   #在转账页面点击KYC认证
    Tranfer_Next = (By.ID, "btn_withdraw")  #转账页面点击下一步
    Add_Address =(By.ID, "iv_menu")     #转账页面添加转账地址
    edit_email = (By.ID, 'ed_email_code')  #

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

    #内部划账
    Virtual_Internal_Transfer2 = (By.ID, "tv_refresh")       #虚拟卡片中内部划转入口
    Virtual_Internal_Transfer_back = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageButton")       #内部划转左上角返回键
    Virtual_Internal_Transfer_change = (By.ID, "iv_exchange")       #虚拟卡片内部划转切卡片位置
    Virtual_Internal_Transfer_FromCard = (By.ID,"tv_from_card_id")      #内部划转选择From方卡片
    Virtual_Internal_Transfer_Tocard = (By.ID, "tv_to_card_id")     #内部划转选择To方卡片
    Virtual_Internal_Transfer_Accoutclose = (By.ID, "ll_close")       #内部划转在选择卡片时，点击X
    Virtual_Internal_Transfer_Accountselect = (By.ID,"rl_layout_pay_type")    #内部划转，选择转账卡片
    Virtual_Internal_Transfer_Coin = (By.ID, "tv_cion")     #内部划转选择点击下拉币种
    Virtual_Internal_Transfer_Coinselect = (By.ID,"rl_layout_pay_type")     #内部划转选择币种
    Virtual_Internal_Transfer_ALl = (By.ID, "tv_available_all")     #内部划转金额选择all
    Virtual_Internal_Transfer_Available = (By.ID, "ed_available")       #内部划转手动输入金额
    Virtual_Internal_Transfer_Confirm = (By.ID, "btn_transfer")     #内部划转选择确认

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



