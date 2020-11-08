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
from varname import nameof


#### Specificy the indexCode, date and MktIndexCode
rdate = datetime.datetime(2020,6,22) #enter date here
indexCode = "RESI"
mktIndexCode = "J203" # Enter Market code for CAPM model

#### read files
Industry_Classification_Benchmark = pd.read_csv("FSD_Project/csv_files/Industry_Classification_Benchmark.csv")
Index_Constituents = pd.read_csv("FSD_Project/csv_files/Index_Constituents.csv")
BA_Beta_Output = pd.read_csv("FSD_Project/csv_files/BA_Beta_Output.csv")
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
ICB_subsector = []
indexCode_column = indexCode + " New"
#define function

def GetICsAndWeights(rdate,indexCode):
    if indexCode == 'FLED':
        indexCode_column = 'ALSI New'
    elif indexCode == 'LRGC' or indexCode == 'MIDC' or indexCode == 'SMLC':
        indexCode_column = 'Index New'
    else:
        indexCode_column = indexCode + " New"
    
    Gross_market = []
    for i in range(len(Index_Constituents)):
        if (Index_Constituents.loc[i,"Date"] == rdate and Index_Constituents.loc[i,indexCode_column] == indexCode):  #and Index_Constituents.loc[i,"ALSI New"] == "ALSI New"):
            ICs.append(Index_Constituents.loc[i, "Alpha"])
            Gross_market.append(Index_Constituents.loc[i, "Gross Market Capitalisation"])
            ICB_subsector.append(Index_Constituents.loc[i, "ICB Sub-Sector"])

    total = np.sum(Gross_market)
    weights = Gross_market/total
    weights = weights.tolist()
    return weights

#store weights and ICs in separate lists
weights = GetICsAndWeights(rdate, indexCode)
#Merge into one table
Date_IC_weights_subsector = {'Date':rdate,'IC': ICs, 'Weight': weights,'ICB Sub_sector': ICB_subsector}
Date_IC_weights_subsector = pd.DataFrame(Date_IC_weights_subsector)
#sum(weights) = 1

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

######################################      aggregate over all the information for function one 
######## DEFINE FUNCTION 1 ######## 
def GetICsAndWeights(rdate,indexCode):
    if indexCode == 'FLED':
        indexCode_column = 'ALSI New'
    elif indexCode == 'LRGC' or indexCode == 'MIDC' or indexCode == 'SMLC':
        indexCode_column = 'Index New'
    else:
        indexCode_column = indexCode + " New"
    
    Gross_market = []
    for i in range(len(Index_Constituents)):
        if (Index_Constituents.loc[i,"Date"] == rdate and Index_Constituents.loc[i,indexCode_column] == indexCode):  #and Index_Constituents.loc[i,"ALSI New"] == "ALSI New"):
            ICs.append(Index_Constituents.loc[i, "Alpha"])
            Gross_market.append(Index_Constituents.loc[i, "Gross Market Capitalisation"])
            ICB_subsector.append(Index_Constituents.loc[i, "ICB Sub-Sector"])
            Index_Code.append(indexCode)
            dates.append(rdate)

    total = np.sum(Gross_market)
    weights = Gross_market/total
    weights = weights.tolist()
    return weights

# GET CODES AND DATES TO PERFORM LOOP AND INTIALISE VARIABLES
indexCodes = ["ALSI", "FLED", "LRGC", "MIDC", "SMLC", "TOPI", "RESI", "FINI", "INDI", "PCAP", "SAPY", "ALTI"]
rdates = [(datetime.datetime(2017,9,18)),
           (datetime.datetime(2017,12,18)),
           (datetime.datetime(2018,3,19)),
           (datetime.datetime(2018,6,18)),
           (datetime.datetime(2018,9,25)),
           (datetime.datetime(2018,12,24)),
           (datetime.datetime(2019,3,18)),
           (datetime.datetime(2019,6,24)),
           (datetime.datetime(2019,9,23)),
           (datetime.datetime(2019,12,23)),
           (datetime.datetime(2020,3,23)),
           (datetime.datetime(2020,6,22))]
