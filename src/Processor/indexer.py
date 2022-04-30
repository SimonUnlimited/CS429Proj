import pickle, numpy, sklearn, re, json
import pandas as pd

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

colnames = {}
stopwords = ['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am',
'an', 'and', 'any', 'are', 'aren\'t', 'as', 'at', 'be', 'because', 'been', 'before', 
'being', 'below', 'between', 'both', 'but', 'by', 'can\'t', 'cannot', 'could', 'couldn\'t', 
'did', 'didn\'t', 'do', 'does', 'doesn\'t', 'doing', 'don\'t', 'down', 'during', 'each', 'few', 
'for', 'from', 'further', 'had', 'hadn\'t', 'has', 'hasn\'t', 'have', 'haven\'t', 'having', 'he', 
'he\'d', 'he\'ll', 'he\'s', 'her', 'here', 'here\'s', 'hers', 'herself', 'him', 'himself', 'his', 
'how', 'how\'s', 'i', 'i\'d', 'i\'ll', 'i\'m', 'i\'ve', 'if', 'in', 'into', 'is', 'isn\'t', 
'it', 'it\'s', 'its', 'itself', 'let\'s', 'me', 'more', 'most', 'mustn\'t', 'my', 'myself', 'no', 
'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours',
'ourselves', 'out', 'over', 'own', 'same', 'shan\'t', 'she', 'she\'d', 'she\'ll', 'she\'s', 
'should', 'shouldn\'t', 'so', 'some', 'such', 'than', 'that', 'that\'s', 'the', 'their', 
'theirs', 'them', 'themselves', 'then', 'there', 'there\'s', 'these', 'they', 'they\'d', 'they\'ll', 
'they\'re', 'they\'ve', 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', 
'wasn\'t', 'we', 'we\'d', 'we\'ll', 'we\'re', 'we\'ve', 'were', 'weren\'t', 'what', 'what\'s', 'when', 
'when\'s', 'where', 'where\'s', 'which', 'while', 'who', 'who\'s', 'whom', 'why', 'why\'s', 'with', 
'won\'t', 'would', 'wouldn\'t', 'you', 'you\'d', 'you\'ll', 'you\'re', 'you\'ve', 'your', 'yours', 'yourself', 'yourselves']

d_t_m = None
colnames = {}
tfidfvectorizer = None

#Grabs the data that the crawler store in wikibody (bad naming i know) 
# processes the documents such that each document 
#Stores them in a pickle file
def preProcessDocs():
    file = open('/Users/laurent/Desktop/CS429Proj/src/scrapper/scrapper/spiders/wikibody.json')
    data = json.load(file)
    documents = []
    for docs in data:
        doc = docs['body']
        doc = re.sub('[^A-Za-z]+', ' ', doc)
        documents.append(doc)

    with open('/Users/laurent/Desktop/CS429Proj/src/Processor/alldocs.pickle', 'wb') as f:
        pickle.dump(documents, f)
    return documents

#Abstraction of the sklear TfidfVectorizer function
def vectorize ():
    vectorizer = TfidfVectorizer(analyzer='word',stop_words= stopwords, use_idf=True)
    return vectorizer

#Given a document corpus will create tfidf vector for them
def tf_idf (docs):
    global colnames
    global tfidfvectorizer
    # convert the documents into a matrix
    tfidfvectorizer = TfidfVectorizer(analyzer='word',stop_words= stopwords, use_idf=True)
    tfidf_docs = tfidfvectorizer.fit_transform(docs)

    tfidf_tokens = tfidfvectorizer.get_feature_names()
    df_tfidfvect = pd.DataFrame(data = tfidf_docs.toarray(),columns = tfidf_tokens)
    print('\nTD-IDF Vectorizer\n')
    colnames = {c: i for i, c in enumerate(df_tfidfvect.columns)}
    print("Done with tf idf")
    return tfidf_docs

#later on I will use this when doing the cosine similarity since all i get back is an array
def getColNames():
    return colnames





# IGNORE

    #tfIdfVectorizer=TfidfVectorizer(use_idf=True)
    #tfIdf = tfIdfVectorizer.fit_transform(documents)
    #df = pd.DataFrame(tfIdf[0].T.todense(), index=tfIdfVectorizer.get_feature_names(), columns=['TF-IDF'])
    #df = df.sort_values('TF-IDF', ascending=False)
    #print (df.head(100))

    ## Try to remove english words later?
    ## Implement cosine similarity later with query?
#def cosine_sim (doc_tf_idf, query):
#    query_tfidf = tfidfvectorizer.transform([query])
#    cos_sim = cosine_similarity(doc_tf_idf, query_tfidf)
#    return cos_sim
#def index ():
#    d_t_m = tf_idf(documents)
#    d_t_m = d_t_m.transpose()

    #retrieve the terms found in the corpora
    # if we take same parameters on both Classes(CountVectorizer and TfidfVectorizer) , it will give same output of get_feature_names() methods)
    #count_tokens = tfidfvectorizer.get_feature_names() # no difference
    #print(tfidf_wm)

    #df_tfidfvect = df_tfidfvect.transpose()

