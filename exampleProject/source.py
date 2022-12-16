import JSONdb

# In this project we are going to simulate a database for a coffee shop.
# The users have what coffee they bought and the price of the coffee
# First we make a connection to our database. We specify the tables we are going to have so that if the database is empty we can populate it with boilerplate code.

JSONdb.ConnectDB(["customers"])

# Now let's imagine that a customer bought a coffee from us. Let's add all the necessary information to the database.
obj = {
    "customerName":"Joshua",
    "coffeeBought":"Late",
    "price": 2,
    "coffeeSpecifications":{
        "milk":1,
        "coffeeBeans":2,
        "earnings":1.2
    }
}
JSONdb.InsertObjectIntoDB(obj,"customers")

# Okay, now we want to see what coffee has Joshua bought

print(JSONdb.GetObjectFromDB("customers","customerName","Joshua")["coffeeBought"])

# Let's imagine that we have made a mistake and that Joshua actually bought a black coffee instead. We can easily modify the database
JSONdb.AlterObjectFromDB("customers","customerName","Joshua","coffeeBought","Black coffee")

# Okay cool. Maybe some time has passed and we want to delete Joshua from our database

JSONdb.DeleteObjectFromDB("customers","customerName","Joshua")


# That's all fine and dandy but what if we want to keep multiple coffee purchases in our customer slot?

# Let's create a dummy Joshua object that has been our customer for a while.
obj = {
    "customerName":"Joshua",
    "coffeesBought":["Late","Black coffee","Espresso"]
}

JSONdb.InsertObjectIntoDB(obj,"customers")

# Now let's get the array of coffees from the database which are connected to our Joshua guy:
arr = JSONdb.GetObjectFromDB("customers","customerName","Joshua")["coffeesBought"]

# Now we add the coffe to the list
arr.append("Red coffee")

# And we alter the object injecting the new array into it. This all can be done in one line of course.
JSONdb.AlterObjectFromDB("customers","customerName","Joshua","coffeesBought",arr)

# Since we have set our customerName to be a unique field if we try to add another Joshua it won't work:
JSONdb.InsertObjectIntoDB(obj,"customers")


# We delete the Joshua object as we don't need it anymore.
JSONdb.DeleteObjectFromDB("customers","customerName","Joshua")
