import json, re

global entryArray, parrentId

def sortRecursion(id=None):
    global entryArray, parrentId
    sorted=[]
    for element in parrentId[str(id)]:
        sorted.append(entryArray[element])
        if str(entryArray[element]['id']) in parrentId:
            sorted.extend(sortRecursion(entryArray[element]['id']))
    return sorted

def sort_function():
    global entryArray, parrentId
    parrentId={}
    for x, item in enumerate(entryArray):
        if str(item['parent_id']) not in parrentId:
            parrentId[str(item['parent_id'])]=[]
        parrentId[str(item['parent_id'])].append(x)
    return sortRecursion()

def trailing_commas_clean(entryString):
    entryString = re.sub(",[ \t\r\n]+}", "}", entryString)
    entryString = re.sub(",[ \t\r\n]+\]", "]", entryString)

    return entryString

if __name__ == '__main__':
    testString='''[
        {
            "name": "Accessories",
            "id": 1,
            "parent_id": 20,
        },
        {
            "name": "Watches",
            "id": 57,
            "parent_id": 1
        },
        {
            "name": "Belt",
            "id": 58,
            "parent_id": 1
        },
        {
            "name": "Men",
            "id": 20,
            "parent_id": null
        },
        {
            "name": "Dress",
            "id": 51,
            "parent_id": 21,
        },
        {
            "name": "Skirt",
            "id": 67,
            "parent_id": 51
        },
        {
            "name": "Woman",
            "id": 21,
            "parent_id": null
        }
        ]'''
    entryArray=json.loads(trailing_commas_clean(testString))
    print(json.dumps(sort_function(), indent = 4))