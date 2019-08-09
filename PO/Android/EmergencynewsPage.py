from PO.basePage import Base
from selenium.webdriver.common.by import By
import time

class EmergencynewsPage(Base):
    '''
    紧急消息界面
    '''

    click_news = (By.XPATH, "//android.widget.ImageView[@resource-id='com.pundix.xwallet:id/iv_notice']")  #点击紧急消息菜单
    click_one_news = (By.XPATH, "//android.widget.TextView[@resource-id='com.pundix.xwallet:id/tv_subTitle']")  #点击第一条信息
    get_page_text = (By.CLASS_NAME, "android.webkit.WebView")  #获取页面的文本


    def Click_Emergencynews(self):
        '''点击紧急消息'''

        time.sleep(2)
        self.driver.find_element(*self.click_news).click()  #点击紧急消息菜单
        time.sleep(2)
        self.driver.find_element(*self.click_one_news).click()  #点击第一条信息
        time.sleep(10)
        text = self.driver.find_element(*self.get_page_text).text #获取页面的文本,如果找到 Webpage not available文本,则返回失败，反之返回成功
        while not self.findElement(text):
            return True
        else:
            return False
