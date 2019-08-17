
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def boxplot_by_value(df, split_by, year):

    for x in df[split_by].unique():
        df_tmp = df.loc[df[split_by] == x]
        try:
            boxplot = df_tmp.boxplot(column=['AQI'], by='Hour')
        except:
            pass
        plt.savefig('Boxplots Year ' + str(year) + ' '+ split_by + ' ' + str(x))
        plt.clf()


if __name__ == "__main__":

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

    df_2016['WeekDay'] = df_2016.Time.dt.dayofweek
    df_2017['WeekDay'] = df_2017.Time.dt.dayofweek
    df_2018['WeekDay'] = df_2018.Time.dt.dayofweek
    df_2019['WeekDay'] = df_2019.Time.dt.dayofweek

    dfs = {2016: df_2016, 2017: df_2017, 2018: df_2018, 2019: df_2019}

    for year in dfs.keys():

        df = dfs[year]
        boxplot = df.boxplot(column=['AQI'], by='Hour')
        plt.savefig('Boxplots Year ' + str(year) + ' Overall')
        plt.clf()

        # for ii in df['Month'].unique():
            # df_list = list()
            # for jj in range(24): # 24 hours per day
                # df_list.append(df.loc[(df['Month'] == ii) & (df['Hour'] == jj)])
            # fg, ax = plt.subplots()
            # ax.hist([df_list[kk]['AQI'] for kk in range(24)])
            # plt.tight_layout()
            # plt.savefig('Histograms Year ' + str(year) + ' Month ' + str(ii))
            # plt.clf()

        boxplot_by_value(df, split_by='Month', year=year)
        boxplot_by_value(df, split_by='WeekDay', year=year)

        df_summer = df.loc[(df['Month'] < 5) | (df['Month'] > 9)]
        df_winter = df.loc[(df['Month'] > 4) & (df['Month'] < 10)]

        time_period =  'winter' + str(year)
        boxplot_by_value(df_winter, split_by='WeekDay', year=time_period)
        time_period =  'summer' + str(year)
        boxplot_by_value(df_summer, split_by='WeekDay', year=time_period)
