
# coding: utf-8

# In[4]:

### 2. write a program to chek given substring is there in actual string or not? (search should be case insensitive) 
str="Sravanya Talathoti"
sub_str="van"
print str.find(sub_str)



# In[6]:

#### 3. take a number from the user and check whether even or odd
a=input("Enter a value: ")
if (a % 2) == 0:
    print "Even Number"
else:
    print "Odd Number"


# In[34]:

### 4. take a number from the user and check whether it is prime?
n=input("Enter number: ")
if n > 1:   
   for i in range(2,n):
       if (n % i) == 0:
           print(n,"is not a prime number")
           break
   else:
       print(n,"is a prime number")
else:
   print(num,"is not a prime number")


# In[8]:

### 5. take a string from the user and check contains only digits or not?
s=raw_input("Enter a string: ")
print s.isdigit()


# In[9]:

### 6. take a string from the user and check contains only alphabets or not?
s=raw_input("Enter string : ")
print s.isalpha()


# In[10]:

### 7. take a string from the user and check contains only special chars or not?


# In[24]:

### 8. take a string from the user and check contains only capiatl letters or not?

s=raw_input("Enter string : ")
print s.isupper()


# In[23]:

### 9. take a string from the user and check contains only small letters or not?
s=raw_input("Enter string : ")
print s.islower()


# In[12]:

###  10. Show the below menu to the user until and until user select quit and display corresponding os message
'''
Menu:
1.Windows
2.Linux
3.Mac
4.Quit
'''

##print "Menu:\n1.Windows\n2.Linux\n3.Mac\n4.Quit"

s=input("Enter option: ")
if(s<=3):
    print "Menu:\n1.Windows\n2.Linux\n3.Mac\n4.Quit"

##if s=="1":
    ##print "Menu:\n1.Windows\n2.Linux\n3.Mac\n4.Quit"

    ##print "Windows Selected"
##elif s=="2":
    ##print "Menu:\n1.Windows\n2.Linux\n3.Mac\n4.Quit"

    ##print "Linux Selected"
##elif s=="3":
    ##print "Menu:\n1.Windows\n2.Linux\n3.Mac\n4.Quit"

    ##print "Mac Selected"
else:
    print "Quit Selected"


# In[15]:

### 16. Take the input from the user for(Total number of people, toatl number of busses, Number of seats for bus). Based on the input
##      Deside whether there is sufficient busses or not and give solution for how many extra busses required.
a=input("Enter total No.of Buses: ")
b=raw_input("Enter total no.of People: ")
c=raw_input("Enter total no.of Seats: ")
if c>b:
    print "Sufficient Buses"
else:
    print "Insufficient Seats"
    while(c<=b):
        
        print "Require buses"


# In[16]:

### 18. Determine the factors of a number entered by the user
num=input("Enter number: ")
factorial=1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num+1):
       factorial = factorial*i
   print "factorial is ",factorial


# In[ ]:

###


# In[17]:

### 20. Take two numbers from the user a,b check whether a is divisible by b or not?
a=input("Enter a value")
b=input("Enter b value")
if (a % b) == 0:
    print "a is divisible by b"
else:
    print "a is not divisible by b"


# In[18]:

### 21. Given an age, figure out whether someone's a baby, toddler, child, teenager, adult or old codger.
a=input("Enter age: ")    
if a<=3:
    print "you are a baby"
elif a<=7:
    print "you are a toddler"
elif a<=12:
    print "you are a child"
elif a<=17:
    print "you are a teenager"
elif a>=18:
    print "you are an adult or old codger"


# In[19]:

### 22. Find the sum of all the multiples of 3 or 5 below 1000
nums = [3, 5]
max = 999


result = 0
for num in nums:
    for i in range(1,max):
        if num*i < max:
            result += num*i
print result

result = 0
for i in range(0,max):
    if i%3 == 0 or i%5 == 0:
        result += i

print result


# In[20]:

### 23. Write a program to findout big of two numbers
a=input("Enter a value:")
b=input("Enter b value: ")
if a>b:
    print "a is big value"
else:
    print "b is big value"


# In[21]:

### 24. Write a program to findout biggest number in the given numbers.
a=input("Enter a value: ")
b=input("Enter b value: ")
c=input("Enter c value: ")
if a>b and a>c:
    print "a is big"
elif b>a and b>c:
    print "b is big"
else:
    print "c is big"


# In[22]:

###


# In[ ]:



