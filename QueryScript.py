import json
import uuid
#from SMS import send_alert, expiry_alert
import BuildItem
import datetime

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
            json.dump(jsonData, jsonFile)

        with open(COSTFILE, 'w') as costJson:

            costData = json.load(costJson)
            if name in costData:
                costData[name]["TotalCost"] += priceATX
                if datetime.date.today in costData[name]:
                    costData[datetime.date.today] += priceATX
                else:
                    costData[name][datetime.date.today] = priceATX
            else:
                costData[name] = {"TotalCost": priceATX, datetime.date.today: priceATX}

            json.dump(costData, costJson)
    else :
        print("ERROR: Item could not be added, Storage Full.")
        send_alert("ERROR: Item could not be added, Storage Full.")





def dict_maker(name, volume, priceBTX, priceATX, expirationDate, dateAdded, generatedID):
    return {"Name" : name, "volume" : volume, "ExpirationDate" : expirationDate, "PriceBTX" : priceBTX, "PriceATX" : PriceATX, "DateAdded" : dateAdded, "ID" : generatedID}

"""QUERY: Remove Items by name"""
#TODO: make faster with sorting by name and binary search for name then remove
def remove_item(itemValue, spec="Name"):
    gItems[:] = [item for item in gItems if itemSpecEqual(item, itemValue, spec)]
    jsonData = {"Items": gItems, "Storage": gStorage}
    with open(DATABASEFILE, 'w') as jsonFile:
        json.dump(jsonData, jsonFile)

def itemSpecEqual(item, value, spec):
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
    with open(COSTFILE) as costJson:
        costData = json.load(costJson)
    for item in costData

def remainingStorage():
    file = open(DATABASEFILE, 'r')
    JSON = file.read()
    file.close()
    d = json.loads(JSON)
    return d["Storage"]["Remaining"]

if runStartup:
    preVolume = 200
    #populate json file with some Items before we do add anything.
    PriceATX = 23* 1.23
    Starting_List = {"Items":[{"Name": "Apples", "ExpirationDate": "2017-04-14", "PriceBTX": 23, "PriceATX": PriceATX, "DateAdded" : "2017-11-18", "Volume": preVolume, "ID": 123456}], "Storage" : { "Size" : CAPACITY, "Remaining" : CAPACITY - preVolume} }
    print("Starting_List: ", repr(Starting_List))
    print("JSON: ", json.dumps(Starting_List))

    with open(DATABASEFILE, 'w') as file:
        json.dump(Starting_List, file)

    

jsonData = {}
with open(DATABASEFILE) as jsonFile:
    jsonData = json.load(jsonFile)

gItems = jsonData["Items"]
gStorage = jsonData["Storage"]
AddItem("1", 2, 3, 4)

remove_item(123456, "ID")

