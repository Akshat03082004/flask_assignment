from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["todo_db"]
collection = db["todo_items"]


@app.route('/')
def home():
    return render_template('todo.html')


@app.route('/submittodoitem', methods=['POST'])
def submit_todo():

    itemName = request.form['itemName']
    itemDescription = request.form['itemDescription']

    data = {
        "itemName": itemName,
        "itemDescription": itemDescription
    }

    collection.insert_one(data)

    return "Todo Item Saved Successfully"


if __name__ == '__main__':
    app.run(debug=True)