from PO.basePage import Base
from selenium.webdriver.common.by import By
import time


class DappVirtualCardPage(Base):
    """
    虚拟卡界面的页面元素
    """

    # DAPP页面 虚拟卡片 DAPP首页
    Virtual_BTC = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.ImageView")  # 虚拟卡片中的BTC
    Virtual_ETH = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.TextView")  #虚拟卡片中的ETH
    Virtual_Go = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ImageView[2]")  #虚拟卡片中的"更多"键

    #卡片详情页面
    Virtual_Eye = (By.ID, "tv_amout")  #虚拟卡片中的加密按键
    Virtual_Setting = (By.ID, "iv_setting")  #虚拟卡片片中的设置按键
    Virtual_bills =(By.ID, "iv_bills")  #虚拟卡片中的账单按键
    Virtual_Receive =(By.ID, "btn_recharge")  #查看虚拟卡片充值地址
    Virtual_transfer =(By.ID, "btn_withdraw")  #查看虚拟卡片转账地址
    Virtual_Menu =(By.ID, "iv_menu")    #虚拟卡片详情页面的菜单按键
    Virtual_Internal_Transfer = (By.ID, "tv_refresh")   #虚拟卡片界面点击卡内划转
    Virtual_Back =(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ImageButton")    #虚拟卡片详情页面左上角返回按钮

    Virtual_refresh =(By.ID, "iv_refresh") #虚拟卡片页面的二维码刷新按键
    Virtual_view_Address = (By.ID, "btn_view_recharge")  #虚拟卡片查看充值地址，提醒页面
    Virtual_Copy_Address = (By.ID, "btn_single_copy") #复制虚拟卡片充值地址
    Receiving_address_close =(By.ID, "iv_close") #查看充值地址说明页面的关闭按键

     # 转账页面
    Transfer_Address=(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.ImageView")  #在转账页面，选择添加地址
    Transfer_Scan =(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.ImageView")      #在转账页面，点击扫码
    Transfer_Amount_All =(By.ID, "tv_allCoinNumber")    #在转账页面金额转出all
    Transfer_server =(By.ID, "tv_serviceCharge")    #在转账页面查看手续费说明
    Transfer_KYC =(By.ID, "tv_kycVerify")   #在转账页面点击KYV认证
    Tranfer_Next = (By.ID, "btn_withdraw")  #转账页面点击下一步
    Add_Address =(By.ID, "iv_menu")     #转账页面添加转账地址

    #BEP-2协议币种转账页面附言
    Transfer_Memo = (By.ID, "ed_transfer_msg")      #在转账页面点击Memo输入框
    transfer_Memo_Scan = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[4]/android.widget.RelativeLayout/android.widget.ImageView")       #在Memo输入时选择扫码

    #Google认证提示
    Google_Notnow =(By.ID, "btn_no")    #Google认证时，选择Not Now
    Google_confirm =(By.ID, "btn_yes")  #google认证时，选择confirm

    #添加提现地址
    Add_address_Send = (By.ID, "tv_send_email_code")    #添加地址时，发送邮箱验证码
    Add_address_Next = (By.ID, "btn_withdrawNext2")     #添加转账地址时，输入验证码后，点击下一步

    #虚拟卡片BEP-2协议币种(带附言的币种:BNB + NPXSXEM）
    Virtual_BNB_QRcode =(By.ID, "btn_many_get_address")     #BNB查看充值地址二维码
    Virtual_BNB_QRcode_close = (By.ID, "iv_close")      #BNB关闭充值地址二维码页面
    Virtual_BNB_copy_address = (By.ID, "btn_many_copy_address")     #复制BNB充值地址
    Virtual_BNB_Memo_QRcode  = (By.ID, "btn_many_get_message")      #BNB查看附言二维码
    Virtual_BNB_Memo_close = (By.ID,"rl_layout_close")      #BNB关闭附言二维码页面
    Virtual_BNB_Copy_Memo = (By.ID, "btn_many_copy_message")    #BNB 复制附言

    #虚拟卡片NPXSXEM
    Virtual_NPXEXEM_Address = (By.ID,"tv_count_down_timer")     #NPXSXEM 查看充值地址，弹出5说明提醒界面
    Virtual_NPXSXEM_agree = (By.ID, "cb_select_agree")      #NPXSXEM 查看充值地址，同意协议
    Virtual_NPXSXEM_Transfer = (By.ID, "btn_ok")        #NPXSXEM 转账弹出确认按钮

    #内部划账
    Virtual_Internal_Transfer = (By.ID, "tv_refresh")       #虚拟卡片中内部划转入口
    Virtual_Internal_Transfer_back = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageButton")       #内部划转左上角返回键
    Virtual_Internal_Transfer_change = (By.ID, "iv_exchange")       #虚拟卡片内部划转切卡片位置
    Virtual_Internal_Transfer_FromCard = (By.ID,"tv_from_card_id")      #内部划转选择From方卡片
    Virtual_Internal_Transfer_Tocard = (By.ID, "tv_to_card_id")     #内部划转选择To方卡片
    Virtual_Internal_Transfer_Accoutclose = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ImageView")       #内部划转在选择卡片时，点击X
    Virtual_Internal_Transfer_Accountselect = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout")       #内部划转，选择转账卡片
    Virtual_Internal_Transfer_Coin = (By.ID, "tv_cion")     #内部划转选择转账币种
    Virtual_Internal_Transfer_Coinselect = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout")
    Virtual_Internal_Transfer_ALl = (By.ID, "tv_available_all")     #内部划转金额选择all
    Virtual_Internal_Transfer_Available = (By.ID, "ed_available")       #内部划转手动输入金额
    Virtual_Internal_Transfer_Confirm = (By.ID, "btn_transfer")     #内部划转选择确认

    #虚拟卡片卡片详情中的历史账单
    Virtual_Transition_Hisrory = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[2]")      #虚拟卡片，卡片详情中的历史账单


    #添加XPASS卡
    Add_card =(By.ID, "ib_add_card")        #添加卡片按钮
    Add_XPASS = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView")      #点击添加XPASS卡
    Add_XPASS_No = (By.ID , "ed_addCardXpassNO")       #输入XPASS卡号输入框
    Add_XPASS_Next = (By.ID, "btn_addCardNext")         #输入卡号后下一步按钮
    Add_XPASS_6pin_code = (By.ID, "ed_addCardXpassNO")      #输入6位密码
    Add_XPASS_confirm = (By.ID, "btn_addCardNext")      #最后一步确认按键

    #添加开放平台卡片
    Add_opencard = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView[2]")     #选择开放平台卡片
    Add_opencard_select_Virtual = (By.Id, "rl_virtualFlag")     #添加开放平台卡片时，选择添加虚拟卡
    Add_opencard_select_Physical =(By.ID, "rl_physicalFlag")    #添加开放平台卡片时，选择添加物理卡片

    # 开放平台卡片
    Open_Platform_Card_Pay = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.ImageView")    #点击开放平台卡片Pay按钮
    Open_Platform_Card_Transfer =(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.ImageView")     #点击开放平台卡片上的Transfer按钮
    Open_Platform_Card_Website =(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout")      #开放平台卡片上的开发者网站

    #添加开放平台APP
    open_platform_app_Add =(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView")    #添加开放平台APP
    Open_Platfrom_app = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.ImageView")  #点击DApp首页APP入口
    Open_Platform_app_About = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.ImageView")   #点击DAPP首页关于入口
