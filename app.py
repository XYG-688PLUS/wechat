print('hellow')


# 导入包
from wxpy import *
# 初始化登录
# import itchat
# from itchat import send_msg
bot = Bot(cache_path=True)
# print(bot,'ss')

# 回复内容
@Bot.register(Friend,TEXT)
def auto_accept_friends(msg):
    print('信息'+msg.text)
    if msg.text!='null':
        msg.chat.send("[微信机器人回复]: 该账号疑似涉嫌一起洗钱行动已被封停30天查询处理")
# 好友统计 性别及地区分布


bot.join()