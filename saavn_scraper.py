#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import bs4
import re
import csv
import os


# In[ ]:


def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


# In[ ]:


url = os.path.join(".","Starred.html")
page = open(url, encoding="utf8")
StarredP = bs4.BeautifulSoup(page.read())


# In[ ]:


songs = StarredP.find_all('div', class_='song-json')


# In[ ]:


keys = ['title','album','singers','duration','year','music','language','label','image_url']


# In[ ]:


Output_file = open('All Songs.csv','w',newline='')
Out_Writer  = csv.writer(Output_file)
Out_Writer.writerow(keys);


# In[ ]:


failed = []
for i in range(0,len(songs)):
    try:
        s = remove_html_tags(str(songs[i]))
        data = json.loads(s)
        l = []
        for key in keys:
               l.append(data[key])
        Out_Writer.writerow(l)
    except:
        failed.append(i)
        continue


# In[ ]:


Output_file.close()


# In[ ]:


if failed:
    print('Details of '+str(len(failed))+' songs could not be extracted.')
    print('Indices: '+str(failed))

