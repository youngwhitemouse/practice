from temp_register import api
@api.route('/login')
def login():
    return 'login'

@api.route('/profile')
def profile():
    return 'profile'