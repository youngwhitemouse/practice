from flask import Blueprint

blue_detail = Blueprint('blue_detail',__name__,url_prefix='/detail')

@blue_detail.route('/detail')
def detail():
    return 'detail'

