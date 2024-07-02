from flask import Flask, request
import json

#GlobalVariables 
items = []
#
app = Flask(__name__)

@app.get("/")
def home():
    return "Hello from Flask"

@app.get("/test")
def test():
    return "Hello from test page"

@app.get("/api/about")
def about():
    me = {"name" : "Adrian RA"}
    return json.dumps(me)

@app.post("/api/products")
def saveProducts(): 
    product = request.get_json()
    print (product)
    #mock the save 
    items.append(product)
    return json.dumps(product)

@app.get("/api/products")
def getProduct():
    return json.dumps(items)

app.run(debug = True)



