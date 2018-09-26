from flask import Flask
from flask import redirect
from flask import render_template
from flask import url_for
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:buzhidao@localhost/author_book'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALSHEMY_COMMIT_ON_TEARDOWN'] = False
app.config['SQLALSHEMY_ECHO'] = False

app.config['SECRET_KEY'] = 'SDJFLSJD'

# 实例化SQLAlche对象
db = SQLAlchemy(app)

# 定义Author模型类
class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32),unique=True)
    # 在一中，设置虚拟字段，表示一对多关系
    relate = db.relationship('Book',backref='fdjaldjf')

    def __repr__(self):
        return "author:%s" %self.name

# 定义Book模型类
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer,primary_key=True)
    info = db.Column(db.String(32))
    # 在 多中，设置关系字段，设置为外键
    au_id = db.Column(db.Integer,db.ForeignKey('authors.id'))

    def __repr__(self):
        return 'book:%s' %self.info




# web表单验证
class Form(FlaskForm):
    get_auth = StringField(validators=[DataRequired()])
    get_book = StringField(validators=[DataRequired()])
    submit = SubmitField('提交')


# 主业务逻辑
@app.route('/',methods=['GET','POST'])
def index():
    # 实例化表单对象
    form = Form()
    # 查询数据库中的数据
    author,book = None,None
    try:
        author = Author.query.all()
        book = Book.query.all()
    except Exception as e:
        print(e)


    # 获取表单参数
    if form.validate_on_submit():
        inp_auth = form.get_auth.data
        inp_book = form.get_book.data
        #添加数据，是通过对象操作
        au = Author(name = inp_auth)
        bk = Book(info = inp_book)

        try:
            db.session.add_all([au,bk])
            db.session.commit()
        except Exception as e:
            print(e)
            # 异常回滚，事物的原子性
            db.session.rollback()

        # 提交后 刷新 再次查询数据库
        author = Author.query.all()
        book = Book.query.all()

    return render_template('index.html',author= author,book=book,form=form)



# 删除数据
@app.route('/delete_author/<int:author_id>')
def delete_author(author_id):
    # 根据id查询数据库
    auth = Author.query.get(author_id)
    try:
        db.session.delete(auth)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
    return redirect(url_for('index'))




@app.route('/delete_book/<int:book_id>')
def delete_book(book_id):
    # 根据id查询数据库
    book = Book.query.get(book_id)
    # book = Book.query.filter(Book.id==book_id).first()
    # book = Book.query.filter_by(id==book_id).first()
    try:
        db.session.delete(book)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
    return redirect(url_for('index'))


if __name__ == '__main__':
    # 先删除旧表再创建新表
    db.drop_all()
    db.create_all()
    # 生成数据
    au_xi = Author(name='我吃西红柿')
    au_qian = Author(name='萧潜')
    au_san = Author(name='唐家三少')
    bk_xi = Book(info='吞噬星空')
    bk_xi2 = Book(info='寸芒')
    bk_qian = Book(info='飘渺之旅')
    bk_san = Book(info='冰火魔厨')
    # 把数据提交给用户会话
    db.session.add_all([au_xi, au_qian, au_san, bk_xi, bk_xi2, bk_qian, bk_san])
    # 提交会话
    db.session.commit()

    app.run(debug=True)





















