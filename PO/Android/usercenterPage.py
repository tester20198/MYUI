from PO.basePage import Base
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


class UsercenterPage(Base):
    """
    个人中心的页面元素
    """

    center = (By.ID, "iv_user_icon")  # 个人中心
    # ———————————————————————头像区域——————————————————————————#
    head = (By.ID, 'iv_head')  # 个人中心-头像
    head2 = (By.ID, 'rl_layout_hand')  # 个人资料-头像
    nickname = (By.ID, 'tv_nickname')  # 昵称
    change_head = (By.ID, 'rl_layout_hand')  # 头像—进入手机相机
    head_gallery = (By.ID, 'btn_gallery')  # 手机相册
    com = (By.ID, 'menu_crop')  # 确定选择照片
    head_photo = (By.ID, 'btn_picturey')  # 照相
    photo = (By.XPATH,
             '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ImageView')  # x选择照片
    photo_back = (By.XPATH,
                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageButton')  # 相册页面的返回
    gender = (By.ID, 'iv_gender_arrow')  # 性别
    ok = (By.XPATH, '//android.widget.TextView[@resource-id="com.pundix.xwallet:id/tv_complete"]')  # 性别选择框-ok
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
    collection_name = (By.ID, 'tv_name')  # 收款人名字
    refund = (By.ID, 'btn_out')  # 退款

    # ———————————————————————总资产——————————————————————————#
    Assets = (By.ID, 'rl_layout_assets')  # 资产
    Assets_Accounts = 'Accounts'
    Assets_Coins = 'Coins'

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
    other_card = (By.ID, 'tv_pay_name')  # 其他卡片
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
    invitation_code = (By.XPATH, '//android.widget.EditText[@resource-id="invitationCode"]')  # 邀请码
    next_btn = (By.ID, 'onMerchantPrincipal')  # next按钮
    work_pic = (By.ID, 'paperworkPicture')  # 上传营业执照
    take_pic = (By.ID, 'tv_camera')  # 拍照
    select_pic = (By.ID, 'tv_album')  # 选择照片
    first_pic = (By.XPATH, '//android.widget.ImageView[@resource-id="com.android.documentsui:id/icon_thumb"]')  # 图库里第一张图片
    cancel_btn = (By.ID, 'tv_cancel')  # 取消按钮
    header_pic = (By.ID, 'paperworkPictureHand')  # 工作地点
    next1_btn = (By.ID, 'onMerchantVerified')  # 第二个next按钮
    logo_pic = (By.XPATH, '//android.view.View[@resource-id="uploadPhotoFileIco"]')  # 商户logo
    store_name = (By.XPATH,
                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[4]/android.widget.EditText')
    store_type = (By.XPATH, '//android.view.View[@resource-id="xwalletMerchantStoreTypeText"]')  # 商户类型
    store_phone = (By.XPATH,
                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[6]/android.widget.EditText')
    store_help = (By.XPATH, '//android.view.View[@resource-id="goHowToApply"]')  # 商户帮助说明
    store_setting = 'Store Settings'
    usdt_btn = (By.ID, 'switch_settle_accounts')  # USDT结算开关

    # ———————————————————————工单——————————————————————————#
    help_btn = (By.ID, 'rl_layout_help_feedback')  # feedback
    help = (By.ID, 'll_layout_help')  # FAQ
    feedback = (By.ID, 'll_layout_feedbcak')  # feedback
    disclaimer = (By.ID, 'll_layout_disclaimer')  # disclaimer

    # ———————————————————————优惠券——————————————————————————#
    my_Vouchers = (By.ID, 'rl_layout_coupon')  # 我的优惠券
    my_Vouchers_Not = (By.ID, 'tv_invalid')  # 我的优惠券-无法使用
    my_Vouchers_instructions = (By.ID, 'iv_menu')  # 我的优惠券说明

    # ———————————————————————KYC——————————————————————————#
    KYC_btn = (By.ID, 'rl_layout_personal_center')  # KYC入口
    KYC_go = (By.ID, 'commonBigBtnKyc')  # go to KYC
    KYC_birth = (By.ID, 'birth')  # KYC出生日期选择
    KYC_birth_year = (By.ID, 'options3')  # KYC 出生日期之年选择
    KYC_brith_ok = (By.ID, 'tv_finish')  # KYC 出生日期之年选择确认
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
    new_code = (By.ID, 'tv_send_news_code')  # 设置-新手机、邮箱号发送验证码
    verification_new_code = (By.ID, 'ed_news_code')  # 设置-新手机、邮箱号确认验证码
    new_confirm = (By.ID, 'btn_confirm')  # 设置-手机号-确认
    cannot_used = (By.ID, 'tv_cannot_be_used')  # 手机号或邮箱无法使用说明
    call_phone_code = (By.ID, 'tv_send_phone_code')  # 语音识别发送验证码
    call_new_phone_code = (By.ID, 'tv_news_send_phone_code')  # 新手机号的语音识别

    # ———————————————————————修改邮箱，与修改手机号元素一致——————————————————————————#
    setting_Email = (By.ID, 'tv_email')  # 设置-邮箱
    email_new = (By.ID, 'et_email')  # 设置-手机号-新手机号

    # ———————————————————————手势密码、指纹识别、谷歌验证码——————————————————————————#
    security_btn = (By.ID, 'rl_safety')  # 设置-安全中心入口
    security_pattern = (By.ID, 'switch_gesture')  # 设置-安全中心-手势密码
    pattern_reset = (By.ID, 'resetBtn')  # 手势密码重置
    security_fingerprint = (By.ID, 'switch_fingerprint')  # 设置-安全中心-指ew纹识别
    security_google = (By.ID, 'switch_google_authen')  # 设置-安全中心-谷歌验证码
    goodle_confirm = (By.ID, 'btn_yes')  # 谷歌验证码，确认开启
    goodle_my_key = (By.ID,'tv_paste')  # 谷歌验证码粘贴
    goodle_2fa = (By.ID,'et_2fa_code')  # 输入谷歌验证码


    # ———————————————————————修改登录密码——————————————————————————#
    setting_Security_loginPWD = (By.ID, 'rl_safety_login_pass')  # 设置-安全中心-修改登录密码
    security_loginOld = (By.ID, 'et_loginpass_old')  # 设置-安全中心-修改登录密码之旧密码
    security_loginNew = (By.ID, 'et_loginpass_new')  # 设置-安全中心-修改登录密码之新密码
    security_loginAgain = (By.ID, 'et_loginpass_again')  # 设置-安全中心-修改登录密码之新密码确认
    security_loginModify = (By.ID, 'bt_loginpass_modify')  # 设置-安全中心-修改登录密码之确认


    # ———————————————————————修改支付密码——————————————————————————#
    setting_Security_payPWD = (By.ID, 'rl_safety_pay_pass')  # 设置-安全中心-修改支付密码
    security_payOld = (By.ID, 'et_paypass_old')  # 设置-安全中心-修改支付密码之旧密码
    security_payNew = (By.ID, 'et_paypass_new')  # 设置-安全中心-修改支付密码之新密码
    security_payAgain = (By.ID, 'et_paypass_again')  # 设置-安全中心-修改支付密码之新密码确认
    security_payModify = (By.ID, 'bt_paypass_modify')  # 设置-安全中心-修改支付密码之确认
    security_payForget = (By.ID, 'tv_forget_old_pass')  # 设置-安全中心-忘记支付密码入口
    payForget_pwd = (By.ID,'et_pay_password')    # 忘记支付密码 -- 输入新密码
    payForget_pwd2 = (By.ID,'et_confirm_pay_password') # 忘记支付密码 --- 输入新确认密码

    # ———————————————————————通用、语言、货币——————————————————————————#
    setting_General_btn = (By.ID, 'rl_common')  # 设置-通用入口
    setting_General_languages = (By.ID, 'tv_language')  # 设置-通用语言
    setting_General_languagesENG = (By.XPATH,
                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.RelativeLayout')  # 设置-通用语言英语
    setting_General_currency = (By.ID, 'rl_common_currency')  # 设置-通用货币 (上下滑动调用)
    nation_XPATH = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[11]/android.widget.RelativeLayout')  # 定位国家 Azerbaijan


    # ———————————————————————软件更新——————————————————————————#
    setting_Software_Update = (By.ID, 'rl_version')  # 设置-软件更新

    # ———————————————————————设置-关于——————————————————————————#
    setting_About_btn = (By.ID, 'rl_about')  # 设置-关于入口
    about_website = (By.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[2]')  # 设置-关于website
    about_email = (By.XPATH,
                           '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.TextView[2]')  # 设置-关于email
    about_twitter = (By.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]/android.widget.TextView[2]')  # 设置-关于twitter

    # ———————————————————————退出登录——————————————————————————#
    setting_Loginout = (By.ID, 'tv_loginout')  # 设置-退出登录

    def my_vouchers(self):
        """我的优惠券"""
        self.driver.find_element(*self.my_Vouchers).click()  # 进入我的优惠券入口
        time.sleep(1)
        self.driver.find_element(*self.my_Vouchers_Not).click()  # 已使用优惠券
        time.sleep(2)
        self.driver.find_element(*self.my_Vouchers_instructions).click()  # 我的优惠券说明
        time.sleep(3)

    def  setting_kyc(self, firstname, middleName, lastname, number):
        """ KYC ---- 选择日期未完成 """

        self.swipeUp()
        self.driver.find_element(*self.KYC_btn).click()  # 进入kyc 界面
        time.sleep(2)
        self.switch_to_view()   # 由于该按键是webdriver ，先切换视察再点击ID  或 直接点击显示文本
        time.sleep(2)
        if self.findElement('commonBigBtnKyc'):
            self.driver.find_element(*self.KYC_go).click()
            print('未KYC！')
        else:
            print('已KYC！')
        time.sleep(2)

        # self.driver.find_element(*self.KYC_firstName).send_key(firstname)  # 分别输入名字
        # self.driver.find_element(*self.KYC_middleName).send_key(middleName)
        # self.driver.find_element(*self.KYC_lastname).send_key(lastname)
        # self.driver.find_element(*self.KYC_number).send_key(number)
        # self.driver.find_element(*self.KYC_birth).click()  # 选择出生日期
        # time.sleep(3)
        # self.driver.find_element(*self.KYC_birth_year).click()  # 出生日期之年
        # while not self.findElement():
        #     self.swipeUp(duration=1000)
        #     self.swipeUp(duration=1000)
        # else:
        #     self.driver.find_element(*self.KYC_birth_year).click()
        # self.driver.find_element(*self.KYC_brith_ok).click()
        # self.driver.find_element(*self.KYC_nationality).click()  # 选择国籍
        # time.sleep(2)
        # self.driver.find_element(*self.KYC_submit).click()  # kyc 第一页提交
        # time.sleep(10)
        # self.driver.find_element(*self.KYC_instructions).click()  # KYC第一页说明

    def into_setting(self):
        """设置入口"""
        self.driver.find_element(*self.setting).click()  # 设置入口
        time.sleep(3)

    def change_phone_call(self):
        """修改手机号、邮箱的语音识别"""

        try:
            WebDriverWait(self.driver, timeout=70, poll_frequency=1).until(expected_conditions.presence_of_element_located(self.call_phone_code)).click()
        except Exception as e:
            print('找不到语音入口？')

    def change_phone(self, code, phone,newCode):
        """修改手机号"""
        self.into_setting()
        self.driver.find_element(*self.setting_phone).click()  # 修改手机号入口
        time.sleep(3)
        if self.findElement('tv_send_email_code'):
            self.driver.find_element(*self.send_email_code).click()  # 发送短信、邮箱验证码
            time.sleep(2)
            self.driver.find_element(*self.verification_email_code).send_keys(code)  # 邮箱验证码
        else:
            pass
        if self.findElement('tv_send_sms_code'):
            self.driver.find_element(*self.send_sms_code).click()
            time.sleep(2)
            self.driver.find_element(*self.verification_sms_code).send_keys(code)
        else:
            pass
        self.driver.find_element(*self.phone_new).send_keys(phone)  # 输入新手机号
        self.driver.find_element(*self.new_code).click()
        time.sleep(2)
        self.driver.find_element(*self.verification_new_code).send_keys(newCode)  # 发送及输入验证码
        self.change_phone_call()  # 新旧手机号的语音识别
        time.sleep(2)
        self.driver.find_element(*self.new_confirm).click()  # 修改提交

    def change_email(self, code, email,newCode):
        """修改邮箱界面"""

        self.into_setting()
        self.driver.find_element(*self.setting_Email).click()  # 修改邮箱入口
        time.sleep(2)
        if self.findElement('tv_send_email_code'):
            self.driver.find_element(*self.send_email_code).click()  # 发送短信、邮箱验证码
            time.sleep(2)
            self.driver.find_element(*self.verification_email_code).send_keys(code)  # 邮箱验证码
        else:
            pass
        if self.findElement('tv_send_sms_code'):
            self.driver.find_element(*self.send_sms_code).click()
            time.sleep(2)
            self.driver.find_element(*self.verification_sms_code).send_keys(code)
            self.change_phone_call()
        else:
            pass
        self.driver.find_element(*self.email_new).send_keys(email)  # 输入修改的新邮箱地址
        self.driver.find_element(*self.new_code).click()  # 发送新邮箱地址的验证码
        time.sleep(1)
        self.driver.find_element(*self.verification_new_code).send_keys(newCode)
        self.driver.find_element(*self.new_confirm).click()  # 提交修改的数据

    def into_general(self):
        """"安全中心入口"""
        self.into_setting()
        self.driver.find_element(*self.security_btn).click()  # 通用入口
        time.sleep(2)

    def change_login_pwd(self, pwd):
        """修改登录密码"""
        self.into_general()
        self.driver.find_element(*self.setting_Security_loginPWD).click()  # 修改登录密码入口
        time.sleep(3)
        self.driver.find_element(*self.security_loginOld).send_keys(pwd)  # 输入旧密码
        time.sleep(3)
        self.driver.find_element(*self.security_loginNew).send_keys(pwd)
        time.sleep(3)
        self.driver.find_element(*self.security_loginAgain).send_keys(pwd)  # 输入新密码及确认密码
        self.Sys_back()  # 收起 键盘
        time.sleep(2)
        self.driver.find_element(*self.security_loginModify).click()  # 提交确认
        time.sleep(2)

    def into_change_payPwd(self):
        """进入修改支付密码界面"""
        self.into_general()
        self.driver.find_element(*self.setting_Security_payPWD).click()  # 修改支付密码入口

    def change_payPwd(self, password):
        """ 修改支付密码 """
        self.into_change_payPwd()
        time.sleep(2)
        self.driver.find_element(*self.security_payOld).send_keys(password)  # 输入旧密码
        time.sleep(1)
        self.driver.find_element(*self.security_payNew).send_keys(password)
        time.sleep(1)
        self.driver.find_element(*self.security_payAgain).send_keys(password)  # 输入新密码及确认新密码
        time.sleep(2)
        self.Sys_back()  # 收起键盘
        self.driver.find_element(*self.security_payModify).click()  # 提交信息

    def forget_payPwd(self, code,pwd):
        """忘记支付密码"""
        self.into_change_payPwd()
        time.sleep(2)
        self.Sys_back()
        time.sleep(1)
        self.driver.find_element(*self.security_payForget).click()  # 忘记支付密码入口
        time.sleep(2)
        if self.findElement('tv_send_email_code'):
            self.driver.find_element(*self.send_email_code).click()  # 点击发送邮箱及短信验证码按键
            time.sleep(2)
            self.driver.find_element(*self.verification_email_code).send_keys(code)  # 输入邮箱及短信验证码
        else:
            pass
        time.sleep(2)
        if self.findElement('tv_send_sms_code'):
            self.driver.find_element(*self.send_sms_code).click()
            time.sleep(2)
            self.driver.find_element(*self.verification_sms_code).send_keys(code)
        else:
            pass
        time.sleep(2)
        self.driver.find_element(*self.new_confirm).click()  # 提交按键
        time.sleep(2)
        # self.driver.find_element(*self.payForget_pwd).click()
        self.driver.find_element(*self.payForget_pwd).send_keys(pwd) # 输入新密码
        # self.driver.find_element(*self.payForget_pwd2).click()
        self.driver.find_element(*self.payForget_pwd2).send_keys(pwd)
        time.sleep(1)
        self.driver.find_element(*self.new_confirm).click() # 提交确认按键

    def pattern(self):
        """ 手势密码设置 """
        self.into_general()
        time.sleep(2)
        self.driver.find_element(*self.security_pattern).click()  # 手势密码入口
        time.sleep(2)
        self.driver.find_element(*self.pattern_reset).click()  # 手势密码重置
        time.sleep(2)

    def fingerprint(self):
        """指纹识别"""
        self.into_general()
        self.driver.find_element(*self.security_fingerprint).click()  # 指纹识别入口

    def google(self, code,goodle):
        """谷歌验证"""

        self.into_general()
        self.driver.find_element(*self.security_google).click()  # 谷歌入口
        self.driver.find_element(*self.goodle_confirm).click()  # 开启谷歌验证码确认
        time.sleep(2)

        if self.findElement('tv_send_email_code'):
            self.driver.find_element(*self.send_email_code).click()  # 发送邮箱、手机验证码
            time.sleep(1)
            self.driver.find_element(*self.verification_email_code).send_keys(code)
        else:
            pass
        if self.findElement('tv_send_sms_code'):
            self.driver.find_element(*self.send_sms_code).click()
            time.sleep(1)
            self.driver.find_element(*self.verification_sms_code).send_keys(code)
        else:
            pass

        time.sleep(1)
        self.driver.find_element(*self.new_confirm).click()  # 确认提交
        time.sleep(2)
        self.driver.find_element(*self.new_confirm).click()  # 查看我的谷歌验证KEY
        time.sleep(2)
        self.driver.find_element(*self.goodle_my_key).click()
        time.sleep(1)
        self.driver.find_element(*self.goodle_2fa).send_keys(goodle) # 输入谷歌验证码
        time.sleep(1)
        # self.driver.find_element(*self.new_confirm).click()  # 确认提交(校验关闭了)


    def general(self):
        """通用 - 语言及货币选择"""
        self.into_setting()
        self.driver.find_element(*self.setting_General_btn).click()  # 通用入口
        time.sleep(2)
        self.driver.find_element(*self.setting_General_languages).click()  # 语言设置入口
        time.sleep(2)
        self.driver.find_element(*self.setting_General_languagesENG).click()  # 语言选择英语
        time.sleep(2)
        self.driver.find_element(*self.setting_General_currency).click()  # 货币设置入口
        time.sleep(2)
        while not self.findElement('Venezuela'):
            self.swipeUp()
            self.swipeUp()
        else:
            self.click2('Venezuela (USD)')  # 货币选择Ven
            time.sleep(2)

    def about(self):
        """ 关于界面 """

        self.into_setting()
        self.driver.find_element(*self.setting_About_btn).click()  # 设置关于入口
        time.sleep(3)
        self.driver.find_element(*self.about_website).click()  # 关于-website
        time.sleep(3)
        self.Sys_back()
        # self.driver.find_element(*self.about_email).click()  # 关于-email
        # time.sleep(3)
        # self.Sys_back()
        # self.driver.find_element(*self.about_twitter).click()  # 关于-twitter
        # time.sleep(3)
        # self.Sys_back()

    def software_update(self):
        """软件更新"""
        self.into_setting()
        self.driver.find_element(*self.setting_Software_Update).click()  # 软件更新

    def login_out(self):
        """ 退出登录 """
        self.into_setting()
        self.driver.find_element(*self.setting_Loginout).click()  # 确认退出登录


    def into_Collection(self):
        """ 进入收款码页面"""

        self.driver.find_element(*self.Collection).click()

    def check_QR_code(self):
        """
        检查二维码是否正常展示
        :return:
        """

        try:
            self.driver.find_element(*self.QR_code).is_displayed()  # 二维码出现
            return True
        except exceptions.NoSuchElementException as E:
            print('找不到收款二维码...', E)
            return False

    def save_QRcode(self):
        """
        保存收款二维码
        :return:
        """

        if self.check_QR_code():
            self.authority()
            self.driver.find_element(*self.save_code).click()
        else:
            raise exceptions.ElementNotVisibleException

    def check_collection_history(self):
        """进入收款历史记录"""

        self.driver.find_element(*self.collection_history).click()
        time.sleep(1)
        self.driver.find_element(*self.collection_name).click()
        time.sleep(1)

    def refund_collection(self):
        """商户收款-退款"""

        self.swipeUp()
        if self.findElement('Refund'):
            self.driver.find_element(*self.refund).click()
        else:
            print('不存在退款或者已经退款了...或者该用户不是商户...')

    def into_Assets(self):
        """进入总资产界面"""

        self.driver.find_element(*self.Assets).click()

    def switch_Assets(self, type='coin'):
        """总资产切换选项"""

        if type == 'coin':
            self.click2(self.Assets_Coins)
        else:
            self.click2(self.Assets_Accounts)
        time.sleep(1)

    def into_Bill(self):
        """进入总账单"""

        self.driver.find_element(*self.Bills).click()

    def click_bill_type(self):
        """点击总账单的账单类别按钮"""

        self.driver.find_element(*self.bill_type).click()

    def click_bill_card(self):
        """点击总账单的账单卡片按钮"""

        self.driver.find_element(*self.bill_card).click()

    def check_every_type_bill(self):
        """遍历所有订单类型订单详情"""

        bills = [self.Receive, self.Expenditure, self.Transfer, self.Extra, self.Distribution, self.Collection1,
                 self.Refund, self.Crypto_Gift_Sent, self.Crypto_Gift_Received, self.Crypto_Gift_Refund]
        for i in bills:
            if self.findElement(i):
                self.click2(i)
                time.sleep(2)
                print(f'______找到了{i}账单类型.')
                self.driver.back()
            else:
                pass
                print(f'------找不到该{i}类型账单...')

    def into_internal_transfer(self):
        """进入内部划转"""

        try:
            self.driver.find_element(*self.Internal_Transfer).click()
        except exceptions.NoSuchElementException:
            print('不存在内部划转入口...')
            pass

    def virtual_to_black(self, coin='BTC'):
        """内部划转，虚拟卡划转(BTC)到black卡"""

        self.driver.find_element(*self.to_card).click()  # 弹出卡片列表
        time.sleep(1)
        if self.findElement('black'):
            print('找到黑卡...')
            self.click2('black')  # 选择黑卡
        else:
            print('找不到黑卡...')
            raise exceptions.NoSuchElementException()

        self.driver.find_element(*self.coins_selector).click()  # 弹出币种列表
        time.sleep(1)
        self.click2(coin)  # 选择币种

    def virtual_to_black_little(self, money):
        """内部划转，虚拟卡划转小额到black卡，小额度"""

        self.driver.find_element(*self.edit_money).send_keys(money)
        self.driver.find_element(*self.confirm_transfer).click()
        time.sleep(2)

    def transfer_all(self):
        """
        内部划转，虚拟卡划转all到black卡，全部划转
        备注：为方便多次使用该函数，需要原地划转回去
        """

        self.driver.find_element(*self.all_btn).click()
        time.sleep(1)
        self.driver.find_element(*self.confirm_transfer).click()
        time.sleep(2)

    def change_card(self):
        """内部划转切换卡片"""

        self.driver.find_element(*self.exchange).click()

    def into_merchant(self):
        """进入商户设置"""

        self.swipeUp()
        time.sleep(1)
        self.driver.find_element(*self.merchant).click()

    def judge_merchant(self):
        """判断是否是商家"""

        if self.findElement(self.store_setting):
            print('已认证商户！')
            return True
        else:
            print('未认证商户！')
            return False

    def into_merchant_settings(self):
        """进入商户设置，查看商户详情"""

        if self.judge_merchant():
            self.driver.find_element(*self.store_setting).click()
            time.sleep(1)
        else:
            pass

    def change_merchant_usdt(self):
        """开启/关闭商户USDT结算"""

        if self.judge_merchant():
            self.driver.find_element(*self.usdt_btn).click()
            time.sleep(1)
        else:
            pass

    def into_merchant_help(self):
        self.driver.find_element(*self.store_help).click()
        time.sleep(5)

    def edit_merchant(self):
        self.driver.find_element(*self.first_name).send_keys('First')
        self.driver.find_element(*self.last_name).send_keys('Last')
        self.driver.find_element(*self.id).send_keys('312313124124')
        self.driver.find_element(*self.invitation_code).send_keys('AWD211')
        self.click2('Next')

    def upload_merchant_pic(self):
        self.click2('Photo of ID card')
        time.sleep(1)
        self.driver.find_element(*self.select_pic).click()  # 选择图库里的图片
        time.sleep(3)
        self.driver.find_element(*self.first_pic).click()  # 选择第一张图片
        time.sleep(10)
        self.click2('Photo of yourself holding the ID card')
        time.sleep(1)
        self.driver.find_element(*self.select_pic).click()  # 选择图库里的图片
        time.sleep(3)
        self.driver.find_element(*self.first_pic).click()  # 选择第一张图片
        time.sleep(10)
        self.click2('Next')

    def finish_merchant(self):
        self.driver.find_element(*self.logo_pic).click()
        time.sleep(1)
        self.driver.find_element(*self.select_pic).click()  # 选择图库里的图片
        time.sleep(3)
        self.driver.find_element(*self.first_pic).click()  # 选择第一张图片
        time.sleep(3)
        self.driver.find_element(*self.store_name).send_keys('hello')
        self.driver.find_element(*self.store_phone).send_keys('+584121580001')
        self.driver.find_element(*self.store_type).click()
        time.sleep(2)
        # ——————————————————————————————注意：此处省略了商户类型选择！！！

    def into_help(self):
        """进入帮助界面"""

        self.swipeUp()
        self.driver.find_element(*self.help_btn).click()

    def into_help_FAQ(self):
        """进入FAQ"""

        self.driver.find_element(*self.help).click()
        self.Sys_back()

    def into_help_feedback(self):
        """进入feedback"""

        self.driver.find_element(*self.feedback).click()
        self.Sys_back()

    def into_help_disclaimer(self):
        """进入disclaimer"""

        self.driver.find_element(*self.disclaimer).click()
        self.Sys_back()

    def go_to_usercenter(self):
        """进入个人中心"""

        if self.findElement('Skip'):
            self.click2('Skip')
        else:
            print('不存在telegram引导页面，无须点击Skip.')
            pass
        self.driver.find_element(*self.center).click()

    def complete_user_picture(self):
        """完善个人资料-头像"""

        self.driver.find_element(*self.head).click()  # 点击个人中心的头像
        time.sleep(2)
        self.driver.find_element(*self.head2).click()  # 点击个人资料的头像
        time.sleep(1)
        self.driver.find_element(*self.head_gallery).click()  # 选择图库的照片
        self.authority()
        self.driver.find_element(*self.first_pic).click()  # 选择第一张图片
        time.sleep(3)
        WebDriverWait(self.driver, timeout=60, poll_frequency=1).until(
            expected_conditions.presence_of_element_located(self.com)).click()
        time.sleep(5)

    def complete_user_gender(self):
        """修改个人资料-性别"""

        self.driver.find_element(*self.gender).click()
        time.sleep(1)
        # self.click2('Female')  # 选择女性
        self.driver.find_element(*self.ok).click()
        time.sleep(1)
