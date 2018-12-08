import os
import itchat
from itchat.content import *
import common.global_var as GlobalVar

# 收到好友图片/表情消息
@itchat.msg_register(PICTURE, isFriendChat=True)
def picture_reply(msg):
    GlobalVar.FRIENDS_NAME = msg['FromUserName']
    fileName = msg['FileName']
    print('收到来自【' + GlobalVar.FRIENDS_NAME + '】的图片:' + fileName)

    # 下载图片
    msg['Text'](fileName)
    # 转发给小冰
    itchat.send_image(fileName, GlobalVar.FRIENDS_NAME)
    # 删除图片
    os.remove(fileName)

    return None