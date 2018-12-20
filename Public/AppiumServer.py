import os, time
from Public.AndroidMessage import Android
import platform


class AppiumServer:
    """
    管理appium服务
    """

    @staticmethod
    def start_server():
        """
        启动单个appium服务时
        """

        os.system('appium')  # mac_OS
        print('启动Appium服务成功，默认aport=4723,bport=4724')
        time.sleep(10)  # 等待启动时间

    @staticmethod
    def start_server_detail(port, device):
        """
        启动多个appium服务时,端口号建议输入4700～4800之间的，且两者不相同
        """

        print('启动Appium多个服务中...')
        cmd = f'appium -a 127.0.0.1 -p {port} -bp {port+1} -U {device}'
        os.system(cmd)
        time.sleep(10)

    @staticmethod
    def stop_server():
        """
        区分系统去停止服务
        """

        server_port = AppiumServer().find_server_port
        if not server_port:
            pass
        else:
            if platform.system() == 'Windows':
                os.popen('taskkill /f /im  node.exe')
                print('Windows:停止Appium服务成功！')
            else:
                os.popen(f'kill -9 {server_port}')
                print('mac OS:停止Appium服务成功！')

    @property
    def find_server_port(self):
        """
        找到appium服务占用的端口(mac OS下)
        :return:
        """
        with os.popen('ps |grep node') as f:
            port = f.readline()
        if port == '':
            print('Appium未被启动')
            return False
        else:
            p = port.split(' ')[0]
            return p