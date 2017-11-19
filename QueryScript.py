import json

runStartup = False;

CAPACITY = 80000
DATABASEFILE = 'Store.json'
gStorage = {}
gItems = {}

"""QUERY: AddItem"""
def AddItem(name, volume, priceBTX, priceATX, expirationDate, dateAdded):

    dict = dict_maker(name, volume, priceBTX, priceATX, expirationDate, dateAdded)
    jsonData = {}
    with open(DATABASEFILE) as jsonFile:
        jsonData = json.load(json.dumps(jsonFile))

    gItems = jsonData["Items"]
    gStorage = jsonData["Storage"]
    gItems.append(dict)
    gStorage["Remaining"] -= volume

    jsonData = {"Items": gItems, "Storage": gStorage}
    with open(DATABASEFILE, 'w') as jsonFile:
        json.dump(jsonData, jsonFile)



def dict_maker(name, volume, priceBTX, priceATX, expirationDate, dateAdded):
    return {"Name" : name, "volume" : volume, "ExpirationDate" : expirationDate, "PriceBTX" : priceBTX, "PriceATX" : PriceATX, "DateAdded" : dateAdded}

"""QUERY: Items With Name"""
def itemsWithName(name, filepath):
    file = open(filepath, 'r')
    JSON =file.read()
    file.close()
    d=json.loads(JSON)
    for item in d["Items"]:
        if item["Name"] == name:
            print (item)

""""QUERY: All Items"""
def allItems(filepath):
    file = open(filepath, 'r')
    JSON = file.read()
    file.close()
    d = json.loads(JSON)
    for item in d["Items"]:
       print(item)

""" QUERY: Storage Status """
def storageStatus(filepath):
    file = open(filepath, 'r')
    JSON = file.read()
    file.close()
    d = json.loads(JSON)
    capacity =(d["Storage"]["Size"]-d["Storage"]["Remaining"])/d["Storage"]["Size"]
    print ("Container is " + str(int(capacity*100))+ "% full!")



if runStartup:
    preVolume = 200
    #populate json file with some Items before we do add anything.
    PriceATX = 23* 1.23
    Starting_List = {"Items":[{"Name" : "Apples", "ExpirationDate" : "2017-04-14", "PriceBTX" : preVolume, "PriceATX" : PriceATX, "DateAdded" : "2017-11-18", "Volume" : "14"}], "Storage" : { "Size" : CAPACITY, "Remaining" : CAPACITY - preVolume} }
    print("Starting_List: ", repr(Starting_List))
    print("JSON: ", json.dumps(Starting_List))

    with open(DATABASEFILE, 'w') as file:
        json.dump(Starting_List, file)

    


