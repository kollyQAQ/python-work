import itchatTest
from itchatTest.content import *
import re
import os

contents = [PICTURE]

CMD_PREFIX = 'prefix'
CMD_CHAT = 'chat'
CMD_SHUTUP = 'shutup'
CMD_SHOW = 'show'


chatRoomName = ''
chatRoomUserList = []
chatRoomUserAll = False
chatPrefix = ''
iceName = ''


@itchatTest.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    global chatRoomName,chatRoomUserList,chatRoomUserAll,chatPrefix,iceName

    fromText = msg['Text']
    fromUserName = msg['FromUserName']
    actualNickName = msg['ActualNickName']
    try:
        if fromText[0] == '#':
            if chatRoomName != '' and chatRoomName != msg['FromUserName']:
                itchatTest.send_msg('sorry,msice is busy~', msg['FromUserName'])
            list = re.split('\s+',fromText[1:],2)
            if '' in list:
                list.remove('')
            cmd = list[0].strip().lower()
            if cmd == CMD_CHAT:
                user = actualNickName if len(list)<2 else list[1]
                if user.lower() == 'all':
                    chatRoomUserAll = True
                    chatRoomUserList = []
                else:
                    if user in chatRoomUserList:
                        raise Exception('%s is already in chatlist' % user)
                    chatRoomUserList.append(user)
                chatRoomName = fromUserName
            elif cmd == CMD_PREFIX:
                if len(list)<2:
                    chatPrefix = ''
                else:
                    if chatPrefix == '#':
                        raise Exception('prefix can not be #')
                    else:
                        chatPrefix = list[1]
            elif cmd == CMD_SHUTUP:
                user = msg['ActualNickName'] if len(list)<2 else list[1]
                if user.lower() == 'all':
                    chatRoomUserAll = False
                    chatRoomUserList = []
                else:
                    if user in chatRoomUserList:
                        chatRoomUserList.remove(user)
                    else:
                        raise Exception('%s is not in chatlist at all' % user)
            elif cmd == CMD_SHOW:
                itchatTest.send_msg('list : %s\nprefix : %s' % (chatRoomUserList, chatPrefix), fromUserName)
            else:
                raise Exception('command not found')
            itchatTest.send_msg('cmd success \nlist : %s\nprefix : %s' % (chatRoomUserList, chatPrefix), fromUserName)
        elif fromText[:].startswith(chatPrefix):
            if chatRoomUserAll or actualNickName in chatRoomUserList:
                itchatTest.send_msg(fromText[:].replace(chatPrefix, '', 1), iceName)
    except Exception as e:
        itchatTest.send_msg(e.args[0], fromUserName)
    return None



@itchatTest.msg_register(TEXT, isMpChat=True)
def text_reply(msg):
    global chatRoomName,charRoomUserName,chatUserName,chatPrefix,iceName
    if msg['FromUserName'] == iceName:
        itchatTest.send(msg['Text'], chatRoomName)
    return None


@itchatTest.msg_register(contents, isGroupChat=True)
def contents_reply(msg):
    global chatRoomName,chatRoomUserList,chatRoomUserAll,chatPrefix,iceName
    actualNickName = msg['ActualNickName']
    if chatPrefix == '':
        if chatRoomUserAll or actualNickName in chatRoomUserList:
            fileName = msg['FileName']
            msg['Text'](fileName)
            itchatTest.send_image(fileName, iceName)
            os.remove(fileName)


@itchatTest.msg_register(contents, isMpChat=True)
def contents_reply(msg):
    global chatRoomName,chatRoomUserList,chatRoomUserAll,chatPrefix,iceName
    if msg['FromUserName'] == iceName:
        fileName = msg['FileName']
        msg['Text'](fileName)
        itchatTest.send_image(fileName, chatRoomName)
        os.remove(fileName)


@itchatTest.msg_register(FRIENDS)
def add_friend(msg):
    itchatTest.add_friend(**msg['Text'])
    itchatTest.send_msg('I am a msice robot!\n\t\t --designed by dxy', msg['RecommendInfo']['UserName'])


itchatTest.auto_login(hotReload=True, enableCmdQR=1)

ice = itchatTest.search_mps(name='微软小冰')
iceName = ice[0]['UserName']

itchatTest.run()

