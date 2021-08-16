import json, re

def sort_function(entryArray, id=None):
    sorted=[]
    for item in entryArray:
        if item['parent_id']==id:
            sorted.append(item)
            sorted.extend(sort_function(entryArray,item['id']))
    return sorted

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

    print(json.dumps(sort_function(json.loads(trailing_commas_clean(testString))), indent = 4))