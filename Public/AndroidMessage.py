import os
from Public.getConfig import Environment


class Android:
    """
    Android 设备相关信息获取
    """

    def __init__(self):
        self.platformName = 'Android'
        self.app = Environment().get_env('app', 'app')

    @property
    def get_device_name(self) -> list:
        """
        获取连接到电脑的安卓设备名称
        """

        devicelist = []
        with os.popen('adb devices', 'r') as f:
            output = f.read().split('\n')  # 切掉换行
            dev = [x for x in output if x != ''][1:]  # 去掉不需要的部分
            ii = 1
            if dev:  # 判断是否有设备连接
                for i in dev:  # 可能有多个设备
                    devicename = i.replace('\tdevice', '')
                    print(f'你有{len(dev)}个设备已连接，第{ii}个设备名为{devicename}')
                    devicelist.append(devicename)
                    ii += 1
            else:
                raise Exception('请重新尝试连接设备...')  # 若无设备连接，引起错误
        return devicelist

    @property
    def get_app_name(self) -> str:
        """
        获取待测目标app的包名
        """

        with os.popen(f'adb shell pm list packages | grep {self.app}', 'r') as f:
            app_name = f.read().replace('package:', '').replace('\n', '')

        if app_name:  # 判断是否存在该安装包
            print(f'查找到相关app包名:{app_name}')
        else:
            print(f'找不到相关的{self.app}包名，请检查安装或者重新输入正确的app名字...')
        return app_name

    @property
    def get_device_version(self) -> str:
        """
        获取安卓版本
        """

        with os.popen('adb shell getprop ro.build.version.release', 'r') as f:
            app_version = f.read().replace('\n', '')
            print('设备的版本为:', app_version)
        return app_version

    @property
    def get_app_Activity(self) -> str:
        """
        获取app的启动页Activity
        """

        # 调用自身的方法去获取app的包名
        with os.popen(f'adb shell dumpsys package {self.get_app_name} | grep Start | grep Activity', 'r') as f:
            output = f.read()
            aa = output.lstrip().split(' ')[1]  # 提取内容主要部分得到主干的activity
            app_activity = aa.replace('/', '')  # 替换掉非法的输入活动名
        print(f'{self.app}的启动页Activity为:', app_activity)
        return app_activity