# JSONdb

## Project explanation

JSONdb is a project I made to make it easier for myself to use databases. I always hated SQL as it seemed way too complex to use for simpler stuff.

That is when I created "JSONdb". It is a Python3 wrapper around JSON that can be used like a database solution. 

**Check out the example project in this repo so you can understand how to use JSONdb to it's fullest potential.**

## Features

- No external dependencies
- Easy insertion of data
- Easy addition of new variables to the whole database
- Easy search for data
- Easy deletion of data
- Easy unique fields
- Easy logging already imbedded
- Easy to configure settings written in a Python3 dictionary object
- Automatic hashing of fields you choose
- Uses Python syntax instead of SQL
- Foreign keys not needed in 90% of cases
- Automatic ID tracking and implementation
- Automatic ID cleanup
- Use of color for understanding if a function completed it's task successfully

## Setup

Here are the necessary steps you need to take in order to use JSONdb:

- Download this repo ( will be adding code to PyPi soon )
- Extract in your projects directory, remove the example project files and folder
- Set up your settings.py file to your liking
- import JSONdb
- Ready to use

## Usage example

### Creating a database connection
```Python
ConnectDB(["users","cars"])
```
### Inserting an object into the database
```Python
InsertObjectIntoDB({"username":"ylcd","password":"test123"},"users")
```
### Altering an objects variable from the database
```Python
AlterObjectFromDB("users","username","ylcd","yourlocalcodedealer")
```
### Retrieving an object from the database
```Python
GetObjectFromDB("users","ID",1)
```
### Deleting an object from the database
```Python
DeleteObjectFromDB("users","username","yourlocalcodedealer")
```
