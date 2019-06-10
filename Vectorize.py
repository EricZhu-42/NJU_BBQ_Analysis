"""Module to vectorize text and save vectorizer.

Developed by EricZhu-42 in June, 2019.
"""

import os
import pickle

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

local_path = os.path.split(__file__)[0]
feature_path = os.path.join(local_path,r'models\TfifVectorizer.pkl')
matrix_path = os.path.join(local_path,r'models\Matrix.pkl')
sep_sentences_path = os.path.join(local_path,r'data\Words_from_content.txt')
max_features_num = 4000

def save_model(sep_sentences_pos:str):

    with open(sep_sentences_pos,'r',encoding='utf-8') as f:
        sep_sentences = f.readlines()

    vectorizer = TfidfVectorizer(max_features=max_features_num)
    vectorizer.fit(sep_sentences)
    X = vectorizer.transform(sep_sentences)
    print(X.toarray())
    print(vectorizer.get_feature_names())

    with open(feature_path,'wb') as fw:
        pickle.dump(vectorizer,fw)
    with open(matrix_path,'wb') as fw:
        pickle.dump(X,fw)

def load_vectorizer(feature_pos:str):
    with open(feature_pos,'rb') as fw:
        vectorizer = pickle.load(fw)
    return vectorizer

def load_sentences(matrix_pos:str):
    with open(matrix_pos,'rb') as fw:
        sentences = pickle.load(fw)
    return sentences

if __name__ == "__main__":
    save_model(sep_sentences_path)


