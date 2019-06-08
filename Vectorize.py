from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pickle

import os



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


"""
max_similarity = 0
max_index = 0

input_str = "电话 心情 抱怨 印象 厉害 大一"
input_vec = vectorizer.transform([input_str]).toarray()[0].T


for index in range(0,len(sep_sentences)):
    dense_vec = X[index].todense()
    dot_value = np.dot(dense_vec,input_vec)
    if dot_value>max_similarity:
        max_index = index
        max_similarity = dot_value

print(sep_sentences[max_index])

#test = ['一点 信息']
#print(vectorizer.transform(test).toarray())
#print(vectorizer.get_feature_names())
"""