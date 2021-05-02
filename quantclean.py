import pandas as pd
from pandas_datareader import data as web
import logging

def sweeper(data):
  for name in logging.Logger.manager.loggerDict.keys():
    logging.getLogger(name).setLevel(logging.CRITICAL)

  #non efficient, right?
  data.columns = ['Open' if 'open' in x else 'Open' if 'OPEN' in x else x for x in data.columns]

  data.columns = ['High' if 'high' in x else 'High' if 'HIGH' in x else x for x in data.columns]

  data.columns = ['Low' if 'low' in x else 'Low' if 'LOW' in x else x for x in data.columns]

  data.columns = ['Close' if 'close' in x else 'Close' if 'CLOSE' in x else x for x in data.columns]

  data.columns = ['Volume' if 'volume' in x else 'Volume' if 'VOLUME' in x else x for x in data.columns]

  data.columns = ['Date' if 'date' in x else 'Date' if 'DATE' in x else x for x in data.columns]

  data.columns = ['Time' if 'time' in x else 'Time' if 'TIME' in x else x for x in data.columns]

  if 'Date' in data.columns and 'Time' in data.columns:
    data['Date'] = data['Date']+" "+data['Time']

  elif 'Time' in data.columns and not 'Date' in data.columns:
    data['Date'] = data['Time']

  elif 'Date' in data.columns and not 'Time' in data.columns:
    pass


  try:
    df = data[['Date','Open','High','Low', 'Close', 'Volume']]
    df.reset_index(drop=True, inplace=True)
    df['Date'] = df['Date'].astype(str)
    df['Date'] = df['Date'].str.replace(r'-|/', '')
    return df

  except KeyError:

    #non sense messages
    print('Oupsi...seems like someone has cast a spell on your dataset')

    print('Checking which column has been bewitched...')

    cols = ['Date','Open','High','Low', 'Close', 'Volume']

    for col in cols:
      if col not in data.columns:
        print(col + " is invisible")
        data[col] = ""

    print("The spell has been successfuly broken!")

    df = data[['Date','Open','High','Low', 'Close', 'Volume']]
    df.reset_index(drop=True, inplace=True)
    df['Date'] = df['Date'].astype(str)
    df['Date'] = df['Date'].str.replace(r'-|/', '')
    return df
