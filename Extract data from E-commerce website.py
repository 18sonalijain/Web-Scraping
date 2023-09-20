#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests


# In[3]:


url="https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
r=requests.get(url)
print(r)


# In[4]:


pip install beautifulsoup4


# In[5]:


from bs4 import BeautifulSoup


# In[6]:


soup=BeautifulSoup(r.text,"lxml")
print(soup)


# In[7]:


boxes=soup.find_all("div",class_="col-sm-4 col-lg-4 col-md-4")
print(boxes)


# In[8]:


names=soup.find_all("a",class_="title")
print(names)


# In[9]:


for i in names:
    print(i.text)


# In[10]:


prices=soup.find_all("h4",class_="pull-right price")
for i in prices:
    print(i.text)


# In[ ]:




