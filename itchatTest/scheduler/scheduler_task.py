import itchat
import utils.contact as contact
from time import sleep
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import utils.weather_util as weather_util
import common.global_var as GlobalVar

# 查询天气信息
def query_weather_info():
    itchat.send_msg('深圳天气', GlobalVar.ICE_NAME)

# 发送天气信息
def send_weather_info():
    info = '啦啦啦，美好的一天又开始啦😝，小糖早报：\n今天是 ' + weather_util.get_weather_today()
    user = contact.get_user_name_by_remark('kolly')
    itchat.send(info, user)
    user = contact.get_user_name_by_remark('彭喜糖')
    itchat.send(info, user)

# 发送午安
def send_good_afternoon():
    info = '中午不睡，下午崩溃，赶紧午休一下吧😝~'
    user = contact.get_user_name_by_remark('kolly')
    itchat.send(info, user)
    user = contact.get_user_name_by_remark('彭喜糖')
    itchat.send(info, user)

# 发送晚安
def send_good_night():
    info = '狗命要紧，赶紧准备准备，滚去睡觉吧😝~'
    user = contact.get_user_name_by_remark('kolly')
    itchat.send(info, user)
    user = contact.get_user_name_by_remark('彭喜糖')
    itchat.send(info, user)

# 发送笑话
def send_joke():
    ice = itchat.search_mps(name='小冰')
    iceName = ice[0]['UserName']
    itchat.send('讲个笑话', iceName)

# 发送八卦娱乐新闻
def send_news():
    ice = itchat.search_mps(name='小冰')
    iceName = ice[0]['UserName']
    itchat.send('最近新闻', iceName)

# 发送指定信息
def send_sth():
    sleep(10)
    user = contact.get_user_name_by_remark('kolly')
    itchat.send('我肥来啦~', user)
    itchat.send('啦啦啦，美好的一天又开始啦😝，小糖早报：\n今天是 ' + weather_util.get_weather_today(), user)

def init_scheduler():
    # BackgroundScheduler
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_weather_info, 'cron', day_of_week='mon-sun', hour=6, minute=0) #corn表达式
    scheduler.add_job(send_good_afternoon, 'cron', day_of_week='mon-sun', hour=13, minute=0) #corn表达式
    scheduler.add_job(send_good_night, 'cron', day_of_week='mon-sun', hour=23, minute=0) #corn表达式
    # scheduler.add_job(send_joke, 'cron', day_of_week='mon-sun', hour=7, minute=15) #corn表达式
    # scheduler.add_job(send_news, 'cron', day_of_week='mon-sun', hour=12, minute=30) #corn表达式
    scheduler.add_job(send_sth, 'date', run_date=datetime.now()) #立刻执行
    # scheduler.add_job(send_sth, 'date', run_date='2018-12-02 21:42:00') #指定时间执行
    scheduler.start()