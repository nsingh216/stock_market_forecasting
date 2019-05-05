# stock_market_forecasting


#### Overview
For this project we explored stock market datasets and will utilize the Deutsche Börse Public Dataset available on AWS [1]. This dataset contains minute-by-minute stock prices for two different markets (Xetra and Eurex). For our final project, we will be focusing our efforts on predicting short-term prices for the tickers in the Xetra market. The Xetra data have records ranging from July 3rd, 2017 to May 15th, 2018 for 100 tickers. The final CSV file used for the code pieces [2] contains about 15 million records in total (too large to upload here).

Additionally, we did some analysis of calculating moving averages using MapReduce and Pandas.

#### Files
1) The linear regression colab notebook (Linear_Regression.ipynb) contains code to predict stock prices using Linear Regression

2) The time series colab notebook (Time_Series.ipynb) contains code used to conduct some time series analysis (ACF Plots, PACF Plots, Decompose Time Series to various components (trend, seasonality, residuals), Dickey Fuller Test). It also contains code used to determine the optimum p, d, and q parameters for ARIMA using auto_arima in the pdarima module an example prediction for 1 of the tickers.

#### Report
A pdf version of the our report can be found on box [2] as well and contains the several other resources used for this project.


#### Resources
[1] The Deutsche Börse Public Dataset & Machine Learning - Notebook 1 (Obtain, Clean & Understand Data) https://github.com/Originate/dbg-pds-tensorflow-demo/blob/master/notebooks/01-data-cleaning-single-stock.ipynb

[2] https://uofi.app.box.com/folder/62554512474 
