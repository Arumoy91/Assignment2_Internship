#!/usr/bin/env python
# coding: utf-8

# In[1]:


import selenium


# In[2]:


import pandas as pd
from selenium import webdriver


# In[3]:


driver=webdriver.Chrome("C:\chromedriver.exe")


# In[4]:


driver.get('https://www.naukri.com/')


# In[5]:


search_job=driver.find_element_by_id('qsb-keyword-sugg')
search_job.send_keys("Data Scientist")
search_loc=driver.find_element_by_id("qsb-location-sugg")
search_loc.send_keys("Bangalore")search_btn=driver.find_element_by_xpath("//div[@class='search-btn']/button")
search_btn.click()


# In[6]:


search_btn=driver.find_element_by_xpath("//div[@class='search-btn']/button")
search_btn.click()


# In[7]:


job_titles=[]
company_names=[]
locations_list=[]


# In[8]:


title_tags=driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
title_tags[0:10]


# In[9]:


for i in title_tags:
    
    title=i.text
    job_titles.append(title)
job_titles[0:10]


# In[10]:


companies_tags=driver.find_elements_by_xpath("//a[@class='subTitle ellipsis fleft']")
companies_tags[0:10]


# In[11]:


for i in companies_tags:
    
    company_name=i.text
    company_names.append(company_name)
company_names[0:10]


# In[12]:


locations_tags=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi location']/span[1]")
locations_tags[0:10]


# In[13]:


for i in locations_tags:
    location=i.text
    locations_list.append(location)
    
    
locations_list[0:10]
    


# In[14]:


print(len(job_titles),len(company_names),len(locations_list))


# In[15]:


import pandas as pd
jobs=pd.DataFrame({})
jobs['title']=job_titles[0:10]
jobs['company']=company_names[0:10]
jobs['locations']=locations_list[0:10]


# In[16]:


jobs


# In[ ]:




