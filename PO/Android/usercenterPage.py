from PO.basePage import Base
from selenium.webdriver.common.by import By
import time


class UsercenterPage(Base):
    """
    个人中心的页面元素
    """

    # ———————————————————————头像区域——————————————————————————#
    head = (By.ID, 'iv_head')  # 头像
    nickname = (By.ID, 'tv_nickname')  # 昵称
    change_head = (By.ID, 'rl_layout_hand')  # 头像—进入手机相机
    head_gallery = (By.ID, 'btn_gallery')  # 手机相册
    head_photo = (By.ID, 'btn_picturey')  # 照相
    photo = (By.XPATH,
             '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ImageView')  # x选择照片
    photo_back = (By.XPATH,
                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageButton')  # 相册页面的返回
    gender = (By.ID, 'iv_gender_arrow')  # 性别
    ok = (By.ID, 'tv_complete')  # 性别选择框-ok
    cancel = (By.ID, 'tv_cancel')  # 性别选择框-cancel
    option_btn = (By.ID, 'options1')  # 第一选项

    # ———————————————————————收款码——————————————————————————#
    Collection = (By.ID, 'rl_layout_collection')  # 收款码

    # ———————————————————————总资产——————————————————————————#
    Assets = (By.ID, 'rl_layout_assets')  # 资产
    Assets_Account = 'Accounts'
    Assets_Coint = 'Coins'

    # ———————————————————————总账单——————————————————————————#
    Bills = (By.ID, 'rl_layout_bill')  # 总账单
    bill_type = (By.ID, 'tv_order_type')  # 账单类别分类
    bill_card = (By.ID, 'tv_card_type')  # 账单卡片分类

    # ———————————————————————优惠券——————————————————————————#
    coupon = (By.ID, 'rl_layout_coupon')  # 优惠券

    # ———————————————————————KYC——————————————————————————#
    kyc = (By.ID, 'rl_layout_personal_center')  # KYC

    # ———————————————————————个人中心——————————————————————————#
    setting = (By.ID, "rl_layout_setting")  # 个人中心的设置

    # ———————————————————————商户后台——————————————————————————#
    merchant = (By.ID, 'rl_layout_merchant_setting')  # 商户后台

    # ———————————————————————工单——————————————————————————#
    help_btn = (By.ID, 'rl_layout_help_feedback')  # feedback

    def into_Collection(self):
        """ 进入收款码页面"""

        self.driver.find_element(*self.Collection).click()

    def into_Assets(self):
        """进入总资产界面"""

        self.driver.find_element(*self.Assets).click()

    def switch_Assets(self, type='coin'):
        """总资产切换选项"""

        if type == 'coin':
            self.driver.find_element_by_android_uiautomator('new UiSelector().text("Accounts")').click()
        else:
            self.driver.find_element_by_android_uiautomator('new UiSelector().text("Coins")').click()

    def into_Bill(self):
        """进入总账单"""

        self.driver.find_element(*self.Bills).click()

    def into_coupon(self):
        """进入优惠券"""

        self.driver.find_element(*self.coupon).click()

    def into_KYC(self):
        """进入kyc"""

        self.driver.find_element(*self.kyc).click()

    def into_setting(self):
        """进入设置界面"""

        self.driver.find_element(*self.setting).click()

    def into_merchant(self):
        """进入商户设置"""

        self.driver.find_element(*self.merchant).click()

    def into_help(self):
        """进入帮助界面"""

        self.driver.find_element(*self.help_btn).click()
