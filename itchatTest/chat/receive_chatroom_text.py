import re
import itchat
from itchat.content import *
from itchatTest.common.global_var import *
import common.global_var as GlobalVar

# 收到群聊的消息
@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    fromText = msg['Text']
    fromUserName = msg['FromUserName']
    actualNickName = msg['ActualNickName']
    chatRoomName = msg['User'].NickName
    try:
        if fromText[0] == '#':
            if chatRoomName != '' and chatRoomName != msg['FromUserName']:
                itchat.send_msg('sorry,msice is busy~', msg['FromUserName'])
            list = re.split('\s+', fromText[1:], 2)
            if '' in list:
                list.remove('')
            cmd = list[0].strip().lower()
            if cmd == CMD_CHAT:
                user = actualNickName if len(list) < 2 else list[1]
                if user.lower() == 'all':
                    GlobalVar.CHATROOM_USER_ALL = True
                    chatRoomUserList = []
                else:
                    if user in GlobalVar.CHATROOM_USER_LIST:
                        raise Exception('%s is already in chatlist' % user)
                    GlobalVar.CHATROOM_USER_LIST.append(user)
                GlobalVar.CHATROOM_NAME = fromUserName
            elif cmd == CMD_PREFIX:
                if len(list) < 2:
                    chatPrefix = ''
                else:
                    if GlobalVar.CHAT_PREFIX == '#':
                        raise Exception('prefix can not be #')
                    else:
                        chatPrefix = list[1]
            elif cmd == CMD_SHUTUP:
                user = msg['ActualNickName'] if len(list) < 2 else list[1]
                if user.lower() == 'all':
                    chatRoomUserAll = False
                    GlobalVar.CHATROOM_USER_LIST = []
                else:
                    if user in GlobalVar.CHATROOM_USER_LIST:
                        GlobalVar.CHATROOM_USER_LIST.remove(user)
                    else:
                        raise Exception('%s is not in chatlist at all' % user)
            elif cmd == CMD_SHOW:
                itchat.send_msg('list : %s\nprefix : %s' %
                                    (GlobalVar.CHATROOM_USER_LIST, GlobalVar.CHAT_PREFIX), fromUserName)
            else:
                raise Exception('command not found')
            itchat.send_msg('cmd success \nlist : %s\nprefix : %s' %
                                (chatRoomUserList, chatPrefix), fromUserName)
        elif fromText[:].startswith(GlobalVar.CHAT_PREFIX):
            print('收到来自群聊【' + chatRoomName + '】【' + actualNickName + '】的消息:' + fromText)
            if GlobalVar.CHATROOM_USER_ALL or actualNickName in GlobalVar.CHATROOM_USER_LIST:
                itchat.send_msg(123456, fromUserName)
    except Exception as e:
        itchat.send_msg(e.args[0], fromUserName)
    return None