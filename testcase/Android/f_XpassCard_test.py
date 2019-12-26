from appium import webdriver
from Page.Android.DappVirtualCardPage import DAPPPage
from Page.basePage import Base
import pytest
import time


class TestXpassCard:
    """
    XPASS卡的测试用例
    """

    def setup_class(self):
        time.sleep(2)
        Base.android_driver_caps["noReset"] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', Base.android_driver_caps)  # 串联
        self.xpass_page = DAPPPage(self.driver)  # 初始化个人中心页元素以及方法
        time.sleep(8)  # 等待初始化完成

    def test_001_check_add_XPASS(self):
        """添加XPASS"""

        try:
            self.xpass_page.save_img('添加XPASS卡')
            self.xpass_page.add_XPASS_card(num='8011008881951290', pin='123456')

            assert self.xpass_page.is_toast_exist('already')
        except (Exception, AssertionError):
            self.xpass_page.save_img('添加XPASS卡')
            raise Exception

    def test_002_check_XPASS_card(self):
        """检查XPASS细节"""

        self.xpass_page.into_XPASS_card()
        time.sleep(3)
        self.xpass_page.click_card_setting()  # 卡片设置
        time.sleep(3)
        self.driver.back()
        self.xpass_page.click_card_bill()  # 卡片账单
        time.sleep(3)
        self.driver.back()
        self.xpass_page.click_card_eye()  # 卡片金额加密
        time.sleep(3)
        self.xpass_page.click_card_eye()  # 卡片金额加密

    def test_003_check_XPASS_NPXS_rec(self, coin='NPXS'):
        """
        检查XPASS卡NPXS的充值地址
        coin：币种，根据币种改变测试用例
        """

        try:
            self.xpass_page.into_XPASS_card()
            time.sleep(2)
            self.xpass_page.into_coin_detail(coin)
            time.sleep(3)
            assert self.xpass_page.check_QR_code()
            time.sleep(1)
            self.xpass_page.click_refresh()  # 点击付款二维码刷新按钮
            time.sleep(2)

            self.xpass_page.check_card_Receive()  # 点击充值码并检查
            self.xpass_page.save_img(f'{coin}充值码')
        except Exception:
            print(f'无法获取{coin}充值二维码...')
            raise Exception

    def test_004_check_XPASS_NPXS_transfer(self, coin='NPXS', address='0xaA3A007c27F41B7527d339270b3c46EDAF51fe84',
                                           money='0.00001'):
        """
        检查XPASS卡的NPXS的转账
        coin：币种，根据币种改变测试用例
        """

        try:
            self.xpass_page.into_XPASS_card()
            time.sleep(2)
            self.xpass_page.into_coin_detail(coin)
            time.sleep(2)
            self.xpass_page.ERC20_transfer(address, money)  # 点击卡片中的转账
            time.sleep(3)
            self.xpass_page.send_codes(pwd='123456')  # 输入转账时的验证码
            time.sleep(1)
            self.xpass_page.confirm_transfer()

            assert self.xpass_page.is_toast_exist('Transfer')
        except (Exception, AssertionError):
            self.xpass_page.save_img(f'{coin}转账')
            raise Exception

    def test_005_XPASS_ETH_rec(self):
        """
        检查XPASS卡ETH的充值地址
        coin：币种，根据币种改变测试用例
        """

        self.test_003_check_XPASS_NPXS_rec(coin='ETH')

    def test_006_check_XPASS_ETH_transfer(self):
        """
        检查XPASS卡的ETH的转账
        coin：币种，根据币种改变测试用例
        """

        time.sleep(30)  # 验证码时间间隔
        self.test_004_check_XPASS_NPXS_transfer(coin='ETH', address='0xaA3A007c27F41B7527d339270b3c46EDAF51fe84',
                                                money='0.00001')

    def test_007_XPASS_BTC_rec(self):
        """
        检查XPASS卡BTC的充值地址
        coin：币种，根据币种改变测试用例
        """

        self.test_003_check_XPASS_NPXS_rec(coin='BTC')

    @pytest.mark.skip('BTC测试链充值地址错误')
    def test_008_check_XPASS_BTC_transfer(self):
        """
        检查XPASS卡的BTC的转账
        coin：币种，根据币种改变测试用例
        """

        self.test_004_check_XPASS_NPXS_transfer(coin='BTC', address='0xaA3A007c27F41B7527d339270b3c46EDAF51fe84',
                                                money='0.00001')

    def test_009_check_XPASS_BNB_rec(self):
        """
        检查XPASS卡BNB的充值地址
        coin：币种，根据币种改变测试用例
        """

        try:
            self.xpass_page.into_XPASS_card()
            time.sleep(2)
            self.xpass_page.into_coin_detail(coin='BNB')
            time.sleep(2)

            self.xpass_page.Copy_Address_Memo()
            self.xpass_page.save_img('BNB充值码')
        except Exception:
            print(f'无法获取BNB充值二维码...')
            raise Exception

    def test_010_check_XPASS_BNB_transfer(self):
        """检查XPASS卡的BNB的转账"""

        try:
            self.xpass_page.into_XPASS_card()
            time.sleep(2)
            self.xpass_page.into_coin_detail(coin='BNB')
            time.sleep(2)
            self.xpass_page.BEP2_transfer(address='tbnb1nlt0zerp80ysn9ve7guqstrshwd9cz3j9z8fzl', memo='4hw4977m6f')
            time.sleep(30)  # 验证码时间间隔
            self.xpass_page.send_codes()  # 输入转账时的验证码
            time.sleep(1)
            self.xpass_page.confirm_transfer()

            assert self.xpass_page.is_toast_exist('Transfer')
        except (Exception, AssertionError):
            self.xpass_page.save_img('BNB转账')
            raise Exception

    def teardown_class(self):
        self.driver.quit()


if __name__ == '__main__':
    pytest.main()
