from flask import Flask, request, jsonify, json
import requests, subprocess, subprocess, Processor.indexer as ind, Processor.runner as runner
import scrapper.scrapper.spiders.projspider as ps
import subprocess

app = Flask(__name__)
@app.route('/', methods = ['POST', 'GET'])

def index():
    return "Hellow World"

@app.route('/search', methods=['GET', 'POST'])
def search():
    #grab arguments
    args = request.args
    query = args['query']
    url = args['url']
    k = args['k']

    #change our spiderstarturl
    ps.spider.start_urls = [url]

    #run crawler
    ps.runSpider()

    
    #gets k docuements ranked based on cosine similarity
    ranker_res = runner.runRanker(query, k)
    k_ranked_docs = ranker_res[0]
    corrected_query = ranker_res[1]

    return_value = {
        "Query after error check": corrected_query,
        "Query": query,
        "K" : k,
        "Top K documents": k_ranked_docs,
    }
    return json.dumps(return_value)

if __name__ == "__main__":
    app.run(debug=True)

