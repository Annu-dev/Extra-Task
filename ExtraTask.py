#!/usr/bin/env python
# coding: utf-8

# In[14]:


#1.Create a list of given structure and get the Access list as provided below:
#x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
#Access list: [1, 2, 3, 4]
#Access list: [600, 700]
#Access list: [100, 300, 500, 600, 800]
#Access list: [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
#Access list: [10]
#Access list: [ ]

x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
print(x[5][:4])
print(x[6:8])
print(x[::2])
print(x[::-1])
print(x[5][5][0])
x.clear()
print(x)


# In[25]:


#2.Create a list of thousand numbers using range and xrange and see the difference between each other.
#With xrange, we get a speedier response; also, it’s consumption of memory is lower.“xrange” has gotits name changed to 
#“range” in Python 3.x.When you have to traverse the list frequently, then it’s better to use range().
r=range(1,1001)
l=[*r]
print('thousand numbers using range function:',r)
print(l)
#s=xrange(1,10)
#t=[*s]
#print('thousand numbers using xrange function:',s)
#print(t)


# In[ ]:


#3.How Tuple is beneficial as compared to the list?
#Solution: Both lists and tuples are data structures in Python, there are remarkable differences between the two, with the main 
#difference being that lists are mutable while tuples are immutable. A list has a variable size while a tuple has a fixed 
#size.Tuples are faster than lists, because they have a constant set of values. Tuples can be used as dictionary keys,because 
#they contain immutable values like strings, numbers, etc.


# In[37]:


#4.Write a program in Python to iterate through the list of numbers in the range of 1,100 and print the number which is 
#divisible by 3 and is a multiple of 2.
l=range(1101)
r=[*l]
print('List of numbers in range of 1,100 and divisible by 3 and multiple of 2 are:')
for i in range(len(r)):
    if (r[i]%3==0 and r[i]%2==0):
        print(r[i])


# In[45]:


#5.Write a program in Python to reverse a string and print only the vowel alphabet if it exists in thestring with their index.
s=input('Enter a string : ')
print('String is :',s)
vowels=['a','e','i','o','u']
s_reverse=s[::-1]
print('After reversing the string :',s_reverse)
for i in range(len(s_reverse)):
    if s_reverse[i].lower() in vowels:
        print('Vowel ',s_reverse[i],' has index ',i)


# In[47]:


#6.Write a program in Python to iterate through the string “hello my name is abcde” and print the string which is having an 
#even length.
str = "Hello my name is Abcde"
print("The string is: ",str)
words = str.split(" ")
print("Even length words are: ")
for i in words:
    if(len(i) %2 == 0):
        print(i)


# In[48]:


#7.Write a program in python to print the pair of numbers whose sum is equal to the result number that is let's say 8.
#x=[1,2,3,4,5,6,7,8,9,-1]
x=[1,2,3,4,5,6,7,8,9,-1]
n=len(x)
sum=8
for i in range(0,n):
    for j in range(i+1,n):
        if x[i]+x[j]==sum:
            print(x[i],x[j])


# In[76]:


#8.Create two lists such as even_list and odd_list
even_list = []
odd_list =[]
counter = 0
while counter <10:
    num = int(input("Enter the number between 1-50: "))
    if num%2 == 0:
        if len(even_list) < 5: 
            even_list.append(num)
    else:
        if len(odd_list) < 5:
            odd_list.append(num)
    counter+= 1

print("Even list: ",even_list)
print("Odd list: ",odd_list)
sum_even = 0
for num in range(len(even_list)):
    sum_even = sum_even + even_list[num]

sum_odd = 0
for num in range(len(odd_list)):
    sum_odd = sum_odd + odd_list[num]

if sum_even > sum_odd:
    print("The maxium list is even list: ",sum_even)
else:
    print("The maxium list is odd list: ",sum_odd)


# In[74]:


#9.Write a program to find out the occurrence of a specific character from an alphanumeric string.
#Sample input: 12abcbacbaba344ab
#Expected output: a=5 b=5 c=2
#NOTE: Make sure to avoid counting the occurrence of numeric values in the string.

def char_count(string):
    alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    freq = {}
    for char in set(string):
        if char in alphabets:
            freq[char] = string.count(char)
    return freq


if __name__ == "__main__":
    s = "12abcbacbaba344ab"
    print(char_count(s))


# In[72]:


#10.Generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
tp = (1,2,3,4,5,6,7,8,9,10)
n=len(tp)
li = list()
for i in range(0,n):
    if tp[i]%2 == 0:
        li.append(tp[i])

tp2 = li
print (tp2)


# In[ ]:




