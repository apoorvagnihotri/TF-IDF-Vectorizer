# Credits: https://www.commonlounge.com/discussion/99e86c9c15bb4d23a30b111b23e7b7b1

from sklearn.feature_extraction.text import TfidfVectorizer
import operator

def TFIDFtrain(file_name):
    # print(file_name)
    fd = open(file_name, 'r')
    corpus = fd.readlines()
    fd.close()
     
    vocabulary = set()
    for doc in corpus:
        vocabulary.update(doc.split())
     
    vocabulary = list(vocabulary)
    word_index = {w: idx for idx, w in enumerate(vocabulary)}
     
    tfidf = TfidfVectorizer(vocabulary=vocabulary)
     
    # Fit the TfIdf model
    tfidf.fit(corpus)
    tfidf.transform(corpus)
    return tfidf

def get_vector(sentence, tfidf):
    score={}
    text = ''
    # Transform a document into TfIdf coordinates
    X = tfidf.transform([sentence])
    print ('X: ', X)
    for word in sentence.split():
        try:
            score[word] = X[0, tfidf.vocabulary_[word]]
        except KeyError:
            score[word] = 0
    sortedscore = sorted(score.items(), key=operator.itemgetter(1), reverse=True)
    text += str(sortedscore)
    return text