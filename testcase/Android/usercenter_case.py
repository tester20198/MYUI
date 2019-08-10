from appium import webdriver
import unittest
from PO.Android.loginPage import LoginPage
from PO.Android.usercenterPage import UsercenterPage
from PO.basePage import Base
import time


class UsercenterTestCase(unittest.TestCase):
    """
    个人中心的测试用例
    """

    def setUp(self):
        Base.android_driver_caps["noReset"] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', Base.android_driver_caps)  # 串联
        # time.sleep(5)  # 等待初始化完成
        # cls.login_page = LoginPage(cls.driver)  # 初始化登录页元素以及方法
        # cls.login_page.check_in()
        # time.sleep(1)
        # cls.login_page.login_by_Email(' 476367003@xinjineng.net', 'Aa123456')
        # time.sleep(5)
        self.user_page = UsercenterPage(self.driver)  # 初始化个人中心页元素以及方法
        time.sleep(5)  # 等待初始化完成
        self.user_page.go_to_usercenter()
        time.sleep(5)


    def test_001_google(self):
        """谷歌验证码"""

        self.user_page.google('2222','12345')  # 不进行完整的开启2FA功能

    def test_002_save_code(self):
        """检查并保存商户收款码"""

        self.user_page.into_Collection()  # 进入收款页面
        time.sleep(1)
        self.assertTrue(self.user_page.check_QR_code(), '判断是否加载收款二维码成功')
        self.user_page.save_QRcode()
        self.assertTrue(self.user_page.is_toast_exist('Image'), '判断是否保存收款二维码成功')

    def test_003_collection_history(self):
        """查看商户收款记录，和退款"""

        self.user_page.into_Collection()  # 进入收款页面
        self.user_page.check_collection_history()
        time.sleep(1)
        self.assertTrue(self.user_page.findElement('Status'), '判断是否加载收款详情成功')
        self.setUp()
        self.user_page.refund_collection()

    def test_004_fingerprint(self):
        """指纹识别设置"""

        self.user_page.fingerprint()
        self.assertTrue(self.user_page.is_toast_exist('one'), '提示需要添加指纹')  # 测试机器没有录入指纹

    def test_005_assets_account(self):
        """检查总资产页面"""

        self.user_page.into_Assets()  # 进入总资产页面
        time.sleep(2)
        self.user_page.click2(self.user_page.Assets_Accounts)  # 总资产-Accounts
        self.assertFalse(self.user_page.is_toast_exist('Sever'), '判断是否出现500')
        self.user_page.click2(self.user_page.Assets_Coins)  # 总资产-Coins
        self.assertFalse(self.user_page.is_toast_exist('Sever'), '判断是否出现500')

    def test_006_pattern(self):
        """手势密码设置"""

        self.user_page.pattern()
        self.assertTrue(self.user_page.findElement('RESET'), '检查是否能跳转到开启手势解锁设图界面')

    def test_007_bills_detail(self):
        """遍历各个账单"""

        self.user_page.into_Bill()  # 进入总账单
        time.sleep(2)
        self.user_page.click_bill_type()
        self.driver.back()
        self.user_page.click_bill_card()
        self.driver.back()
        time.sleep(1)
        self.user_page.check_every_type_bill()  # 检查各个账单类型
        self.assertFalse(self.user_page.is_toast_exist('Sever'), '判断是否出现500')

    def test_008_internal_transfer(self):
        """BTC内部转账"""

        self.user_page.into_internal_transfer()  # 进入内部划转
        time.sleep(2)
        self.user_page.virtual_to_black('BTC')  # 选择虚拟卡到黑卡
        self.user_page.virtual_to_black_little('0.00000001')  # 划转小金额的BTC
        self.assertTrue(self.user_page.is_toast_exist('successful'), '判断转账是否成功')

    # @unittest.skip('防止XPASS卡不够钱转账')
    def test_009_internal_transfer_all(self):
        """NPXS 来回内部转账"""

        self.user_page.into_internal_transfer()  # 进入内部划转
        time.sleep(2)
        self.user_page.virtual_to_black('NPXS')  # 选择虚拟卡到黑卡
        self.user_page.transfer_all()  # 虚拟卡划转全部金额到黑卡
        self.assertTrue(self.user_page.is_toast_exist('successful'), '判断转账是否成功')

        # 原地划转返回，方便多次run case
        time.sleep(2)
        self.user_page.into_internal_transfer()
        time.sleep(5)
        self.user_page.virtual_to_black('NPXS')  # 选择虚拟卡到黑卡
        self.user_page.change_card()  # 切换卡片位置
        self.user_page.transfer_all()  # 黑卡划转全部金额到虚拟卡
        self.assertTrue(self.user_page.is_toast_exist('successful'), '判断转账是否成功')

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

        self.user_page.complete_user_picture()  # 上传头像
        self.assertTrue(self.user_page.is_toast_exist('uploaded'), '判断上传头像成功')
        self.user_page.complete_user_gender()
        self.assertTrue(self.user_page.is_toast_exist('Saved'), '判断保存性别成功')
        self.driver.back()

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

        self.user_page.change_phone(2222, 4120909090, 2222)
        self.assertTrue(self.user_page.is_toast_exist('registered'))

    def test_018_change_email(self):
        """ 修改邮箱地址"""

        self.user_page.change_email(2222, '476367003@qq.com','1111')
        # self.assertTrue(self.user_page.is_toast_exist(''), '判断是否新邮箱已被注册')

    def test_019_change_loginPWD(self):
        """修改登录密码"""

        self.user_page.change_login_pwd('Aa123456')
        self.assertTrue(self.user_page.is_toast_exist('same'), '判断是否重复密码')

    def test_020_change_payPWD(self):
        """修改支付密码"""

        self.user_page.change_payPwd('123456')
        self.assertTrue(self.user_page.is_toast_exist('same'), '判断是否重复密码')

    def test_021_forget_payPwd(self):
        """忘记支付密码"""

        self.user_page.forget_payPwd('2222','123456')
        self.assertTrue(self.user_page.is_toast_exist('same'), '判断是否重复密码')


if __name__ == '__main__':
    unittest.main(verbosity=0)
