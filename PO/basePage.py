from Public.AndroidMessage import Android


class Base:
    """
    基本页，包含设备的所有所需信息（暂时只支持安卓）
    用来连接页面元素和操作过程的类
    """

    driver = None
    # 选择Android设备中的app
    caps = Android('hhtc.dialer')
    # 初始化设备数据
    driver_caps = {'platformName': caps.platformName,
                   'platformVersion': caps.get_android_version(),
                   'deviceName': caps.get_android_name()[0],  # 第一个设备
                   'appPackage': caps.get_android_app(),
                   'appActivity': caps.get_app_Activity()
                    }

    def __init__(self, driver):
        self.driver = driver


print(Base.driver_caps)