ICs = []
ICB_subsector = []
weights = []
Index_Code = []
dates = []  


# LOOP THROUGH FUNCTION 1 TO GET EVERY POSSIBLE ITERATION

for i in indexCodes:  
    for j in rdates:
        weights.append(GetICsAndWeights(j,i))

weights = [item for sublist in weights for item in sublist]
Date_IC_weights_subsector = {'Date':dates,'Index Code': Index_Code,'IC': ICs, 'Weight': weights,'ICB Sub_sector': ICB_subsector}
Date_IC_weights_subsector = pd.DataFrame(Date_IC_weights_subsector)

# add industry using merge
Date_IC_weights_subsector = Date_IC_weights_subsector.merge(Industry_Classification_Benchmark[['Industry','Sub-Sector Code']], left_on=['ICB Sub_sector'], right_on=['Sub-Sector Code']).drop(columns='Sub-Sector Code')

#Get weights of industry for each date for each indice
Index_Date_Idustry_Weight = Date_IC_weights_subsector.groupby(["Index Code","Date","Industry"], as_index = False)["Weight"].sum()
#PERFROM Unit Test
Date_IC_weights_subsector[(Date_IC_weights_subsector['Date'] == datetime.datetime(2017,9,18)) & (Date_IC_weights_subsector['Index Code'] == 'ALSI')]['Weight'].sum()
######## END FUNCTION 1 ######## 

######## DEFINE FUNCTION 2 ######## 
BA_Beta_Output_New = BA_Beta_Output
BA_Beta_Output_New['Year_Month'] = BA_Beta_Output_New['Date'].dt.to_period('M')
BA_Beta_Output_New = BA_Beta_Output_New.drop(columns = ["Date","Start Date","End Date"])
BA_Beta_Output_New = BA_Beta_Output_New[['Index','Year_Month', 'Instrument','Beta', 'Unique Risk']]


Date_IC_weights_subsector_New = Date_IC_weights_subsector
Date_IC_weights_subsector_New['Year_Month'] = Date_IC_weights_subsector_New['Date'].dt.to_period('M')
Date_IC_weights_subsector_New = Date_IC_weights_subsector_New.drop(columns = ["Date"])
Date_IC_weights_subsector_New  = Date_IC_weights_subsector_New.rename(columns={'IC': 'Instrument'})

#Grab only date instrument and sub-setor-code and change name to Instrument 
Date_instrument_sub_sector_code = Date_IC_weights_subsector_New[['Year_Month','Instrument','ICB Sub_sector','Industry']]
Date_instrument_sub_sector_code = Date_instrument_sub_sector_code.rename(columns={'IC': 'Instrument'})


#Second have to get the separate the BA_Beta_table into the different index codes
J200_Beta  = BA_Beta_Output_New[BA_Beta_Output_New['Index'] == 'J200']
J203_Beta  = BA_Beta_Output_New[BA_Beta_Output_New['Index'] == 'J203']
J250_Beta  = BA_Beta_Output_New[BA_Beta_Output_New['Index'] == 'J250']
J257_Beta  = BA_Beta_Output_New[BA_Beta_Output_New['Index'] == 'J257']
J258_Beta  = BA_Beta_Output_New[BA_Beta_Output_New['Index'] == 'J258']
# grab relevant information
J200_Beta = J200_Beta[['Index','Year_Month', 'Instrument','Beta', 'Unique Risk']]
J203_Beta = J203_Beta[['Index','Year_Month', 'Instrument','Beta', 'Unique Risk']]
J250_Beta = J250_Beta[['Index','Year_Month', 'Instrument','Beta', 'Unique Risk']]
J257_Beta = J257_Beta[['Index','Year_Month', 'Instrument','Beta', 'Unique Risk']]
J258_Beta = J258_Beta[['Index','Year_Month', 'Instrument','Beta', 'Unique Risk']]

