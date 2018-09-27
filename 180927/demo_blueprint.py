from flask import Flask

from temp_detail import blue_detail
from temp_register import api

app = Flask(__name__)
# 3---注册蓝图对象到程序实例上
app.register_blueprint(api)
app.register_blueprint(blue_detail)

@app.route('/')
def index():
    return 'index'

@app.route('/list')
def list():
    return 'list'

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)