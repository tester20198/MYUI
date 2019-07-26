from PO.basePage import Base
from selenium.webdriver.common.by import By
import time


class UsercenterPage(Base):
    """
    个人中心的页面元素
    """

    # ———————————————————————头像区域——————————————————————————#
    head = (By.ID, 'iv_head')  # 头像
    nickname = (By.ID, 'tv_nickname')  # 昵称
    change_head = (By.ID, 'rl_layout_hand')  # 头像—进入手机相机
    head_gallery = (By.ID, 'btn_gallery')  # 手机相册
    head_photo = (By.ID, 'btn_picturey')  # 照相
    photo = (By.XPATH,
             '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ImageView')  # x选择照片
    photo_back = (By.XPATH,
                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageButton')  # 相册页面的返回
    gender = (By.ID, 'iv_gender_arrow')  # 性别
    ok = (By.ID, 'tv_complete')  # 性别选择框-ok
    cancel = (By.ID, 'tv_cancel')  # 性别选择框-cancel
    option_btn = (By.ID, 'options1')  # 第一选项

    # ———————————————————————收款码——————————————————————————#
    Collection = (By.ID, 'rl_layout_collection')  # 收款码入口
    collection_history = (By.ID, 'tv_collect_record')  # 收款历史
    collection_help = (By.ID, 'iv_menu')  # 帮助按钮
    QR_code = (By.ID, 'iv_qr_code')  # 二维码
    save_code = (By.ID, 'tv_save')  # 保存二维码
    time_filter = (By.ID, 'tv_timer')  # 收款历史日期筛选
    start_time = (By.ID, 'tv_startTime')  # 开始时间
    end_time = (By.ID, 'tv_endTime')  # 结束时间
    ok_btn = (By.ID, 'tv_menu')  # ok按钮

    # ———————————————————————总资产——————————————————————————#
    Assets = (By.ID, 'rl_layout_assets')  # 资产
    Assets_Account = 'Accounts'
    Assets_Coint = 'Coins'

    # ———————————————————————总账单——————————————————————————#
    Bills = (By.ID, 'rl_layout_bill')  # 总账单
    bill_type = (By.ID, 'tv_order_type')  # 账单类别分类
    bill_card = (By.ID, 'tv_card_type')  # 账单卡片分类
    bill_list = (By.XPATH,
                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]')  # 账单列表第一个
    Receive = 'Receive'  # 收款类型
    Expenditure = 'Expenditure'  # 消费类型
    Transfer = 'Transfer'  # 转账类型
    Extra = 'Extra'  # 活动类型
    Distribution = 'Distribution'
    Collection1 = 'Collection'  # 收款类型
    Refund = 'Refund'  # 退款类型
    Crypto_Gift_Sent = 'Crypto_Gift_Sent'  # telegram红包发送
    Crypto_Gift_Received = 'Crypto_Gift_Received'  # telegram红包接收
    Crypto_Gift_Refund = 'Crypto_Gift_Refund'  # telegram红包退款
    All_Types = 'All_Types'

    # ———————————————————————内部划转——————————————————————————#
    Internal_Transfer = (By.ID, 'rl_layout_transfer')  # 内部划转入口
    from_card = (By.ID, 'tv_from_card_id')  # from哪张卡
    to_card = (By.ID, 'tv_to_card_id')  # to哪张卡
    exchange = (By.ID, 'iv_exchange')  # 交换卡的位置
    coins_selector = (By.ID, 'tv_cion')  # 选择币种
    close_btn = (By.ID, 'll_close')  # 关闭按钮
    edit_money = (By.ID, 'ed_available')  # 输入金额
    all_btn = (By.ID, 'tv_available_all')  # 点击all按钮
    confirm_transfer = (By.ID, 'btn_transfer')  # 确认划转

    # ———————————————————————优惠券——————————————————————————#
    coupon = (By.ID, 'rl_layout_coupon')  # 优惠券

    # ———————————————————————KYC——————————————————————————#
    kyc = (By.ID, 'rl_layout_personal_center')  # KYC

    # ———————————————————————个人中心——————————————————————————#
    setting = (By.ID, "rl_layout_setting")  # 个人中心的设置

    # ———————————————————————商户申请——————————————————————————#
    merchant = (By.ID, 'rl_layout_merchant_setting')  # 商户申请
    first_name = (By.XPATH,
                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText')
    last_name = (By.XPATH,
                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[3]/android.widget.EditText')
    id = (By.XPATH,
          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[4]/android.widget.EditText')
    invitation_code = (By.ID, 'invitationCode')  # 邀请码
    next_btn = (By.ID, 'onMerchantPrincipal')  # next按钮
    work_pic = (By.ID, 'paperworkPicture')  # 上传营业执照
    take_pic = (By.ID, 'tv_camera')  # 拍照
    select_pic = (By.ID, 'tv_album')  # 选择照片
    firs_pic = (By.ID, 'icon_thumb')  # 图库里第一张图片
    cancel_btn = (By.ID, 'tv_cancel')  # 取消按钮
    header_pic = (By.ID, 'paperworkPictureHand')  # 工作地点
    next1_btn = (By.ID, 'onMerchantVerified')  # 第二个next按钮
    logo_pic = (By.ID, 'uploadPhotoFileIco')  # 商户logo
    store_name = (By.XPATH,
                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[4]/android.widget.EditText')
    store_type = (By.ID, 'xwalletMerchantStoreTypeText')  # 商户类型
    store_phone = (By.XPATH,
                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[6]/android.widget.EditText')
    store_help = (By.ID, 'goHowToApply')  # 商户帮助说明

    # ———————————————————————工单——————————————————————————#
    help_btn = (By.ID, 'rl_layout_help_feedback')  # feedback

    # ———————————————————————优惠券——————————————————————————#
    my_Vouchers = (By.ID, 'rl_layout_coupon')  # 我的优惠券
    my_Vouchers_Not = (By.ID, 'tv_invalid')  # 我的优惠券-无法使用
    my_Vouchers_instructions = (By.ID, 'iv_menu')  # 我的优惠券说明

    # ———————————————————————KYC——————————————————————————#
    KYC_btn = (By.ID, 'rl_layout_personal_center')  # KYC入口
    KYC_go = (By.ID, 'webView')  # go to KYC
    KYC_birth = (By.ID, 'birth')  # KYC出生日期选择
    KYC_nationality = (By.ID, 'click_country')  # KYC国籍选择
    KYC_firstName = (By.ID, 'firstName')  # KYC-firstName
    KYC_middleName = (By.ID, 'middleName')  # KYC-middleName
    KYC_lastname = (By.ID, 'lastname')  # KYC-last—name
    KYC_number = (By.ID, 'ed_id_number')  # KYC-ID number
    KYC_submit = (By.ID, 'btn_submit')  # KYC-第一页提交
    KYC_instructions = (By.ID, 'iv_menu')  # KYC-第一页说明


    # ———————————————————————设置入口——————————————————————————#
    setting_btn = (By.ID, 'rl_layout_setting')  # 设置入口

    # ———————————————————————修改手机号——————————————————————————#
    setting_phone = (By.ID, 'tv_mobile')  # 设置-手机号
    send_email_code = (By.ID, 'tv_send_email_code')  # 设置-发送邮箱验证码
    send_sms_code = (By.ID, 'tv_send_sms_code')  # 设置-发送短信验证码
    verification_email_code = (By.ID, 'ed_email_code')  # 设置-确认邮箱验证码
    verification_sms_code = (By.ID, 'ed_sms_code')  # 设置-确认短信验证码
    phone_nationality = (By.ID, 'tv_select_country')  # 设置-手机号-选择国籍
    phone_new = (By.ID, 'et_phone_number')  # 设置-手机号-新手机号
    phone_new__code = (By.ID, 'tv_send_news_code')  # 设置-新手机号发送验证码
    phone_new_Verification_code = (By.ID, 'ed_news_code')  # 设置-新手机号确认验证码
    phone_new_confirm = (By.ID, 'btn_confirm')  # 设置-手机号-确认

    # ———————————————————————修改邮箱，与修改手机号元素一致——————————————————————————#
    Setting_Email = (By.ID, 'tv_email')  # 设置-邮箱
    email_new = (By.ID, 'et_email')  # 设置-手机号-新手机号

    # ———————————————————————手势密码、指纹识别、谷歌验证码——————————————————————————#
    Setting_Security_btn = (By.ID, 'rl_safety')  # 设置-安全中心入口
    Setting_Security_pattern = (By.ID, 'switch_gesture')  # 设置-安全中心-手势密码
    Setting_Security_fingerprint = (By.ID, 'switch_fingerprint')  # 设置-安全中心-指ew纹识别
    Setting_Security_google = (By.ID, 'switch_google_authen')  # 设置-安全中心-谷歌验证码

    # ———————————————————————修改登录密码——————————————————————————#
    Setting_Security_loginPWD = (By.ID, 'rl_safety_login_pass')  # 设置-安全中心-修改登录密码
    Setting_Security_loginOld = (By.ID, 'et_loginpass_old')  # 设置-安全中心-修改登录密码之旧密码
    Setting_Security_loginNew = (By.ID, 'et_loginpass_new')  # 设置-安全中心-修改登录密码之新密码
    Setting_Security_loginAgain = (By.ID, 'et_loginpass_again')  # 设置-安全中心-修改登录密码之新密码确认
    Setting_Security_loginModify = (By.ID, 'bt_loginpass_modify')  # 设置-安全中心-修改登录密码之确认

    # ———————————————————————修改支付密码——————————————————————————#
    Setting_Security_payPWD = (By.ID, 'rl_safety_pay_pass')  # 设置-安全中心-修改支付密码
    Setting_Security_payOld = (By.ID, 'et_paypass_old')  # 设置-安全中心-修改支付密码之旧密码
    Setting_Security_payNew = (By.ID, 'et_paypass_new')  # 设置-安全中心-修改支付密码之新密码
    Setting_Security_payAgain = (By.ID, 'et_paypass_again')  # 设置-安全中心-修改支付密码之新密码确认
    Setting_Security_payModify = (By.ID, 'bt_paypass_modify')  # 设置-安全中心-修改支付密码之确认
    Setting_Security_payForget = (By.ID, 'tv_forget_old_pass')  # 设置-安全中心-忘记支付密码入口

    # ———————————————————————通用、语言、货币——————————————————————————#
    Setting_General_btn = (By.ID, 'rl_common')  # 设置-通用入口
    Setting_General_languages = (By.ID, 'tv_language')  # 设置-通用语言
    Setting_General_languagesENG = (By.XPATH,
                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.RelativeLayout')  # 设置-通用语言英语
    Setting_General_currency = (By.ID, 'rl_common_currency')  # 设置-通用货币 (上下滑动调用)

    # ———————————————————————软件更新——————————————————————————#
    Setting_Software_Update = (By.ID, 'rl_version')  # 设置-软件更新

    # ———————————————————————设置-关于——————————————————————————#
    Setting_About_btn = (By.ID, 'rl_about')  # 设置-关于入口
    Setting_About_website = (By.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[2]')  # 设置-关于website
    Setting_About_email = (By.XPATH,
                           '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.TextView[2]')  # 设置-关于email
    Setting_About_twitter = (By.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]/android.widget.TextView[2]')  # 设置-关于twitter

    # ———————————————————————退出登录——————————————————————————#
    Setting_Loginout = (By.ID, 'tv_loginout')  # 设置-退出登录

    def my_vouchers(self):
        """我的优惠券"""
        self.driver.find_element(*self.my_Vouchers).click() # 进入我的优惠券入口
        time.sleep(1)
        self.driver.find_element(*self.my_Vouchers_Not).click() # 已使用优惠券
        time.sleep(2)
        self.driver.find_element(*self.my_Vouchers_instructions).click()    # 我的优惠券说明
        time.sleep(3)


    def setting_kyc(self,firstname,middleName,lastname,number):
        """ KYC ---- 选择日期未完成 """
        self.driver.find_element(*self.KYC_btn).click() # 进入kyc 界面
        time.sleep(2)
        self.driver.find_element(*self.KYC_go).click()
        time.sleep(3)
        self.driver.find_element(*self.KYC_birth).click()   # 选择出生日期及国籍
        time.sleep(3)
        self.driver.find_element(*self.KYC_nationality).click()
        time.sleep(3)
        self.driver.find_element(*self.KYC_firstName).send_key(firstname)   # 分别输入名字
        self.driver.find_element(*self.KYC_middleName).send_key(middleName)
        self.driver.find_element(*self.KYC_lastname).send_key(lastname)
        self.driver.find_element(*self.KYC_number).send_key(number)
        time.sleep(2)
        self.driver.find_element(*self.KYC_submit).click()  # kyc 第一页提交
        time.sleep(10)
        self.driver.find_element(*self.KYC_instructions).click()    # KYC第一页说明


    def change_phone(self,code,num):
        """修改手机号界面"""
        self.driver.find_element(*self.setting).click()    # 设置入口
        time.sleep(3)
        self.driver.find_element(*self.setting_phone).click()   # 修改手机号入口
        time.sleep(3)
        self.driver.find_element(*self.send_email_code).click()
        self.driver.find_element(*self.send_sms_code).click()   #发送短信、邮箱验证码
        time.sleep(2)
        self.driver.find_element(*self.verification_email_code).send_keys(code)
        time.sleep(2)
        self.driver.find_element(*self.verification_sms_code).send_keys(code)   # 输入短信、邮箱验证码
        time.sleep(2)
        self.driver.find_element(*self.phone_new).send_keys(num)    # 输入新手机号
        time.sleep(1)
        self.driver.find_element(*self.phone_new__code).click()
        time.sleep(3)
        self.driver.find_element(*self.phone_new_Verification_code).send_keys(code) # 发送及输入验证码
        time.sleep(2)
        self.driver.find_element(*self.phone_new_confirm).click()   # 修改提交





    def into_Collection(self):
        """ 进入收款码页面"""

        self.driver.find_element(*self.Collection).click()

    def into_Assets(self):
        """进入总资产界面"""

        self.driver.find_element(*self.Assets).click()

    def switch_Assets(self, type='coin'):
        """总资产切换选项"""

        if type == 'coin':
            self.driver.find_element_by_android_uiautomator('new UiSelector().text("Accounts")').click()
        else:
            self.driver.find_element_by_android_uiautomator('new UiSelector().text("Coins")').click()

    def into_Bill(self):
        """进入总账单"""

        self.driver.find_element(*self.Bills).click()

    def into_coupon(self):
        """进入优惠券"""

        self.driver.find_element(*self.coupon).click()

    def into_KYC(self):
        """进入kyc"""

        self.driver.find_element(*self.kyc).click()

    def into_setting(self):
        """进入设置界面"""

        self.driver.find_element(*self.setting).click()

    def into_merchant(self):
        """进入商户设置"""

        self.driver.find_element(*self.merchant).click()

    def into_help(self):
        """进入帮助界面"""

        self.driver.find_element(*self.help_btn).click()
