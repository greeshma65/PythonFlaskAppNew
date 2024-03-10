# app.py

from flask import Flask 
from urllib.parse import quote 

def create_app():
    app = Flask(__name__)
    x =4
    y =    777

    @app.route('/')
    def home():
        return 'Welcome Guys12345232323!'

    return app

def a():
    print("test..")
    a()
def test():
    p=8

def test():
    q=10

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=80, debug=True)
