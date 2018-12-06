# 导入:
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(Integer, primary_key=True, autoincrement=True)
    nick_name = Column(String(64))
    remark_name = Column(String(64))
    sex = Column(Integer)
    remark = Column(String(256))

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://jiayoubao:root1234@172.16.1.13:3306/test_db')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(nick_name='Steven', remark_name='sss', sex=1)
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()