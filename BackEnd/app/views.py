from app import app

@app.route('/')
@app.route('/index')
def index():
    return "hello world"

@app.route('/register/')
def register():
    pass

@app.route('/logIn/')
def logIn():
    pass

@app.route('/LogOut/')
def LogOut():
    pass
