from configparser import ConfigParser
import os


class Environment:
    """
    读取环境设置
    """

    def __init__(self):
        self.config = ConfigParser()
        self.filename = os.path.dirname(__file__) + '/config.ini'  # 配置文件

    def get_env(self, title, subtitle):
        """
        :param title: 配置头部
        :param subtitle: 配置内的内容
        :return:
        """

        self.config.read(self.filename)  # 读取配置文件
        if title not in self.config.sections():
            print('不存在该配置项目，请检查配置文件config.ini')
        elif subtitle not in self.config.options(title):
            print('该%s配置项目下不存在%s元素，请检查配置文件config.ini' % (title, subtitle))
        else:
            setting = self.config.get(title, subtitle)
        return setting

    @property
    def iOS_cpas(self) -> dict:
        """
        以字典形式返回设备配置
        :return:
        """

        self.config.read(self.filename)
        return dict(self.config._sections['iOS_caps'])
