from modules import logger
from modules.settings import settings

import hashlib
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
        return -1

def InsertObjectIntoDB(obj,table):
    # Inserts an object to a database
    try:
        with open(settings["databaseName"]+".json","r") as f:
            db = json.loads(f.read())

    except:
        logger.Log("Could not open database...",3,"fail")
        return -1

    # Check for unique fields

    for uniqueField in settings["uniqueFields"]:
        for i,entry in enumerate(db[table]):
            try:
                if obj[uniqueField] in db[table][i][uniqueField]:
                    logger.Log("Unique constraint failed -> "+uniqueField + " -> "+obj[uniqueField],1,"warning")
                    return -2
                else:
                    continue
            except:
                pass

    for secureField in settings["secureFields"]:
        if secureField in obj.keys():
            obj[secureField] = hashlib.sha256(obj[secureField].encode("utf-8")).hexdigest()


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
        return -1

    try:
        for obj in db[table]:
            if obj[variable] == param:
                return obj
    except:
        logger.Log("Could not loop through the table requested...",3,"fail")
        return -1
    
    return None

def AlterObjectFromDB(table,searchVariable,searchParam,newParam):
    try:
        with open(settings["databaseName"]+".json","r") as f:
            db = json.loads(f.read())

    except:
        logger.Log("Could not open database...",3,"fail")
        return -1

    for i,obj in enumerate(db[table]):
        try:
            if obj[searchVariable] == searchParam:
                db[table][i][searchVariable] = newParam
        except:
            pass
    with open(settings["databaseName"]+".json","w") as f:
        f.write(json.dumps(db,indent=4))

def DeleteObjectFromDB(table,seachVariable,searchParam):
    try:
        with open(settings["databaseName"]+".json","r") as f:
            db = json.loads(f.read())

    except:
        logger.Log("Could not open database...",3,"fail")
        return -1
    
    for i,obj in enumerate(db[table]):
        try:
            if db[table][i][seachVariable] == searchParam:
                del db[table][i]
                logger.Log("Deleted object succesfully",3)
        except:
            pass
    with open(settings["databaseName"]+".json","w") as f:
        f.write(json.dumps(db,indent=4))
        

ConnectDB(["users","cars"])
# ^^ Done once.
InsertObjectIntoDB({"username":"mazdaKing","password":"test"},"users")
#AlterObjectFromDB("users","username","mazdaKing","mazaSwing")
#GetObjectFromDB("users","ID",0)
DeleteObjectFromDB("users","username","kakavac")