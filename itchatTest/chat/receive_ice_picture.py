import os
import itchat
from itchat.content import *
import common.global_var as GlobalVar

# 收到小冰的的图片/表情
@itchat.msg_register(PICTURE, isMpChat=True)
def picture_reply(msg):
    if msg['FromUserName'] == GlobalVar.ICE_NAME and GlobalVar.FRIENDS_NAME != '':
        fileName = msg['FileName']
        print('收到来自【小冰】的图片:' + fileName)
        # 下载图片
        msg['Text'](fileName)
        # 转发图片/表情给好友
        # 随机等1-2秒，避免被检测
        itchat.send_image(fileName, GlobalVar.FRIENDS_NAME)
        # GlobalVar.FRIENDS_NAME = ''
        # 删除图片
        os.remove(fileName)
    return None