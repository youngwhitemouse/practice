from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 配置数据库的连接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:buzhidao@localhost/role_user'
# 动态追踪修改，可以不配，只会有警告信息，设置为True或False都可以关闭警告信息
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 在请求过程中自动提交数据，省掉手动commit操作
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False
# 显示具体的sql语句
app.config['SQLALCHEMY_ECHO'] = False

# # 设置用于csrf的秘钥
# app.config['SECRET_KEY'] = 'DJFLFJL'


# 实例化SQLAlchemy对象
# orm对象关系映射，模型类只能映射数据库中的表，不能映射数据库
db = SQLAlchemy(app)

# 定义模型类

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key=True)
    info = db.Column(db.String(32),unique=True)

    user = db.relationship('User',backref='role')

    def __repr__(self):
        return 'info:%s' %self.info

class User(db.Model):
    __table__name = 'users'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32))
    email = db.Column(db.String(32),unique=True)
    pswd = db.Column(db.String(32))

    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __repr__(self):
        return 'name:%s' %self.name









@app.route('/')
def xxx():

    return xxx


if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    ro1 = Role(info='admin')
    ro2 = Role(info='user')

    db.session.add_all([ro1,ro2])
    db.session.commit()

    us1 = User(name='wang', email='wang@163.com', pswd='123456', role_id=ro1.id)
    us2 = User(name='zhang', email='zhang@189.com', pswd='201512', role_id=ro2.id)
    us3 = User(name='chen', email='chen@126.com', pswd='987654', role_id=ro2.id)
    us4 = User(name='zhou', email='zhou@163.com', pswd='456789', role_id=ro1.id)
    db.session.add_all([us1, us2, us3, us4])
    db.session.commit()




    app.run(debug=True)























