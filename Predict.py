import numpy as np
import os
from Vectorize import load_vectorizer, load_sentences
from Subject import load_commented_df, tokenize
from pprint import pprint

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
    #s = "都过去好久了 还是会偶尔想起你" --- "一厢情愿是没有好结果的→_→"
    #s = "大家一般都怎么和室友说晚上别人睡觉以后敲键盘和鼠标声音太大呢，耳塞没有用，直接说吗？还是委婉暗示，真的被这个声音烦的不行。。。" --- '直接客气一点说啊，一般正常舍友都会理解你的[em]e249[/em]' '睡得跟死猪一样的我可能无法感受到'
    #s = "墙墙 最近校园网是出什么问题了吗 在宿舍装的wifi连校园网就一直卡在登录界面进不去 大家也有这个问题吗" --- '挺正常的。。' '换备用线路_(´ཀ`」 ∠)_' '换线路。我试过' '就今天不行...' '网页都打不开[em]e400824[/em]' '昨天也打不开'
    df = predict(s)
    for item in df['commentlist']:
        pprint(item['content'])