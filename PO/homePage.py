from PO.basePage import Base
from selenium.webdriver.common.by import By
import time


class HomePage(Base):
    """
    主页+注册界面的页面元素
    """

    center = (By.ID, "rl_open_user_info")  # 个人中心
    setting = (By.ID, "rl_layout_setting")  # 设置
    logout = (By.ID, "tv_loginout")  # 退出登录
    comfirm_logout = (By.ID, "button1")  # 确认退出登录

    def log_out(self):
        self.driver.find_element(*self.center).click()
        self.driver.find_element(*self.setting).click()
        self.driver.find_element(*self.logout).click()
        time.sleep(1)
        self.driver.find_element(*self.comfirm_logout).click()
        time.sleep(2)
