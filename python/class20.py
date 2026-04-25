a = [1,1,1,2,2,2,3,3,3,3,4,4,4,5,5,5,6,6,6,7,7]

d = {}

for i in a: 
    if i in d.keys(): 
        d[i] += 1 # if the key is already in the dictionary, it will increment its value by 1
    else: 
        d[i] = 1 # if the key is not in the dictionary, it will add it to the dictionary with the value 1

print(d.keys())

def newJewelsInStones(jewels: str, stones: str) -> int: 
    d = {}

    for i in stones: 
        if i in d.keys(): 
            d[i] += 1 # if the key is already in the dictionary, it will increment its value by 1
        else: 
            d[i] = 1 # if the key is not in the dictionary, it will add it to the dictionary with the value 1

    count = 0
    for i in d.keys(): 
        if i in jewels: 
            count += d[i] # if the key is in the jewels string, it will add its value to the count
    
    return count # it will return the count of the jewels in the stones string


print(newJewelsInStones("aA", "aAAbbbb")) # it will return 3 because there are 3 jewels in the stones string (2 "a" and 1 "A")

def checkIfPangram(sentence: str) -> bool: 
    d = {}

    for i in sentence: 
        if i in d.keys(): 
            d[i] += 1 # if the key is already in the dictionary, it will increment its value by 1
        else: 
            d[i] = 1 # if the key is not in the dictionary, it will add it to the dictionary with the value 1
        
        

    