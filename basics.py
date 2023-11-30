#basic
x=1
Y="Python is open source langauage"
a=float(x)#Conversion
b=Y[1]#indexing
print(len(Y))
c=Y[0:22]#Slicing
print(a,b,c)

#Operators(A Symbol that performs certain operations)
a=10
b=2
c="hai"
d="hello"
e=2
print("\n")
print(a+b)#adding two integers
print(c+d)#adding two strings
#relational operator
print(a>b)
print(c>d)
#Identity Operator 
print(b is e) #"is " if both values are same true, 
print(c is not d)#"is not " both values are not same true
print((a+b)*a/e)#precedence operator(BADMAS Rule)

#Condiotional statements
print("\n")
n1=35 #given by user int(input('enter 1st number:'))
n2=20 #by default            or  #take viceversa
if n1>=n2:
   if n1>n2:
    print("its greatest number")
   else:
    print("Both are equal")
else:
    print("its lesser number")
    
#Looping statements
print("\n")
A="Looping"
for i in A:   #repeat of block
      print(i)
print("\n")
x=1
while x<=10: # repeat until Condition is true
    print(x)
    x=x+1
    
#transfer Statements
numbers=[2,3,5,20,9,15]
for i in numbers:
    if i>10:
        break#observe the o/p after 5 ,9is not updated bcz its break the loop
    print('processing enogh break number',i)
    print("\n")    
        
#Data Type
#Strings
num="10"
a=36
Name="here is ,examples on strings {1},we can take{0}"
print("\n")
print(Name.upper())#uppercase
print(Name.count("s"))#Counts the particuar letter
print(len(Name))#length of strings
print(Name.split())
print(Name.format(num,a)) #Strings on format method
a=36
name="Hai"
txt="His name is {1},and he is {0} years old"
print(txt.format(a,name))

#List[],Tuple(),Sets{}
print("\n")
a=(1,4,5,3,'a','b') #its in tuple
x=list(a) #Coversion to list
y=set(a)#Conversion to set
print(x)
print(y)

#list
a=[1,2,3,4,b]
x=a.append('a')#add the new variables at last
y=a.insert(1,"hai")#
z=a.pop(3)#removing of specfic index value
print(a)

#tuple
print("\n")
t=(7,6,8,5)
t_add = t+(3,5,7)#adding the values in tuple 
print(t_add)
#another method of adding
x=list(t)
x.append(10)
print(x)
x[1]="hi" #changing the value tuple
t=tuple(x)
print(t)
print(t[2])#Acceing the value

 #Sets
print("\n")
a1={"a,b,c,d"}
b1={"1,2,3,4"}
a1.add(10)
print(a1)
a1.update(b1) #add the items from one to another set
print(a1)

#Dictionary

values={"brand":"Apple","Model":"i5","year":"2023"}
print(values)
x=values.update({"RAM":"4GB"})#Adding the Dictornary
y=values.pop("Model")#Removing The dictonary
print(values)
for x in values.keys():#use the keys() method to return the keys of a dictionary:
    print(x)
print(values.get("brand"))#Returns the value of the specified key



