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

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', Base.android_driver_caps)  # 串联
        time.sleep(5)  # 等待初始化完成
        cls.login_page = LoginPage(cls.driver)  # 初始化登录页元素以及方法
        cls.login_page.check_in()
        time.sleep(1)
        cls.login_page.login_by_Email(' 476367003@xinjineng.net', 'Aa123456')
        time.sleep(5)
        cls.user_page = UsercenterPage(cls.driver)  # 初始化个人中心页元素以及方法
        cls.user_page.go_to_usercenter()
        time.sleep(2)

        # def test_100_vouchers(self):
        #     """ 我的优惠券"""
        #     time.sleep(3)
        #     self.user_page.my_vouchers()

        # def test_101_kyc(self):
        #     """设置KYC-第一页"""
        #     time.sleep(2)
        #     self.user_page.setting_kyc('first', 'second', 'third', '6742384')

        # def test_102_change_phone(self):
        #     """设置 -- 修改手机号"""
        #     time.sleep(3)
        #     self.user_page.change_phone(2222, 4120909090)
        #     time.sleep(3)
        #     self.user_page.change_phone_call()
        #
        # def test_103_change_email(self):
        #     """ 修改邮箱地址"""
        #     time.sleep(3)
        #     self.user_page.change_email(2222, '120@qq.com')

        # def test_104_change_loginPWD(self):
        #     """修改登录密码"""
        #     time.sleep(2)
        #     self.user_page.change_login_pwd('Test1234')

        # def test_105_change_payPWD(self):
        #     """修改支付密码"""
        #     time.sleep(2)
        #     self.user_page.change_payPwd('123456')

        # def test_106_forget_payPwd(self):
        #     """忘记支付密码"""
        #     time.sleep(2)
        #     self.user_page.forget_payPwd('2222')

        # def test_107_pattern(self):
        #     """手势密码设置"""
        #     time.sleep(2)
        #     self.user_page.pattern()

        # def test_108_fingerprint(self):
        #     """指纹识别设置"""
        #     time.sleep(2)
        #     self.user_page.fingerprint()

        # def test_109_google(self):
        #     """谷歌验证码"""
        #     time.sleep(2)
        #     self.user_page.google('2222')


    def test_001_check_code(self):
        time.sleep(2)
        self.user_page.into_Collection()  # 进入收款页面
        time.sleep(1)
        self.assertTrue(self.user_page.check_QR_code(), '判断是否加载收款二维码成功')

    def test_002_save_code(self):
        # self.user_page.into_Collection()  # 进入收款页面
        time.sleep(1)
        self.user_page.save_QRcode()
        self.assertTrue(self.user_page.is_toast_exist('Image'), '判断是否保存收款二维码成功')

    def test_003_collection_history(self):
        # self.user_page.into_Collection()  # 进入收款页面
        time.sleep(1)
        self.user_page.check_collection_history()
        time.sleep(1)
        self.assertTrue(self.user_page.findElement('Status'), '判断是否加载收款详情成功')
        self.assertFalse(self.user_page.is_toast_exist('Sever'), '判断是否出现500')

    def test_004_collection_refund(self):
        time.sleep(1)
        self.user_page.refund_collection()

    def test_005_assets_account(self):
        self.driver.back()
        self.driver.back()
        self.driver.back()   # 退回个人中心页面
        self.user_page.into_Assets()  # 进入总资产页面
        time.sleep(2)
        self.user_page.click2(self.user_page.Assets_Accounts)  # 总资产-Accounts
        self.assertFalse(self.user_page.is_toast_exist('Sever'), '判断是否出现500')

    def test_006_assets_coin(self):
        time.sleep(1)
        self.user_page.click2(self.user_page.Assets_Coins)  # 总资产-Coins
        self.assertFalse(self.user_page.is_toast_exist('Sever'), '判断是否出现500')

    def test_007_bills_detail(self):
        self.driver.back()
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
        self.driver.back()
        time.sleep(2)
        self.user_page.into_internal_transfer()  # 进入内部划转
        time.sleep(2)
        self.user_page.virtual_to_black('BTC')  # 选择虚拟卡到黑卡
        self.user_page.virtual_to_black_little('0.00000001')  # 划转小金额的BTC
        self.assertTrue(self.user_page.is_toast_exist('successful'), '判断转账是否成功')

    @unittest.skip('防止不够钱转账')
    def test_009_internal_transfer_all(self):
        time.sleep(2)
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
        time.sleep(2)
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
            time.sleep(2)

    def test_011_into_feedback(self):
        self.driver.back()
        self.driver.back()
        self.driver.back()
        time.sleep(3)
        self.user_page.into_help()  # 进入feedback页面
        time.sleep(2)
        self.user_page.into_help_FAQ()
        time.sleep(10)
        self.driver.back()
        time.sleep(2)
        self.user_page.into_help_feedback()
        time.sleep(10)
        self.driver.back()
        time.sleep(2)
        self.user_page.into_help_disclaimer()
        time.sleep(5)

    def test_012_edit_user_detail(self):

        self.driver.back()
        self.driver.back()
        time.sleep(1)
        self.user_page.complete_user_picture()  # 上传头像
        self.assertTrue(self.user_page.is_toast_exist('uploaded'), '判断上传头像成功')
        self.user_page.complete_user_gender()
        self.assertTrue(self.user_page.is_toast_exist('Saved'), '判断保存性别成功')
        self.driver.back()

    def test_013_general(self):
        """通用 - 语言及货币选择 """
        time.sleep(2)
        self.user_page.general()
        # print(self.driver.page_source)

    def test_014_about(self):
        self.driver.back()
        self.driver.back()
        """关于界面"""
        time.sleep(2)
        self.user_page.about()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=0)
