# Quantclean 🧹

<strong><em>"Make it cleaner, make it leaner"</em></strong>

A program that **reformats** every financial dataset to **US Equity TradeBar** (Quantconnect format)

(Works great with datas from Quandl, Algoseek, Alpha Vantage, yfinance, and many other more...)

## Few things you may want to know before getting started 🍉

1) Even if you don't have a open, close, volume, high, low, date column, quantclean will create a blank column for it. No problem!

2) The dataframe generated will look like this if you have a date and time column (or if both are on the same column):

| Date| Open | High | Low | Close | Volume
| ----------- | ---------- | --------- | ---------- | --------- | ---------
| 20131001 09:00 | 6448000  | 6448000 | 6448000 | 6448000 | 90

 - DateTime - String date "YYYYMMDD HH:MM" in the timezone of the data format.
 - Open - Deci-cents Open Price for TradeBar.
 - High - Deci-cents High Price for TradeBar.
 - Low - Deci-cents Low Price for TradeBar.
 - Close - Deci-cents Close Price for TradeBar.
 - Volume - Number of shares traded in this TradeBar.
 

3) You can also get somethig like that if use the ```sweeper_dash``` function instead of ```sweeper```


| Date| Open | High | Low | Close | Volume
| ----------- | ---------- | --------- | ---------- | --------- | ---------
| **2013-10-01** | 6448000  | 6448000 | 6448000 | 6448000 | 90


As you can see, the date format is YYYY-MM-DD and no more YYYYMMDD.


4) If you just have a date column (e.g : something like YYYY-MM-DD), it will look like this:

| Date| Open | High | Low | Close | Volume
| ----------- | ---------- | --------- | ---------- | --------- | ---------
| 20131001 | 6448000  | 6448000 | 6448000 | 6448000 | 90


You can also use the ```sweeper_dash``` function here.

## How to use it? 🚀

First, download the quantclean.py file in the folder where you are working

<u>Note :</u> I took this data from Quandl, your dataset doesn't have to look like this one necessarily, quantclean adapts to your dataset as well as possible

```
from quantclean import sweeper

df = pd.read_csv('AS-N100.csv')
df
```
<img src="https://i.ibb.co/zVfYx5J/Capture.jpg"/>

```
_df = sweeper(df)
_df
```
Output: 

<img src="https://i.ibb.co/YdncjPz/Capture.jpg"/>

Now, you may not be happy of this date colum which is presented in the YYYYMMDD format and maybe be prefer YYYY-MM-DD.

In that case do :

```
_df = sweeper_dash(df)
_df
```

Output: 

<img src = "https://i.ibb.co/LNd5Kb9/Capture.jpg"/>
