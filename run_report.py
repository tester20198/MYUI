from Public.AppiumServer import AppiumServer
import pytest
import os


class RunReport(AppiumServer):
    """运行 & 产生报告"""

    def terminal_report(self, root='./testcase/'):
        """
        在pycharm终端跑测试用例,但不生成报告
        :root: 指定运行文件，默认testcase中所有含有test的py脚本
        """

        pytest.main(['-s', '-q', root])  # 在终端运行报告

    def generate_report(self):
        """
        生成allure报告
        """

        pytest.main(['-s', '--alluredir', './reports/data/'])  # 在终端运行报告
        os.system(
            'allure generate ./reports/data/ -o ./reports/html/ --clean')  # --clean清除上一期数据

    def open_report(self):
        """
        生成报告，且用浏览器打开allure报告
        """

        self.generate_report()
        os.system('allure open -h 127.0.0.1 -p 8083 ./reports/html/')


if __name__ == '__main__':
    R = RunReport()
    R.terminal_report(
        root='/Users/pundix047/PycharmProjects/MYUI/testcase/Android/a_Register_test.py')
