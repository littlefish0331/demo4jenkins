#!/usr/bin/env python
# coding: utf-8

# In[32]:


import requests
import os

with open('./image-number.txt', 'r') as f:
    img_num = f.read()

response = requests.get(f"https://api.thecatapi.com/v1/images/search?limit={img_num}")
res_all = response.json()
img_urls = [res['url'] for res in res_all]
img_paths = ['./cat-image/'+os.path.basename(img_url) for img_url in img_urls]
for (img_path, img_url) in zip(img_paths, img_urls):
    with open(img_path, 'wb') as f:
        response = requests.get(img_url)
        f.write(response.content)
        f.close()


# In[ ]:




