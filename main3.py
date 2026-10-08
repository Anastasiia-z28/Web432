n=0
j=0
while n < 10:
    while j < 10:
        print(n*j, end="\t")
        j+=1
    n+=1
    j=1
    print ("\n")    
    
c1= "hello"
for c in c1:
    print (c)

c1= "ab"
c2= "cd"
for c in c1:
    for s in c2:
        print(f"{c}{s}")

for i in [1,2,3,4]:
    if i==3:
        break
    print(f"Number:{i}")

for i in [1,2,3,4]:
    if i==3:
        continue
    print(f"Number:{i}")