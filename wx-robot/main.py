# 导入模块
from wxpy import *
from time import sleep
import random
import jobs.job as jobUtil
import common.weather_spider as weatherSpider

# 初始化机器人，扫码登陆
bot = Bot(cache_path=True, qr_path="/Users/kolly/workspace-demo/python-work/wx-robot/qrcode.jpg")
bot.enable_puid('wxpy_puid.pkl')

user_kolly = ensure_one(bot.friends().search('kolly'))


# 注册好友请求类消息
@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    # 自动接受验证信息中包含 'wxpy' 的好友请求
    # 判断好友请求中的验证文本
    # if 'wxpy' in msg.text.lower():
    # 接受好友 (msg.card 为该请求的用户对象)
    new_friend = bot.accept_friend(msg.card)
    # 或 new_friend = msg.card.accept()
    # 向新的好友发送消息
    new_friend.send('哈喽~我是你的专属机器人助理小糖 😘\n'
                    '你可以输入「help」查看小糖的使用指南噢~')
    user_kolly.send("自动回复已启动！")


# 打印所有收到的消息
@bot.register()
def print_messages(msg):
    print('收到消息：' + msg)


# 转发所有收到的好友消息或者群聊@消息给kolly
@bot.register(chats=[User, Group])
def forward_to_kolly(msg):
    # 随机等几秒，避免被风控
    sleep(random.randint(1, 3))
    # 如果是群聊，但没有被 @，则不回复
    if isinstance(msg.chat, Group) and not msg.is_at:
        return
    else:
        msg.forward(user_kolly, prefix=msg.sender.name + '发送内容:')


# 自动回复
@bot.register(chats=User)
def auto_reply(msg):
    # 随机等几秒，避免被风控
    sleep(random.randint(1, 3))
    if '天气' == msg.text:
        return weatherSpider.get_weather_today()
    if '篮球' == msg.text:
        return "https://sports.qq.com/kbsweb/kbsshare/gamelist.htm#nav-nba"
    if '热榜' == msg.text:
        return "https://tophub.today/"
    if '我要定制' == msg.text:
        return "请联系作者添加你想要的定制功能吧"
    if 'test' == msg.text:
        content = '/Users/kolly/workspace-demo/python-work/wx-robot/image/test.png'
        msg.reply_image(content)
        return
    if 'help' in msg.text:
        return "输入「天气」即可查询天气\n" \
               "输入「提醒」即可查询未来的提醒\n" \
               "输入「无聊」即可打发时间\n" \
               "输入「热榜」即可查询今日热榜消息\n" \
               "输入「股票」即可查询你关注的股票涨跌\n" \
               "输入「篮球」即可查询 NBA 今日赛事\n" \
               "输入「笑话」即可获得一个段子\n" \
               "输入「我要定制」即可添加小糖定制功能\n" \
               "输入「好文」即可开启阅读\n" \
               "输入「打卡」即可完成打卡\n" \
               "输入「我的打卡」即可查看打卡列表\n" \
               "输入「作者」即可联系作者\n" \
               "输入「赞赏」即可为小糖充电唷"
    return "小糖无法识别这个指定喔😯"


# 通知 kolly 程序已启动
user_kolly.send("自动回复已启动！")

# 启动定时任务
jobUtil.init_scheduler(bot)

# 进入 Python 命令行、让程序保持运行
# embed()
bot.join()

############################################################################################
# bot.friends()
# [<Friend: 小糖>, <Friend: kolly>, <Friend: Yocan>, <Friend: 彭喜糖>]
# 查看当前的注册配置情况
# bot.registered
############################################################################################
