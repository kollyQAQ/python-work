from apscheduler.schedulers.blocking import BlockingScheduler

# 输出时间
def job():
    print(111111111)

# BlockingScheduler
scheduler = BlockingScheduler()
scheduler.add_job(job, 'interval', seconds=1) #每1秒执行
scheduler.start()