def GetMktVols(mktIndexCode,rdate):
    for i in range(len(BA_Beta_Output)): # loop through ever row of table     
        if BA_Beta_Output["Date"][i].month == rdate.month and BA_Beta_Output["Date"][i].year == rdate.year and BA_Beta_Output["Instrument"][i] == mktIndexCode:
            mktVol = BA_Beta_Output["Total Risk"][i]            
    return mktVol



#check if any NAs in industry
#Date_IC_weights_subsector_New['Industry'].isna().count()
# No NAs
#merge industry for J200
J200_merge_test = Date_instrument_sub_sector_code.merge(J200_Beta,left_on = ['Year_Month', 'Instrument'], right_on =['Year_Month', 'Instrument'])
J200_Beta_Unique_Risk = J200_merge_test.groupby(['Year_Month', 'Instrument','ICB Sub_sector','Industry','Beta', 'Unique Risk'], as_index = False).count()
#remove index column
J200_Beta_Unique_Risk = J200_Beta_Unique_Risk[['Year_Month', 'Instrument','ICB Sub_sector','Industry','Beta', 'Unique Risk']]
J200_Industry_Beta_Unique_Risk = J200_Beta_Unique_Risk.groupby(['Year_Month','Industry'], as_index = False)["Beta"].sum()
#now merge all of them
J200_full_table = Date_IC_weights_subsector_New.merge(J200_Beta_Unique_Risk, left_on=['Year_Month','Instrument','Industry','ICB Sub_sector'], right_on=['Year_Month','Instrument','Industry','ICB Sub_sector'], how = 'left')
J200_full_table.fillna(0)

#merge industry for J203
J203_merge_test = Date_instrument_sub_sector_code.merge(J203_Beta,left_on = ['Year_Month', 'Instrument'], right_on =['Year_Month', 'Instrument'])
J203_Beta_Unique_Risk = J203_merge_test.groupby(['Year_Month', 'Instrument','ICB Sub_sector','Industry','Beta', 'Unique Risk'], as_index = False).count()
#remove index column
J203_Beta_Unique_Risk = J203_Beta_Unique_Risk[['Year_Month', 'Instrument','ICB Sub_sector','Industry','Beta', 'Unique Risk']]
J203_Industry_Beta_Unique_Risk = J203_Beta_Unique_Risk.groupby(['Year_Month','Industry'], as_index = False)["Beta"].sum()
#now merge all of them
J203_full_table = Date_IC_weights_subsector_New.merge(J203_Beta_Unique_Risk, left_on=['Year_Month','Instrument','Industry','ICB Sub_sector'], right_on=['Year_Month','Instrument','Industry','ICB Sub_sector'], how = 'left')
J203_full_table.fillna(0)

#merge industry for J250
J250_merge_test = Date_instrument_sub_sector_code.merge(J250_Beta,left_on = ['Year_Month', 'Instrument'], right_on =['Year_Month', 'Instrument'])
J250_Beta_Unique_Risk = J250_merge_test.groupby(['Year_Month', 'Instrument','ICB Sub_sector','Industry','Beta', 'Unique Risk'], as_index = False).count()
#remove index column
J250_Beta_Unique_Risk = J250_Beta_Unique_Risk[['Year_Month', 'Instrument','ICB Sub_sector','Industry','Beta', 'Unique Risk']]
J250_Industry_Beta_Unique_Risk = J250_Beta_Unique_Risk.groupby(['Year_Month','Industry'], as_index = False)["Beta"].sum()
#now merge all of them
J250_full_table = Date_IC_weights_subsector_New.merge(J250_Beta_Unique_Risk, left_on=['Year_Month','Instrument','Industry','ICB Sub_sector'], right_on=['Year_Month','Instrument','Industry','ICB Sub_sector'], how = 'left')
J250_full_table.fillna(0)

#merge industry for J257
J257_merge_test = Date_instrument_sub_sector_code.merge(J257_Beta,left_on = ['Year_Month', 'Instrument'], right_on =['Year_Month', 'Instrument'])
J257_Beta_Unique_Risk = J257_merge_test.groupby(['Year_Month', 'Instrument','ICB Sub_sector','Industry','Beta', 'Unique Risk'], as_index = False).count()
#remove index column
J257_Beta_Unique_Risk = J257_Beta_Unique_Risk[['Year_Month', 'Instrument','ICB Sub_sector','Industry','Beta', 'Unique Risk']]

