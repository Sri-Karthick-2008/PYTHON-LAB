from itertools import combinations
a=[1,-2,4,-5,6,7,-8]
print("Positive combinations")
for r in range(1,len(a)+1):
    for combo in combinations(a,r):
        if all(num>0 for num in combo):
            print(combo)
