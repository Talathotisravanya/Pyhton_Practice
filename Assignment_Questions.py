
# coding: utf-8

# In[14]:

## 1. f=lambda x: 0 if x else 1 
##    print f(10)


f=lambda x: 0 if x else 1
print f(10)


# In[15]:

## 2.print  map(int,[‘a’,’b’],[12,13])


print  map(int,[‘a’,’b’],[12,13])


# In[16]:

##3.  x=0
#     y= “positive” if x else “negative”
#     print y


x=0
y= “positive” if x else “negative”
print y



# In[18]:

## 4.l=[1,2,3,4]
    # print  l*3
    
l=[1,2,3,4]
print  l*3


# In[31]:

## 5. l=[[]]
 ## l1 = l*3
#    print l1


l=[[]]
l1 = l*3
print l1
print l


# In[30]:

##6.l1[0]=10 take l from 5th question
#    print l1

l1[0]=10
print l1


# In[33]:

##7.l1.insert(0,10) take l1 from 6th question
 #   print l1
    
l1.insert(0,10)
print l1


# In[27]:

## 8. l1=[1,2,3,4]
    #   l2=l1
    #   l1.insert(20,30)
    #   print l2 
    
    
l1=[1,2,3,4]
l2=l1
l1.insert(20,30)
print l2


# In[28]:

## 9.l3 = (1,2,3,4)
#    l3[0]=10

l3 = (1,2,3,4)
l3[0]=10
print l3


# In[4]:

## 10. s=”python”
    #  WAP to remove “o” from s  
    

s="python"
s.split()
l=[]
for i in s:
    l.append(i)
print l
l.remove('o')
print l


# In[ ]:

## 11.


# In[ ]:

## 12.


# In[25]:

## 13.print int(12.34) ?
print int(12.34)


# In[26]:

## 14.print int(12.34) ?
print int("12.34")


# In[ ]:

## 15.


# In[27]:

##16. a=1j
 #     print a, type(a)?
    

a=1j
print a
type(a)


# In[29]:

## 17. a=[i+10 for I in rage(10,20,2)]


a=[i+10 for i in range(10,20,2)]
print a


# In[28]:

## 18. a=[i+20 for I in range(10,2,2)]

a=[i+20 for i in range(10,2,2)]
print a


# In[30]:

## 21. print bool(“0”)

print bool('0')


# In[31]:

## 22. b= 10 if -10 else 0 print b
b= 10 if -10 else 0
print b


# In[32]:

## 23. print bool(-10)

print bool(-10)


# In[33]:

## 24. for j in range(10):
#           print j
#          break
#      print j


for j in range(10):
    print j
    break
print j


# In[35]:

## 25. for j in range(10):
#          if j<5:
#               continue
#          else:
#             break
#    print j


for j in range(10):
    if j<5:
        continue
    else:
        break
print j


# In[36]:

## 26.i=0
#     while i<10:
#        print I


i=0
while i<10:
    print I


# In[11]:

## 27. print “12” > “2”

print "12" >"2"


# In[37]:

## 28.l1=[1,2,3,4]
#l2=[1,2,3,4]
#l3=l1
#print l1 is l3
#print l1 == l3
#print l1 is l2
#print l1 == l2

l1=[1,2,3,4]
l2=[1,2,3,4]
l3=l1
print l1 is l3
print l1 == l3
print l1 is l2
print l1 == l2


# In[38]:

## 30. print “12” > 30

print "12">30


# In[39]:

## 31.l=['2','13','1000']
# l.sort()
# print l

l=['2','13','1000']
l.sort()
print l


# In[45]:

## 32. l1=[1,2,3,4]
#      l2=l1.append(10)
#     print l2

l1=[1,2,3,4]
l2=l1.append(10)
print l2
print l1


# In[48]:

## 33. l1.extend(10) take l1 from the 32nd question
l1=[1,2,3,4,10]
l1.extend(10)
print l1


# In[17]:

## 34.

if 10<20:
    print '10<20 is true'
if 10>20:
    print '10>20 is true'
else:
    print '10>20 is false'


# In[18]:

## 35.

if 10<20:
    print '10<20 is true'
elif 10>20:
    print '10>20 is true'
else:
    print '10>20 is false'


# In[ ]:

## 36.

i=0
while i<10:
    I = i+1
    if i>3:
        break
print I


# In[3]:

## 38. WAP Take a string from the user and remove “aeiou” letters from that string.

#s=raw_input("Enter string: ")
s="aeiou"
j=[]
l=s.split()
print l
for i in l:
    j.append(i)
print j
    
# s.remove()


# In[4]:

## 39. print “pYThon ProgrAm”.title()
s="pYThon ProgrAm"
s.title()


# In[5]:

## 40. print “pYThon ProgrAm”.capitalize()
s="pYThon ProgrAm"
s.capitalize()


# In[6]:

## 41.

d={1:10,1:100}
print d.get(1)
print d.get(10)


# In[13]:

## 47.
d={'name':'n1', 'id':2}
print d.popitem()
#print d


# In[17]:

## 48.

d={'name':'n1','id':2}
print d.pop()


# In[9]:

## 50.
d={'name':'n1', 'id':2}
d1 = d
d['id'] = 3
print d1


# In[ ]:



