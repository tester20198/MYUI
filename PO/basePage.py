from Public.AndroidMessage import Android
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from appium.webdriver.mobilecommand import MobileCommand
import time, os


class Base:
    """
    基本页，包含设备的所有所需信息（暂时只支持安卓）
    用来连接页面元素和操作过程的类
    """

    driver = None

    an = Android()  # 初始化设备数据
    android_driver_caps = {'platformName': an.platformName,
                           'platformVersion': an.get_device_version,
                           'deviceName': an.get_device_name[0],  # 第一个设备
                           'appPackage': an.get_app_name,
                           'appActivity': an.get_app_Activity,
                           'autoGrantPermissions': True,  # 获取默认权限
                           # "noReset": True,  # 不清空数据
                           "automationName": "Uiautomator2"  # 使用Uiautomator2
                           }
    """
    ios_driver_caps = {"platformName": "iOS",
                       "platformVersion": "12.1",
                       "bundleId": "com.pundix.wallet",
                       "automationName": "XCUITest",
                       "udid": "72c8074b6e518ba2c4a462a5bbe169f90c802f8c",
                       "deviceName": "“PundiX051”的 iPhone"
                       }
    """

    def __init__(self, driver, ):
        self.driver = driver

    def Sys_back(self):
        """
        点击系统返回键
        :return:
        """

        self.driver.keyevent(4)

    def Sys_home(self):
        """
        点击系统home键
        :return:
        """

        self.driver.keyevent(3)

    def Sys_power(self):
        """
        点击power按键
        :return:
        """

        self.driver.keyevent(26)

    def findElement(self, el):
        """
        判断某元素是否存在
        :return:
        """

        source = self.driver.page_source  # 打印当前页面全部的元素
        if el in source:
            return True
        else:
            print('找不到该元素...')
            return False

    def get_size(self):
        """
        获取屏幕分辨率大小
        :return:
        """

        size = self.driver.get_window_size()
        print(size['width'], size['height'])
        return size['width'], size['height']

    def swipeDown(self, duration=500):
        """
        根据屏幕相对大小，向下滑动
        :return:
        """

        x, y = self.get_size()
        self.driver.swipe(x / 2, y / 4, x / 2, y * 3 / 4, duration)

    def swipeUp(self, duration=500):
        """
        根据屏幕相对大小，向上滑动
        :return:
        """

        x, y = self.get_size()
        self.driver.swipe(x / 2, y * 3 / 4, x / 2, y / 4, duration)

    def wait_element(self, time, element, msg):
        """
        等待元素出现
        :param time: 等待时间
        :param element: 元素
        :param msg: 输出信息
        :return:
        """
        WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(element), msg)

    def clear(self, *el):
        """
        清空输入框
        :param el:控件
        :return:
        """

        conn = self.driver.find_element(el)
        conn.click()
        self.driver.keyevent(123)  # 光标追尾
        textLength = len(str(conn.text))
        for i in range(0, textLength):
            self.driver.keyevent(67)  # 逐个删除已输入的内容

    def getAttribute(self, *el, attr) -> str:
        """
        获取控件的各项属性
        :param el:控件
        :param attr:属性类别
        :return:返回"true"/"false"
        """

        return self.driver.find_element(el).get_attribute(attr)

    def save_img(self, picname):
        """
        截图并保存
        :param filename:文件名
        :使用例子：self.usercenterPage.save_img('/hello')
        """

        path = os.path.abspath('../../img')
        # print(path + picname + '.png')
        self.driver.get_screenshot_as_file(path + picname + '.png')

    def ios_swipeUP(self):
        """
        iOS端向上滑动
        :return:
        """
        self.driver.execute_script('mobile: swipe', {'direction': 'up'})

    def ios_swipeDown(self):
        """
        iOS端向上滑动
        :return:
        """
        self.driver.execute_script('mobile: swipe', {'direction': 'down'})

    def is_toast_exist(self, text, timeout=10, poll_frequency=0.1):
        """
        定位toast提示语
        :param text: 提示语内容（全部）
        :param timeout: 多少秒后超时，不再监控
        :param poll_frequency: 监控间隔
        :return:
        """

        try:
            toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % text)

            WebDriverWait(self.driver, timeout, poll_frequency).until(
                expected_conditions.presence_of_element_located(toast_loc))
            return True
        except:
            return False

    def switch_to_view(self, target='H5'):
        """
        切换app视窗 或 h5视窗
        :target:目标视窗（app/H5），默认切换到H5
        :return:
        """

        view_list = self.driver.contexts
        print('当前页面的webview元素有：', view_list)
        webview = [i for i in view_list if 'xwallet' in i]
        app = [a for a in view_list if 'APP' in a]

        if target == 'H5':
            self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": webview[0]})
        else:
            self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": app[0]})
        print(self.driver.current_context)
        time.sleep(2)

    def click2(self, text):
        """
        特殊点击法，点击一些只有text标识的元素
        :param text: 元素名称
        :return:
        """

        try:
            text_loc = ("xpath", ".//*[contains(@text,'%s')]" % text)
            self.driver.find_element(*text_loc).click()
        except:
            raise AttributeError('不存在该元素...')

    def send_keys2(self, el, text):
        """
        特殊点击法，点击一些只有text标识的元素
        :param el: 元素名称
        :text: 输入内容
        :return:
        """

        try:
            text_loc = ("xpath", ".//*[contains(@text,'%s')]" % el)
            self.driver.find_element(*text_loc).send_keys(text)
        except:
            raise AttributeError('不存在该元素...')


if __name__ == '__main__':
    print(Base(1).android_driver_caps)