J257_Industry_Beta_Unique_Risk = J257_Beta_Unique_Risk.groupby(['Year_Month','Industry'], as_index = False)["Beta"].sum()

#now merge all of them
J257_full_table = Date_IC_weights_subsector_New.merge(J257_Beta_Unique_Risk, left_on=['Year_Month','Instrument','Industry','ICB Sub_sector'], right_on=['Year_Month','Instrument','Industry','ICB Sub_sector'], how = 'left')
J257_full_table.fillna(0)

#merge industry for J258
J258_merge_test = Date_instrument_sub_sector_code.merge(J258_Beta,left_on = ['Year_Month', 'Instrument'], right_on =['Year_Month', 'Instrument'])
J258_Beta_Unique_Risk = J258_merge_test.groupby(['Year_Month', 'Instrument','ICB Sub_sector','Industry','Beta', 'Unique Risk'], as_index = False).count()
#remove index column
J258_Beta_Unique_Risk = J258_Beta_Unique_Risk[['Year_Month', 'Instrument','ICB Sub_sector','Industry','Beta', 'Unique Risk']]

J258_Industry_Beta_Unique_Risk = J258_Beta_Unique_Risk.groupby(['Year_Month','Industry'], as_index = False)["Beta"].sum()

#now merge all of them
J258_full_table = Date_IC_weights_subsector_New.merge(J258_Beta_Unique_Risk, left_on=['Year_Month','Instrument','Industry','ICB Sub_sector'], right_on=['Year_Month','Instrument','Industry','ICB Sub_sector'], how = 'left')
J258_full_table.fillna(0)

####End Function 2

### Function 3

#### build function
rdates_func3 = pd.DataFrame(rdates)
rdates_func3[0] = rdates_func3[0].dt.to_period('M')

Index_Date_Industry_Weight_Func3 = Index_Date_Idustry_Weight 
Index_Date_Industry_Weight_Func3['Year_Month'] = Index_Date_Industry_Weight_Func3['Date'].dt.to_period('M')
Index_Date_Industry_Weight_Func3 = Index_Date_Industry_Weight_Func3.drop(columns = ["Date"])
Index_Date_Industry_Weight_Func3 = Index_Date_Industry_Weight_Func3[['Index Code','Year_Month','Industry','Weight']]

Industry_list = ['Basic Materials','Technology','Financials', 'Utilities', 'Telecommunications','Consumer Services', 'Health Care', 'Consumer Goods', 'Industrials', 'Oil & Gas']

#J200_Index_Date_Industry_Weight_pfBeta = Index_Date_Industry_Weight_Func3



