import itchat
from itchat.content import *

# 收到加好友邀请
@itchat.msg_register(FRIENDS)
def add_friend(msg):
    print(msg)
    msg.user.verify()
    msg.user.send('终于等到你啦，主人~')
    msg.user.send('我是你的贴心机器人小糖，可以陪你聊天、唱歌、讲段子，还有好玩的小游戏哦')