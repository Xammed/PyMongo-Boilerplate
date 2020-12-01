import random
import sys, os
import pymongo


class Customer:
    def __init__(self, cust_id, first_name, last_name, address, activity):
        self.cust_id = cust_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.activity = activity
        self.wishlist = []

class Purchase:
    def __init__(self, first_name, last_name, product_name, cust_id, prod_id, amount, date):
        import datetime
        self.first_name = first_name
        self.last_name = last_name
        self.product_name = product_name
        self.cust_id = cust_id
        self.prod_id = prod_id
        self.amount = amount
        self.date = date
        self.shipping_date = self.date + datetime.timedelta(days=4)


class Product:
    def __init__(self, prod_id, name, description, price, supplier, stock, restock_level):
        self.prod_id = prod_id
        self.name = name
        self.description = description 
        self.price = price
        self.supplier = supplier
        self.stock = stock
        self.restock_level = restock_level
        
class Address:
    def __init__(self, add_id, line_1, line_2, city, state, zip):
        self.add_id = add_id 
        self.line_1 = line_1
        self.line_2 = line_2
        self.city = city
        self.state = state
        self.zip = zip

class Supplier:
    def __init__(self, supp_id, supp_name, contact_name, contact_number, contact_email):
        self.supp_id = supp_id
        self.supp_name = supp_name
        self.contact_name = contact_name
        self.contact_number = contact_number
        self.contact_email = contact_email

class Restocking:
    def __init__(self, order_id, product_key, amount, date):
        self.order_id = order_id
        self.product_key = product_key
        self.amount = amount
        self.date = date

class Procedurals:

    addresses = open("addresses.txt", "r")
    a = addresses.read().splitlines()
    random.shuffle(a)
    names = open("names.txt", "r")
    n = names.read().splitlines()
    random.shuffle(n)
    words = open("words.txt", "r")
    w = words.read().splitlines()
    random.shuffle(w)
    spices = open("spices.txt", "r")
    s = spices.read().splitlines()
    random.shuffle(s)
    countries = open("countries.txt", "r")
    c = countries.read().splitlines()
    random.shuffle(c)
    latin = open("latin.txt", "r")
    l = [x.split(" : ", 1)[0] for x in latin.read().splitlines()]
    random.shuffle(l)
    id_starter = 0

    Suppliers = ["Sakila Films", "Adventure Works", "VilKhaFid", "Northwind"]
    def __init__(self):
        pass
    def generate_customers(self, n):
        customers = []
        ids = list(range(self.id_starter, self.id_starter+n))
        self.id_starter += n 
        random.shuffle(ids)
        for i in range(n):
            customers.append(Customer(ids[i], self.n[i], self.n[i+1], self.a[i], 0))
        return customers
        
    def generate_movies(self, n):
        movies = []
        ids = list(range(self.id_starter, self.id_starter+n))
        self.id_starter += n 
        random.shuffle(ids)
        for i in range(n):
            movies.append(Product(ids[i], self.w[i], "movie about " + self.w[i], 
            round(random.uniform(0, random.uniform(100, 500)), 2), 
            self.Suppliers[0], int(random.uniform(500, 600)), int(random.uniform(100, 500))))
        return movies 
    
    def generate_spices(self, n):
        if (n > len(self.s)):
            n = len(self.s)
        spices = []
        ids = list(range(self.id_starter, self.id_starter+n))
        self.id_starter += n 
        random.shuffle(ids)
        for i in range(n):
            spices.append(Product(ids[i], self.s[i].split("(")[0].strip(")"), "Latin: " + self.s[i], 
            round(random.uniform(0, random.uniform(100, 500)), 2), 
            self.Suppliers[3], int(random.uniform(500, 600)), int(random.uniform(100, 500))))
        return spices

    def generate_hippie_items(self, n):
        roast_level = ["Dark", "Medium", "Light"]
        hippies = []
        ids = list(range(self.id_starter, self.id_starter+n))
        self.id_starter += n 
        random.shuffle(ids)
        for i in range(n):
            hippies.append(Product(ids[i], 
            self.c[i] + " " + str(roast_level[i%3]) + " " + "Coffee", 
            str(roast_level[i%3]) + " coffee imported from " + self.c[i], 
            round(random.uniform(5, 21), 2), 
            self.Suppliers[2], int(random.uniform(500, 600)), int(random.uniform(100, 500))))
        return hippies 

    def generate_bikes(self, n):
        bikes = []
        ids = list(range(self.id_starter, self.id_starter+n))
        self.id_starter += n 
        random.shuffle(ids)
        for i in range(n):
            bikes.append(Product (ids[i],
                "The " + self.l[i], 
                "", 
                round(random.uniform(100, 964.3),2),
                self.Suppliers[1],int(random.uniform(500, 600)), int(random.uniform(100, 500))
            ))
        return bikes

    def generate_Suppliers(self):
        suppliers = []
        self.id_starter+=1
        suppliers.append(Supplier(self.id_starter, "Sakilla Films", "Sack Man", "123-432-9867", "sakila@gmail.com"))
        self.id_starter+=1
        suppliers.append(Supplier(self.id_starter, "North Wind Traders", "Rob Stark, King of the North", "323-422-5807", "fknightwalkers@gmail.com"))
        self.id_starter+=1
        suppliers.append(Supplier(self.id_starter, "Adventure Works", "Stanley Boehm", "854-299-6534", "fknightwalkers@gmail.com"))
        self.id_starter+=1
        suppliers.append(Supplier(self.id_starter, "Hipster Depot", "Mathew JAMES Fiduk", "145-981-0769", "mark@gmail.com"))
        self.id_starter+=1
        return suppliers




    def generate_key(self):
        self.id_starter += 10
        return self.id_starter
    
        


