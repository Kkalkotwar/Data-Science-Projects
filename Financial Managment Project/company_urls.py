#!/usr/bin/env python
# coding: utf-8

# In[11]:


# importing the necessary liberies

from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as urReq

# Getting company urls for user specified letter using function

def company_urls():
    
    moneycontrol_url = "https://www.moneycontrol.com/india/stockpricequote/"
    letter = input("Please enter letter")
    upper = letter[0].upper()
    data_url = moneycontrol_url + upper
    website_response = urReq(data_url)
    letter_company_data = website_response.read()
    beautified_results = bs(letter_company_data,"html.parser")
    finding_box = beautified_results.find_all("div",{"class":"PT15"})
    tr_finding_box = finding_box[0].find_all("tr")
    
    for d in range(1,len(tr_finding_box)):
        td_finder = tr_finding_box[d].find_all("td")
    
    urls = []
    for i in range(1,len(tr_finding_box)):
        z = tr_finding_box[i].find_all("td")
        for j in range(0,len(td_finder)):
            k = z[j].a["href"]
            k = urls.append(k)
    return urls


"""if __name__ == "__main__":
    a_urls = company_urls()"""





