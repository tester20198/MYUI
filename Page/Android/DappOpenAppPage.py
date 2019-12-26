from Page.basePage import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class DappOpenAppPage(Base):
    """
    Dapp-开放平台app
    """
    click_dapp = (By.XPATH, "//android.widget.TextView[@text='DApp']")  # 点击dapp标题
    get_balance_text = (By.XPATH, "//android.widget.TextView[@text='Balance']")  #获取Dapp页面Balance的文本信息
    add_card = (By.ID, "ib_add_card")  # 添加卡片按钮

    # 添加开放平台APP
    add_open_app = (By.XPATH, "//android.widget.TextView[@resource-id='com.pundix.xwallet:id/tv_type_app']")  # 添加app
    Open_Platfrom_app = (By.XPATH, "//android.widget.TextView[@resource-id='com.pundix.xwallet:id/tv_currency']")  # 点击DApp首页APP入口
    Open_Platform_app_About = (By.XPATH, "//android.widget.TextView[@text='About us']")  # 点击DAPP首页关于入口

    about_us_title = (By.XPATH,"//android.widget.TextView[@resource-id='com.pundix.xwallet:id/developer_tv_title']") #关于页面标题
    home_app = (By.CLASS_NAME,'android.view.View') #首页APP跳转页面
    home_app_delele = (By.ID,'developer_iv_menu') #首页APP跳转页面关闭按钮
    rmove_app1 = (By.ID,'developer_iv_menu') #删除app
    rmove_app2 = (By.XPATH,"//android.widget.TextView[@text='Remove form my XApp']") #删除app


    def dapp_page(self):
        '''进入dapp页面'''

        WebDriverWait(self.driver, 10, 0.5).until(EC.text_to_be_present_in_element(self.get_balance_text,u'Balance'))  #获取Dapp页面Balance
        self.driver.find_element(*self.click_dapp).click()  # 进入dapp页面

    def add_app_buisess(self,type):
        '''添加卡片流程'''

        self.swipeUp(duration=1500)
        self.swipeUp(duration=1500)
        self.driver.find_element(*self.add_card).click()  # 点击添加按钮
        time.sleep(2)
        Virtual_Card = (By.XPATH, f'//android.widget.TextView[contains(@text, "{type}")]')  # 进入添加卡片列表界面定位app
        while not self.findElement(type):
            self.swipeUp(duration=1500)
            self.swipeUp(duration=1500)
        else:
            self.driver.find_element(*Virtual_Card).click()

    def click_app_home(self):
        '''点击app首页'''

        self.driver.find_element(*self.Open_Platfrom_app).click()
        time.sleep(3)
        text = self.driver.find_element(*self.home_app).text  # 获取页面内容，为空则失败,反之返回成功
        if text == None:
            return False
        else:
            return True

    def click_About_us(self):
        '''点击app关于'''

        self.driver.find_element(*self.Open_Platform_app_About).click()
        time.sleep(3)
        text = self.driver.find_element(*self.about_us_title).text  # 获取页面标题，为空则失败,反之返回成功
        if text == None:
            return False
        else:
            return True

    def remove_app(self):
        '''删除app'''

        self.driver.find_element(*self.Open_Platfrom_app).click()
        time.sleep(3)
        self.driver.find_element(*self.rmove_app1).click()
        time.sleep(1)
        self.driver.find_element(*self.rmove_app2).click()
        time.sleep(2)

    def app_home_colse(self):
        '''app首页关闭按钮'''

        self.driver.find_element(*self.Open_Platform_app_About).click()
        time.sleep(3)
        self.driver.find_element(*self.home_app_delele).click()
        time.sleep(2)
        msg = WebDriverWait(self.driver, 10, 0.5).until(EC.text_to_be_present_in_element(self.get_balance_text, u'Balance'))
        print(msg)
        return msg