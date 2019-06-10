import matplotlib.pyplot as plt
import json
import jieba
import re
import time
import numpy as np


with open("models//BosonNLP_sentiment_score.txt",'r',encoding='utf-8') as f:
    senlist=f.readlines()
sendict={}
for sen in senlist:
    sen=sen.strip()
    s=sen.split(' ')
    if len(s)==2:
        sendict[s[0]]=eval(s[1])
        

with open("raw_data//NJU_BBQ.json",'r',encoding='utf-8') as load_f:
    load_dict=json.load(load_f)
te={}
for k in load_dict.keys():
    s=load_dict[k]['content']
    s=s[1:-1]
    s=s.replace("\n","")
    
    if ('[em]' in s and '[/em]' in s):
        pattern=re.compile('(.*?)\[em\].*\[\/em\](.*)')
        m=pattern.match(s)
     
        s=''
      
        if(m!=None):
           for item in m.groups():
               s=s+item+'。'
               s=s[:-1]
    if('[em]' in s and '[/em' in s):
        pattern=re.compile('(.*?)\[em\].*\[\/em(.*)')
        m=pattern.match(s)
        s=''
      
        if(m!=None):
           for item in m.groups():
               s=s+item+'。'
               s=s[:-1]
    if('em]' in s and '[/em]' in s):
        pattern=re.compile('(.*?)em\].*\[\/em\](.*)')
        m=pattern.match(s)
        s=''
      
        if(m!=None):
           for item in m.groups():
               s=s+item+'。'
               s=s[:-1]
    if('em]' in s and '[/em' in s):
        pattern=re.compile('(.*?)em\].*\[\/em(.*)')
        m=pattern.match(s)
        s=''
      
        if(m!=None):
           for item in m.groups():
               s=s+item+'。'
               s=s[:-1]
    words=(' '.join(jieba.cut(s))).split(' ')
    scores=0
    count=0
    for w in words:
        if w in sendict.keys():
            scores+=sendict[w]
            count+=1
    if count!=0:
        te[eval(k)]=scores/count
    else:
        te[eval(k)]=0
te=sorted(te.items(), key=lambda e:e[0], reverse=False)
with open("data//emotion.json",'w',encoding='utf-8') as f:
    json.dump(te,f)