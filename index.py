import datetime as dt
import pandas as pd
from dateutil import relativedelta as rd
import numpy as np

class IndexModel:
    def __init__(self) -> None:
        pass


    def calc_index_level(self, start_date: dt.date, end_date: dt.date) -> None:
        # To be implemented
        global df_final
        df=pd.read_csv('stock_prices.csv')
        df['Date']=list(map(lambda x: dt.datetime.strptime(x, '%d/%m/%Y'),df.Date))
        df.set_index('Date',drop=True,inplace=True)
        df=df.loc[:end_date,:]
        index_start_date=pd.Timestamp(2020, 1, 1)
        index_start_value=100
        index_divisor=100
        df_final=pd.DataFrame(columns=['IndexValue'],index=df.index)
        for i in df.index:
            if i<index_start_date:
                continue
            
            if i==index_start_date:
                print(i)
                port_date=index_start_date-dt.timedelta(days=1)
                portfolio_list=df.loc[port_date].sort_values(ascending=False)[0:3].index
                Shares=((index_start_value*index_divisor)/df.loc[index_start_date][portfolio_list]*[0.5,0.25,0.25])
                df_final.loc[i,'IndexValue']=100
            
            elif i.day==2:
                port_date= i - rd.relativedelta(months=1) -rd.relativedelta(day=31)
                date_finder=True
                while date_finder:
                    try:
                        df.loc[port_date]
                        date_finder=False
                    except:
                        port_date= port_date - dt.timedelta(days=1)
                portfolio_list=df.loc[port_date].sort_values(ascending=False)[0:3].index
                index_value_prev=df_final.loc[port_date]['IndexValue']
                if i==pd.Timestamp(2020, 1, 2):
                    prices=df.loc[i][portfolio_list]
                    Shares=((index_start_value*index_divisor)/df.loc[index_start_date][portfolio_list]*[0.5,0.25,0.25])
                    df.loc[i][portfolio_list]
                    Index_value=(prices*Shares).sum()/100
                    df_final.loc[i,'IndexValue']=round(Index_value,2)
                    continue
                
                Shares=((index_value_prev*index_divisor)/df.loc[port_date][portfolio_list]*[0.5,0.25,0.25])
                prices=df.loc[i][portfolio_list]
                Index_value=(prices*Shares).sum()/100
                df_final.loc[i,'IndexValue']=round(Index_value,2)
            elif i.day==3:
                port_date= i - rd.relativedelta(months=1) -rd.relativedelta(day=31)
                date_finder=True
                while date_finder:
                    try:
                        df.loc[port_date]
                        date_finder=False
                    except:
                        port_date= port_date - dt.timedelta(days=1)
                portfolio_list=df.loc[port_date].sort_values(ascending=False)[0:3].index
                index_value_prev=df_final.loc[port_date]['IndexValue']
                if i==pd.Timestamp(2020, 1, 3):
                    prices=df.loc[i][portfolio_list]
                    Shares=((index_start_value*index_divisor)/df.loc[index_start_date][portfolio_list]*[0.5,0.25,0.25])
                    df.loc[i][portfolio_list]
                    Index_value=(prices*Shares).sum()/100
                    df_final.loc[i,'IndexValue']=round(Index_value,2)
                    continue
                Shares=((index_value_prev*index_divisor)/df.loc[port_date][portfolio_list]*[0.5,0.25,0.25])
                prices=df.loc[i][portfolio_list]
                Index_value=(prices*Shares).sum()/100
                df_final.loc[i,'IndexValue']=round(Index_value,2)
                
            else:
                portfolio_list=df.loc[port_date].sort_values(ascending=False)[0:3].index
                index_value_prev=df_final.iloc[np.where(df_final.index==i)[0][0]-1].values[0]
                prices=df.loc[i][portfolio_list]
                Index_value=(prices*Shares).sum()/100
                df_final.loc[i,'IndexValue']=round(Index_value,2)
        df_final.dropna(subset=['IndexValue'],inplace=True)
        return df_final
        #df_final.IndexValue=df_final.IndexValue.apply(lambda x: round(x,2))

    def export_values(self, file_name: str) -> None:
        # To be implemented
        df_final.to_csv(file_name)
        pass
