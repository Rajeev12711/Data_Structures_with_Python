def maxIceCream(costs, coins):
    costs.sort()
    result = 0
    for i in costs:
        if coins >= i:
            coins -= i
            result += 1
        else:
            break
    return result


cost =[1,3,2,4,1]
coin =7

print(maxIceCream(cost,coin))