# JSONdb

## Project explanation

JSONdb is a project I made to make it easier for myself to use databases. I always hated SQL as it seemed way too complex to use for simpler stuff.

That is when I created "JSONdb". It is a Python3 wrapper around JSON that can be used like a database solution. It even has automatic encryption for chosen fields. You can of course choose which encryption algorithms you would like or implement your own easily.

## Features

- Easy insertion of data
- Easy deletion of data
- Easy search for data
- Easy foreign key implementation
- Easy addition of new variables to the whole database
- Easy auto back-up feature
- Automatic protection procedures like password encryption
- Uses Python syntax instead of SQL
- Foreign keys not even needed in most cases
- Easy logging already imbedded
- Easy to configure settings written in a hashmap
- Automatic ID tracking and implementation
- Use of color for understanding if a function completed it's task successfully
- Easy unique fields
- Built in date expiry check

## Setup

Here are the necessary steps you need to take in order to use JSONdb:

- Download this repo ( will be adding code to PyPi soon )
- Extract in your projects directory ( with folders intact )
- import the modules and it's ready for use.

## Usage example

```Python
# First we need to create a database connection:

ConnectDB(["users","cars"])
# We specify the tables we will have in our database.
# If the database file exists and is not empty we just create a connection.
# If the database does not exists or is empty we populate it with tables and start IDs



```