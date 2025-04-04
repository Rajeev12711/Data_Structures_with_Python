digits = [4,3,2,1]
val = ""
num =[]
for i in range(len(digits)):
    val += str(digits[i])
val = int(val)
val = val + 1
val = str(val)
for i in range(len(val)):
    num.append(int(val[i]))
print(num)