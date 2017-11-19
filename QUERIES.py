import json
import datetime
def itemsWithName(name, filepath):
    file = open(filepath, 'r')
    JSON =file.read()
    file.close()
    d=json.loads(JSON)
    for item in d["Items"]:
        if item["Name"] == name:
            print (item)


def allItems(filepath):
    file = open(filepath, 'r')
    JSON = file.read()
    file.close()
    d = json.loads(JSON)
    for item in d["Items"]:
       print(item)

def storageStatus(filepath):
    file = open(filepath, 'r')
    JSON = file.read()
    file.close()
    d = json.loads(JSON)
    capacity =(d["Storage"]["Size"]-d["Storage"]["Remaining"])/d["Storage"]["Size"]
    print ("Container is " + str(int(capacity*100))+ "% full!")


def daysToExpiry(filepath, name):
    file = open(filepath, 'r')
    JSON = file.read()
    file.close()
    d = json.loads(JSON)
    for item in d["Items"]:
        if item["Name"] == name:
            daystillexp=item["ExpirationDate"]
            year = int((item["DateAdded"])[0:4])
            month=int((item["DateAdded"])[5:7])
            day = int((item["DateAdded"])[8:10])
            day+=daystillexp
            if (day>30):
                month += day/31
                day=day%31

                if (month >12):
                    year+=month/13
                    month=month%13
            daysleft =(year-datetime.datetime.now().year)*365 +(month-datetime.datetime.now().month)*12 +(day-datetime.datetime.now().day)

            return daysleft

