import itchat
from itchatTest.utils import weather_util
from apscheduler.schedulers.background import BackgroundScheduler

# 发送天气信息
def send_weather_info():
    itchat.send(weather_util.get_weather_today(), '@71857beb8d5bd020fc16f2a55173cc17')

# BackgroundScheduler
scheduler = BackgroundScheduler()
scheduler.add_job(send_weather_info, 'cron', day_of_week='mon-sun', hour=18, minute=18) #corn表达式
scheduler.start()