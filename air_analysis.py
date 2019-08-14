
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df_2016 = pd.read_csv("./Lima_PM2.5_2016_YTD.csv")
df_2017 = pd.read_csv("./Lima_PM2.5_2017_YTD.csv")
df_2018 = pd.read_csv("./Lima_PM2.5_2018_YTD.csv")
df_2019 = pd.read_csv("./Lima_PM2.5_2019_YTD.csv")

df_2016.dropna(inplace=True)
df_2017.dropna(inplace=True)
df_2018.dropna(inplace=True)
df_2019.dropna(inplace=True)

df_2016['Time'] = pd.to_datetime(df_2016['Date (LT)'])
df_2017['Time'] = pd.to_datetime(df_2017['Date (LT)'])
df_2018['Time'] = pd.to_datetime(df_2018['Date (LT)'])
df_2019['Time'] = pd.to_datetime(df_2019['Date (LT)'])

df_2016 = df_2016[['Hour', 'Month', 'AQI']]
df_2017 = df_2017[['Hour', 'Month', 'AQI']]
df_2018 = df_2018[['Hour', 'Month', 'AQI']]
df_2019 = df_2019[['Hour', 'Month', 'AQI']]

dfs = {2016: df_2016, 2017: df_2017, 2018: df_2018, 2019: df_2019}

for year in dfs.keys():

    df = dfs[year]
    boxplot = df.boxplot(column=['AQI'], by='Hour')
    plt.savefig('Boxplots Year ' + str(year) + ' Overall')
    plt.clf()

    for ii in df['Month'].unique():
        df_list = list()
        for jj in range(24): # 24 hours per day
            df_list.append(df.loc[(df['Month'] == ii) & (df['Hour'] == jj)])
        fg, ax = plt.subplots()
        ax.hist([df_list[kk]['AQI'] for kk in range(24)])
        plt.tight_layout()
        plt.savefig('Histograms Year ' + str(year) + ' Month ' + str(ii))
        plt.clf()

    for ii in df['Month'].unique():
        df_tmp = df.loc[df['Month'] == ii]
        try:
            boxplot = df_tmp.boxplot(column=['AQI'], by='Hour')
        except:
            pass
        plt.savefig('Boxplots Year ' + str(year) + ' Month ' + str(ii))
        plt.clf()
