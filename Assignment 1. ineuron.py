#!/usr/bin/env python
# coding: utf-8

# In[72]:


a=[]
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        a.append(str(x))
print (','.join(a))


# In[35]:


fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print (lname + " " + fname)


# In[73]:


r = 6.0
pi = 3.1415926535897931
V = 4.0/3.0*pi* r**3
print(V)


# In[48]:


s = list([2,3,3])


# In[49]:


s


# In[54]:


n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


# In[69]:


def reverse(a): 
  str = "" 
  for i in a: 
    str = i + str
  return str
  
a = input(" Enter your name")

print ("The original string  is : ",end="") 
print (a) 
  
print ("The reversed string(using loops) is : ",end="") 
print (reverse(a)) 


# In[79]:


Sentence = "WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens"
print ("Sentence : " + Sentence)

print ("\n\n")

New_Sentence = input_sentence.replace("INDIA, ", "INDIA,\n").replace("SOVEREIGN, ", "SOVEREIGN, !\n").replace("REPUBLIC ", "REPUBLIC \n") + (":")
print ("New sentence : " + New_Sentence)