class MongoManager:

    p = Procedurals()
    people = p.generate_customers(50)
    movies = p.generate_movies(50)
    spices = p.generate_spices(50)
    hippie = p.generate_hippie_items(50)
    bikes = p.generate_bikes(50)
    suppliers = p.generate_Suppliers()
    dbHandle = 0

    def __init__(self, db):
        self.dbHandle = db
    
    def initialize_mongo(self, db):
        for person in self.people:
            db.customers.insert_one(person.__dict__)
        for movie in self.movies:
            db.sakila.insert_one(movie.__dict__)
        for spice in self.spices:
            db.northwind.insert_one(spice.__dict__)
        for hip in self.hippie:
            db.vilkhafid.insert_one(hip.__dict__)
        for bike in self.bikes:
            db.adventureworks.insert_one(bike.__dict__)
        for supplier in self.suppliers:
            db.suppliers.insert_one(supplier.__dict__)
        return 0
    
    def initialize_Purchases(self, purchases):
        for purchase in purchases:
            self.dbHandle.purchases.insert_one(purchase.__dict__)
        return 0

    def add_Customer(self, name, address):
        nameA = name.split(" ")
        fname = ""
        lname = ""
        id = self.p.generate_key()
        if len(nameA)<2:
            lname = ""
            fname = nameA[0]
        else:
            fname = nameA[0]
            lname = nameA[len(nameA)-1]
        print(fname, lname)
        customer = Customer(id, fname, lname, address, 0)
        self.dbHandle.customers.insert(customer.__dict__)


class Commerce_Simulator:

    client = pymongo.MongoClient("mongodb+srv://GradDBTest:test@whatismongo.5azno.mongodb.net/<WhatIsMongo>?retryWrites=true&w=majority")
    db=client.WhatIsMongo
    mm = MongoManager(db)
    def __init__(self):
        pass

    def begin_simulation(self):
        #self.mm.initialize_mongo(self.db)
        #purchases = self.generate_Purchases()
        #self.mm.initialize_Purchases(purchases)
        return 0
    def get_db_handle(self):
        return self.db

    def add_Customer(self, name, address):
        self.mm.add_Customer(name, address)

    def generate_Purchases(self):
        import datetime
        purchases = []
        s = self.db.sakila.find()
        n = self.db.northwind.find()
        a = self.db.adventureworks.find()
        h = self.db.vilkhafid.find()
        c = self.db.customers.find()
        products = [s,n,a,h]
        prod_hash = {s:"sakila", n:"northwind", a:"adventureworks", h:"vilkhafid"}
        for product in products:
            for i in range(50):
                pid = product[i]["prod_id"]
                pname = product[i]["name"]
                old_stock = product[i]["stock"]
                highest_amt = int(product[i]["stock"])
                numpurchases = 0
                if highest_amt > 0:
                    numpurchases = random.randint(0, highest_amt)
                new_stock = int(old_stock) - numpurchases
                query = {"prod_id":pid}
                self.db[prod_hash[product]].update_one(query, {"$set":{"stock":new_stock}})
                count = 0
                index = 0
                customers = list(range(50))
                random.shuffle(customers)
                while count<numpurchases:
                    customer = customers[index]
                    quantity = random.randint(10, 20)
                    cid = c[customer]["cust_id"]
                    cfname = c[customer]["first_name"]
                    clname = c[customer]["last_name"]
                    old_activity = c[customer]["activity"]
                    new_activity = old_activity + quantity
                    query = {"cust_id":cid}
                    self.db["customers"].update_one(query, {"$set":{"activity":new_activity}})
                    date = datetime.datetime.today() - datetime.timedelta(days=random.randint(5, 60))
                    purchases.append(Purchase(cfname, clname, pname, cid, pid, quantity, date))
                    index += 1
                    count += quantity
                    print(prod_hash[product], count)
        return purchases




#CS = Commerce_Simulator()
#CS.begin_simulation()
    
        




client = pymongo.MongoClient("mongodb+srv://GradDBTest:test@whatismongo.5azno.mongodb.net/<WhatIsMongo>?retryWrites=true&w=majority")
db=client.WhatIsMongo


        



    

'''

customertest = Customer(1, "a", "b", "c", 0)
setattr(customertest, 'first_name', "e")
#customertest.first_name = "e"
print(customertest.first_name)
print(customertest.__dict__)
'''