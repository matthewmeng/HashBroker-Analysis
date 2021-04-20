import pandas as pd 

import  matplotlib.pyplot as plt 
from matplotlib import style 
import matplotlib as mpl 
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


df = pd.read_excel('HashchingBrokerData.xlsx',sheet_name='Sheet1',usecols="A,Z")

df['RegisterationDate'] = pd.to_datetime(df['RegisterationDate'])
# df['RegisterationDate'] = df['RegisterationDate'].astype('datetime64[ns]')

# df['Name'].groupby(df['RegisterationDate'].dt.to_period('M')).sum().plot(kind='bar')

s = df.resample('M', on ='RegisterationDate')['Name'].count()
print(s)


mpl.rc('figure',figsize(8,7))

mpl.__version__

ax = plt.subplot(111)

style.use('ggplot')

s.plot(lable="Broker Data")

plt.legend()

plt.show()
# print(df['RegisterationDate'])

# print(df.dtypes)