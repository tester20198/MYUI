import os


class Android:
    """
    Android 设备相关信息获取
    """

    def __init__(self, app):
        self.platformName = 'Android'
        self.app = app

    def get_android_name(self):
        """
        获取连接到电脑的安卓设备名称，返回一个list
        """

        devicelist = []
        with os.popen('adb devices', 'r') as f:
            output = f.read().split('\n')  # 切掉换行
            dev = [x for x in output if x != ''][1:]  # 去掉不需要的部分
            if dev:  # 判断是否有设备连接
                for i in dev:  # 可能有多个设备
                    devicename = i.replace('\tdevice', '')
                    print(f'你有{len(dev)}个设备已连接，设备名为{devicename}')
                    devicelist.append(devicename)
            else:
                raise Exception('请重新尝试连接设备...')  # 若无设备连接，引起错误
        return devicelist

    def get_android_app(self):
        """
        获取待测目标app的包名
        : app: 模糊搜索包名
        """

        with os.popen(f'adb shell pm list packages | grep {self.app}', 'r') as f:
            app_name = f.read().replace('package:', '').replace('\n', '')

        if app_name:  # 判断是否存在该安装包
            print(f'查找到相关app包名:{app_name}')
        else:
            print('找不到相关的app包名，请检查安装或者重新输入正确的app名字...')
        return app_name

    def get_android_version(self):
        """
        获取安卓版本
        """

        with os.popen('adb shell getprop ro.build.version.release', 'r') as f:
            app_version = f.read().replace('\n', '')
            print('设备的版本为:', app_version)
        return app_version

    def get_app_Activity(self):
        """
        获取app的启动页Activity
        """

        # 调用自身的方法去获取app的包名
        with os.popen(f'adb shell dumpsys package {self.get_android_app()} | grep filter | grep Activity', 'r') as f:
            output = f.read()
            aa = output.lstrip().split(' ')[1]  # 提取内容主要部分得到主干的activity
            app_Activity = aa.replace('/', '')  # 替换掉非法的输入活动名
        print(f'{self.app}的启动页Activity为:', app_Activity)
        return app_Activity