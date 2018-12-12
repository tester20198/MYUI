from PO.basePage import Base
from selenium.webdriver.common.by import By
import time


class HomePage(Base):
    """
    主页的页面元素
    """

    scan = (By.ID, "rl_layout_scan")  # 扫码
    scan_permission = (By.ID, "permission_allow_button")  # 相机权限
    edit_amount = (By.ID, "ed_amount")  # 输入金额


"""
    def scanQR(self):
        # 扫码专项测试
        
        self.driver.find_element(*self.scan).click()
        try:
            self.wait_element(time=10, element=self.edit_amount, msg='超过10s,没有扫码成功')
        except TimeoutError:
            return False
        finally:
            self.Sys_back()
            self.Sys_back()
            time.sleep(1)
"""