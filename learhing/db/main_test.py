from learhing.db.User import User
import db.mysql_api as mysqlApi

class Demo:
    def add(self):
        # 创建session对象:
        session = mysqlApi.getSession()
        # 创建新User对象:
        new_user = User(nick_name='Steven', remark_name='sss', sex=1)
        # 添加到session:
        session.add(new_user)
        # 提交即保存到数据库:
        session.commit()
        # 关闭session:
        session.close()

    def query(self):
        # 创建Session:
        session = mysqlApi.getSession()
        # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
        user = session.query(User).filter(User.id=='8').one()
        user2 = session.query(User).all()
        # 打印类型和对象的name属性:
        print('type:', type(user))
        print('nick_name:', user.nick_name)
        for u in user2:
            print('nick_name:', u.nick_name, 'remark_name:', u.remark_name)
        # 关闭Session:
        session.close()


if __name__ == '__main__':
    demo = Demo()
    demo.query()

