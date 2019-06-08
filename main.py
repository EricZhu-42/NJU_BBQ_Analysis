import os.path
import pandas as pd
import json

local_path = os.path.split(__file__)[0]

with open(os.path.join(local_path,r"NJU_BBQ.json"),'r',encoding='utf-8') as f:
    data = json.loads(f.read())

pd_data = pd.DataFrame(data)

print(pd_data)