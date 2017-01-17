
# coding: utf-8

# In[16]:

## 27. Taake some single digit numbers from the user and findout min, maximum, sum, average
s=input("Enter numbers: ")
print min(s)
print max(s)
print sum(s)
avg=sum(s,0.0)/len(s)
print ("Average of s is: ",avg )
 


# In[21]:

## 28.WAP> 10 -> 000010
#       100 ->  000100
#      1000 ->  001000
#      2345678 -> 2345678

s=raw_input("Enter value: ")
print s.rjust(6,'0')


# In[22]:

## 29. names ="emp1,emp2,emp3,emp4" iterate through the employee names.
names="emp1,emp2,emp3,emp4"
str=names.split()
for word in str:
    print (word)


# In[ ]:

## 30. Take actuual string, soucrce string, destination string. replce first nth occurances of soucestring with 
##      destination string of actual string



# In[5]:

## 31. Taake numbers from the user and findout min, maximum, sum, average
n=input("Enter numbers: ")
print min(n)
print max(n)
print sum(n)
avg=sum(n,0.0)/len(n)
print ("Average of s is: ",avg )


# In[39]:

## 32. l=[10,20,30,[40,50,60],70,[80,90,20]]. Convert this list as sigle dimentiona list

l=[10,20,30,[40,50,60],70,[80,90,20]]

l1=l[3]
print l1
l2=l[5]
print l2
l3=l[2]


# In[11]:

## 33. input: "google" print count of each character
input="google"
l=list(input)
s=set(l)
for i in s:
    print (i,input.count(i))


# In[ ]:

## 34. Convert n dimentional list to single dimentiona list.


# In[2]:

## 35. l=[1,2,3] just make it as a string.
l=[1,2,3]
print map(str,l)


# In[16]:

## 38. l=['a','A','b','B','d','D','c','C'] sort the list properly
l=['a','A','b','B','d','D','c','C']
l1=l.sort();
print ("List:", l)


# In[15]:

## 40. WAP to find union and intersection of lists.
a=[1,2,3,4,5,6]
b=[2,3,6,8,9,1]
c=list(set(a) & set(b))
print c
d=list(set(a) | set(b))
print d


# In[14]:

## 43. Remove duplicates from the list: a=[1,2,3,2,3,4,1,,3,4]
a=[1,2,3,2,3,4,1,3,4]
s=set(a)
print s


# In[10]:

##44. l=['1','2','3'] get the sum of the list
l=['1','2','3'] 
l1=map(int,l)
print l1
print sum(l1)


# In[12]:

## 45. l1=[1,2,3,4] l2=[5,6,7,8] sum of two lists
l1=[1,2,3,4]
l2=[5,6,7,8]
print sum(l1+l2)


# In[ ]:



