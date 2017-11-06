#!/usr/bin/env python3


from bs4 import BeautifulSoup as bs
import requests


# Grap the html and find the rows
addr = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General"
resp = requests.get(addr)
html = resp.content
soup = bs(html, "html.parser")

# Grap all the election item classes
item = soup.find_all("tr", "election_item")

# From each row, grap the ids and corresponding years, and print them out to a file.
for i in item:    
    y = int(i.find("td", "year first").contents[0])
    n = int(i.get("id")[-5:])
    print(y,n,file=open("ELECTION_ID", "a"))


