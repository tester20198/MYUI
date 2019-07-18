from PO.basePage import Base
from selenium.webdriver.common.by import By
import time


class LoginPage(Base):
    """
    启动页+登录界面的页面元素
    """

    # Android
    sunge = (By.ID, 'zhuce')