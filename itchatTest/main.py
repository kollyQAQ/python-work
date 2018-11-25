import re
import os
import itchat
from itchat.content import *
from itchatTest.utils import contact
import random
from time import sleep
from itchatTest.scheduler import send_weather_info #勿删

CMD_PREFIX = 'prefix'
CMD_CHAT = 'chat'
CMD_SHUTUP = 'shutup'
CMD_SHOW = 'show'

friendsName = contact.get_user_name_by_remark('赖皮糖')
chatRoomName = ''
chatRoomUserList = []
chatRoomUserAll = False
chatPrefix = ''

# 收到加好友邀请
@itchat.msg_register(FRIENDS)
def add_friend(msg):
    print(msg)
    msg.user.verify()
    msg.user.send('终于等到你啦，主人~')
    msg.user.send('我是你的贴心机器人，可以陪你聊天，给你唱歌、讲段子，还有好玩的小游戏哦')

# 收到好友文字消息
@itchat.msg_register(TEXT, isFriendChat=True)
def text_reply(msg):
    global friendsName, iceName

    # 保存好友信息
    friendsName = msg['FromUserName']
    print('收到来自【'+friendsName+'】【' + msg['User'].NickName + '】的消息：' + msg['Text'])

    itchat.send_msg(msg['Text'], iceName)

    return None

# 收到好友图片/表情消息
@itchat.msg_register(PICTURE, isFriendChat=True)
def picture_reply(msg):
    global friendsName, iceName

    friendsName = msg['FromUserName']
    fileName = msg['FileName']
    print('收到来自【' + friendsName + '】的图片:' + fileName)

    # 下载图片
    msg['Text'](fileName)
    # 转发给小冰
    itchat.send_image(fileName, iceName)
    # 删除图片
    os.remove(fileName)

# 收到好友语音消息
@itchat.msg_register(RECORDING, isFriendChat=True)
def picture_reply(msg):
    global friendsName, iceName

    friendsName = msg['FromUserName']
    fileName = msg['FileName']
    print('收到来自【' + friendsName + '】的语音:' + fileName)

    # 下载语音
    msg['Text']('D:\workspace-demo\python-work\itchatTest\static\other\\' + fileName)
    sleep(5)
    itchat.send_msg('等我升级后再跟你说话~', friendsName)

# 收到小冰的文本消息
@itchat.msg_register(TEXT, isMpChat=True)
def text_reply(msg):
    global friendsName, iceName

    # 如果是小冰的消息，转发给好友
    if msg['FromUserName'] == iceName and friendsName != '':
        print('收到来自小冰的消息：' + msg['Text'])
        # 如果是小冰的消息，转发给好友
        # 随机等1-2秒，避免被检测
        sleep(random.randint(1, 3))
        itchat.send(msg['Text'], friendsName)
        # friendsName = ''
    return None

# 收到小冰的的图片/表情
@itchat.msg_register(PICTURE, isMpChat=True)
def picture_reply(msg):
    global friendsName, iceName

    if msg['FromUserName'] == iceName and friendsName != '':
        fileName = msg['FileName']
        print('收到来自小冰的图片:' + fileName)
        # 下载图片
        msg['Text'](fileName)
        # 转发图片/表情给好友
        # 随机等1-2秒，避免被检测
        itchat.send_image(fileName, friendsName)
        # friendsName = ''
        # 删除图片
        os.remove(fileName)
    return None

# 收到小冰的语音消息
@itchat.msg_register(RECORDING, isMpChat=True)
def recording_reply(msg):
    global friendsName, iceName

    if msg['FromUserName'] == iceName and friendsName != '':
        fileName = msg['FileName']
        print('收到来自小冰的语音:' + fileName)
        # 下载语音
        msg['Text']('D:\workspace-demo\python-work\itchatTest\static\ice\\' + fileName)
        # 转发语音给好友
        sleep(5)
        itchat.send_file(fileName, friendsName)
        # friendsName = ''
    return None

# # 收到群聊的消息
# @itchat.msg_register(TEXT, isGroupChat=True)
# def text_reply(msg):
#     global chatRoomName, chatRoomUserList, chatRoomUserAll, chatPrefix, iceName
#
#     fromText = msg['Text']
#     fromUserName = msg['FromUserName']
#     actualNickName = msg['ActualNickName']
#     chatRoomName = msg['User'].NickName
#     try:
#         if fromText[0] == '#':
#             if chatRoomName != '' and chatRoomName != msg['FromUserName']:
#                 itchat.send_msg('sorry,msice is busy~', msg['FromUserName'])
#             list = re.split('\s+', fromText[1:], 2)
#             if '' in list:
#                 list.remove('')
#             cmd = list[0].strip().lower()
#             if cmd == CMD_CHAT:
#                 user = actualNickName if len(list) < 2 else list[1]
#                 if user.lower() == 'all':
#                     chatRoomUserAll = True
#                     chatRoomUserList = []
#                 else:
#                     if user in chatRoomUserList:
#                         raise Exception('%s is already in chatlist' % user)
#                     chatRoomUserList.append(user)
#                 chatRoomName = fromUserName
#             elif cmd == CMD_PREFIX:
#                 if len(list) < 2:
#                     chatPrefix = ''
#                 else:
#                     if chatPrefix == '#':
#                         raise Exception('prefix can not be #')
#                     else:
#                         chatPrefix = list[1]
#             elif cmd == CMD_SHUTUP:
#                 user = msg['ActualNickName'] if len(list) < 2 else list[1]
#                 if user.lower() == 'all':
#                     chatRoomUserAll = False
#                     chatRoomUserList = []
#                 else:
#                     if user in chatRoomUserList:
#                         chatRoomUserList.remove(user)
#                     else:
#                         raise Exception('%s is not in chatlist at all' % user)
#             elif cmd == CMD_SHOW:
#                 itchat.send_msg('list : %s\nprefix : %s' %
#                                     (chatRoomUserList, chatPrefix), fromUserName)
#             else:
#                 raise Exception('command not found')
#             itchat.send_msg('cmd success \nlist : %s\nprefix : %s' %
#                                 (chatRoomUserList, chatPrefix), fromUserName)
#         elif fromText[:].startswith(chatPrefix):
#             print('收到来自群聊【' + chatRoomName + '】【' + actualNickName + '】的消息:' + fromText)
#             if chatRoomUserAll or actualNickName in chatRoomUserList:
#                 itchat.send_msg(123456, fromUserName)
#     except Exception as e:
#         itchat.send_msg(e.args[0], fromUserName)
#     return None
#
# # 收到群聊的图片/表情
# @itchat.msg_register(PICTURE, isGroupChat=True)
# def picture_reply(msg):
#     fileName = msg['FileName']
#     fromUserName = msg['FromUserName']
#     actualNickName = msg['ActualNickName']
#     chatRoomName = msg['User'].NickName
#     try:
#         print('收到来自群聊【' + chatRoomName + '】【' + actualNickName + '】的图片:' + fileName)
#         if chatRoomName == '微信测试群' and actualNickName.startswith('kolly'):
#             itchat.send_msg(123456, fromUserName)
#     except Exception as e:
#         itchat.send_msg(e.args[0], fromUserName)
#     return None

# 微信登录
# itchat.auto_login(enableCmdQR=2, hotReload=True)
itchat.auto_login(hotReload=True)
# itchat.auto_login()

# 查找小冰公众号名称保存到 iceName 变量
ice = itchat.search_mps(name='小冰')
iceName = ice[0]['UserName']

itchat.run()


