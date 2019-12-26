from appium import webdriver
from Page.Android.VirtualCardPage import DAPPPage
from Page.basePage import Base
from Page.Android.UsercenterPage import UsercenterPage
import pytest
import time


class TestVirtualCard:
    """
   VirtualCard界面的测试用例
    """

    def setup_class(self):
        Base.android_driver_caps["noReset"] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', Base.android_driver_caps)  # 串联
        self.Dapppage = DAPPPage(self.driver)
        self.usercenterPage = UsercenterPage(self.driver)
        time.sleep(8)

    def test_01_BTC_Receive(self):
        """
        点击查看BTC充值地址
        """
        try:
            self.Dapppage.click_BTC_Detail()
            time.sleep(3)
            self.Dapppage.Copy_Receive_Address()
            time.sleep(3)

            assert self.Dapppage.check_receive_code()
        except (Exception, AssertionError):
            self.Dapppage.save_img("BTC_Receive1")
            raise Exception

    @pytest.mark.skip('转BTC全部金额，暂不跑')
    def test_02_BTC_transfer(self):
        """BTC转账转全部"""

        try:
            self.Dapppage.click_BTC_Detail()
            time.sleep(2)
            self.Dapppage.Click_Transfer_without_Memo("n4mz19LnL84u4YQdNxX4V5kE6fwpyiMjcK")
            self.Dapppage.send_codes()
            self.Dapppage.confirm_transfer()

            assert self.Dapppage.is_toast_exist('succee')
            assert not self.Dapppage.is_toast_exist('500')
        except (Exception, AssertionError):
            self.Dapppage.save_img('BTC_transfer1')
            raise Exception
        finally:
            time.sleep(30)

    def test_03_BTC_transfer2(self):
        """BTC转账转指定金额"""

        try:
            self.Dapppage.click_BTC_Detail()
            time.sleep(5)
            self.Dapppage.ERC20_transfer(address="n4mz19LnL84u4YQdNxX4V5kE6fwpyiMjcK", money='0.005')
            time.sleep(2)
            self.Dapppage.send_codes()
            self.Dapppage.confirm_transfer()

            assert self.Dapppage.is_toast_exist('succee')
            assert not self.Dapppage.is_toast_exist('500')
        except (Exception, AssertionError):
            self.Dapppage.save_img('BTC_transfer2')
            raise Exception
        finally:
            time.sleep(30)

    def test_04_ETH_Receive(self):
        """
        点击查看ETH充值地址
        """
        try:
            self.Dapppage.click_ETH_Detail()
            time.sleep(3)
            self.Dapppage.Copy_Receive_Address()
            time.sleep(3)

            assert self.Dapppage.check_receive_code()
        except (Exception, AssertionError):
            self.Dapppage.save_img("ETH_Receive1")
            raise Exception

    @pytest.mark.skip('转ETH全部金额，暂不跑')
    def test_05_ETH_transfer(self):
        """ETH转账"""
        try:
            self.Dapppage.click_ETH_Detail()
            time.sleep(2)
            self.Dapppage.Click_Transfer_without_Memo("0x4d7e60eab27597522232e04ab2743f14d903eeb5")
            self.Dapppage.send_codes()
            self.Dapppage.confirm_transfer()

            assert self.Dapppage.is_toast_exist("succee")
            assert not self.Dapppage.is_toast_exist("500")
        except (Exception, AssertionError):
            self.Dapppage.save_img("ETH_transfer1")
            raise Exception
        finally:
            time.sleep(30)

    def test_06_ETH_transfer2(self):
        """ETH转账转指定金额"""
        try:
            self.Dapppage.click_ETH_Detail()
            time.sleep(2)
            self.Dapppage.ERC20_transfer(address="0x4d7e60eab27597522232e04ab2743f14d903eeb5", money='0.1')
            time.sleep(2)
            self.Dapppage.send_codes()
            time.sleep(1)
            self.Dapppage.confirm_transfer()

            assert self.Dapppage.is_toast_exist('succee')
            assert not self.Dapppage.is_toast_exist('500')
        except (Exception, AssertionError):
            self.Dapppage.save_img('ETH_transfer2')
            raise Exception
        finally:
            time.sleep(30)

    def test_07_NPXS_Receive(self):
        """
        点击查看NPXS充值地址
        """
        try:
            self.Dapppage.click_NPXS_Detail()
            time.sleep(3)
            self.Dapppage.Copy_Receive_Address()
            time.sleep(3)

            assert self.Dapppage.check_receive_code()
        except AssertionError:
            self.Dapppage.save_img("NPXS_Receive")
            raise Exception

    def test_08_NPXS_transfer(self):
        """NPXS转账"""
        try:
            self.Dapppage.click_NPXS_Detail()
            time.sleep(4)
            self.Dapppage.Click_Transfer_without_Memo("0x07a4a5ed9da97773e56dedcc0725e62efbcd61d1")
            self.Dapppage.send_codes()
            self.Dapppage.confirm_transfer()

            assert self.Dapppage.is_toast_exist("succe")
            assert not self.Dapppage.is_toast_exist("500")
        except (Exception, AssertionError):
            self.Dapppage.save_img("NPXS_transfer")
            raise Exception
        finally:
            time.sleep(30)

    def test_09_NPXS_transfer2(self):
        """NPXS 转账转指定金额"""

        try:
            self.Dapppage.click_NPXS_Detail()
            time.sleep(5)
            self.Dapppage.ERC20_transfer(address="0x07a4a5ed9da97773e56dedcc0725e62efbcd61d1", money='600')
            time.sleep(2)
            self.Dapppage.send_codes()
            self.Dapppage.confirm_transfer()

            assert self.Dapppage.is_toast_exist("succe")
            assert not self.Dapppage.is_toast_exist("500")
        except (Exception, AssertionError):
            self.Dapppage.save_img("NPXS_transfer")
            raise Exception
        time.sleep(30)

    def test_10_BNB_Receive(self):
        """
        点击查看BNB充值地址
        """

        try:
            self.Dapppage.click_BNB_Detail()
            time.sleep(3)
            self.Dapppage.Copy_Address_Memo()
            time.sleep(3)
            self.Dapppage.save_img("/BNB_Recevice")  # 保存BNB充值地址图片

            assert self.Dapppage.check_receive_code()
        except (Exception, AssertionError):
            self.Dapppage.save_img("BNB_Receive")
            raise Exception

    def test_11_BNB_transfer(self):
        """BNB转账"""

        try:
            self.Dapppage.click_BNB_Detail()
            time.sleep(5)
            self.Dapppage.BEP2_transfer(address='tbnb1nlt0zerp80ysn9ve7guqstrshwd9cz3j9z8fzl', memo='4hw4977m6f',
                                        money='0.5')
            time.sleep(2)
            self.Dapppage.send_codes()
            self.Dapppage.confirm_transfer()

            assert self.Dapppage.is_toast_exist("succe")
            assert not self.Dapppage.is_toast_exist("500")
        except (Exception, AssertionError):
            self.Dapppage.save_img("BNB_transfer")
            raise Exception
        finally:
            time.sleep(30)

    def test_12_QTUM_Receive(self):
        """
        点击查看QTUM充值地址
        """
        try:
            self.Dapppage.click_QTUM_Detail()
            time.sleep(3)
            self.Dapppage.Copy_Receive_Address()
            time.sleep(3)

            assert self.Dapppage.check_receive_code()
        except (Exception, AssertionError):
            self.Dapppage.save_img("QTUM_Receive")
            raise Exception

    @pytest.mark.skip('转QTUM全部金额，暂不跑')
    def test_13_QTUM_transfer(self):
        """QTUM转账"""
        try:
            self.Dapppage.click_QTUM_Detail()
            time.sleep(2)
            self.Dapppage.Click_Transfer_without_Memo("qevcAgqD8rrJjaGutwQhDA1AT2FaXctdhm")
            time.sleep(2)
            self.Dapppage.send_codes()
            self.Dapppage.confirm_transfer()

            assert self.Dapppage.is_toast_exist("succe")
            assert not self.Dapppage.is_toast_exist("500")
        except (Exception, AssertionError):
            self.Dapppage.save_img("QTUM_transfer")
            raise Exception
        finally:
            time.sleep(30)

    def test_14_QTUM_transfer(self):
        """QTUM转指定金额"""

        try:
            self.Dapppage.click_QTUM_Detail()
            time.sleep(2)
            self.Dapppage.ERC20_transfer(address="qevcAgqD8rrJjaGutwQhDA1AT2FaXctdhm", money="0.5")
            time.sleep(2)
            self.Dapppage.send_codes()
            self.Dapppage.confirm_transfer()

            assert self.Dapppage.is_toast_exist("succe")
            assert not self.Dapppage.is_toast_exist("500")
        except (Exception, AssertionError):
            self.Dapppage.save_img("QTUM_transfer1")
            raise Exception
        finally:
            time.sleep(30)

    def test_15_XEM_Receive(self):
        """点击查看XEM充值地址"""
        self.Dapppage.click_XEM_Detail()
        time.sleep(3)
        self.Dapppage.Copy_Address_Memo()
        self.Dapppage.save_img("XEM_Recevice")  # 保存XEM充值地址图片

    def test_16_XEM_transfer(self):
        """XEM转账"""

        try:
            self.Dapppage.click_XEM_Detail()
            time.sleep(2)
            self.Dapppage.BEP2_transfer(address="TBF3ZZGCVY7NTWDABEH7P3KXD2LOYABEXASYDRUO", money='0.5')
            time.sleep(2)
            self.Dapppage.send_codes()
            self.Dapppage.confirm_transfer()

            assert self.Dapppage.is_toast_exist("succe")
            assert not self.Dapppage.is_toast_exist("500")
        except (Exception, AssertionError):
            self.Dapppage.save_img("XEM_transfer")
            raise Exception
        finally:
            time.sleep(30)

    def test_17_NPXSXEM_Recevice(self):
        """点击查看NPXSXEM充值地址"""
        self.Dapppage.click_NPXSXEM_Detail()
        time.sleep(5)
        self.Dapppage.click_NPXSXEM_Receice()
        self.Dapppage.save_img("NPXSXEM_Recevice")  # 保存NPXSXEM充值地址图片
        time.sleep(5)

    def test_18_NPXSXEM_transfer(self):
        """NPXSXEM转账"""

        try:
            self.Dapppage.click_NPXSXEM_Detail()
            time.sleep(2)
            self.Dapppage.Click_NPXSXEM_Transfer()

            assert not self.Dapppage.is_toast_exist("500")
        except (Exception, AssertionError):
            self.Dapppage.save_img("NPXSXEM_transfer")
            raise Exception

    def test_19_Internal_Transfer(self):
        """内部划转"""
        try:
            self.Dapppage.Internal_Transfer()
            time.sleep(5)
            self.usercenterPage.transfer_all()

            assert self.Dapppage.is_toast_exist("succe")
            assert not self.Dapppage.is_toast_exist("500")
        except (Exception, AssertionError):
            self.Dapppage.save_img("Internal_Transfer")
            raise Exception

    def teardown_class(self):
        self.driver.quit()


if __name__ == '__main__':
    pytest.main()
