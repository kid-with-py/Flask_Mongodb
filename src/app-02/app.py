from flask import Flask, request,json,jsonify
from bson.json_util import dumps
import json
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://admin:IvaMongoAdmin@mongodb:27017/flaskmongo?authSource=admin"
mongo= PyMongo(app)

app = Flask(__name__)

@app.route('/')
def list_id():
    incoming_data = request.json
  #  mongo.db.user_id.insert_one(incoming_data)
    #print(incoming_data, flush=True)
    
    _id = incoming_data["id"]
    users = mongo.db.user_id.find({"id":_id})
    print(users, flush=True)
    reps = dumps(users)
    
    return reps




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8002)    