from appium import webdriver
import unittest
from PO.registerPage import registerPage
from PO.basePage import Base
from Public.getLog import write_log,stop_log
import time


class RigisterTestCase(unittest.TestCase):
    """
    注册的测试用例
    """

    def setUp(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', Base.driver_caps)  # 串联
        self.register_page = registerPage(self.driver)  # 初始化登录页元素以及方法
        time.sleep(3)  # 等待初始化完成
        self.imgs = []  # 截图列表
        # write_log()  # 写入日志

    def tearDown(self):
        # stop_log()  # 停止写入日志
        self.driver.quit()

    def add_img(self):
        # 截图方法
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def test_register_by_mobile(self):
        self.register_page.click_register()
        self.register_page.register_by_mobile('China', '13765657769')
        self.register_page.verify()
        self.register_page.send_pwd()
        self.register_page.send_pay_pwd()
        self.register_page.save_img('tester.png')
        time.sleep(1)


"""
    def test_all_nation_mobile(self):
        self.setUp()
        time.sleep(2)
        num = 0
        self.register_page.click_register()
        for key, values in phone_num.items():
            for v in values:
                self.register_page.register_by_mobile(key, v)
                # print(self.register_page.getAttribute())
                if self.register_page.getAttribute() == 'true':
                    num += 1
                    print(f'{key}国家的{v}手机号码is OK...')
                else:
                    print(f'{key}国家的{v}手机号码is Wrong...')
                self.register_page.edit_clear()
        print(f'共{num}个成功！！！')
"""


if __name__ == '__main__':
    unittest.main()