def Calc_pf_Beta(rdate, IndexCode, J200_full_table):
    #get mktVol
    MktIndex = nameof(J200_full_table)[0:4]
    mktVol = GetMktVols(MktIndex,rdates_func3[0][0])
  
    rdate_J200_test = rdate #enter date here
    #group by index code and year_month and then by a particular index code and a particular year month
    J200_full_per_indice_Beta = J200_full_table.groupby(['Index Code','Year_Month']).get_group((IndexCode, rdate_J200_test))["Beta"]
    J200_full_per_indice_weight = J200_full_table.groupby(['Index Code','Year_Month']).get_group((IndexCode, rdate_J200_test))["Weight"]
    J200_full_per_indice_specVol = J200_full_table.groupby(['Index Code','Year_Month']).get_group((IndexCode, rdate_J200_test))["Unique Risk"]


    #convert Beta and replace nan with 0
    J200_full_per_indice_Beta = J200_full_per_indice_Beta.to_list()
    where_are_nans_b = np.isnan(J200_full_per_indice_Beta)
    J200_full_per_indice_Beta = np.array(J200_full_per_indice_Beta)
    J200_full_per_indice_Beta[where_are_nans_b] = 0

    #convert weights and replace nan with 0
    J200_full_per_indice_weight = J200_full_per_indice_weight.to_list()
    where_are_nans_w = np.isnan(J200_full_per_indice_weight)
    J200_full_per_indice_weight = np.array(J200_full_per_indice_weight)
    J200_full_per_indice_weight[where_are_nans_w] = 0
    
    #convert specvols and replace nan with 0
    J200_full_per_indice_specVol = J200_full_per_indice_specVol.to_list()
    where_are_nans_s = np.isnan(J200_full_per_indice_specVol)
    J200_full_per_indice_specVol = np.array(J200_full_per_indice_specVol)
    J200_full_per_indice_specVol[where_are_nans_s] = 0

    #transpose the weights
    J200_full_per_indice_weight_T = np.transpose(J200_full_per_indice_weight)
    #transpose the betas
    J200_full_per_indice_Beta_T = np.transpose(J200_full_per_indice_Beta)
    
    #specific volatility
    # create S: a diagonal matrix with specVols as entries
    S = np.diag(J200_full_per_indice_specVol)

    #calculate the pfBeta, for a particular index code, year_month, mktindexcode(j200)
    J200_full_per_indice_pfBeta = J200_full_per_indice_weight_T.dot(J200_full_per_indice_Beta)
    
    #calculate SysVol
    pfSysVol = np.dot(np.dot(np.dot(J200_full_per_indice_weight_T,J200_full_per_indice_Beta),J200_full_per_indice_Beta_T),J200_full_per_indice_weight)*(mktVol**2)#Portfolio_Systematic_Variance
    
    #calcualte SpecVar
    pfSpecVar = np.dot(np.dot(J200_full_per_indice_weight_T,S**2),J200_full_per_indice_weight)
    
    ###now times the pfbeta,sysVol and specVar by the weightings per industry per date per index in the Index_Date_Industry_Weight table
    # first grab the relevant information and convert date column to approproiate dtype
    
    #perform groupby to grab the relevant info
    Industry_weight_per_date = Index_Date_Industry_Weight_Func3.groupby(['Index Code','Year_Month']).get_group((IndexCode, rdate_J200_test))
    
    #add pfbeta column and perform calculation
    Industry_weight_per_date['pfBeta']  = Industry_weight_per_date['Weight']*J200_full_per_indice_pfBeta
    #add pfSysVol column and perform calculation
    Industry_weight_per_date['pfSysVol'] = Industry_weight_per_date['Weight']*pfSysVol
     #add pfpecVar column and perform calculation
    Industry_weight_per_date['pfSpecVar'] = Industry_weight_per_date['Weight']*pfSpecVar
    
    #add additional industries if not contained in frame
    Industry_list_func3 = Industry_weight_per_date['Industry'].to_list() 
    missing_list = list(set(Industry_list)-set(Industry_list_func3))
    
    for i in missing_list:
        Industry_add = {'Index Code': IndexCode, 'Year_Month': rdate, 'Industry': i, 'Weight': 0, 'pfBeta': 0, 'pfSysVol': 0, 'pfSpecVar': 0}
        Industry_weight_per_date = Industry_weight_per_date.append(Industry_add, ignore_index = True)

    return Industry_weight_per_date


#### execute for J200

J200_Index_Year_Month_Industry_Weight_Beta = Calc_pf_Beta(rdates_func3[0][0], 'ALSI', J200_full_table)

for i in indexCodes:
    for j in rdates_func3[0]:
        J200_Index_Year_Month_Industry_Weight_Beta = J200_Index_Year_Month_Industry_Weight_Beta.append(Calc_pf_Beta(j, i, J200_full_table))

J200_Index_Year_Month_Industry_Weight_Beta['Count'] = ""
J200_Index_Year_Month_Industry_Weight_Beta = J200_Index_Year_Month_Industry_Weight_Beta.groupby(['Index Code', 'Year_Month','Industry','Weight','pfBeta','pfSysVol','pfSpecVar'], as_index = False)['Count'].count()
J200_Index_Year_Month_Industry_Weight_Beta = J200_Index_Year_Month_Industry_Weight_Beta[['Index Code', 'Year_Month','Industry','Weight','pfBeta','pfSysVol','pfSpecVar']]

