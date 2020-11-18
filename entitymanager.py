import random
import sys, os


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

    id_starter = 0

    Suppliers = ["Sakila Films", "Adventure Works", "VilKhaFid", "Northwind"]
    def __init__(self):
        pass
    def generate_customers(self, n):
        customers = []
        Procedurals.id_starter += n 
        ids = list(range(self.id_starter))
        random.shuffle(ids)
        for i in range(n):
            customers.append(Customer(ids[i], self.n[i], self.n[i+1], self.a[i], 0))
        return customers
        
    def generate_movies(self, n):
        movies = []
        self.id_starter += n 
        ids = list(range(self.id_starter))
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
        self.id_starter += n 
        ids = list(range(self.id_starter))
        random.shuffle(ids)
        for i in range(n):
            spices.append(Product(ids[i], self.s[i].split("(")[0].strip(")"), "Latin: " + self.s[i], 
            round(random.uniform(0, random.uniform(100, 500)), 2), 
            self.Suppliers[3], int(random.uniform(100, 500))))
        return spices
        
        #NEED TO GENERATE BIKES. GET COLORS OR COOL WORDS

p = Procedurals()
for s in p.generate_spices(10):
    print(s.__dict__)

        



    

'''

customertest = Customer(1, "a", "b", "c", 0)
setattr(customertest, 'first_name', "e")
#customertest.first_name = "e"
print(customertest.first_name)
print(customertest.__dict__)
'''