from appium import webdriver
import unittest
from Public.getLog import InsertLog,Screenshot
from PO.Android.ChatPage import ChatPage
from PO.basePage import Base
import time

class ChatTestCase(unittest.TestCase):
    """
    Chat界面的测试用例
    """
    @classmethod
    def setUpClass(cls):
        Base.android_driver_caps["noReset"] = True
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', Base.android_driver_caps)  # 串联
        # cls.login_page = LoginPage(cls.driver)  # 初始化登录页元素以及方法
        time.sleep(3)  # 等待初始化完成
        # cls.login_page.email_login('xgq1@xinjineng.net', 'Abc123456') #调用登陆
        cls.chat_page = ChatPage(cls.driver)

    def test01_Send_little_personal_redpacket(self,nickname=u'谢国强',amount='0.0000001',explain=u'发送个人红包',paypwd='000000'):
        '''
        用例一: 发送个人红包BTC(小额)
        :param nickname: 输入需要发送的好友昵称(全称)
        :param amount:  输入红包的金额
        :param explain: 输入红包的祝福语
        :param paypwd: 输入支付密码
        :return:
        '''
        try:
            self.chat_page.Click_chat() #点击chat菜单
            time.sleep(1)
            self.chat_page.Send_personal_redpacket(nickname,amount,explain) #输入接收者名称、红包金额、红包祝福语
            time.sleep(1)
            self.chat_page.Select_redpacket_coin_BTC()   #发送btc币种
            self.chat_page.Click_Send_redpacket(paypwd)   #输入支付密码
            msg = self.chat_page.judge_redpacket_status()  #判断发出去的红包状态是否为View
            self.assertTrue(msg)
            print('发送红包后,获取的页面红包的状态信息：%s' % msg)
        except (BaseException, AssertionError) as msg:
            Screenshot(self.driver)
            InsertLog().debug(msg)
            raise BaseException

    def test02_Send_little_personal_redpacket(self,nickname=u'谢国强',amount='0.001',explain=u'发送个人红包',paypwd='000000'):
        '''
        用例二: 发送个人红包ETH(小额)
        :param nickname: 输入需要发送的好友昵称(全称)
        :param amount:  输入红包的金额
        :param explain: 输入红包的祝福语
        :param paypwd: 输入支付密码
        :return:
        '''
        try:
            self.chat_page.Click_chat() #点击chat菜单
            time.sleep(1)
            self.chat_page.Send_personal_redpacket(nickname,amount,explain) #输入接收者名称、红包金额、红包祝福语
            time.sleep(1)
            self.chat_page.Select_redpacket_coin_ETH()   #发送ETH币种
            self.chat_page.Click_Send_redpacket(paypwd)   #输入支付密码
            msg = self.chat_page.judge_redpacket_status()  #判断发出去的红包状态是否为View
            self.assertTrue(msg)
            print('发送红包后,获取的页面红包的状态信息：%s' % msg)
        except (BaseException, AssertionError) as msg:
            Screenshot(self.driver)
            InsertLog().debug(msg)
            raise BaseException

    def test03_Send_little_group_redpacket(self,nickname=u'测试组',amount=1,explain=u'发送群红包',number=10,paypwd='000000'):
        '''
        用例三: 发送群红包NPXS(小额)
        :param nickname: 输入需要发送的好友昵称(全称)
        :param amount:  输入红包的金额
        :param explain: 输入红包的祝福语
        :param number:  输入红包的个数
        :param paypwd: 输入支付密码
        :return:
        '''
        try:
            self.chat_page.Click_chat()
            time.sleep(1)
            self.chat_page.Send_group_redpacket(nickname,amount,explain,number) #发送群红包
            time.sleep(1)
            self.chat_page.Select_redpacket_coin_NPXS()  # 发送NPXS币种
            self.chat_page.Click_Send_redpacket(paypwd)  # 输入支付密码
            msg = self.chat_page.judge_redpacket_status()  # 判断发出去的红包状态是否为View
            self.chat_page.Open_group_redpacket() #打开群红包
            self.assertTrue(msg)
            print('发送红包后,获取的页面红包的状态信息：%s' % msg)
        except (BaseException, AssertionError) as msg:
            Screenshot(self.driver)
            InsertLog().debug(msg)
            raise BaseException

    def test04_Send_little_group_redpacket(self,nickname=u'测试组',amount=1,explain=u'发送群红包',number=10,paypwd='000000'):
        '''
        用例四: 发送群红包BNB(小额)
        :param nickname: 输入需要发送的好友昵称(全称)
        :param amount:  输入红包的金额
        :param explain: 输入红包的祝福语
        :param number:  输入红包的个数
        :param paypwd: 输入支付密码
        :return:
        '''
        try:
            self.chat_page.Click_chat()
            time.sleep(1)
            self.chat_page.Send_group_redpacket(nickname,amount,explain,number) #发送群红包
            time.sleep(1)
            self.chat_page.Select_redpacket_coin_BNB()  # 发送BNB币种
            self.chat_page.Click_Send_redpacket(paypwd)  # 输入支付密码
            msg = self.chat_page.judge_redpacket_status()  # 判断发出去的红包状态是否为View
            self.chat_page.Open_group_redpacket() #打开群红包
            self.assertTrue(msg)
            print('发送红包后,获取的页面红包的状态信息：%s' % msg)
        except (BaseException, AssertionError) as msg:
            Screenshot(self.driver)
            InsertLog().debug(msg)
            raise BaseException

    def test05_Send_big_group_redpacket(self,nickname=u'测试组',amount=10,explain=u'发送群红包',
                                           number=1,paypwd='000000',code='2222',code2fa='222222'):
        '''
        用例五: 发送群红包ETH(大额)
        :param nickname: 输入需要发送的好友昵称(全称)
        :param amount:  输入红包的金额(默认ETH)
        :param explain: 输入红包的祝福语
        :param number:  输入红包的个数
        :param paypwd: 输入支付密码
        :param code: 输入验证码
        :param code2fa: 输入谷歌验证码
        :return:
        '''
        try:
            self.chat_page.Click_chat()
            time.sleep(1)
            self.chat_page.Send_group_redpacket(nickname,amount,explain,number) #发送群红包
            time.sleep(1)
            self.chat_page.Select_redpacket_coin_ETH()  # 发送ETH币种
            self.chat_page.Click_Send_redpacket(paypwd)  # 输入支付密码
            self.chat_page.business_processes_2FA(code,code2fa) #输入验证码、2FA的验证码
            msg = self.chat_page.judge_redpacket_status()  # 判断发出去的红包状态是否为View
            print('发送红包后,获取的页面红包的状态信息：%s' % msg)
        except (BaseException, AssertionError) as msg:
            Screenshot(self.driver)
            InsertLog().debug(msg)
            raise BaseException

    def test06_Send_group_emjoy_message(self,nickname=u'测试组',message=u'发送群红包'):
        '''
        用例六: 发送群消息(文字和表情)
        :param nickname: 输入需要发送的好友昵称(全称)
        :param message:  输入需要发送的消息内容，表情默认选择第26个表情
        :return:
        '''
        try:
            self.chat_page.Click_chat()
            self.chat_page.Send_group_emjoy_message(nickname,message)
            # print('发送红包后,获取的页面红包的状态信息：%s' % msg)
        except (BaseException, AssertionError) as msg:
            Screenshot(self.driver)
            InsertLog().debug(msg)
            raise BaseException

    def test07_Forgot_payment_password(self,nickname=u'谢国强',amount='0.001',explain=u'发送个人红包',emailcode='2222',pwd='000000'):
        '''
        用例七: 忘记密码流程
        :param emailcode: 输入邮箱验证码
        :param pwd:  输入支付密码
        :return:
        '''
        try:
            self.chat_page.Click_chat()  # 点击chat菜单
            time.sleep(1)
            self.chat_page.Send_personal_redpacket(nickname, amount, explain)  # 输入接收者名称、红包金额、红包祝福语
            time.sleep(1)
            self.chat_page.Select_redpacket_coin_ETH()  # 发送ETH币种
            time.sleep(1)
            self.chat_page.business_forgot_payment_password(emailcode,pwd)
        except (BaseException, AssertionError) as msg:
            Screenshot(self.driver)
            InsertLog().debug(msg)
            raise BaseException

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=0)
