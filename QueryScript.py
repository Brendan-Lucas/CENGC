
#from bson import json_util
import json
import uuid
from SMS import send_alert, expiry_alert
import BuildItem
from datetime import date, datetime

runStartup = True;
COSTFILE = 'Costs.json'
CAPACITY = 80000
DATABASEFILE = 'Store.json'
gStorage = {}
gItems = {}

"""QUERY: AddItem"""
def AddItem(name, volume, price, daysToExpiration):
    item = BuildItem.build_item(name, volume, price, daysToExpiration, remainingStorage())
    if not item["errors"]:
        CreateItem(item["name"], item["volume"], item["price_before_tax"], item["price_after_tax"], item["expiry_date"], item["date_added"])
    else:
        print("Add item was not completed")
        for error in item["errors"]:
            print (error)

def CreateItem(name, volume, priceBTX, priceATX, expirationDate, dateAdded):

    generatedID = uuid.uuid4()
    generatedID = generatedID.hex
    dict = dict_maker(name, volume, priceBTX, priceATX, expirationDate, dateAdded, generatedID)
    jsonData = {}
    with open(DATABASEFILE) as jsonFile:
        jsonData = json.load(jsonFile)


    gItems = jsonData["Items"]
    gStorage = jsonData["Storage"]
    if gStorage["Remaining"] >= volume :

        gItems.append(dict)
        gStorage["Remaining"] -= volume

        jsonData = {"Items": gItems, "Storage": gStorage}
        with open(DATABASEFILE, 'w') as jsonFile:
            json.dump(jsonData, jsonFile) #default=json_serial)

        """with open(COSTFILE, 'w') as costJson:

            costData = json.load(costJson)
            if name in costData:
                costData[name]["TotalCost"] += priceATX
                if datetime.date.today() in costData[name]:
                    costData[datetime.date.today()] += priceATX
                else:
                    costData[name][datetime.date.today()] = priceATX
            else:
                costData[name] = {"TotalCost": priceATX, datetime.date.today(): priceATX}

            json.dump(costData, costJson)"""
    else :
        print("ERROR: Item could not be added, Storage Full.")
        send_alert("ERROR: Item could not be added, Storage Full.")


def kill_expired():
    global jsonData
    for item in jsonData:
        if item["ExpirationDate"] < datetime.date.today:
            remove_item(item["Name"])


def dict_maker(name, volume, priceBTX, priceATX, expirationDate, dateAdded, generatedID):
    return {"Name" : name, "volume" : volume, "ExpirationDate" : expirationDate.isoformat(), "PriceBTX" : priceBTX, "PriceATX" : PriceATX, "DateAdded" : dateAdded.isoformat(), "ID" : generatedID}

"""QUERY: Remove Items by name"""
#TODO: make faster with sorting by name and binary search for name then remove
def remove_item(itemValue, spec="Name"):
    #gItems[:] = [item for item in gItems if itemSpecEqual(item, itemValue, spec)]
    global gStorage, gItems

    with open(DATABASEFILE) as jsonFile:
        jsonData = json.load(jsonFile)

    gItems = jsonData["Items"]
    gStorage = jsonData["Storage"]

    newList = []
    for i in range(len(gItems)):
        toAppend = itemSpecEqual(gItems[i], itemValue, spec)
        if toAppend!= None:
            newList.append(toAppend)
    gItems = newList

    jsonData = {"Items": gItems, "Storage": gStorage}
    with open(DATABASEFILE, 'w') as jsonFile:
        json.dump(jsonData, jsonFile)

def itemSpecEqual(item, value, spec):
    global gStorage
    if item[spec] != value:
        return item
    else:
        gStorage["Remaining"] += item["Volume"]


"""QUERY: Items With Name"""
def itemsWithName(name, filepath=DATABASEFILE):
    file = open(filepath, 'r')
    JSON =file.read()
    file.close()
    d=json.loads(JSON)
    for item in d["Items"]:
        if item["Name"] == name:
            print (item)

""""QUERY: All Items"""
def allItems(filepath=DATABASEFILE):
    file = open(filepath, 'r')
    JSON = file.read()
    file.close()
    d = json.loads(JSON)
    for item in d["Items"]:
       print(item)

""" QUERY: Storage Status """
def storageStatus(filepath=DATABASEFILE):
    file = open(filepath, 'r')
    JSON = file.read()
    file.close()
    d = json.loads(JSON)
    capacity =(d["Storage"]["Size"]-d["Storage"]["Remaining"])/d["Storage"]["Size"]
    print ("Container is " + str(int(capacity*100))+ "% full!")


def CostCalculation(name):
    totalcost = 0
    with open(COSTFILE) as costJson:
        costData = json.load(costJson)
    for item in costData:
        totalcost += item["TotalCost"]
    print("Total Cost: " + str(totalcost))


def remainingStorage():
    file = open(DATABASEFILE, 'r')
    JSON = file.read()
    file.close()
    d = json.loads(JSON)
    return d["Storage"]["Remaining"]

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))


if runStartup:
    preVolume = 200
    #populate json file with some Items before we do add anything.
    PriceATX = 23* 1.23
    Starting_List = {"Items":[{"Name": "Apples", "ExpirationDate": "2017-04-14", "PriceBTX": 23, "PriceATX": PriceATX, "DateAdded" : "2017-11-18", "Volume": preVolume, "ID": 123456}], "Storage" : { "Size" : CAPACITY, "Remaining" : CAPACITY - preVolume} }
    print("Starting_List: ", repr(Starting_List))
    print("JSON: ", json.dumps(Starting_List))
    print(Starting_List["Storage"])
    with open(DATABASEFILE, 'w') as  file:
        json.dump(Starting_List, file)

    """with open(COSTFILE, 'w') as file:
        jList = {"Item1" : {"totalCost" : 123, str(datetime.date.today()): 123}}
        json.dump(jList, file)
""""""
jsonData = {}
with open(DATABASEFILE) as jsonFile:
    jsonData = json.load(jsonFile)

gItems = jsonData["Items"]
gStorage = jsonData["Storage"]
"""""
remove_item(123456, "ID")
