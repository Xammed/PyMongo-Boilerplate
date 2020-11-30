from flask import Flask, render_template, request, flash
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from flask_table import Table, Col
from pymongo import DESCENDING
import entitymanager

app = Flask(__name__)

CS = entitymanager.Commerce_Simulator()
CS.begin_simulation()
db = CS.get_db_handle()

def hello():
    return 'Hello Universe'


class ItemTable(Table):
    name = Col('Name')
    description = Col('Description')
    price = Col("Price")
    stock = Col("Stock")
    restock_level = Col("Restocking Amount")

class CustomerTable(Table):
    first_name = Col("First Name")
    last_name = Col("First Name")
    address = Col("Address")
    activity = Col("Activity")

@app.route('/Group2')
def dropdown():
    return render_template("test.html")

@app.route('/Sakilla')
def getSakilla():
    cursor = db.sakila.find()
    table = ItemTable(cursor)
    return render_template("param'd.html", param = table)

@app.route('/NorthWind')
def getNorthWind():
    cursor = db.northwind.find()
    table = ItemTable(cursor)
    return render_template("param'd.html", param = table)

@app.route('/AdventureWorks')
def getAdventureWorks():
    cursor = db.adventureworks.find()
    table = ItemTable(cursor)
    return render_template("param'd.html", param = table)


@app.route('/Hipster Home Base')
def getHipster():
    cursor = db.vilkhafid.find()
    table = ItemTable(cursor)
    return render_template("param'd.html", param = table)

@app.route('/Customers')
def getCustomers():
    cursor = db.customers.find().sort("cust_id", DESCENDING)
    table = CustomerTable(cursor)
    return render_template("param'd.html", param = table)

@app.route('/Products')
def getAll():
    s = db.sakila.find()
    n = db.northwind.find()
    a = db.adventureworks.find()
    h = db.vilkhafid.find()
    items = []
    for i in range(50):
        items.append(s[i])
        items.append(n[i])
        items.append(a[i])
        items.append(h[i])
    table = ItemTable(items)
    return render_template("param'd.html", param = table)

@app.route("/Shop")
def shop():
    return render_template("form.html")

@app.route('/Shop', methods=['GET', 'POST'])
def my_form_post():
    name = TextField('Name:', validators=[validators.required()])
    email = TextField('Address:', validators=[validators.required(), validators.Length(min=6, max=35)])
    #text = request.form['text']
    #processed_text = text.upper()
    name=request.form['name']
    address=request.form['address']
    CS.add_Customer(name, address)
    return render_template("test.html")

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