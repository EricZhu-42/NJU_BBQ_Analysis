import pandas as pd
import os
local_path = os.path.split(__file__)[0]
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=['a','b','c'])

sentences_list = ['123\n','456\n','789 8778']

with open(os.path.join(local_path,r'test.txt'),'w',encoding='utf-8') as f:
    f.writelines(sentences_list)
