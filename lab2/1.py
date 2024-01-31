#Bool
print(10>9)
#True
print(10 == 9)
#False
print(10 < 9)
#False
print(bool("abc"))
#True


#Operators
print(10 * 5)
print(10 / 2)
fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Yes, apple is a fruit!")

if 5 != 10:
    print("5 and 10 is not equal")
if 5 == 10 or 4 == 4:
    print("At least one of the statements is true")

#list
fruits = ["apple", 'banana', 'cherry']
print(fruits[1])
fruits[0] = "kiwi"
fruits.append("orange")
fruits.insert(1, "lemon")
fruits.remove("banana")
print(fruits[-1])
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
print(len(fruits))


#tuple
fruits = ("apple", "banana", "cherry")
print(fruits[0])
print(len(fruits))
print(fruits[-1])
print(fruits[2:5])


#sets
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print('Yes, apple is a fruit')
fruits.add("orange")
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
fruits.remove("banana")
fruits.discard("banana")


#dictionaries
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get('model'))
car["year"] = 2020
car['color'] = 'red'
car.pop("model")
car.clear()


#If_else
a = 50
b = 10
if a > b:
    print("hello world")
if a != b:
    print('hello world')
if a == b:
    print("Yes")
else:
    print("No")
if a == b:
    print("1")
elif a > b:
    print("2")
else:
    print("3")
if a == b and c == d:
    print("hello")
if a == b or c == d:
    pring("hello")
if 5 > 2:
    print("YES")
a = 2
b = 5
print("YES") if a == b else print("NO")
if a == c or b == c:
    print("YES")



#while
i = 1
while i < 6:
    print(i)
    i += 1
while i < 6:
    if i == 3:
        break
    i += 1
while i < 6:
    if i == 3:
        continue
    i += 1
else:
    print("i is no longer less than 6")


#for
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
for x in fruits:
    if x == "banana":
        continue
    print(x)
for x in range(6):
    print(x)
for x in fruits:
    if x == "banana":
        break
    print(x)