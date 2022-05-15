import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import math
from scipy.stats import variation
from pylab import rcParams
import statsmodels.api as sm
import os
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
warnings.filterwarnings('ignore')
sns.set_style('darkgrid')


def read_data(file_directory = None, resample_period = 'D', resample_aggregate = 'mean'):
    '''
    file_directory: str, directory of csv file to be read
    resample_period: str, 'H' for hours, 'D' for days
    resample_aggregate: list, will create a new column for each aggregate
    '''
    
    df = pd.read_csv(file_directory)
    df['ds'] = pd.to_datetime(df['ds'])
    df = df.set_index('ds')

    if resample_aggregate == 'mean':
        df = df.resample(resample_period).mean()
        

    if resample_aggregate == 'max':
        df = df.resample(resample_period).max()
       
        
    if resample_aggregate == 'min':
        df = df.resample(resample_period).min()
      
        
    if resample_aggregate == 'sum':
        df = df.resample(resample_period).sum()
        
        
    df = df.fillna(0)

    return df

def add_aggregate(df = None, resample_aggregate = None, resample_period = None):

    if resample_aggregate == 'mean':
        df2 = df.resample(resample_period).mean()

    if resample_aggregate == 'max':
        df2 = df.resample(resample_period).max()

    if resample_aggregate == 'min':
        df2 = df.resample(resample_period).min()

    if resample_aggregate == 'sum':
        df2 = df.resample(resample_period).sum()

    df = pd.merge(df, df2, left_index = True, right_index = True, suffixes = ("", f"_{resample_aggregate}"))

    return df



    # df_dict = {}

    # if 'mean' in resample_aggregates:

    #     df_mean = df.resample(resample_period).mean()
    #     df_dict['mean'] = ['mean', df_mean]

    # if 'sum' in  resample_aggregates:

    #     df_sum = df.resample(resample_period).sum()
    #     df_dict['sum'] = ['sum', df_sum]

    # if 'max' in resample_aggregates:

    #     df_max = df.resample(resample_period).max()
    #     df_dict['max'] = ['max', df_max]

    # if 'min' in resample_aggregates:

    #     df_min = df.resample(resample_period).min()
    #     df_dict['min'] = ['min', df_min]

    
    # reduce(lambda: df_dict.keys())
    
    
    # if len(df_dict) > 1:
    #     for i in df_dict:
    #         df = pd.merge(df, df_dict[i], 
    #         left_index = True, 
    #         right_index = True,
    #         suffixes = (f"_{i}", f"_{i}"))




    # return df

    #def sarimax_model()