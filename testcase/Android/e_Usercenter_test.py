from appium import webdriver
from Page.Android.UsercenterPage import UsercenterPage
from Page.basePage import Base
import pytest
import time


class UsercenterTestCase:
    """
    个人中心的测试用例
    """

    def setup_class(self):
        Base.android_driver_caps["noReset"] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', Base.android_driver_caps)  # 串联
        self.user_page = UsercenterPage(self.driver)  # 初始化个人中心页元素以及方法
        time.sleep(5)  # 等待初始化完成
        self.user_page.go_to_usercenter()
        time.sleep(5)

    @pytest.mark.skip('不用测试2FA')
    def test_001_google(self):
        """谷歌验证码"""

        self.user_page.google('2222', '12345')  # 不进行完整的开启2FA功能

    def test_002_save_code(self):
        """检查并保存商户收款码"""

        try:
            self.user_page.into_Collection()  # 进入收款页面
            time.sleep(1)

            assert self.user_page.check_QR_code()
            self.user_page.save_QRcode()
            assert self.user_page.is_toast_exist('Image')
        except (Exception, AssertionError):
            self.user_page.save_img('商户收款码')
            raise Exception

    def test_003_collection_history(self):
        """查看商户收款记录，和退款"""

        try:
            self.user_page.into_Collection()  # 进入收款页面
            time.sleep(2)
            self.user_page.check_collection_history()
            time.sleep(3)

            assert self.user_page.findElement('Status')
            time.sleep(2)
            self.user_page.refund_collection()
        except (Exception, AssertionError):
            self.user_page.save_img('商户退款详情页')
            raise Exception

    def test_004_fingerprint(self):
        """指纹识别设置"""

        try:
            self.user_page.fingerprint()

            assert self.user_page.is_toast_exist('one')  # 测试机器没有录入指纹
        except (Exception, AssertionError):
            self.user_page.save_img('添加指纹')
            raise Exception

    def test_005_assets_account(self):
        """检查总资产页面"""

        try:
            self.user_page.into_Assets()  # 进入总资产页面
            time.sleep(2)
            self.user_page.click2(self.user_page.Assets_Accounts)  # 总资产-Accounts
            assert not self.user_page.is_toast_exist('500')
            time.sleep(2)

            self.user_page.click2(self.user_page.Assets_Coins)  # 总资产-Coins
            assert not self.user_page.is_toast_exist('500')
        except (Exception, AssertionError):
            self.user_page.save_img('总资产')
            raise Exception

    def test_006_pattern(self):
        """手势密码设置"""

        try:
            self.user_page.pattern()

            assert self.user_page.findElement('RESET')
        except (Exception, AssertionError):
            self.user_page.save_img('手势解锁')
            raise Exception

    def test_007_bills_detail(self):
        """遍历各个账单"""

        try:
            self.user_page.into_Bill()  # 进入总账单
            time.sleep(2)
            self.user_page.click_bill_type()
            self.driver.back()
            self.user_page.click_bill_card()
            self.driver.back()
            time.sleep(1)

            self.user_page.check_every_type_bill()  # 检查各个账单类型
            assert not self.user_page.is_toast_exist('500')
        except (Exception, AssertionError):
            self.user_page.save_img('账单详情')
            raise Exception

    def test_018_internal_transfer(self):
        """BTC内部转账"""

        try:
            self.user_page.into_internal_transfer()  # 进入内部划转
            time.sleep(2)
            self.user_page.virtual_to_black('BTC')  # 选择虚拟卡到黑卡
            self.user_page.virtual_to_black_little('0.00000001')  # 划转小金额的BTC

            assert self.user_page.is_toast_exist('successful')
        except (Exception, AssertionError):
            self.user_page.save_img('内部划转')
            raise Exception

    def test_009_internal_transfer_all(self):
        """NPXS 来回内部转账"""

        try:
            self.user_page.into_internal_transfer()  # 进入内部划转
            time.sleep(2)
            self.user_page.virtual_to_black('NPXS')  # 选择虚拟卡到黑卡
            self.user_page.transfer_all()  # 虚拟卡划转全部金额到黑卡

            assert self.user_page.is_toast_exist('successful')
        except (Exception, AssertionError):
            self.user_page.save_img('全部内部划转')
            raise Exception

        # 原地划转返回，方便多次run case
        time.sleep(2)
        self.user_page.into_internal_transfer()
        time.sleep(5)
        self.user_page.virtual_to_black('NPXS')  # 选择虚拟卡到黑卡
        self.user_page.change_card()  # 切换卡片位置
        self.user_page.transfer_all()  # 黑卡划转全部金额到虚拟卡
        try:
            assert self.user_page.is_toast_exist('successful')
        except AssertionError:
            self.user_page.save_img('全部内部划转2')
            raise Exception

    def test_010_into_merchant(self):
        """进入商户"""

        self.user_page.into_merchant()  # 进入商户中心页面
        time.sleep(3)
        if self.user_page.judge_merchant():  # 判断是否是商户
            pass  # 另建case去测试
        else:
            self.user_page.into_merchant_help()  # 进入商户帮助说明
            self.driver.back()
            self.user_page.edit_merchant()  # 输入商户资料
            time.sleep(2)
            self.user_page.upload_merchant_pic()  # 上传商户图片
            time.sleep(2)
            self.user_page.finish_merchant()  # 完善商户资料

    def test_011_into_feedback(self):
        """进入帮助界面"""

        self.user_page.into_help()  # 进入feedback页面
        time.sleep(2)
        self.user_page.into_help_FAQ()
        time.sleep(2)
        self.user_page.into_help_feedback()
        time.sleep(2)
        self.user_page.into_help_disclaimer()

    def test_012_edit_user_detail(self):
        """修改个人资料"""

        try:
            self.user_page.complete_user_picture()  # 上传头像

            assert self.user_page.is_toast_exist('uploaded')
            self.user_page.complete_user_gender()
            assert self.user_page.is_toast_exist('Saved')
        except (Exception, AssertionError):
            self.user_page.save_img('个人资料')
            raise Exception

    def test_013_general(self):
        """通用 - 语言及货币选择 """

        self.user_page.general()

    def test_014_about(self):
        """关于界面"""

        self.user_page.about()

    def test_015_vouchers(self):
        """ 我的优惠券"""

        self.user_page.my_vouchers()

    def test_016_kyc(self):
        """设置KYC-第一页"""

        self.user_page.setting_kyc('first', 'second', 'third', '6742384')

    def test_017_change_phone(self):
        """设置 -- 修改手机号"""

        try:
            self.user_page.change_phone(2222, 4120909090, 2222)

            assert self.user_page.is_toast_exist('registered')
        except (Exception, AssertionError):
            self.user_page.save_img('修改手机号码')
            raise Exception

    def test_008_change_email(self):
        """ 修改邮箱地址"""

        try:
            self.user_page.change_email(2222, '476367003@xinjineng.net', 2222)

            assert self.user_page.is_toast_exist('registered')
        except (Exception, AssertionError):
            self.user_page.save_img('修改邮箱')
            raise Exception

    def test_019_change_loginPWD(self):
        """修改登录密码"""

        try:
            self.user_page.change_login_pwd('Aa123456')

            assert self.user_page.is_toast_exist('same')
        except (Exception, AssertionError):
            self.user_page.save_img('修改登录密码')
            raise Exception

    def test_020_change_payPWD(self):
        """修改支付密码"""

        try:
            self.user_page.change_payPwd('123456')

            assert self.user_page.is_toast_exist('same')
        except (Exception, AssertionError):
            self.user_page.save_img('修改支付密码')
            raise Exception

    def test_021_forget_payPwd(self):
        """忘记支付密码"""

        try:
            self.user_page.forget_payPwd('2222', 123456)

            assert self.user_page.is_toast_exist('same')
        except (Exception, AssertionError):
            self.user_page.save_img('忘记支付密码')
            raise Exception

    def teardown_class(self):
        self.driver.quit()


if __name__ == '__main__':
    pytest.main()
