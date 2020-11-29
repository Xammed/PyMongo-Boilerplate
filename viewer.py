import pymongo
import random as random


client = pymongo.MongoClient("mongodb+srv://GradDBTest:test@whatismongo.5azno.mongodb.net/<WhatIsMongo>?retryWrites=true&w=majority")
db=client.WhatIsMongo
db.reviews.insert_one({"cucumber" : "melon",
                "rating" : 10,
                "food" : "salad"})
#Step 2: Create sample data
names = ['Kitchen','Animal','State', 'Tastey', 'Big','City','Fish', 'Pizza','Goat', 'Salty','Sandwich','Lazy', 'Fun']
company_type = ['LLC','Inc','Company','Corporation']
company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian', 'Mexican', 'American', 'Sushi Bar', 'Vegetarian']
for x in range(1, 501):
    business = {
        'name' : names[0] + ' ' + names[0]  + ' ' + company_type[0],
        'rating' : 5,
        'cuisine' : company_cuisine[0] 
    }
    #Step 3: Insert business object directly into MongoDB via isnert_one
    result=db.reviews.insert_one(business)
    #Step 4: Print to the console the ObjectID of the new document
    print('Created {0} of 500 as {1}'.format(x,result.inserted_id))
#Step 5: Tell us that you are done
print('finished creating 500 business reviews')


