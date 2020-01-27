#!/usr/bin/env python
# coding: utf-8

# # Assignment - I

# ### Importing packages

# In[82]:


import nltk
from nltk.book import *


# ### Checking if everything is loaded

# In[83]:


texts()


# In[84]:


sents()


# # Q1

# In[85]:


print(text5.collocation_list())


# # Q2

# In[86]:


my_sent_list = text5[:10]
print(f"Text is {my_sent_list}")
my_sent_string = " ".join(my_sent_list)
print(f"String formed is : {my_sent_string}")
my_sent_list_new = my_sent_string.split()
print(f"New list splitted is {my_sent_list_new}")


# # Q3

# In[87]:


print(f"Index occurs at : {text9.index('sunset')}")


# # Q4

# In[88]:


for i in [sent1, sent2, sent3, sent4, sent5, sent6, sent7, sent8]:
    temp = set([w.lower() for w in i])
    print(f"Vocab size for {i} is {len(temp)}")


# # Q5

# In[89]:


inner_set = [w.lower() for w in set(sent9)]
outer_set = set([w.lower() for w in sent9])

print(f'length containing inner set : {len(inner_set)}')
print(f'length containing outer set : {len(outer_set)}')


# ### The difference in above methods is that in case of inner set, we are only focusing on duplicacy before lowering the case so, like "THE" -> "the" and suppose already "the" occurs previosuly existed, so duplicacy of some words will remain there whereas in case of outer one, we are using set after the lowering of case , which means removing duplicacy after case lowered, thus no duplicacy possible in this case.

# # Q6

# In[90]:


print(f"Last two words of text2 : {text2[len(text2) - 2:]}")


# # Q7

# In[91]:


temp_words = [w for w in text5 if len(w) == 4]
fdist = FreqDist(temp_words)


# In[92]:


fdist.plot(30,cumulative=False, title = 'Frequency Distribution')


# # Q8

# In[93]:


print("All capital letters for Monty Python and the Holy Grail :")
for i in text6:
    if i.isupper():
        print(i)


# # Q9

# In[94]:


print('All the words of text6 ending with ize')
for i in text6:
    if i.endswith('ize'):
        print(i)

# There are no such words 


# In[95]:


print('All the words of text6 containing z')
for i in text6:
    if 'z' in i:
        print(i)


# In[96]:


print('All the words of text6 containing pt')
for i in text6:
    if 'pt' in i:
        print(i)


# In[97]:


print('All the words of text6 containing titlecase initials')
for i in text6:
    if i.istitle():
        print(i)


# # Q10

# In[98]:


sent =  ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']


# In[99]:


print('Printing all the words from sent which starts with sh : ')
for i in sent:
    if i.startswith('sh'):
        print(i)


# In[100]:


print('Printing all the words from sent which has length more than 4 : ')
for i in sent:
    if len(i) > 4:
        print(i)


# # Q11

# In[101]:


sum([len(w) for w in text1])  # taking individual sum of all words giving overall length of total words 


# In[102]:


print(f"Average word length : {sum([len(w) for w in text1]) / len(text1)}")


# # Q12

# In[103]:


def vocab_size(text):
    return len(set([w.lower() for w in text]))


# In[104]:


for i in [text1, text2, text3, text4, text5, text6, text7, text8, text9]:
    print(f'vocab size for {i} is : {vocab_size(i)}')


# # Q13

# In[105]:


def count_occ(word, text):
    return 100 *(text.count(word) / len(text))


# In[106]:


count_occ('on', text9)

