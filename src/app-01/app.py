from flask import Flask, request,json,jsonify
import json
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://admin:IvaMongoAdmin@mongodb:27017/flaskmongo?authSource=admin"
mongo= PyMongo(app)


@app.route('/')
def add_user():
    print("REQUEST SUCCESS | Add_User")
    incoming_data= request.json
   
    mongo.db.user_id.insert_one(incoming_data)
    print(incoming_data, flush=True)
    return {
        "message": "success"
    }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)    