import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import Processor
from Processor import indexer as ind

with open('/Users/laurent/Desktop/CS429Proj/src/Processor/alldocs.pickle', 'rb') as f:
    docs = pickle.load(f)

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

#Creates a tfidf vector for the query
def getQueryTFIDF(query):
    #Grab query from Flask here
    tfidfvectorizer = TfidfVectorizer(analyzer='word',stop_words= stopwords, use_idf=True)
    # convert th documents into a matrix
    tfidf_docs = tfidfvectorizer.fit_transform(docs)
    query_tfidf = tfidfvectorizer.transform([query])
    #print(query_tfidf)
    return query_tfidf

#given a query vector and a document vector calculates the cosine similarity
def getCosineSim(query_tfidf, docs_tf_idf):
    cosine_sim = ind.cosine_similarity(query_tfidf, docs_tf_idf)
    #print(cosine_sim)
    return cosine_sim




#IGNORE
#tfidfvectorizer = TfidfVectorizer(analyzer='word',stop_words= stopwords, use_idf=True)
    # convert th documents into a matrix
#tfidf_wm = tfidfvectorizer.fit_transform(docs)
#print(tfidf_wm)
#print(cosine_sim)

#tfidfvectorizer = TfidfVectorizer(analyzer='word',stop_words= stopwords, use_idf=True)
#    # convert th documents into a matrix
#tfidf_wm = tfidfvectorizer.fit_transform(docs)
#query_tfidf = tfidfvectorizer.transform([query])


#Grab query from Flask here
#query = "Hello From Wikipedia"

#tfidfvectorizer = TfidfVectorizer(analyzer='word',stop_words= stopwords, use_idf=True)
    # convert th documents into a matrix
#tfidf_wm = tfidfvectorizer.fit_transform(docs)
#query_tfidf = tfidfvectorizer.transform([query])

#print(tfidf_wm)
#print(query_tfidf)
#cosine_sim = cosine_similarity(query_tfidf, tfidf_wm)

#print(cosine_sim)
