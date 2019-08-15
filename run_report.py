import os
import unittest
from BeautifulReport import BeautifulReport
from Public import other


class RunReport:
    """
    输出报告
    """

    def __init__(self):
        # 测试用例位置
        self.case_path = os.path.join(other.append_path('testcase'))  # + Environment().get_env('testing_cases', 'cases'))
        print(f'执行的测试用例路径为：{self.case_path}')

    def add_cases(self):
        """
        批量添加测试用例
        :pattern:测试用例脚本模板
        :top_level_dir:顶层目录的名称,默认None
        :return:
        """

        discover = unittest.defaultTestLoader.discover(self.case_path, pattern="*_case.py",
                                                       top_level_dir=None)
        return discover

    def run_cases_by_beautiful_report(self, cases):
        """
        借用BeautifulReport模版输出测试用例报告
        :param cases:测试用例集
        :return:
        """

        result = BeautifulReport(cases)
        result.report(description='测试报告', log_path='./reports')


if __name__ == "__main__":
    # 用例集合
    re = RunReport()
    cases = re.add_cases()
    re.run_cases_by_beautiful_report(cases)
