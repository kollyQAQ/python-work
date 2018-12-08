import itchat
from itchat.content import *
from time import sleep
import random
import common.global_var as GlobalVar

# 收到小冰的文本消息
@itchat.msg_register(TEXT, isMpChat=True)
def text_reply(msg):
    # 如果是小冰的消息，转发给好友
    if msg['FromUserName'] == GlobalVar.ICE_NAME and GlobalVar.FRIENDS_NAME != '':
        print('收到来自【小冰】的消息：' + msg['Text'])
        if '小冰' in msg['Text']:
            msg['Text'].replace('小冰','小糖')
        # 随机等1-3秒，避免被检测
        sleep(random.randint(1, 3))
        itchat.send(msg['Text'], GlobalVar.FRIENDS_NAME)
        # GlobalVar.FRIENDS_NAME = ''
    return None