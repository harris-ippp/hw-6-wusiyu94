#!/usr/bin/env python3

import requests


for line in open("ELECTION_ID"):
    year = line[0:4]
    code = line[5:10]
    #insert code into the url
    addr = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/".format(code)
    resp = requests.get(addr)
    #insert year into filename
    file_name = "president_general_{}.csv".format(year)
    with open(file_name,"w") as out:
        out.write(resp.text)
    
  