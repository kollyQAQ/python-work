import os
import itchat
from itchat.content import *

# 收到群聊的图片/表情
@itchat.msg_register(PICTURE, isGroupChat=True)
def picture_reply(msg):
    fileName = msg['FileName']
    fromUserName = msg['FromUserName']
    actualNickName = msg['ActualNickName']
    chatRoomName = msg['User'].NickName
    try:
        print('收到来自群聊【' + chatRoomName + '】【' + actualNickName + '】的图片:' + fileName)
        if chatRoomName == '微信测试群' and actualNickName.startswith('kolly'):
            itchat.send_msg(123456, fromUserName)
    except Exception as e:
        itchat.send_msg(e.args[0], fromUserName)
    return None