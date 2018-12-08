import itchat
import common.global_var as GlobalVar
import scheduler.scheduler_task as schedulerTask
from itchatTest.chat import *

# 微信登录
# itchat.auto_login(enableCmdQR=2, hotReload=True)
itchat.auto_login(hotReload=True)
# itchat.auto_login()

# 查找小冰公众号名称保存到 iceName 变量
ice = itchat.search_mps(name='小冰')
GlobalVar.ICE_NAME = ice[0]['UserName']

# 启动定时任务
schedulerTask.init_scheduler()

itchat.run()