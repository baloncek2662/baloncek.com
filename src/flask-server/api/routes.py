from api import app

from models import User


@app.route('/')
@app.route('/index')
def index():
    return "Hello,aaaa World!"