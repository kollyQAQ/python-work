import itchat
from itchat.content import *
from time import sleep
import common.global_var as GlobalVar

# 收到小冰的语音消息
@itchat.msg_register(RECORDING, isMpChat=True)
def recording_reply(msg):
    if msg['FromUserName'] == GlobalVar.ICE_NAME and GlobalVar.FRIENDS_NAME != '':
        fileName = msg['FileName']
        print('收到来自【小冰】的语音:' + fileName)
        # 下载语音
        msg['Text'](GlobalVar.FILE_PATH + fileName)
        # 转发语音给好友
        sleep(5)
        itchat.send_file(GlobalVar.FILE_PATH + fileName, GlobalVar.FRIENDS_NAME)
        # GlobalVar.FRIENDS_NAME = ''
    return None