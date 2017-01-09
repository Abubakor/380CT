
A = []

for x in range(0, 450):
    A.append(randint(0,1000))
    
print ("Brute Force")
print (" ")
print (len(A))
#print (A)

A.sort()
one = 0
two = 0
base = 0
total = 0
half = 0
Partitioned = False
start = time.time()

print (A)

    
    for x in range(0, y):
        base = base + A[x]
    
    two = base
        
    for x in range(y, len(A)):
        one = one + A[x]
        for z in range((x + 1), len(A)):
            
        if one == two:
            Partitioned = false
        two = base


