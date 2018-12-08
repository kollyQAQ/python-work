# 导入:
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 't_user'

    # 表的结构:
    id = Column(Integer, primary_key=True, autoincrement=True)
    nick_name = Column(String(64))
    remark_name = Column(String(64))
    sex = Column(Integer)
    role = Column(Integer)