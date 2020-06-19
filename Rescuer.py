#!/usr/bin/env python
# coding: utf-8

# In[9]:


import datetime
a = input("Library name whose functions you want to find ") 
#print(a)

import importlib
importlib.import_module(a)


TimeNow = datetime.datetime.now()
funcs = dir(importlib.import_module(a))
for f in funcs:
    with open('functions.txt','a') as fd:
        fd.write(f"{f } , ")
print(f"Successfully stored data at {TimeNow} in file functions.txt , search your pc for the following file")


    


# In[ ]:




