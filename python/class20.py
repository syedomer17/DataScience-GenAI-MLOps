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
        
        if len(d.keys()) == 26: # if the length of the keys in the dictionary is 26, it means that all the letters of the alphabet are present in the sentence
            return True # it will return True if all the letters of the alphabet are present in the sentence
        else: 
            return False # it will return False if not all the letters of the alphabet are present in the sentence

print(checkIfPangram("The quick brown fox jumps over the lazy dog")) # it will return True because all the letters of the alphabet are present in the sentence
print(checkIfPangram("Hello World")) # it will return False because not all the letters of the alphabet are present in the sentence

def repeatedCharecter(s: str) -> str: 
    d = {}

    for i in s: 
        if i in d.keys(): 
            return i # if the key is already in the dictionary, it will return the key because it is the first repeated character
        else: 
            d[i] = 1 # if the key is not in the dictionary, it will add it to the dictionary with the value 1

print(repeatedCharecter("abccba")) # it will return "c" because it is the first repeated character

def sumOfUnique(nums) -> int: 
    d = {}

    for i in nums: 
        if i in d.keys(): 
            d[i] += 1 # if the key is already in the dictionary, it will increment its value by 1
        else: 
            d[i] = 1 # if the key is not in the dictionary, it will add it to the dictionary with the value 1

    sum = 0
    for i in d.keys(): 
        if d[i] == 1: # if the value of the key is 1, it means that it is a unique number
            sum += i # it will add the key to the sum
    
    return sum # it will return the sum of the unique numbers in the list

def sortPeople(names, heights):
    d = {}

    for i in range(len(names)): 
        d[heights[i]] = names[i] # it will add the name and height to the dictionary

    sorted_items = sorted(d.items(), key=lambda x: x[0], reverse=True) # it will sort the dictionary by the height in descending order
    
    for i in range(len(sorted_items)):
        names[i] = sorted_items[i][1] # it will update the names list with the sorted names based on the heights

    return names # it will return the sorted names list based on the heights

print(sortPeople(["Mary","John","Emma"], [180,165,170])) # it will return ["Mary","Emma","John"] because Mary is the tallest, followed by Emma and then John



def isAnagram(s1: str, s2: str) :

    if len(s1) == len(s2):
        d = {}
        for i in s1: 
            if i in d.keys(): 
                d[i] += 1 # if the key is already in the dictionary, it will increment its value by 1
            else: 
                d[i] = 1 # if the key is not in the dictionary, it will add it to the dictionary with the value 1
        
        for i in s2: 
            if i in d.keys(): 
                d[i] -= 1 # if the key is already in the dictionary, it will decrement its value by 1
            else: 
                print('An extra character is found in s2') # if the key is not in the dictionary, it means that there is an extra character in s2 that is not in s1
        
        for i in d: 
            if d[i] != 0: # if the value of the key is not 0, it means that there is an extra character in s1 that is not in s2
                print('An extra character is found in s1') # it will print that there is an extra character in s1 that is not in s2
                break
            else:
                print('The two strings are anagrams') # if the value of all the keys is 0, it means that the two strings are anagrams
    else:
        print('The two strings are not anagrams because they have different lengths') # if the lengths of the two strings are different, it means that they cannot be anagrams
    
isAnagram("listen", "silent") # it will print that the two strings are anagrams because they have the same characters with the same frequency
isAnagram("hello", "bello") # it will print that there is an extra character in s1 because "h" is not in s2 and there is an extra character in s2 because "b" is not in s1
isAnagram("abc", "abcd") # it will print that the two strings are not anagrams because they have different lengths

def findDuplicates(nums):
d = {}

    for i in nums: 
        if i in d.keys(): 
            d[i] += 1 # if the key is already in the dictionary, it will increment its value by 1
    else: 
        d[i] = 1 # if the key is not in the dictionary, it will add it to the dictionary with the value 1

for i in d: 
    if d[i] > 1: # if the value of the key is greater than 1, it means that it is a duplicate number
        print(i) # it will print the duplicate numbers in the list

findDuplicates([1,2,3,4,5,6,7,8,9,1,2,3]) # it will print 1, 2 and 3 because they are the duplicate numbers in the list

def mostFrequentEven(nums): 
    d = {}

    for i in nums: 
        if i % 2 == 0: # it will check if the number is even
            if i in d.keys():
                d[i] += 1 # if the key is already in the dictionary, it will increment its value by 1
            else: 
                d[i] = 1 # if the key is not in the dictionary, it will add it to the dictionary with the value 1

        if not d: # if the dictionary is empty, it means that there are no even numbers in the list
            return -1 # it will return -1 if there are no even numbers in the list
        
        max_frequency = max(d.values()) # it will find the maximum frequency of the even numbers in the list

        candidates = [nums for nums, freq in d.items() if freq == max_frequency] # it will find the even numbers with the maximum frequency

        return min(candidates) # it will return the smallest even number with the maximum frequency

print(mostFrequentEven([0,1,2,2,4,4,1])) # it will return 2 because it is the smallest even number with the maximum frequency (2 appears twice and 4 appears twice but 2 is smaller than 4)

def digitCount(num): 
    d = {} 

    for i in num: 
        if i in d.keys(): 
            d[i] += 1 # if the key is already in the dictionary, it will increment its value by 1
        else: 
            d[i] = 1 # if the key is not in the dictionary, it will add it to the dictionary with the value 1
        
        for i in range(len(num)): 
            if d.get(str(i), 0) != int(num[i]): # it will check if the frequency of the digit i is equal to the digit at index i in the num string
                return False # it will return False if the frequency of the digit i is not equal to the digit at index i in the num string
            else: 
                return True # it will return True if the frequency of the digit i is equal to the digit at index i in the num string
print(digitCount("1210")) # it will return True because the frequency of 0 is 1, the frequency of 1 is 2 and the frequency of 2 is 1 which matches the digits at index 0, 1 and 2 in the num string


a = [1,2,2,1]
b = [2,2]

def intersect(a, b):
    d = {}
    j =[] # it will create an empty list to store the common elements between the two lists a and b

    for i in a: 
        if i in d.keys(): 
            d[i] += 1 # if the key is already in the dictionary, it will increment its value by 1
        else: 
            d[i] = 1 # if the key is not in the dictionary, it will add it to the dictionary with the value 1
        
    for i in b: 
        if i in d and d[i] > 0: 
            j.append(i) # if the element in list b is in the dictionary and its frequency is greater than 0, it will add it to the list j
            d[i] -= 1 # it will decrement the frequency of the element in the dictionary by 1

    return j # it will return the list of common elements between the two lists a and b

print(intersect(a, b)) # it will return [2, 2] because 2 is the common element between the two lists a and b and it appears twice in both lists