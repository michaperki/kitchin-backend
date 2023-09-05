import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Use the PORT environment variable provided by Heroku
port = int(os.environ.get("PORT", 5000))

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Define a User model (you may have already done this).
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username already exists in the database.
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return "Username already exists. Please choose another username."
        
        # Create a new user and add it to the database.
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        
        return "Registration successful!"
    
    return render_template('register.html')  # You can create an HTML template for the registration form.


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
