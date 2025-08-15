print("Iteration")

arr=[5,33,60,10,200,200,33]
for i in arr:
    print(i)

for i in range(len(arr)):
    print("----",arr[i]+10)

for index,val in enumerate(arr):
    print(index,"--->",val)

print("reversed")

for i in range(len(arr)-1,-1,-1):
    print(arr[i])

for i in reversed(arr):
    print(i,"##")

for i in arr[::-1]:
    print(i)

for index,val in enumerate(reversed(arr)):
    print(index,"--",val)


print("Min/Max")

min_val= max_val = arr[0]
for i in arr[1:]:
    if i < min_val:
        min_val = i
    if i> max_val:
        max_val=i
print(min_val,max_val)

print("remove duplicates")
seen = set()
result = []
for i in arr:
    if i not in seen:
        seen.add(i)
        result.append(i)
print(result)

print("remove duplicates form sorted array")
nums = [1,2,3,4,7,7,5,5]
i = 0
while i < len(nums)-1:
    if nums[i] == nums[i+1]:
        nums.pop(i+1)
    else:
        i+=1
print(nums,"duplicates")


print("sorted array")
arr1=[1,2,50,50,22,46,46]

i = 0 
for j in range(1,len(arr1)):
    if arr1[i] != arr1[j]:
        arr1[i+1] = arr1[j]
        i+=1
print(arr1)

print("array is sorted")
for i in range(len(arr)-1):
    if arr[i] == arr[i+1]:
        print("false")
    if arr[i] >arr[i+1]:
        print("not sorted")

print("move zeros to end")
data = [0,2,3,4]
i = 0
for j in range(len(data)):
    if data[j] != 0:
        data[i] = data[j]
        i+=1
    
while i < len(data):
    data[i] = 0
    i+=1

print(data)
