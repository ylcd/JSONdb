settings={
    "logLevel":3, # Min log level to log ( 1 is log all, 3 log only the most important stuff)
    "logTime":False, # Should the time and date be logged?
    "logToAFile":False, # Should you save logs to a file?
    "logLocation":"log", # Where to save the log file

    "databaseName":"database/coffeShop", # What is the name you want the database to have and where it should be? No .json at the end please.
    "uniqueFields":["customerName"], # Define what fields will be unique in the database
    "secureFields":[""], # Define what fields need to be encrypted
    "cypher":"sha256" # What hash algorithm do you want to use? Currently only sha256 has been programmed in. Feel free to add your own in JSONdb.py
}

# Returns:

# -1 = Database file iteration or opening/writing to failed
# -2 = Unique constraint failed