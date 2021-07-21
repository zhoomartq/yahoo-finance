import time
import datetime
import pandas as pd

# PD
ticker = 'PD'
period1 = int(time.mktime(datetime.datetime(2019, 4, 11, 23, 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2021, 7, 21, 12, 59).timetuple()))
interval = '1d' # 1d, 1m

query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

df = pd.read_csv(query_string)
df.to_csv('Pd.csv')


# ZUO
ticker = 'ZUO'
period1 = int(time.mktime(datetime.datetime(2020, 7, 21, 23, 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2021, 7, 21, 12, 59).timetuple()))
interval = '1d' # 1d, 1m

query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

df = pd.read_csv(query_string)
df.to_csv('ZUO.csv')



# PINS
ticker = 'PINS'
period1 = int(time.mktime(datetime.datetime(2019, 4, 18, 23, 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2021, 7, 21, 12, 59).timetuple()))
interval = '1d' # 1d, 1m

query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

df = pd.read_csv(query_string)
df.to_csv('PINS.csv')



# ZM
ticker = 'ZM'
period1 = int(time.mktime(datetime.datetime(2019, 4, 18, 23, 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2021, 7, 21, 12, 59).timetuple()))
interval = '1d' # 1d, 1m

query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

df = pd.read_csv(query_string)
df.to_csv('ZM.csv')



# DOCU
ticker = 'DOCU'
period1 = int(time.mktime(datetime.datetime(2018, 4, 27, 23, 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2021, 7, 21, 12, 59).timetuple()))
interval = '1d' # 1d, 1m

query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

df = pd.read_csv(query_string)
df.to_csv('DOCU.csv')



# CLDR
ticker = 'CLDR'
period1 = int(time.mktime(datetime.datetime(2017, 4, 28, 23, 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2021, 7, 21, 12, 59).timetuple()))
interval = '1d' # 1d, 1m

query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

df = pd.read_csv(query_string)
df.to_csv('CLDR.csv')




# RUN
ticker = 'RUN'
period1 = int(time.mktime(datetime.datetime(2015, 8, 5, 23, 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2021, 7, 21, 12, 59).timetuple()))
interval = '1d' # 1d, 1m

query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

df = pd.read_csv(query_string)
df.to_csv('RUN.csv')
























