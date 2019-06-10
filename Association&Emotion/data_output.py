import re
import jieba
import gensim
import json
import matplotlib.pyplot as plt
model = gensim.models.Word2Vec.load("models//w2v.model")

with open("raw_data//NJU_BBQ.json",'r',encoding='utf-8') as load_f:
    load_dict=json.load(load_f)
    
dic={}
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
    #words=(' '.join(jieba.cut(s)))
    dic[eval(k)]=s
with open("data//bbq.json","w",encoding='utf-8') as f:
    json.dump(dic,f)
f.close()