#change year_month to string format
J200_Index_Year_Month_Industry_Weight_Beta['Year_Month'] = J200_Index_Year_Month_Industry_Weight_Beta['Year_Month'].astype(str)

J200_Index_Year_Month_Industry_Weight_Beta.Year_Month.replace({'2017-09':'2017-Q3',
                                                               '2017-12':'2017-Q4',
                                                               '2018-03':'2018-Q1',
                                                               '2018-06':'2018-Q2',
                                                               '2018-09':'2018-Q3',
                                                               '2018-12':'2018-Q4',
                                                               '2019-03':'2019-Q1',
                                                               '2019-06':'2019-Q2',
                                                               '2019-09':'2019-Q3',
                                                               '2019-12':'2019-Q4',
                                                               '2020-03':'2020-Q1',
                                                               '2020-06':'2020-Q2'}, inplace=True)


#### execute for J203

J203_Index_Year_Month_Industry_Weight_Beta = Calc_pf_Beta(rdates_func3[0][0], 'ALSI', J203_full_table)

for i in indexCodes:
    for j in rdates_func3[0]:
        J203_Index_Year_Month_Industry_Weight_Beta = J203_Index_Year_Month_Industry_Weight_Beta.append(Calc_pf_Beta(j, i, J203_full_table))

J203_Index_Year_Month_Industry_Weight_Beta['Count'] = ""
J203_Index_Year_Month_Industry_Weight_Beta = J203_Index_Year_Month_Industry_Weight_Beta.groupby(['Index Code', 'Year_Month','Industry','Weight','pfBeta','pfSysVol','pfSpecVar'], as_index = False)['Count'].count()
J203_Index_Year_Month_Industry_Weight_Beta = J203_Index_Year_Month_Industry_Weight_Beta[['Index Code', 'Year_Month','Industry','Weight','pfBeta','pfSysVol','pfSpecVar']]

#change year_month to string format
J203_Index_Year_Month_Industry_Weight_Beta['Year_Month'] = J203_Index_Year_Month_Industry_Weight_Beta['Year_Month'].astype(str)

J203_Index_Year_Month_Industry_Weight_Beta.Year_Month.replace({'2017-09':'2017-Q3',
                                                               '2017-12':'2017-Q4',
                                                               '2018-03':'2018-Q1',
                                                               '2018-06':'2018-Q2',
                                                               '2018-09':'2018-Q3',
                                                               '2018-12':'2018-Q4',
                                                               '2019-03':'2019-Q1',
                                                               '2019-06':'2019-Q2',
                                                               '2019-09':'2019-Q3',
                                                               '2019-12':'2019-Q4',
                                                               '2020-03':'2020-Q1',
                                                               '2020-06':'2020-Q2'}, inplace=True)


#### execute for J250

J250_Index_Year_Month_Industry_Weight_Beta = Calc_pf_Beta(rdates_func3[0][0], 'ALSI', J250_full_table)

for i in indexCodes:
    for j in rdates_func3[0]:
        J250_Index_Year_Month_Industry_Weight_Beta = J250_Index_Year_Month_Industry_Weight_Beta.append(Calc_pf_Beta(j, i, J250_full_table))

J250_Index_Year_Month_Industry_Weight_Beta['Count'] = ""
J250_Index_Year_Month_Industry_Weight_Beta = J250_Index_Year_Month_Industry_Weight_Beta.groupby(['Index Code', 'Year_Month','Industry','Weight','pfBeta','pfSysVol','pfSpecVar'], as_index = False)['Count'].count()
J250_Index_Year_Month_Industry_Weight_Beta = J250_Index_Year_Month_Industry_Weight_Beta[['Index Code', 'Year_Month','Industry','Weight','pfBeta','pfSysVol','pfSpecVar']]

