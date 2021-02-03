
import nltk
#循环10次，从cfdist中取当前单词最大概率的连词，并打印出来
def generate_model(cfdist,word,num=10):
    for i in range(num):
        print(word,end=' ')
        word =cfdist[word].max()

#加载预料库
text=nltk.corpus.genesis.words('english-kjv.txt')

#生成双连词
bigrams=nltk.bigrams(text)

#生成条件频率分布
cfd=nltk.ConditionalFreqDist(bigrams)
#以the开头，生成随机串
generate_model(cfd,'the')

