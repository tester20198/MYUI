from appium import webdriver
import unittest
from PO.Android.EmergencynewsPage import EmergencynewsPage
from PO.Android.loginPage import LoginPage
from PO.basePage import Base
from BeautifulReport import BeautifulReport
import time


class EmergencynewsTestCase(unittest.TestCase):
    """
    紧急消息界面的测试用例
    """

    def setUp(self):
        Base.android_driver_caps["noReset"] = False
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', Base.android_driver_caps)  # 串联
        self.login_page = LoginPage(self.driver)  # 初始化登录页元素以及方法
        time.sleep(5)  # 等待初始化完成
        self.login_page.check_in()
        self.login_page.login_by_Email('476367010@xinjineng.net', 'Aa123456')  # 调用登陆
        self.Emergencynews_Page = EmergencynewsPage(self.driver)

    @BeautifulReport.add_img('Emergencynews_fail')
    def test_001_Click_Emergencynews(self):
        '''
        用例一: 测试点击打开紧急消息
        断言如果页面出现了'网页不可用'或'加载不出来'则用例失败
        '''
        try:
            msg = self.Emergencynews_Page.Click_Emergencynews()
            self.assertTrue(msg)
            print('打开紧急消息,获取的页面文本信息：%s' % msg)
        except (Exception, AssertionError):
            self.Emergencynews_Page.save_img("Emergencynews_fail")
            raise Exception

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=0)