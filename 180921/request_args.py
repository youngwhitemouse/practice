from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    # 使用request对象，获取查询字符串的参数
    # http://127.0.0.1:5000/?abc=python13
    # http://127.0.0.1:5000/?abc=python13&name=itcast
    abc = request.args.get("abc")
    name = request.args.get("name")
    print(abc,name)
    return jsonify(abc=abc,name=name)

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
