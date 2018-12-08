import itchat
from itchat.content import *
import common.global_var as GlobalVar

# 收到好友文字消息
@itchat.msg_register(TEXT, isFriendChat=True)
def text_reply(msg):
    # 保存好友信息
    GlobalVar.FRIENDS_NAME = msg['FromUserName']
    print('收到来自【'+GlobalVar.FRIENDS_NAME+'】【' + msg['User'].NickName + '】的消息：' + msg['Text'])

    if msg['Text'] == '小游戏' or msg['Text'] == '玩游戏':
        itchat.send_msg('想玩小游戏了吗，嘿嘿，试着输入[猜码图]、[猜明星]、[成语接龙]吧，更有隐藏小游戏等你解锁哟~', GlobalVar.FRIENDS_NAME)
    else:
        itchat.send_msg(msg['Text'], GlobalVar.ICE_NAME)

    return None