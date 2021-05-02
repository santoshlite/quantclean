# Quantclean 🧹

A program that **reformats** every financial dataset to **US Equity TradeBar** (Quantconnect format)

## How to use it? 🚀

First, download the quantclean.py file in the folder where you are working

Note : I took this data from Quandl, your dataset doesn't have to look like this one necessarily, quantclean adapts to your dataset as well as possible

```
from quantclean import sweeps

df = pd.read_csv('AS-N100.csv')
df
```
<img src="https://i.ibb.co/zVfYx5J/Capture.jpg"/>

```
_df = sweeps(df)
_df
```
<img src="https://i.ibb.co/YdncjPz/Capture.jpg"/>
