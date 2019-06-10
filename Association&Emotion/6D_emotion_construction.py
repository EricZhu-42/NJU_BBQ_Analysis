

import matplotlib.pyplot as plt
import numpy as np
import json
import time
import gensim
model=gensim.models.word2vec.Word2Vec.load('models//w2v.model')
kwl=['焦虑','轻松','伤心','开心','生气','满意']
with open("data//bbq.json",encoding='utf-8') as f:
    bbq=dict(json.load(f))
mte={}
for k in bbq.keys():
    words=bbq[k]
    ev=[]
    for i in range(len(kwl)):
        m=0
        if(words!=''):
            wlist=words.split(' ')
            s=0
            count=0
            for w in wlist:
                if w in model:
                    count+=1
                    s+=model.similarity(w,kwl[i])
        if(count!=0):
            m=s/count
        ev.append(m)
    mte[k]=ev
with open("data//6D_emotion.json",'w',encoding='utf-8') as f:
    json.dump(mte,f)
    f.close()