from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security

app = Flask(__name__)




@app.route('/')
def index():
    return 'Hello'

if __name__ == '__main__':
    app.run(debug=True)