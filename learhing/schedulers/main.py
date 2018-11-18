from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

# 输出时间
def job1():
    print(111111111)

def job2():
    print(2222222)

# BlockingScheduler
scheduler = BlockingScheduler()
scheduler.add_job(job1, 'interval', seconds=1) #每1秒执行
scheduler.add_job(job2, 'date', run_date='2018-11-18 17:50:00') #指定时间执行
scheduler.add_job(job2, 'date', run_date=datetime.now()) #指定时间执行
scheduler.add_job(job2, 'cron', day_of_week='mon-fri', hour=18, minute=10) #corn表达式
scheduler.start()
