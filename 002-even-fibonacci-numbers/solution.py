f1 = 1
f2 = 2
evens = []

while(f1 < 4000000):
    if(f1 % 2 == 0):
        evens.append(f1)
    
    f3 = f1 + f2
    f1 = f2
    f2 = f3

print(sum(evens))