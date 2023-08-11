from dingtalkchatbot.chatbot import DingtalkChatbot
from django.conf import settings

def send(message, at_mobiles=['18501705997']):
    # 引用 settings 里面配置的钉钉群消息通知的 webhook 地址：
    webhook = settings.DING_TALK_WEB_HOOK

    # 初始化机器人小丁，#方式一：通常初始化方式
    xiaoding = DingtalkChatbot(webhook)

    # 方式二：勾选"加签"选项时候使用的（v1.5以上新功能）
    # xiaoding = DingtalkChatbot(webhok, secret=secret)

    xiaoding.send_text(msg=('面试通知： %s' %message), at_mobiles=at_mobiles)

