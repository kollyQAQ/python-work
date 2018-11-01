# autor: kolly
# email: 1026774829@qq.com
# date: 2018-10-30

import itchat
from itchat.content import *

text = [TEXT]
contents = [PICTURE]


# 收到群聊的消息
@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    fromText = msg['Text']
    fromUserName = msg['FromUserName']
    actualNickName = msg['ActualNickName']
    chatRoomName = msg['User'].NickName
    try:
        print('收到来自群聊【' + chatRoomName + '】【' + actualNickName + '】的消息:' + fromText)
        if chatRoomName == '微信测试群' and actualNickName == 'kolly':
            itchat.send_msg(123, fromUserName)
    except Exception as e:
        itchat.send_msg(e.args[0], fromUserName)
    return None


# 收到群聊的图片/表情
@itchat.msg_register(contents, isGroupChat=True)
def contents_reply(msg):
    fileName = msg['FileName']
    fromUserName = msg['FromUserName']
    actualNickName = msg['ActualNickName']
    chatRoomName = msg['User'].NickName
    try:
        print('收到来自群聊【' + chatRoomName + '】【' + actualNickName + '】的图片:' + fileName)
        if chatRoomName == '微信测试群' and actualNickName == 'kolly':
            itchat.send_msg(123, fromUserName)
    except Exception as e:
        itchat.send_msg(e.args[0], fromUserName)
    return None


# 微信登录
itchat.auto_login(enableCmdQR=2, hotReload=True)

itchat.run()
