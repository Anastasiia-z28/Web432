def hello(username,age,country = "Россия"):
    print(f"Hello {username}, age: {age}, country: {country}")

hello("John", 21)

hello(username ="Vasya",age=68)

def print_numbers(*numbs):
    for n in numbs:
        print (n)

print_numbers(1,2,3,4,5)        

def print_numbers(*numbs):
    s=0
    for n in numbs:
        s+=n
    return s
    #print (s)

s=print_numbers(1,2,3,4,5)    
print(s)

