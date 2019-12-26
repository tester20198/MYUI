from Public.AppiumServer import AppiumServer
import pytest
import os


class RunReport(AppiumServer):
    """运行 & 产生报告"""

    def __init__(self, root='./testcase'):
        self.root = root

    def terminal_report(self):
        """
        在pycharm终端跑测试用例,但不生成报告
        :root: 指定运行文件，默认testcase中所有含有test的py脚本
        """

        pytest.main(['-s', '-q', self.root])  # 在终端运行报告

    def generate_report(self):
        """
        生成allure报告
        """

        pytest.main(['-s', self.root, '--alluredir', './reports/data/'])  # 在终端运行报告
        os.system(
            'allure generate ./reports/data/ -o ./reports/html/ --clean')  # --clean清除上一期数据

    def open_report(self):
        """
        生成报告，且用浏览器打开allure报告
        """

        self.generate_report()
        os.system('allure open -h 127.0.0.1 -p 8083 ./reports/html/')

    def rerun(self):
        """
        失败重跑机制 & 生产报告
        --lf参数（last fail）：运行上次运行失败的测试用例，如果没有失败用例则运行全部测试用例。
        -–ff参数(fail first)：运行所有的测试用例，上次运行失败的用例优先执行。
        :return:
        """
        pytest.main(['-s', '--lf', self.root, '--alluredir', './reports/data/'])  # 在终端运行报告
        os.system(
            'allure generate ./reports/data/ -o ./reports/html/ --clean')  # --clean清除上一期数据


if __name__ == '__main__':
    R = RunReport(root='/Users/pundix047/PycharmProjects/MYUI/testcase/Android/a_Register_test.py')
    R.rerun()
