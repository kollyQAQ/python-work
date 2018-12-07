import itchat
from itchatTest.utils import contact
from time import sleep
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

filePath = 'D:\workspace-demo\python-work\itchatTest\static\ice\\'

# 发送天气信息
def send_weather_info():
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

# 发送指定信息
def send_sth():
    sleep(10)
    user = contact.get_user_name_by_remark('彭喜糖')
    itchat.send('亲爱哒~我肥来啦~MUA', user)
    sleep(1)
    itchat.send('我给你唱首歌吧~', user)
    sleep(1)
    itchat.send_file(filePath + '181125-155837.mp3', user)

# BackgroundScheduler
scheduler = BackgroundScheduler()
scheduler.add_job(send_weather_info, 'cron', day_of_week='mon-sun', hour=7, minute=0) #corn表达式
scheduler.add_job(send_joke, 'cron', day_of_week='mon-sun', hour=7, minute=15) #corn表达式
scheduler.add_job(send_news, 'cron', day_of_week='mon-sun', hour=12, minute=30) #corn表达式
# scheduler.add_job(send_sth, 'date', run_date=datetime.now()) #指定时间执行
# scheduler.add_job(send_sth, 'date', run_date='2018-12-02 21:42:00') #指定时间执行
scheduler.start()