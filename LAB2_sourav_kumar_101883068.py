#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/souravs17031999/UML602-NLP/blob/master/LAB_2.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# # ASSIGNMENT - 2 
# ### @ name : sourav kumar
# ### @ roll no. : 101883068
# ### @ COE-5

# #### Importing required packages

# In[1]:


import nltk
from nltk import *
from nltk.book import *
import string
nltk.download('brown')
nltk.download('inaugural')
nltk.download('state_union')
print("Importing packages...")
from nltk.corpus import brown
from nltk.corpus import inaugural
from nltk.corpus import state_union


# In[2]:


print("All packages imported !")


# In[3]:


print("Checking the brown corpus categories...")


# In[4]:


brown.categories()


# ### Q1

# In[5]:


print("Q1")
count_wh = 0
for i in brown.words():
    if i.startswith('wh'):
        count_wh += 1

print(count_wh)


# ### Q2

# In[6]:


print("Q2")
modals = ['can', 'could', 'may', 'might', 'must', 'will']
all_words = brown.words()
f_dist = FreqDist([w.lower() for w in all_words])


# In[7]:


for i in modals:
    print(f"{i} : {f_dist[i]}")


# In[8]:


cfd = ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre)
)


# In[9]:


cfd.tabulate(samples=modals)


# ### Q3

# In[10]:


print("Q3")
import re
years = [re.findall('[0-9]+', x) for x in inaugural.fileids()]


# In[11]:


print(years)


# ### Q4

# In[12]:


print("Q4")
cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in state_union.fileids()
    for w in state_union.words(fileid)
    for target in ['men', 'women', 'people']
    if w.lower() == target)


# In[13]:


print(cfd.tabulate())


# In[14]:


cfd.plot()


# ### Q5

# In[15]:


print("Q5")
print("Studying texts from brown corpus for news and religion category...")
news = brown.words(categories='news')
religion = brown.words(categories='religion')


# In[16]:


print(f"vocab size of news : {len([w.lower() for w in news])}")
print(f"vocab size of religion : {len([w.lower() for w in religion])}")


# In[17]:


print(f"lexical diversity of news : {len(news)/len(set(news))}")
print(f"lexical diversity of religion : {len(religion)/len(set(religion))}")


# In[18]:


nltk.Text(news).concordance('india')


# In[19]:


nltk.Text(religion).concordance('india')


# ### Q6

# In[20]:


print("Q6")
f_dist_brown = FreqDist([w.lower() for w in brown.words()])
required_words = []
for i, j in f_dist_brown.items():
    if j >= 3:
        required_words.append(i)


# In[21]:


print(f"printing some words which occured at least 3 times... ")
print(f"{required_words[:30]}...")
print()
print(f"Printing some words which occured at least 3 times after removal of stop words...")
stopwords = nltk.corpus.stopwords.words('english')
print([w for w in required_words[:50] if w.lower() not in stopwords])


# ### Q7

# In[22]:


print("Q7")
def ldt(corpus):
    cfd = nltk.ConditionalFreqDist(
        (genre, len(corpus.words(categories=genre))/len(set(corpus.words(categories=genre))))
        for genre in corpus.categories()
        )

    print(cfd.tabulate())
    cfd.plot()


# In[23]:


ldt(brown)


# In[24]:


print("Q8")
print("Printing 50 most frequent words for text1 after removing stopwords and punctuation...")
def most_frequent(text):
    list_without_stop = [w for w in text if w.lower() not in stopwords and w.lower() not in string.punctuation]
    f_dist = nltk.probability.FreqDist(list_without_stop)
    return sorted(f_dist, key=f_dist.get, reverse=True)


# In[25]:


print(most_frequent(text1)[:50])

