import gensim
import re
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud
import json
with open("raw_data//NJU_BBQ.json",'r',encoding='utf-8') as load_f:
    load_dict=json.load(load_f)
strs=[]


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
    if(s!=''):
        strs.append(' '.join(jieba.cut_for_search(s)))
with open("data//sentencesS.txt",'w',encoding='utf-8') as f:
    for s in strs:
        f.write(s+'\n')
    f.close()
ss=gensim.models.word2vec.Text8Corpus('data//sentencesS.txt')

model=gensim.models.Word2Vec()
model = gensim.models.Word2Vec(ss, min_count=5, size=100, workers=2, window=5, iter=10)
model.save("models//w2vS.model")  # 保存模型