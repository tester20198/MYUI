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

    # ----------fx卡片主界面元素---------------
    fx_amout = (By.ID, "tv_amout")  # fx卡片里面的加密按钮
    fx_setting = (By.ID, "iv_setting")  # fx卡片里面的设置按钮
    fx_back_btn = (By.CLASS_NAME, "android.widget.ImageButton")  # fx卡片里面的左上角返回键
    fx_conversion_btn = "Conversion"  # 转换按钮
    fx_staking_btn = "Staking"  # 挖矿按钮
    FX_btn = "FX"  # fx按
    fx_NPXS_btn = "NPXS"  # npxs按钮
    fx_NPXSXEM_btn = "NPXSXEM"  # npxsxem按钮

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
    fx_transfer = (By.ID, "btn_withdraw")  # 转账按钮
    fx_type_name = (By.ID, "tv_type_name")  # 账单名称
    # 扫码按钮
    fx_sacn = (By.XPATH,
               "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.ImageView")
    fx_all = (By.ID, "tv_allCoinNumber")  # all按钮
    fx_transferNext = (By.ID, "btn_transferNext")  # 下一步按钮

    # ------------NPXS界面元素------------
    npxs_menu = (By.ID, "iv_menu")  # 帮助按钮
    npxs_transfer = (By.ID, "btn_transfer")  # NPXS转账
    npxs_add = (By.ID, "rl_layout_add")  # add按钮
    npxs_private = (By.ID, "ll_layout_private")  # private wallet account
    npxs_exchange = (By.ID, "iv_exchange")  # 切换按钮
    npxs_all = (By.ID, "tv_available_all")  # 全部按钮
    npxs_confirm = (By.ID, "btn_transfer")  # 确认转账按钮

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
        self.driver.find_element(*self.fx_conversion_btn)


    def enter_conversion(self):

        """
        进入转换的帮助按钮
        """
        self.driver.find_element(*self.fx_conversion_btn).click()
