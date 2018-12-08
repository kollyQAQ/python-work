import itchat
from itchat.content import *
import common.global_var as GlobalVar

# 收到好友语音消息
@itchat.msg_register(RECORDING, isFriendChat=True)
def recording_reply(msg):
    GlobalVar.FRIENDS_NAME = msg['FromUserName']
    fileName = msg['FileName']
    print('收到来自【' + GlobalVar.FRIENDS_NAME + '】的语音:' + fileName)

    # 下载语音
    msg['Text'](GlobalVar.FILE_PATH_OTHER + fileName)
    itchat.send_msg('小糖还不够智能，没办法识别主人说的话呢，呜呜呜~', GlobalVar.FRIENDS_NAME)

    return None