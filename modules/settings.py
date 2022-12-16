settings={
    "logLevel":3, # Min log level to log ( 1 is log all, 3 log only the most important stuff)
    "logTime":False, # Should the time and date be logged?
    "logToAFile":False, # Should you save logs to a file?
    "logLocation":"log", # Where to save the log file

    "databaseName":"database", # What is the name you want the database to have and where it should be? No .json at the end please.
    "uniqueFields":["username"], # Define what fields will be unique in the database
    "secureFields":["password"], # Define what fields need to be encrypted
    "cypher":"sha256" # What hash algorithm do you want to use?
}

# Returns:

# -1 = Database file iteration or opening/writing to failed
# -2 = Unique constraint failed