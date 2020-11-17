# Welcome to the Financial Systems Design Project
**Group Members**

* Alex Stewart
* Bingle Kruger
* Charl Everts

# Installation

## Setup

1. Clone this repository

2. Move into this `financials` subfolder:

	```
	cd financials
	```

3. Install package dependencies:

	```
	npm install
	```

# Run Dashboard
1. Once packages are installed:

	```
	npm run serve
	```
2. Copy the local host address shown in the terminal into your local browser:

## Quit dashboard
1. Open the terminal where the dashboard is running:

2. Quit the dashboard by entering "crtl+c" on keyboard.

# Dashboard Instructions
To navigate the dashboard, select the different pages on the left hand side of the screen. 

## Welcome Page
The Welcome page is the default page when the dashboard is opened.
The blue text below the heading on the page can be clicked and expanded to display more infomration regarding the dashboard.
Below the blue text are two tables of the stastical beta information for both the Indices and Shares. 

The tables display the latest changes in the betas of the shares and indices and are interactive so they can be sorted and . 
The green buttons on the bottom right of each table enable the user to download the table in a csv file.

## Search by Share

The Search by Share page contains the different JSE Shares and the different betas at different quarters of the year. 
The table contains a multitude of variables, namely: Share code, Start Date, End Dates, Dats Traded, Data Points, Year Month, Beta J200, Beta J203, Beta J250, Beta J257, Beta J258,  and Industry. Additionally, filtering by: specific share, date range and industry are added to improve the overall user experience and increase the functionality.

The “select all rows” button is used to select all the entries displayed in the table (before or after filtering), these values can be downloaded as a csv file with the “Download selected rows” button. Shares can also be selected manually for download. The user can generate plots on the historic Beta values for specific shares. After entering the code of the share (and applying other filters if the user wants to), the user has to select all the rows they want to view in the plot. Thereafter, a button is displayed, namely “Generate/update plot”. After pressing the button the plot is generated. These plots are completely interactive and are updated based on the selected Beta indices. The plots can also be downloaded by the user. 

## Search by Index

The Search by Share page contains the different JSE/FTSE indices and the different betas at different quarters of the year. 
The layout and functionality is the same as the Search by Share page.

The user can also download the selected entries (as csv) from the table before (or after) the required filtering has been done. The user can filter by entering the code of the required instrument. After selecting all the entries the user is interested in, a plot of the historic Beta values for this instrument can also be generated. These plots have exactly the same features as those on the Search by Share page. 

## Client Indices

This page was to meet the specific requirements of one of AIMFRMs clients. 

A table displays a synthetic construction of the most important risk statistics for a specific index across various industries. The dashboard created is able to display a table for five different market proxies, namely: Top 40 (J200), All Share (J203), Financials and Industrials (J250), Industrials (J257), Resources (J258). The table contains seven variables, the Index, Date, Industry, Weight, Portfolio Beta, Portfolio Systematic Volatility and the Portfolio Specific Variance. Once again the user has the option to download the selected rows as a csv file. The table can also be sorted by the user however they require.

Below the table the user has some options to generate plots. After selecting a relevant index for the selected market proxy the user has the option to create plots using the aforementioned statistics. The plots that can be created are the weight decomposition, the beta decomposition, systematic volatility decomposition and specific variance decomposition. These plots are interactive and update dynamically based on the index the user selects. The user can use the built in plotly tools to only view the entries for specific quarters should it be required. 

### Problems

Please email Alex on stwale002@myuct.ac.za

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


