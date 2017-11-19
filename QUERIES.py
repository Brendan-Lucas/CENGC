import json

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


