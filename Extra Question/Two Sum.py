arr =[3,2,4]
result = []
target = 6
for i in range(len(arr)):
    for z in range(i+1, len(arr)):
        if target == (arr[i]+arr[z]):
            result.append(i)
            result.append(z)
print(result)