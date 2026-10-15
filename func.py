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

def print_kwargs(**kwargs):
    #print(type(kwargs))
    print (kwargs)
print_kwargs(
    a="Hello",
    b="world",
    c="Tomsk"
)

people = {
    "name":"John",
    "age":28,
    "lastname":"Mideator",
    "Job":"Teacher"
}
print (people["name"])

person_data={
    "person": {
        "name": "Ипатий",
        "last_name": "Streich",
        "middle_name": "Азарий",
    },
    "company": {
        "post": "менеджер",
        "company_name": "ОАО ДудинкТрейдРус"
    },
    "address": {
        "street": "Komsomolskiy prospect",
    },
}
print(person_data["person"]["name"])

if "address" in person_data:
    print(person_data["address"])
else:
    print("No address")

print(
    person_data.get("person1111")
)

person_data["education"]={
    "school": "higt",
    "cours": 4,
}

#Получение ключей
print(person_data.keys())
print("a"*10)
#Получение значений
print(person_data.values())
#Замена значения
person_data["person"]["last_name"]="Abdraham"
print(person_data)
print("-"*30)

#Удаление по ключу
del person_data["address"]
print(person_data)

a= 5**2 #Возведение в степень
b= 25**0.5 #Корень от числа
print(b)
print(a)

