import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
db.init_app(app)

# Use the PORT environment variable provided by Heroku
port = int(os.environ.get("PORT", 5000))

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
