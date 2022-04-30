import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import Levenshtein as lev

import Processor
from Processor import indexer as ind
from Processor import ranker as rank

#Runs all the necessary functions from index and rank to be able get cosine similarity
def runRanker(query, k):
    #grab documents
    docs = ind.preProcessDocs()

    #create tfidf for docs
    docs_tf_idf = ind.tf_idf(docs)

    #keeps track of column/term names and their indexes
    colnames = ind.getColNames()

    #corrects the query if necessary
    corrected_query = []
    querry_arr = query.split(" ")
    for qt in querry_arr:
        spell_correction = errorCheck(qt, docs)
        corrected_query.append(spell_correction)

    corrected_query = ' '.join(corrected_query)

    #generates the query tfidf
    query_tf_idf = rank.getQueryTFIDF(query)
    
    #calcuate cosine similarity of docs and query
    cosine_sim = cosine_similarity(query_tf_idf, docs_tf_idf)
    cosine_sim_list = list(cosine_sim)
    cosine_sim_list = cosine_sim_list[0]
    
    #sort the documents by putting documents of highest cosine similarity first
    docs_cosine_sim = []
    for i, val in enumerate(cosine_sim_list):
        docs_cosine_sim.append([i, val])
    docs_cosine_sim = sorted(docs_cosine_sim, key=lambda x : x[1], reverse=True)

    #Retives the actual document content from the docs array since cosine similarity calculation only returns the document index
    results = []
    count = 0
    for cossim in docs_cosine_sim:
        if count < int(k):
            for i in range(len(docs)):
                if cossim[0] == i:
                    results.append(docs[i])
            count+=1
    print(len(results)) #should be equal to k
    return [results, corrected_query]

#calculates edit distance of strings
def edit_distance(s1, s2):
    n = len(s1)
    m = len(s2)

    matrix = [[i+j for j in range(m+1)] for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                d = 0
            else:
                d = 1

            matrix[i][j] = min(matrix[i-1][j]+1, matrix[i][j-1]+1, matrix[i-1][j-1]+d)

    distance_score = matrix[n][m]
   
    return distance_score

#does error checking of the query using the term corpus
def errorCheck(query, docs):
    doc_array = [x.split(" ") for x in docs]
    closest_match = []
    for doc in doc_array:
        for term in doc:
            distance = edit_distance(query, term)
            if len(closest_match) == 0:
                closest_match = [distance, term]
            else:
                if distance < closest_match[0]:
                    closest_match = [distance, term]
    
    return closest_match[1]



    










