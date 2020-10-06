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
Industry_Classification_Benchmark = pd.read_csv("../csv_files/Industry_Classification_Benchmark.csv")
Index_Constituents = pd.read_csv("../csv_files/Index_Constituents.csv")
BA_Beta_Output = pd.read_csv("../csv_files/BA_Beta_Output.csv")
#FTSEJSE_Index_Series = pd.read_csv("../csv_files/FTSEJSE_Index_Series.csv")
#EOD_Interest_Rate_Data = pd.read_csv("../csv_files/EOD_Interest_Rate_Data.csv")
#EOD_Equity_Data = pd.read_csv("../csv_files/EOD_Equity_Data.csv")


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
#sum(weights) = 1
   
IC_weights = {'IC': ICs, 'Weight': weights}
IC_weights = pd.DataFrame(IC_weights)

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
                #mktVol.append(BA_Beta_Output["Total Risk"][i])
    #for i in range(len(BA_Beta_Output)):       
        if BA_Beta_Output["Date"][i].month == rdate.month and BA_Beta_Output["Date"][i].year == rdate.year and BA_Beta_Output["Instrument"][i] == mktIndexCode:
            mktVol = BA_Beta_Output["Total Risk"][i]            
    return mktVol

mktVol = GetBetasMktAndSpecVols(mktIndexCode,rdate,ICs)

### Third Function

# set weights
#weights_np_array = np.array([0.05, 0.15, 0.4, 0.134, 0.189, 0.003, 0.074]) given from previous function
weights_t = np.transpose(weights)

# set betas
#betas = np.array([1.05, 0.75, 0.84, 0.9134, 1.189, 1.003, 0.574]) given from previous function
betas_t = np.transpose(betas)

# specific volatility
#specVols = np.array([0.05, 0.15, 0.4, 0.134, 0.189, 0.003, 0.074]) given from previous function
specVols_t = np.transpose(specVols)

# create S: a diagonal matrix with specVols as entries
S = np.diag(specVols)

# create D: a diagonal matrix of total asset volatilities
D = np.diag(betas)
D_inverse = np.linalg.inv(D)

# market volatility
#mktVol = np.array([1.1])
mktVol = np.array(mktVol) #change mktvol to a numpy array

# Variance <=> Total Volatility
# Calculations

pfBeta = weights_t*betas #Portfolio_Beta

sysCov = betas*betas_t*(mktVol**2) #Systematic_Covariance_Matrix

pfSysVol = weights_t*betas*betas_t*weights*(mktVol**2) #Portfolio_Systematic_Variance

specCov = S**2 #Specific_Covariance_Matrix

pfSpecVol = weights_t*(S**2)*weights #Portfolio_Specific_Variance

totCov = betas*betas_t*(mktVol**2) + S**2 #Total_Covariance_Matrix

pfVol = weights_t*betas*betas_t*weights*(mktVol**2) + weights_t*(S**2)*weights # Portfolio_Variance

CorrMat = D_inverse*(betas*betas_t*mktVol**2 + S**2)*D_inverse #Correlation_Matrix

