import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt


def actuals_plot(x, y, ticker):
    figure = plt.figure()
    plt.title = "Start prices of " + ticker
    plt.scatter(x, y)
    plt.xlabel("Time")
    plt.ylabel("Starting Price")
    plt.show()
    # plt.savefig(ticker + ".png")

data_path = "./data/"

df = pd.read_csv(data_path + "cooked_v3.csv")
print(df.head())

# tickers and their traded volumes
volume_series = df.groupby('Mnemonic')['TradedVolume'].sum()
volume_series.sort_values(ascending=False, inplace=True)
print(volume_series)

df.head()
df.replace([np.inf, -np.inf], np.nan)
df.dropna(inplace=True)

for ticker in volume_series.index:
    ticker_data = df[df.Mnemonic == ticker]

    X = pd.to_numeric(pd.to_datetime(ticker_data['CalcDateTime']))
    X = X.values.reshape(-1, 1)

    Y = ticker_data['StartPrice']
    print("Ticker " + ticker + " has " + str(len(X)) + " records.")

    # plot hourly
    ticker_data['CalcDateTime'] = pd.to_datetime(ticker_data['CalcDateTime'])
    hourly_ticker_data = ticker_data.reset_index().set_index(
        'CalcDateTime').resample('H').mean()
    hourly_ticker_data = hourly_ticker_data.reset_index()
    hourly_X = pd.to_datetime(hourly_ticker_data['CalcDateTime'])
    hourly_Y = hourly_ticker_data['StartPrice']
    actuals_plot(hourly_X, hourly_Y, ticker)

    # run regression
    # using 30:70 break
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3,
                                                        random_state=0)
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    predictions = regressor.predict(X_test)

    r2 = r2_score(y_test, predictions)
    print("R2 for " + ticker + ": " + str(r2))

    mse = mean_squared_error(y_test, predictions)
    print("MSE for " + ticker + ": " + str(mse))

