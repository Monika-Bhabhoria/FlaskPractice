from flask import Flask,r

#create flask app

app=Flask(__name__)

# define homepage
@app.route('/')
def home():
    return("Hello there!")

@app.route('/welcome')
def welcome():
    return('Welcome page!!')

@app.route('/index')
def index():
    return('Index page!!')

if __name__=='__main__':
    app.run()