#change year_month to string format
J250_Index_Year_Month_Industry_Weight_Beta['Year_Month'] = J250_Index_Year_Month_Industry_Weight_Beta['Year_Month'].astype(str)

J250_Index_Year_Month_Industry_Weight_Beta.Year_Month.replace({'2017-09':'2017-Q3',
                                                               '2017-12':'2017-Q4',
                                                               '2018-03':'2018-Q1',
                                                               '2018-06':'2018-Q2',
                                                               '2018-09':'2018-Q3',
                                                               '2018-12':'2018-Q4',
                                                               '2019-03':'2019-Q1',
                                                               '2019-06':'2019-Q2',
                                                               '2019-09':'2019-Q3',
                                                               '2019-12':'2019-Q4',
                                                               '2020-03':'2020-Q1',
                                                               '2020-06':'2020-Q2'}, inplace=True)


#### execute for J257

J257_Index_Year_Month_Industry_Weight_Beta = Calc_pf_Beta(rdates_func3[0][0], 'ALSI', J257_full_table)

for i in indexCodes:
    for j in rdates_func3[0]:
        J257_Index_Year_Month_Industry_Weight_Beta = J257_Index_Year_Month_Industry_Weight_Beta.append(Calc_pf_Beta(j, i, J257_full_table))

J257_Index_Year_Month_Industry_Weight_Beta['Count'] = ""
J257_Index_Year_Month_Industry_Weight_Beta = J257_Index_Year_Month_Industry_Weight_Beta.groupby(['Index Code', 'Year_Month','Industry','Weight','pfBeta','pfSysVol','pfSpecVar'], as_index = False)['Count'].count()
J257_Index_Year_Month_Industry_Weight_Beta = J257_Index_Year_Month_Industry_Weight_Beta[['Index Code', 'Year_Month','Industry','Weight','pfBeta','pfSysVol','pfSpecVar']]

#change year_month to string format
J257_Index_Year_Month_Industry_Weight_Beta['Year_Month'] = J257_Index_Year_Month_Industry_Weight_Beta['Year_Month'].astype(str)

J257_Index_Year_Month_Industry_Weight_Beta.Year_Month.replace({'2017-09':'2017-Q3',
                                                               '2017-12':'2017-Q4',
                                                               '2018-03':'2018-Q1',
                                                               '2018-06':'2018-Q2',
                                                               '2018-09':'2018-Q3',
                                                               '2018-12':'2018-Q4',
                                                               '2019-03':'2019-Q1',
                                                               '2019-06':'2019-Q2',
                                                               '2019-09':'2019-Q3',
                                                               '2019-12':'2019-Q4',
                                                               '2020-03':'2020-Q1',
                                                               '2020-06':'2020-Q2'}, inplace=True)


#### execute for J258

J258_Index_Year_Month_Industry_Weight_Beta = Calc_pf_Beta(rdates_func3[0][0], 'ALSI', J258_full_table)

for i in indexCodes:
    for j in rdates_func3[0]:
        J258_Index_Year_Month_Industry_Weight_Beta = J258_Index_Year_Month_Industry_Weight_Beta.append(Calc_pf_Beta(j, i, J258_full_table))

J258_Index_Year_Month_Industry_Weight_Beta['Count'] = ""
J258_Index_Year_Month_Industry_Weight_Beta = J258_Index_Year_Month_Industry_Weight_Beta.groupby(['Index Code', 'Year_Month','Industry','Weight','pfBeta','pfSysVol','pfSpecVar'], as_index = False)['Count'].count()
J258_Index_Year_Month_Industry_Weight_Beta = J258_Index_Year_Month_Industry_Weight_Beta[['Index Code', 'Year_Month','Industry','Weight','pfBeta','pfSysVol','pfSpecVar']]

#change year_month to string format
J258_Index_Year_Month_Industry_Weight_Beta['Year_Month'] = J258_Index_Year_Month_Industry_Weight_Beta['Year_Month'].astype(str)

