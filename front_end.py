from flask import Flask, render_template, request
import entitymanager

app = Flask(__name__)

CS = entitymanager.Commerce_Simulator()
CS.begin_simulation()
db = CS.get_db_handle()

def hello():
    return 'Hello Universe'


@app.route('/Group2')
def dropdown():
    return render_template("test.html")

@app.route('/Sakilla')
def getSakilla():
    cursor = db.sakila.find()
    output = ""
    for i in range(50):
        output += "Film Title: " + cursor[i]["name"] + "<br/>" + "price: $" + str(cursor[i]["price"]) + "<br/>"  + "Description: "  + str(cursor[i]["description"]) + "<br/>" +"<br/>" 
    #print(db.sakila.find({'supplier': 'Sakila Films'}))
    return output

@app.route('/NorthWind')
def getNorthWind():
    cursor = db.northwind.find()
    output = ""
    for i in range(50):
        output += "Spice Name: " + cursor[i]["name"] + "<br/>" + "price: $" + str(cursor[i]["price"]) + "<br/>"  + "Description: "  + str(cursor[i]["description"]) + "<br/>" +"<br/>" 
    #print(db.sakila.find({'supplier': 'Sakila Films'}))
    return output

@app.route('/AdventureWorks')
def getAdventureWorks():
    cursor = db.adventureworks.find()
    output = ""
    for i in range(50):
        output += "Bike Name: " + cursor[i]["name"] + "<br/>" + "price: $" + str(cursor[i]["price"]) + "<br/>"  + "Description: "  + str(cursor[i]["description"]) + "<br/>" +"<br/>" 
    #print(db.sakila.find({'supplier': 'Sakila Films'}))
    return output


@app.route('/Hipster Home Base')
def getHipster():
    cursor = db.vilkhafid.find()
    output = ""
    for i in range(50):
        output += "Type: " + cursor[i]["name"] + "<br/>" + "price: $" + str(cursor[i]["price"]) + "<br/>"  + "Description: "  + str(cursor[i]["description"]) + "<br/>" +"<br/>" 
    #print(db.sakila.find({'supplier': 'Sakila Films'}))
    return output

@app.route('/Customers')
def getCustomers():
    cursor = db.customers.find()
    output = ""
    for i in range(50):
        output += "Name: " + cursor[i]["first_name"] +" " + cursor[i]["last_name"]+ "<br/>" + "Address: " + str(cursor[i]["address"]) +  "<br/>" +"<br/>" 
    #print(db.sakila.find({'supplier': 'Sakila Films'}))
    return output

@app.route('/Products')
def getAll():
    output = getSakilla() + getAdventureWorks() + getNorthWind() + getHipster()
    return output
'''
@app.route('/NorthWind')
@app.route('/AdventureWorks')
@app.route('/HipsterDepot')
'''

app.run(host='localhost', port=5000)
'''
cursor = db.sakila.find()
output = db.sakila.find()[0]["name"]
print(output)
'''

'''
ASK MYERS IF WE NEED SHOPPING CART FLAKSS.
IS THIS ENOUGH?
CAN WE DO THE EXTRA STUFF ON NOSQL?
'''