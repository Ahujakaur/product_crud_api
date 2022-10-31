from flask import Flask, request, jsonify
import pymongo


from bson import json_util

app=Flask(__name__)
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#mydb=MongoConnect()
mydb = myclient["mydata"]

#route for post user
@app.route('/pro',methods=['POST'])
def pro():
    mycol=mydb["user"]
    t=request.json["Title"]
    d=request.json["Description"]
    p=request.json["price"]
    pro={
        "Title":" Title",
        "Description":"Description",
        "price":"price"
    }
    x=mycol.insert_one(pro)
    print(x)
    response={
        #"id":str(x.inserted_id),
        "Title":t,
        'Description': d,
        'price': p
    }
    return response
#route for get user's database
@app.route('/prov',methods=['GET'])
def prov():
    mycol=mydb["user"]
    users=mycol.find()
    response=json_util.dumps(users)
    return response

#route for find any specific data
@app.route('/user/<name>',methods=['GET'])
def single_user(name):
    mycol=mydb["user"]
    users=mycol.find_one({
        "username": name
    })
    response=json_util.dumps(users)
    return response
#route for delete any data
@app.route('/pro/<name>',methods=['DELETE'])
def delete_user(name):
    mycol=mydb["pro"]
    users=mycol.delete_one({
        "username": name
    })
    return jsonify({"Message" :name+" is Deleted"})
#route for change in database
@app.route('/pro/<name>',methods=['PUT'])
def update_user(name):
    mycol=mydb["user"]
    username=request.json['username']
    age=request.json['age']
    q=request.json['qualificarion']

    data={
        "username":username,
        'age':age,
        'qualification':q
    }
    mycol.update_one({"username":name},{"$set":data})
    return jsonify({"Message" :name+" is Updated"})


if __name__=='__main__':
    app.run(debug=True)
