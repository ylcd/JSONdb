from modules.settings import settings
from datetime import datetime

def Log(toLog,logLevel,status="ok"):
    """
    Write a log to a log file of your choice.
    """
    OKCYAN = '\033[96m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    if settings["logLevel"]>=logLevel:
        if status == "ok":
            print(OKCYAN + toLog + ENDC)
        if status == "warning":
            print(WARNING + toLog + ENDC)
        if status == "fail":
            print(FAIL + toLog + ENDC)

        if settings["logToAFile"]:
            with open(settings["logLocation"]+".log","a+") as f:
                if settings["logTime"]:
                    toLog +=" @ "+ str(datetime.today())
                f.write(f"[{status.upper()}] "+toLog+"\n") # + log time if time needs to be logged
