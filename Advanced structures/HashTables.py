hashTable = [
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    
]

def hash(key):
    key = int(key)
    hashvalue = key % len(hashTable)
    return hashvalue
    

def add(data):
    location = hash(data)
    print(location)
    hashTable[location] = data


add(9)
print(hashTable)