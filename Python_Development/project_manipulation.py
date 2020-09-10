#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 14:09:23 2020

@author: Alex Stewart
"""
#### Load libraries
import numpy as np
import pandas as pd
import datetime as datetime

#### Specificy the indexCode, date and MktIndexCode
rdate = datetime.datetime(2020,6,22) #enter date here
indexCode = "RESI"
mktIndexCode = "J203" # Enter Market code for CAPM model

#### read files
Industry_Classification_Benchmark = pd.read_csv("/Users/myhome/Documents/work/UCT 2020/Course Work/Semester 2/Financial Systems design/Project/Industry_Classification_Benchmark.csv")
Index_Constituents = pd.read_csv("/Users/myhome/Documents/work/UCT 2020/Course Work/Semester 2/Financial Systems design/Project/Index_Constituents.csv")
FTSEJSE_Index_Series = pd.read_csv("/Users/myhome/Documents/work/UCT 2020/Course Work/Semester 2/Financial Systems design/Project/FTSEJSE_Index_Series.csv")
EOD_Interest_Rate_Data = pd.read_csv("/Users/myhome/Documents/work/UCT 2020/Course Work/Semester 2/Financial Systems design/Project/EOD_Interest_Rate_Data.csv")
EOD_Equity_Data = pd.read_csv("/Users/myhome/Documents/work/UCT 2020/Course Work/Semester 2/Financial Systems design/Project/EOD_Equity_Data.csv")
BA_Beta_Output = pd.read_csv("/Users/myhome/Documents/work/UCT 2020/Course Work/Semester 2/Financial Systems design/Project/BA_Beta_Output.csv")

#### convert Date column to datetime format
Index_Constituents.Date = pd.to_datetime(Index_Constituents.Date)
BA_Beta_Output.Date = pd.to_datetime(BA_Beta_Output.Date)

#### First Function
##intialise
#store ICs
ICs = []
#define function
def GetICsAndWeights(rdate,indexCode):
    indexCode_column = indexCode + " New"
    Gross_market = []
    
    for i in range(len(Index_Constituents)):
        if (Index_Constituents.loc[i,"Date"] == rdate and Index_Constituents.loc[i,indexCode_column] == indexCode):  #and Index_Constituents.loc[i,"ALSI New"] == "ALSI New"):
            ICs.append(Index_Constituents.loc[i, "Alpha"])
            Gross_market.append(Index_Constituents.loc[i, "Gross Market Capitalisation"])

    total = np.sum(Gross_market)
    weights = Gross_market/total
    weights = weights.tolist()
    return weights

#store weights and ICs in separate lists
weights = GetICsAndWeights(rdate, indexCode)    

#### Second Function
##Initialise and create lists to store data 
F2_date = []
betas = []
F2_Instruments = []
F2_Index = []
mktVol = []
specVols = []

#define function
def GetBetasMktAndSpecVols(mktIndexCode,rdate,ICs):
    for i in range(len(BA_Beta_Output)): # loop through ever row of table
        for j in ICs: # loop through every constituent of the ICs
            if BA_Beta_Output["Date"][i].month == rdate.month and BA_Beta_Output["Date"][i].year == rdate.year and BA_Beta_Output["Instrument"][i] == j and BA_Beta_Output["Index"][i] == mktIndexCode:
                #add to lists
                F2_date.append(BA_Beta_Output["Date"][i])
                betas.append(BA_Beta_Output["Beta"][i])
                F2_Instruments.append(BA_Beta_Output["Instrument"][i])
                F2_Index.append(BA_Beta_Output["Index"][i])
                specVols.append(BA_Beta_Output["Unique Risk"][i])
                mktVol.append(BA_Beta_Output["Total Risk"][i])
    return 

GetBetasMktAndSpecVols(mktIndexCode,rdate,ICs)

### Third Function
