# 导入:
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://jiayoubao:root1234@172.16.1.13:3306/test_db')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

def getSession():
    return DBSession()