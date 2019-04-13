# stock_market_forecasting


### Time Series Forecasting Models

In a time series model, the time interval of the input data must be constant (hourly, weekly, monthly, etc)
We used univariate time series, where we used only one variable (time) to forecast the price. 


#### 1) Linear Regression
#### 2) ARIMA
    AR = Auto Regression: Linear Regression where lags from itself are used to predict future model [10]
         In the python model, this value is represented by p, which is the number of lags that should be used in the prediction
    I = Integrated: d = number of differencing required to make the it stationary
        A time series data set has stationarity [11] when its statistical properties, such as mean and standard deviation do not change over time. With time series models, we make the assumption that the data is already stationary or can be transformed to be made stationary.
        
    MA = Moving Average: represented by q in the model; number of lagged forecast errors 
    
    
    

#### 3) FBProphet:



### Sources 
10 https://www.machinelearningplus.com/time-series/arima-model-time-series-forecasting-python/

11 https://people.duke.edu/~rnau/411diff.htm
