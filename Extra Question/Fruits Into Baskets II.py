fruits=[1,3,6]
baskets=[2,5,2]
for z in fruits:
    for y in baskets:
        if z <= y:
            baskets.remove(y)
            break
print(len(baskets))

