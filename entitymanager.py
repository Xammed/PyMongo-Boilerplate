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

class Product:
    def __init__(self, prod_id, name, description, price, supplier, restock_level):
        self.prod_id = prod_id
        self.name = name
        self.description = description 
        self.price = price
        self.supplier = supplier
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
            self.Suppliers[0], int(random.uniform(100, 500))))
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
            self.Suppliers[3], int(random.uniform(100, 500))))
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
            self.Suppliers[2], 
            int(random.uniform(100, 500))))
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
                self.Suppliers[1],
                int(random.uniform(100, 500))
            ))
        return bikes
        
        #NEED TO GENERATE BIKES. GET COLORS OR COOL WORDS



class MongoManager:
    def __init__(self):
        pass

    p = Procedurals()
    people = p.generate_customers(50)
    movies = p.generate_movies(50)
    spices = p.generate_spices(50)
    hippie = p.generate_hippie_items(50)
    bikes = p.generate_bikes(50)
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
        return 0

class Commerce_Simulator:

    client = pymongo.MongoClient("mongodb+srv://GradDBTest:test@whatismongo.5azno.mongodb.net/<WhatIsMongo>?retryWrites=true&w=majority")
    db=client.WhatIsMongo

    def __init__(self):
        pass

    def begin_simulation(self):
        mm = MongoManager()
        #mm.initialize_mongo(self.db)
        return 0
    def get_db_handle(self):
        return self.db

CS = Commerce_Simulator()
CS.begin_simulation()
    
        




client = pymongo.MongoClient("mongodb+srv://GradDBTest:test@whatismongo.5azno.mongodb.net/<WhatIsMongo>?retryWrites=true&w=majority")
db=client.WhatIsMongo


        



    

'''

customertest = Customer(1, "a", "b", "c", 0)
setattr(customertest, 'first_name', "e")
#customertest.first_name = "e"
print(customertest.first_name)
print(customertest.__dict__)
'''