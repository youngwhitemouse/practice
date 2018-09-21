from flask import Flask, make_response, request

app = Flask(__name__)

# 设置cookie信息
@app.route('/')
def index():
    # 使用响应对象，来给客户端设置cookie
    response = make_response('set cookies')
    response.set_cookie('itcast','python666',max_age=60)
    return response

# 获取cookie信息
@app.route('/get')
def get_cookie():
    print(request.headers)
    # 从客户端获取的cookie信息
    itcast = request.cookies.get('itcast')
    return itcast



if __name__ == '__main__':
    app.run(debug=True)