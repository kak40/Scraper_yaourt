#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 17:17:48 2018

@author: Karine 
"""

###### Carrefour Activia nature 4 pots: page HTML
from urllib.request import Request, HTTPCookieProcessor, build_opener
import re

#Cookie problem: need to define a store by visiting the store specifing page
#url: store finder (City: Gennevilliers)
url ="https://courses-en-ligne.carrefour.fr/set-store/37?sectorZip=92230&sectorCity=Gennevilliers"
cookieProcessor = HTTPCookieProcessor()
opener = build_opener(cookieProcessor)

request = Request(url)
response = opener.open(request)

#url2: product
url2 = "https://courses-en-ligne.carrefour.fr/3033491147067/yaourts-nature-activia?pk=activa"
request2 = Request(url2)
response2 = opener.open(request2)

html = response2.read().decode("utf8")
#print(type(html))

#for inspection
#f=open("text.txt","w")
#f.write(html)
#f.close()

#find the price inside the html page
resu = re.search(r"cd-ProductPriceUnitInteger[^0-9]*([0-9]*,)[^0-9]*([0-9]{2})€", html)
print(resu.group(1)+resu.group(2))
#1,09


###### Auchan Activia nature 4 pots : page javescript (mais pas vraiment finalement)

import requests
from bs4 import BeautifulSoup

# Specify url: url
url = 'https://www.auchandirect.fr/produits/225870'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extracts the response as html: html_doc
html_doc = r.text

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc, "lxml")

# Prettify the BeautifulSoup object: pretty_soup (for page inspection)
pretty_soup = soup.prettify()
#print(pretty_soup)

#find the price
whole = soup.findAll("span", {"class": "SparkCurrency__Whole", "data-reactid":"621"})
cent = soup.findAll("span", {"class":"SparkCurrency__Cent", "data-reactid":"623"})

print(whole[0].get_text() + ","+ cent[0].get_text())
#1,45

#Conclusion: achetez chez carouf!