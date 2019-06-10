import matplotlib.pyplot as plt
import numpy as np
import json
import time
def get_time(time_str:str):
    """Get formated time from timestamp"""
    timeArray = time.localtime(eval(time_str))
    new_time = time.strftime("%Y%m%d%H%M%S", timeArray)
    return new_time

def get_year(time_str:str):
    """Get year from timestamp"""
    new_time = get_time(time_str)
    return new_time[0:4]

def get_month(time_str:str):
    """Get month from timestamp"""
    new_time = get_time(time_str)
    return new_time[4:6]

def get_hour(time_str:str):
    """Get hour from timestamp"""
    new_time = get_time(time_str)
    return new_time[8:10]

with open("data//6D_emotion.json",'r',encoding='utf-8') as f:
    mte=dict(json.load(f))

kwl=['焦虑','轻松','伤心','开心','生气','满意']
jl,qs,sx,kx,sq,my={},{},{},{},{},{}
hedic=[jl,qs,sx,kx,sq,my]
for i in range(len(kwl)):
    for k in mte.keys():
        h=get_hour(str(k))
        if h in hedic[i].keys():
            hedic[i][h].append(mte[k][i])
        else:
            hedic[i][h]=[mte[k][i]]
    hedic[i]=dict(sorted(hedic[i].items(), key=lambda e:e[0], reverse=False))
    hd={}
    for k in hedic[i].keys():
        hd[k]=np.mean(hedic[i][k])
    
    keys=[int(x) for x in hd.keys()]
    values=hd.values()
    plt.title=kwl[i]
    plt.plot(keys,values)
    plt.show()