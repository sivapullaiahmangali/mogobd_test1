from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
# Connect to your MongoDB Cloud database
client = MongoClient('mongodb+srv://mangalisivapullaiah:9391993975@cluster0.tmdwkd0.mongodb.net/?retryWrites=true&w=majority&collection=users')
# mongodb+srv://<username>:<password>@cluster0.tmdwkd0.mongodb.net/?retryWrites=true&w=majority

# Define the collection
db = client['your_database_name']
collection = db['signup_details']

@app.route('/')
def signup():
    return render_template('signup.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    
    # Insert the signup details into the collection
    collection.insert_one({'name': name, 'email': email, 'password': password})
    
    return 'Signup successful!'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
