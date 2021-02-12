#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Kütüphaneleri import edelim
import requests #HTTP get yapabilmek için gerekli
from bs4 import BeautifulSoup
import logging


# In[2]:


BASE_PATH = "https://www.vatanbilgisayar.com"
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)


# In[5]:


def get_page_source(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup


def get_all_first_category_pages(link):
    all_category_links = list()
    soup = get_page_source(link)
    all_links = [a['href'] for a in
                 soup.find_all('a', href=True, attrs={'class': 'dropdown-menu-list__link special-menu-link'})]
    logging.info("We got all links.")
    for link in all_links:
        all_category_links.append("%s%s%s" % (BASE_PATH, link, "?page="))
    return all_category_links


def main():
    logging.info("It's starting.")
    all_categories = get_all_first_category_pages(BASE_PATH)
    for category in all_categories:
        print(category)


# In[6]:


if __name__ == "__main__":
    main()


# ## BS4 ün özelliği DOM kullanmaları ve onları içerisinden belirli bir path ler verilerek ya da özellikler verilerek veri çekilmesidir.

# ### Sayfa içerisinde class ya da div ler sayesinde gezinerek istediğimiz veriye ulaşmaya çalışıyoruz. Direkt bir kelime yazarak arama yapılırsa yanlış olur. path kullanmalıyız.

# ### Soupların yaptığı iş: DOM içerisinden istediğiniz elemanı çekip almak!

# In[ ]:




