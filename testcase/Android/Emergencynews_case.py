from appium import webdriver
import unittest
from Public.getLog import InsertLog,Screenshot
from PO.Android.EmergencynewsPage import EmergencynewsPage
from PO.basePage import Base
import time

class EmergencynewsTestCase(unittest.TestCase):
    """
    紧急消息界面的测试用例
    """

    @classmethod
    def setUpClass(cls):
        Base.android_driver_caps["noReset"] = True
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', Base.android_driver_caps)  # 串联
        time.sleep(3)  # 等待初始化完成
        cls.Emergencynews_Page = EmergencynewsPage(cls.driver)

    def test01_Click_Emergencynews(self):
        '''
        用例一: 测试点击打开紧急消息
        断言如果页面出现了'网页不可用'则用例失败
        '''
        try:
            msg = self.Emergencynews_Page.Click_Emergencynews()
            self.assertTrue(msg)
            print('打开紧急消息,获取的页面文本信息：%s' % msg)
        except (BaseException, AssertionError) as msg:
            Screenshot(self.driver)
            InsertLog().debug(msg)
            raise BaseException



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=0)