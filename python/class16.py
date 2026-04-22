a = [10,20,30,40,50]
sum = 0 
for i in a: 
    sum += i
print(f"sum of the list is {sum}")
print(f"average of the list is {sum/len(a)}")

a = [1,45,23,89,45,90,12,36,82]
max = a[0]
index = 0 

for i in range(len(a)):
    if a[i] > max: 
        max = a[i]
        index = i 
print(f"maximum element in the list is {max} and its index is {index}")

a = [1,45,23,89,45,90,12,36,82]
max = a[0]
max2 = a[0]
index = 0
index2 = 0

for i in range(len(a)): 
    if a[i] > max:
        max2 = max 
        max = a[i]
        index2 = index
        index = i
    elif a[i] > max2 and a[i] != max:
        max2 = a[i]
        index2 = i
print(f"maximum element in the list is {max} and its index is {index}")
print(f"second maximum element in the list is {max2} and its index is {index2}")

a = [12,13,14,15,16,17,11,23,24,25,36,78,90]
for i in range(len(a) - 1): 
    if a[i] < a[i + 1]: 
        continue
    else: 
        print("list is not in ascending order")
        break
else:
    print("list is in ascending order")

a = [10,20,30,40,50]

for i in range(len(a) - 1): 
    a[i], a[i + 1] = a[i + 1],a[i] # we are swapping the elements of the list
print(a) # [50, 40, 30, 20, 10]

for i in range(len(a) -1, 0, -1): 
    a[i], a[i - 1] = a[i - 1], a[i] # we are swapping the elements of the list
print(a) # [50, 20, 30, 40, 10]

k = int(input("Enter the number to do rotate:"))

for i in range(k): 
    for i in range(len(a) - 1): 
        a[i], a[i + 1] = a[i + 1], a[i] # we are swapping the elements of the list
print(a) 

a  =  [10,20,30,40,50]
b = len(a) - 1
for i in range(len(a) // 2): 
    a[i], a[b] = a[b], a[i] # we are swapping the elements of the list
    b -= 1
print(a) # [50, 40, 30, 20, 10]

a = [12,13,14,15,16,17,23,24,25,36,78,90]

search = int(input("Enter the number to search:"))

start = 0
last = len(a) - 1
mid = (start + last) // 2 

while start <= last: 
    if a[mid] == search: 
        print(f"element found at index {mid + 1}")
        break
    elif a[mid] < search: 
        start = mid + 1
        mid = (start + last) // 2
    else: 
        last = mid - 1 
        mid = (start + last) // 2
else: 
    print("element not found in the list")

a = [12,13,14,15,16,17,23,24,25,36,78,90]

for i in range(len(a) - 1):
    for j in range(len(a) - 1 - i): 
        if a[j] > a[j + 1]: 
            a[j], a[j + 1] = a[j + 1], a[j] # we are swapping the elements of the list
print(a) # [12, 13, 14, 15, 16, 17, 23, 24, 25, 36, 78, 90]

a = [12,13,14,15,16,17,23,24,25,36,78,90]

for i in range(len(a) - 1): 
    j = i + 1
    min = i 
    for k in range(j, len(a)): 
        if a[k] < a[min]:
            min = k
        a[i], a[min] = a[min], a[i] # we are swapping the elements of the list
print(a) # [12, 13, 14, 15, 16, 17, 23, 24, 25, 36, 78, 90]