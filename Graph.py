import matplotlib.pyplot as plt
import os.path
import json
import seaborn as sns
import pandas as pd

working_path = os.path.dirname(__file__)
df = pd.DataFrame(columns=[str(i) for i in range(1,13)])

monthly_dict = dict()
for month in ['0'+str(i) for i in range(1,10)]+['10','11','12']:
    with open(os.path.join(working_path,r'data\Comment_time_of_month\Comment_time_of_'+month+'_month.json'),encoding='utf-8') as f:
        time_dict = json.loads(f.read())
    comment_sum = sum([time_dict[index] for index in time_dict])
    monthly_dict[month] = comment_sum

comment_sum = sum([monthly_dict[index] for index in monthly_dict])
for index in monthly_dict:
    monthly_dict[index] /= comment_sum

fig = plt.figure()
plt.xlabel('Month')
plt.ylabel('Frequency')
plt.title('Comment Frequency by Month')
plt.xticks(range(12), df.columns)

data = pd.Series(monthly_dict)

data.plot(kind='bar')
data.plot(kind='line')

#sns.distplot()

plt.show()



"""
for year in ['0'+str(i) for i in range(1,10)]+['10','11','12']:
    with open(os.path.join(working_path,r'data\Comment_time_of_month\Comment_time_of_'+year+'_month.json'),encoding='utf-8') as f:
        time_dict = json.loads(f.read())
    comment_sum = sum([time_dict[index] for index in time_dict])
    for index in time_dict:
        time_dict[index] /= comment_sum
    df.loc[(year)]=pd.Series(time_dict)

fig = plt.figure()
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.title('Monthly Comment Frequency by Time')
plt.xticks(range(1,25), df.columns)

for index, row in df.iterrows():
    row.plot(kind='line')

plt.legend(frameon=True,title='Month')
plt.savefig(os.path.join(working_path,'figure.png'))
plt.show()

"""