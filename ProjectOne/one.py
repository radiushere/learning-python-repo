#Importing Libraries
import sys
import random
import moduletest
import datetime
import math
import json
import re #RegEX Library



#Variables etc
dic = {"name" : "aqib", "age" : 17} #This is a Dictionary

newlist = [x for x in range(10) if x%2] #This is a List, this list finds prime numbers within 1 to 10

atuple = ("what", "why", "when") #This is a Tuple
anothertuple = ("woah",) #for a single entry tuple, add a comma (,) at the end 
boom = list(anothertuple) #Converts the tuple (anothertuple) into a list and stores it into boom

storestime = datetime.datetime.now() #Stores current time data

matrix1 = [1, 2, 3]
matrix2 = [4, 5, 6]

u = int(2222)
y = str("po")
x = 8.8

i = 0

combinedtext = f"He is legal, his age is {20 * 2}" #Used to join a number and a string in the same sentence 

abc = "bad"

shusui = ["hyorinmaru", "sakanade", "zabimaru"] #This is a List
ice, flip, snake = shusui #This is called "Unpacking"
green, *red = shusui #Unpacks the remaining entries after "green's" associated entry into "red"

randomnumber = random.randrange(1, 10)


#A Nested Dictionary
nestdec = {
    "Student 1" : {
        "Name" : "Denji",
        "Age" : 19,
        "Gender" : "M",
        "Class" : 2
    },
    "Student 2" : {
        "Name" : "Yoshida",
        "Age" : 19,
        "Gender" : "M",
        "Class" : 2
    },
    "Student 3" : {
        "Name" : "Asa Mitaka",
        "Age" : 19,
        "Gender" : "F",
        "Class" : 2
    }
}


#For multiple lined string use 3 single or double qoute
stringtest = """The Undying Queen,
With Her Majestic Demeanor, 
Squealing Maids, 
Fainting Knights, 
She Rides Her Horse, Drifts She Away"""



#Functions etc
print(sys.version)

print("Hello World double qoute") 
print('Hello World single qoute') #no difference

print(f"This technique allows me to write an integer with a string together: {8}, as you just saw") #Writing int and string (str) together

print(datetime.datetime.now()) #Prints current time
print(datetime.datetime(2020, 9, 21)) #Prints a custom year-month-date
print(storestime.year)
print("Current Weekday:", storestime.strftime("%A")) #This function prints a string version of a datetime value, the key code written inside the double qoute is representing some sort of value (differs for every value)

print(shusui)
print(ice, flip, snake)

print(nestdec)

if 8 > 7:
    print("nuhuh")
elif 8 < 0:
    print("never")
else:
    print("shee")

"""
A comment string
"""

print(u, "ABRACADABRA")
print(y, x)
print(type(x))

print(dic) #Prints the dictionary as is
print(dic["name"], dic["age"]) #Prints the info of the keyword mentioned

print("Here is a random number (1-10):", randomnumber)

if randomnumber > 5:
    print("You Lose")

else:
    print("You win")

print(stringtest)
print(stringtest[0])

for p in y: #For Loop, here p is an empty variable being used to write the list(y) in a column form
    print(p)

print(y.upper()) #for uppercase 
print(y.replace("o", "ee")) #replacing "o" with "ee" in the string y
print(abc.split("a")) #the string(abc) will be splitted in two using "a" as the centre excluded point

print(combinedtext)

if "x" not in y:
    print("No, there is no x in po")

while i<len(shusui): #While Loop
    print(shusui[i])
    i+=1

print(newlist)

print(type(atuple))
atuple += anothertuple #Conjoins the first tuple (atuple) with the second tuple (anothertuple)
print(atuple) #Prints the conjoined tuple

boom.remove("woah")
print(boom) #It will be empty

print(green, red)

for x in atuple: #Prints the tuple as a list
    print(x)

for x in range(2): #Prints Damn 2 times in column format, works like for loop of C++ (increment by 1 case)
    print("Damn")

i = 0
while i < 3: #Prints string 3 times
    print("the blasphemous irony")
    i+=1

print(atuple.index("why")) #Prints the index address of "why" in the tuple (atuple)

for x in matrix1: #It doesnt print in matrix form, dont know why
    for y in matrix2:
         print(x, y)



#A Function
def myfunction(): #declaring and defining a function
    abc = "shit"
    print("Python is", abc)

print(abc)

myfunction() #called a function



#A Lambda
lmblmb = lambda pp, oo : pp * oo * 2

print(lmblmb(5, 5)) #Multiplies numbers written inside the brackets with 2



#A Class
class testclass: #A Parent Class
    x = 8 * 7

class childclass(testclass): #A Child Class
    pass

obj1 = testclass() #Object created of the class 
childobj1 = childclass()

print("Here is the variable from parent class:" ,obj1.x) #Prints the referred value stored withing the class being accessed by an oject created of the said class
print("Here is the variable from child class:", childclass.x) #Prints content of parent class by being referred by child class' object

obj1.x = 9 * 7 #Modification of variable inside class
    #del obj1 (used for deleting an object)

print("Modified value:",obj1.x) #Prints modified variable



#A Class with __init() and __str__() functions
class classtwo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Here is the record: {self.name} and {self.age}"

obj2 = classtwo("Aqib", 17)
print(obj2)



#A Module
    #Import the module first by using its name (look at the Importing Libraries section)
moduletest.welcomefunc("Aqib")



#Useful Maths Methods/Functions
print(max(2, 8, 0)) #Prints the highest value from the ones given in the brackets
print(min(9, 101, -1)) #Prints the lowest value from the ones given in the brackets
print(pow(9, 2)) #Prints power of the first value by the second value (in this case 9 will be squared)
print(abs(-22.02)) #Prints the absolute positive value of the number given in the bracket
print(math.sqrt(16)) #Prints square root of given value
print(math.ceil(1.4)) #Prints the value's nearest upwards approximate
print(math.floor(1.4)) #Prints the value's nearest downwards approximate
print(math.pi) #Prints the value of Pi



#JSON (JSON is text, written with JavaScript object notation) (Truth be told i donno whats going on this ones weird as hell)
    #Converts JSON to Python 
        #Some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
        #Parse x:
y = json.loads(x)
        #The result is a Python dictionary:
print(y["age"])

    #Converts Python to JSON
        #A Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
        #Convert into JSON:
y = json.dumps(x)
        #The result is a JSON string:
print(y)

    #Random examples
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))



#A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern
    #First import the package
txt = "The rain in Spain"
ii = re.search("^The.*Spain$", txt) #Search the string to see if it starts with "The" and ends with "Spain"

if x:
    print("Yes")
else:
    print("No")



#Try Except Statements (Runs code if there are no errors, if no errors executes statement written under "except")
    #Try to open and write to a file that is not writable:
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

    #Exception

# x = -1
# if x < 0:
#   raise Exception("Sorry, no numbers below zero")

# x = "hello"
# if not type(x) is int:
#    raise TypeError("Only integers are allowed")



#Taking Input
print("Whats your name?")
namename = input()
print("Hello", namename)

if "ali" in namename:
    print("you retard, you should kys")
    
elif "aqib" in namename:
    print("my glorious king thee has returned")
    
else:
    print("you better leave")