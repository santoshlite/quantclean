# Quantclean 🧹

A program that reformats every financial dataset to US Equity TradeBar (Quantconnect format)

## How to use it? 🚀

First, download the quantclean.py file in the folder where you are working

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
