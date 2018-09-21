from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    print("index run ")
    return 'index run'

# 请求钩子：在请求前执行和请求后执行
# 在第一次请求前执行before_first_request,只执行一次
@app.before_first_request
def before_first_request():
    print('before first request run------')

# 在每次请求前执行，before_request，执行多次
@app.before_request
def before_request():
    print("before request run----")

# 在请求后执行，after_request
# 必须接受响应作为参数，并且必须返回响应，在发生异常的情况下，不会执行
@app.after_request
def after_request(response):
    print('after request run----')
    return response

# 在请求后执行，
# 接受的参数为异常信息，即使有异常，也会执行
@app.teardown_request
def teardown_request(e):
    print('teardown request run----')


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
