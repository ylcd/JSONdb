from modules import logger
from modules.settings import settings

import json

def ConnectDB(tables=[]):
    # Creates a database
    try:
        with open(settings["databaseName"]+".json","r+") as f:
            # Make sure to create tables that the user selected
            if len(f.read()) == 0: # If the database requires first time setup
                if len(tables) == 0:
                    return logger.Log("Could not create database, no tables specified...",3,"fail")
                # If there are tables specified:
                db = {}
                for table in tables:
                    db[table] = [{"ID":0}]
                f.write(json.dumps(db,indent=4))
                logger.Log("Database created",3)
    except:
        return "fail"

def InsertObjectIntoDB(obj,table):
    # Inserts an object to a database
    # Add an option for unique field check
    try:
        with open(settings["databaseName"]+".json","r") as f:
            db = json.loads(f.read())

    except:
        return "fail"
    # Add the obj
    prevID=db[table][-1]["ID"]
    #obj["ID"] = prevID + 1
    obj["ID"] = prevID+1
    db[table].append(obj)
    
    print(db)
    with open(settings["databaseName"]+".json","w") as f:
        f.write(json.dumps(db,indent=4))

ConnectDB(["users","cars"])
InsertObjectIntoDB({"make":"mazda","year":1992},"cars")
#logger.Log("Inserting into db",1,InsertObjectIntoDB({"kaka":"paka"}))