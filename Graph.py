"""Module to create graphs from processed data.

Developed by EricZhu-42 in June, 2019.
"""

import json
import os.path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

working_path = os.path.dirname(__file__)

def ini_df():
    return pd.DataFrame(columns=[str(i) for i in range(1,13)])

def create_monthly_graph(df):
    monthly_dict = dict()
    for month in ['0'+str(i) for i in range(1,10)]+['10','11','12']:
        with open(os.path.join(working_path,r'data\Comment_time_of_month\Comment_time_of_'+month+'_month.json'),encoding='utf-8') as f:
            time_dict = json.loads(f.read())
        comment_sum = sum([time_dict[index] for index in time_dict])
        monthly_dict[month] = comment_sum

    comment_sum = sum([monthly_dict[index] for index in monthly_dict])
    for index in monthly_dict:
        monthly_dict[index] /= comment_sum

    plt.figure()
    plt.xlabel('Month')
    plt.ylabel('Frequency')
    plt.title('Comment Frequency by Month')
    plt.xticks(range(12), df.columns)

    data = pd.Series(monthly_dict)

    data.plot(kind='bar')
    data.plot(kind='line')

    plt.show()



def create_yearly_Graph(df):
    for year in ['0'+str(i) for i in range(1,10)]+['10','11','12']:
        with open(os.path.join(working_path,r'data\Comment_time_of_month\Comment_time_of_'+year+'_month.json'),encoding='utf-8') as f:
            time_dict = json.loads(f.read())
        comment_sum = sum([time_dict[index] for index in time_dict])
        for index in time_dict:
            time_dict[index] /= comment_sum
        df.loc[(year)]=pd.Series(time_dict)

    plt.figure()
    plt.xlabel('Time')
    plt.ylabel('Frequency')
    plt.title('Monthly Comment Frequency by Time')
    plt.xticks(range(1,25), df.columns)

    for index, row in df.iterrows():
        row.plot(kind='line')

    plt.legend(frameon=True,title='Month')
    plt.savefig(os.path.join(working_path,'figure.png'))
    plt.show()
