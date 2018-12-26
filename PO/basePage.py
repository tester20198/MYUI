from Public.AndroidMessage import Android
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from Public import other


class Base:
    """
    基本页，包含设备的所有所需信息（暂时只支持安卓）
    用来连接页面元素和操作过程的类
    """

    driver = None
    # 选择Android设备中的app
    an = Android()
    # 初始化设备数据
    driver_caps = {'platformName': an.platformName,
                   'platformVersion': an.get_device_version,
                   'deviceName': an.get_device_name[0],  # 第一个设备
                   'appPackage': an.get_app_name,
                   'appActivity': an.get_app_Activity,
                   'autoGrantPermissions': True  # 获取默认权限
                   }

    def __init__(self, driver):
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
        self.driver.swipe(x/2, y/4, x/2, y*3/4, duration)

    def swipeUp(self, duration=500):
        """
        根据屏幕相对大小，向上滑动
        :return:
        """

        x, y = self.get_size()
        self.driver.swipe(x/2, y*3/4, x/2, y/4, duration)

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

    def save_img(self, filename):
        """
        截图并保存
        :param filename:文件名+文件后缀
        :return:
        """

        path = other.upper_path() + 'img/'
        # print(path)
        self.driver.get_screenshot_as_file(path+filename)
        return True


if __name__ == '__main__':
    print(Base(1).driver_caps)
