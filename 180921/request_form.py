from flask import Flask,request,current_app,g,session

app = Flask(__name__)

# post请求的表单参数
@app.route('/index',methods=['GET','POST'])
def index():
    # 使用request对象获取表单参数
    name = request.form.get("name")
    password = request.form.get("password")
    print(name,password)
    return 'login success'

# post请求的文件参数
@app.route('/file',methods=['POST'])
def save_file():
    # 使用request对象获取save_file文件对象
    image = request.files.get('image')
    image.save('./book2s.jpg')
    return 'save image success'

# 其它属性
@app.route("/")
def other_info():
    # 输出请求方法
    print(request.method)
    # 请求的url
    print(request.url)
    print(request.headers)

    return 'hello world'


if __name__ == '__main__':
    # print(app.url_map)
    app.run(debug=True)
