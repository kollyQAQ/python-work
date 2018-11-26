import itchat
from itchatTest.utils import weather_util
from itchatTest.utils import contact
from apscheduler.schedulers.background import BackgroundScheduler

# 发送天气信息
def send_weather_info():
    # itchat.send(weather_util.get_weather_today(), contact.get_user_name_by_remark('kolly'))
    ice = itchat.search_mps(name='小冰')
    iceName = ice[0]['UserName']
    itchat.send('深圳天气', iceName)

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

# BackgroundScheduler
scheduler = BackgroundScheduler()
scheduler.add_job(send_weather_info, 'cron', day_of_week='mon-sun', hour=7, minute=0) #corn表达式
scheduler.add_job(send_joke, 'cron', day_of_week='mon-sun', hour=7, minute=15) #corn表达式
scheduler.add_job(send_news, 'cron', day_of_week='mon-sun', hour=12, minute=30) #corn表达式
scheduler.add_job(send_news, 'cron', day_of_week='mon-sun', hour=17, minute=30) #corn表达式
scheduler.start()