J258_Index_Year_Month_Industry_Weight_Beta.Year_Month.replace({'2017-09':'2017-Q3',
                                                               '2017-12':'2017-Q4',
                                                               '2018-03':'2018-Q1',
                                                               '2018-06':'2018-Q2',
                                                               '2018-09':'2018-Q3',
                                                               '2018-12':'2018-Q4',
                                                               '2019-03':'2019-Q1',
                                                               '2019-06':'2019-Q2',
                                                               '2019-09':'2019-Q3',
                                                               '2019-12':'2019-Q4',
                                                               '2020-03':'2020-Q1',
                                                               '2020-06':'2020-Q2'}, inplace=True)


#save each table into its own and change name
J200_Index_Year_Month_Industry_Weight_Beta.to_csv('J200_Full_Demo_FINAL.csv', index = True)
J203_Index_Year_Month_Industry_Weight_Beta.to_csv('J203_Full_Demo_FINAL.csv', index = True)
J250_Index_Year_Month_Industry_Weight_Beta.to_csv('J250_Full_Demo_FINAL.csv', index = True)
J257_Index_Year_Month_Industry_Weight_Beta.to_csv('J257_Full_Demo_FINAL.csv', index = True)
J258_Index_Year_Month_Industry_Weight_Beta.to_csv('J258_Full_Demo_FINAL.csv', index = True)
    
#### Join all tables into one 
#first add mktindexCode to differentiate
J200_Index_Year_Month_Industry_Weight_Beta['Market Code'] = "J200"
J200_Index_Year_Month_Industry_Weight_Beta = J200_Index_Year_Month_Industry_Weight_Beta[['Market Code','Index Code', 'Year_Month','Industry','Weight','pfBeta','pfSysVol','pfSpecVar']]

J203_Index_Year_Month_Industry_Weight_Beta['Market Code'] = "J203"
J203_Index_Year_Month_Industry_Weight_Beta = J203_Index_Year_Month_Industry_Weight_Beta[['Market Code','Index Code', 'Year_Month','Industry','Weight','pfBeta','pfSysVol','pfSpecVar']]

J250_Index_Year_Month_Industry_Weight_Beta['Market Code'] = "J250"
J250_Index_Year_Month_Industry_Weight_Beta = J250_Index_Year_Month_Industry_Weight_Beta[['Market Code','Index Code', 'Year_Month','Industry','Weight','pfBeta','pfSysVol','pfSpecVar']]

J257_Index_Year_Month_Industry_Weight_Beta['Market Code'] = "J257"
J257_Index_Year_Month_Industry_Weight_Beta = J257_Index_Year_Month_Industry_Weight_Beta[['Market Code','Index Code', 'Year_Month','Industry','Weight','pfBeta','pfSysVol','pfSpecVar']]

J258_Index_Year_Month_Industry_Weight_Beta['Market Code'] = "J258"
J258_Index_Year_Month_Industry_Weight_Beta = J258_Index_Year_Month_Industry_Weight_Beta[['Market Code','Index Code', 'Year_Month','Industry','Weight','pfBeta','pfSysVol','pfSpecVar']]

Full_demo = pd.concat([J200_Index_Year_Month_Industry_Weight_Beta, J203_Index_Year_Month_Industry_Weight_Beta, J250_Index_Year_Month_Industry_Weight_Beta, J257_Index_Year_Month_Industry_Weight_Beta, J258_Index_Year_Month_Industry_Weight_Beta],ignore_index = True)

#check dates
awe = J258_Index_Year_Month_Industry_Weight_Beta['Year_Month'].drop_duplicates()
awe = J258_Index_Year_Month_Industry_Weight_Beta['Year_Month'].drop_duplicates()
awe = J200_Index_Year_Month_Industry_Weight_Beta['Year_Month'].drop_duplicates()
awe = J250_Index_Year_Month_Industry_Weight_Beta['Year_Month'].drop_duplicates()
awe = J258_Index_Year_Month_Industry_Weight_Beta['Year_Month'].drop_duplicates()
awe = J258_Index_Year_Month_Industry_Weight_Beta['Year_Month'].drop_duplicates()



Full_demo.to_csv('Full_demo_updated_SpevVol.csv', index = True)







