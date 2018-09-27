# 蓝图：模块化应用
from flask import Blueprint

# 1---创建蓝图对象
api = Blueprint('api', __name__,url_prefix='/user')

# 把再次拆分出去的文件，导入到创建蓝图对象的下面
from temp_login import login,profile


# 2-----使用蓝图对象，调用route方法
@api.route('/register')
def register():
    return 'register'