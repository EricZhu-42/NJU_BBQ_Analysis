"""Module to predict comments of given information.

Developed by EricZhu-42 in June, 2019.
"""

import os
from pprint import pprint

import numpy as np

from Subject import load_commented_df, tokenize
from Vectorize import load_sentences, load_vectorizer

local_path = os.path.split(__file__)[0]
feature_path = os.path.join(local_path,r'models\TfifVectorizer.pkl')
matrix_path = os.path.join(local_path,r'models\Matrix.pkl')
sep_sentences_path = os.path.join(local_path,r'data\Words_from_content.txt')
df_path = os.path.join(local_path,r'models\df.pkl')

def predict(input_str:str):
    vectorizer = load_vectorizer(feature_path)
    sentences = load_sentences(matrix_path)
    df = load_commented_df(df_path)

    max_similarity = 0
    max_index = 0

    input_str = tokenize(input_str)
    input_vec = vectorizer.transform([input_str]).toarray()[0].T

    for index in range(0,sentences.shape[0]):
        dense_vec = sentences[index].todense()
        dot_value = np.dot(dense_vec,input_vec)
        if dot_value>max_similarity:
            max_index = index
            max_similarity = dot_value

    return df.iloc[max_index]

if __name__ == "__main__":
    s = "大家一般都怎么和室友说晚上别人睡觉以后敲键盘和鼠标声音太大呢，耳塞没有用，直接说吗？还是委婉暗示，真的被这个声音烦的不行。。。"
    df = predict(s)
    for item in df['commentlist']:
        pprint(item['content'])
