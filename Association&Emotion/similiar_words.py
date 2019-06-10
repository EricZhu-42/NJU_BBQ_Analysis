import gensim
model=gensim.models.word2vec.Word2Vec.load('models//w2v.model')

words=['墙','npy','腻','鸭','蟹','小刀','qwq','军理','mdzz']
f=open('output//similiar_words.txt','w',encoding='utf-8')
for w in words:
    req_count = 20
    f.write('与\''+w+'\'最相似的'+str(req_count)+'个词及其相似度:\n')
    
    for key in model.similar_by_word(w, topn=req_count):
        
        if 0<len(key[0]) <6:
            req_count -= 1
            f.write('    '+key[0]+' '+str(key[1])+'\n')
            if req_count == 0:
                break     
    f.write('\n')
f.close()