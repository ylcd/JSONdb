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
                    db[table] = [{"ID":-1}]
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
        logger.Log("Could not open database...",3,"fail")
    # Add the obj
    prevID=db[table][-1]["ID"]
    obj["ID"] = prevID+1
    db[table].append(obj)
    
    with open(settings["databaseName"]+".json","w") as f:
        f.write(json.dumps(db,indent=4))

def GetObjectFromDB(table,variable,param):
    try:
        with open(settings["databaseName"]+".json","r") as f:
            db = json.loads(f.read())

    except:
        logger.Log("Could not open database...",3,"fail")

    try:
        for obj in db[table]:
            if obj[variable] == param:
                return obj
    except:
        logger.Log("Could not loop through the table requested...",3,"fail")
    
    return None

def AlterObjectFromDB(table,searchVariable,searchParam,newParam):
    pass

ConnectDB(["users","cars"])
InsertObjectIntoDB({"username":"mazdaKing","password":"test"},"users")
print(GetObjectFromDB("users","ID",0))
