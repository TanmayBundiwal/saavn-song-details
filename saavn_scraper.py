#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tk
import tkinter.filedialog as f   #because tkinter is structured in this way
from tkinter import messagebox
import json
import bs4
import re
import csv


# In[3]:


def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


# In[4]:


keys = ['title','album','singers','duration','year','music','language','label','image_url']


# Getting filepath from simple UI

# In[5]:


root = tk.Tk()
root.withdraw()
filepath = tk.filedialog.askopenfile(parent=root,mode='r', title='Choose a file').name


# In[6]:


page = open(filepath, encoding="utf8")
Playlist = bs4.BeautifulSoup(page.read())


# In[7]:


songs = Playlist.find_all('div', class_='song-json')


# In[7]:


root = tk.Tk()
root.withdraw()
filename = tk.filedialog.asksaveasfile(mode='w',title = 'Save file as',defaultextension=".csv", )


# In[8]:


Output_file = open(filename.name,'w',newline='')
Out_Writer  = csv.writer(Output_file)
Out_Writer.writerow(keys);


# In[9]:


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


# In[10]:


Output_file.close()


# In[21]:


if failed:
    root = tk.Tk()
    root.withdraw()
    messagebox.showwarning("Warning",'Details of '+str(len(failed))+' songs could not be extracted.  Indices: '+str(failed))

