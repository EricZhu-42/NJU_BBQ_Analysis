import os
import numpy as np
import json
import pandas as pd
import jieba
import jieba.analyse
import pickle

import time, datetime

local_path = os.path.split(__file__)[0]
jieba.load_userdict(os.path.join(local_path,r"data\dict.txt"))
stop_words = set(line.strip() for line in open(os.path.join(local_path,r'depedencies\stopwords.txt'), encoding='utf-8'))
stop_words.update([' ','全','前','发表','图片','\n'])

#-----------------Initialize--------------------

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

def load_raw_data(file_name:str):
    """Load raw json data to DataFrame"""
    with open(os.path.join(local_path,file_name),encoding='utf-8') as f:
        raw_data = json.loads(f.read())
    pd_data = pd.DataFrame(raw_data).T
    return pd_data

def create_frequency_dict(sentences:list):
    """Create word frequency dict from list of sentences"""
    words_dict = dict()
    for sentence in sentences:
        key_words_list = jieba.analyse.extract_tags(sentence,topK=2)
        if key_words_list is not None:
            for word in key_words_list:
                words_dict[word] = words_dict.get(word,0) + 1
    stop_words = set(line.strip() for line in open(r'depedencies\stopwords.txt', encoding='utf-8'))
    p = sorted([(v,k) for k,v in words_dict.items()],reverse=True)[:300]
    content = dict()
    for item in p:
        times = item[0]
        word = item[1]
        is_word = False
        for ch in word:
            if u'\u4e00' <= ch <= u'\u9fff':
                is_word = True
                break
        if not is_word or (word in stop_words):
            continue
        content[word]=times
    BBQ_stopwords_list = ['发表','图片','问下']
    for item in BBQ_stopwords_list:
        try:
            content.pop(item)
        except:
            pass
    return content

def create_keywords_list(raw_data):
    """Get Keyword information from DataFrame"""
    df_data = load_raw_data(r'raw_data\NJU_BBQ.json')
    df_data['year']=list(map(get_year,df_data.index))

    for index,data in df_data.groupby('year'):
        sentences = data['content']
        content = create_frequency_dict(sentences)
        with open(os.path.join(local_path,"{}.json".format(index)),'w',encoding='utf-8') as f:
            f.write(json.dumps(content,indent=4,ensure_ascii=False))

def create_year_comment_time_data():
    """Get yearly comment time dict"""
    df_data = load_raw_data(r'raw_data\NJU_BBQ.json')
    df_data['year']=list(map(get_year,df_data.index))
    df_data['month']=list(map(get_month,df_data.index))

    for index,data in df_data.groupby('year'):
        year_time_list = list()
        commentlists = data['commentlist']
        for commentlist in commentlists:
            if len(commentlist)!=0:
                for comment in commentlist:
                    year_time_list.append(get_hour(str(comment["time"])))
        year_time_dict = dict()
        for i in set(year_time_list):
            year_time_dict[i] = year_time_list.count(i)
        with open(os.path.join(local_path,"Comment_time_of_{}.json".format(index)),'w',encoding='utf-8') as f:
            f.write(json.dumps(year_time_dict,indent=4,ensure_ascii=False))

def create_month_comment_time_data():
    """Get monthly comment time dict"""
    df_data = load_raw_data(r'raw_data\NJU_BBQ.json')
    df_data['year']=list(map(get_year,df_data.index))
    df_data['month']=list(map(get_month,df_data.index))

    for index,data in df_data.groupby('month'):
        year_time_list = list()
        commentlists = data['commentlist']
        for commentlist in commentlists:
            if len(commentlist)!=0:
                for comment in commentlist:
                    year_time_list.append(get_hour(str(comment["time"])))
        year_time_dict = dict()
        for i in set(year_time_list):
            year_time_dict[i] = year_time_list.count(i)
        with open(os.path.join(local_path,"Comment_time_of_{}_month.json".format(index)),'w',encoding='utf-8') as f:
            f.write(json.dumps(year_time_dict,indent=4,ensure_ascii=False))

def tokenize(string:str):
    words = list()
    if string!="":
        for word in jieba.cut(string):
            if word not in stop_words and not word.startswith('e'):
                    words.append(word)
    sep_sentence = str()
    if len(words)!=0:
        for word in words:
            sep_sentence += (word + ' ')
    sep_sentence += '\n'
    return sep_sentence

def create_words_list():
    """Get words list"""
    file_name = r"raw_data\NJU_BBQ.json"
    with open(os.path.join(local_path,file_name),encoding='utf-8') as f:
        raw_data = json.loads(f.read())
    data = dict()

    for index in raw_data:
        commentlist = raw_data[index].get('commentlist',None)
        if len(commentlist)!=0:
            data[index]=raw_data[index]

    series_list = list()
    sentences_list = list()

    for index in data:
        content = data[index]['content']
        sentence = tokenize(content)
        commentlist = data[index]['commentlist']
        new_series = [index,commentlist,sentence]
        series_list.append(new_series)
        sentences_list.append(sentence)
    df = pd.DataFrame(series_list,columns=['index','commentlist','words'])

    df_path = os.path.join(local_path,r'models\df.pkl')
    with open(df_path,'wb') as fw:
        pickle.dump(df,fw)
    with open(os.path.join(local_path,r'data\Words_from_content.txt'),'w',encoding='utf-8') as f:
        f.writelines(sentences_list)

def load_commented_df(df_pos):
    """Get comments DataFrame"""
    with open(df_pos,'rb') as fw:
        df = pickle.load(fw)
    return df
#-----------Main---------------------
if __name__ == "__main__":
    create_words_list()
