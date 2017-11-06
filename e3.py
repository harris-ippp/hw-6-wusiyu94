#!/usr/bin/env python3

import pandas as pd

def cleandata(year):
    file_name = "president_general_{}.csv".format(year)
    header = pd.read_csv(file_name, nrows = 1).dropna(axis = 1)
    d = header.iloc[0].to_dict()
    df = pd.read_csv(file_name, index_col = 0,
                   thousands = ",", skiprows = [1])
    
    df.rename(inplace = True, columns = d) # rename to democrat/republican
    df.dropna(inplace = True, axis = 1)    # drop empty columns
    df["Year"] = year
    # only keep the colunms we need
    df = df[["Republican", "Total Votes Cast", "Year"]]    
    return df

# merge data from 1924 to 2016
mergedata = []
for line in open("ELECTION_ID"):
    real_year = line[0:4]
    file = cleandata(real_year)
    mergedata.append(file)
finaldata = pd.concat(mergedata)

# calculate the republican share
finaldata["Share"]= finaldata["Republican"] / finaldata["Total Votes Cast"]

# creat a list for the counties we want
county_list = ["Accomack County","Albemarle County","Alexandria City","Alleghany County"]
plotname_list = ["accomack_county","albemarle_county","alexandria_city","alleghany_county"]

# a function for plot
def plot(i):
    plotdata = finaldata.loc[i]
    # make sure the x axis is in correct order
    plotdata = plotdata.sort_values("Year", ascending=True)
    ax = plotdata.plot(kind = "line", x = "Year", y = "Share")
    plottitle = "Republican Vote Share in {}".format(i)
    ax.set_title(plottitle)
    ax.yaxis.set_label_text("")
    return ax

# loop over the counties to plot and save 
for i in range(0,4):
    plotfile_name = "{}.pdf".format(plotname_list[i])
    plot(county_list[i]).figure.savefig(plotfile_name)

