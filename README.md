# CS429Proj

**Abstract**

The goal was to build a basic search enginer using a crawler that grabs data online, passing it to an indexer that creates a tfidf and calculates cosine similarity and then uses that data to rank webpages. My objective was to be able to build all these 3 components correctly and make them work together such that a person can go on my flask server, provide a url, and query and my project would output ranked documents based on the query. I was a ble to get most things running however, there are a few kinks worth mentioning (which will be mentioned below).

**Overview**

From a user standpoint this is how the user would interact with the system. First they would run the app (app.py) on vscode and access the application via, localhost:5000. A user could go to the route /search and then input a query. This is an example query: http://localhost:5000/search?query=Hello+Wikipedia&url=https://en.wikipedia.org/wiki/Main_Page&k=3. And then the application would do it's magic and output a json that would contani 1. The query that user user input 2. A corrected query (since our application would do error checking on the query) 3. The K number that the user wanted and 4. The top K documents. 

Because All the user has to is to run the application in an IDE, then go to the localhost and write the query it would make the user experience as seemless as possible without the need of a frontend.


**Design**
By running app.py on vscode and providing a query similar to what was mentioned above, our application will crawl the web, create a tfidf for query and coument and provide a result in the form of json (top k ranked documents included in the result). All one needs to do is download this github repository and follow the steps metioned.

**Architecture
**

Folder Structture:
CS429Proj

  src
  
    Processor --> Since indexing, calculating cosine similarity, and grabbing the k_ranked documents are very related I grouped them in 1 package
    
      picklefiles --> all the relevant files that would possibly be pickled are store here since all of them are generated in the modules in this package
      
      indexer --> Module holds functions required for 1. Processing the json resulting from the scrapper and creating a tfidf of the documents
      
      ranker --> Module holes functions that 1. create a tfidf vector for the query and calculate cosine similarity between documents and query
      
      runner ---> Modules bings both the indexer and ranker module in addition to error checking the query (as it is called in app.py) to return our k_ranked documents
    
    Scrapper --> This package contains all the modules needed to run the crawler
    
      ...
      
        ...
        
          spiders
          
            projspider.py --> this modules holds all the functions required to run the scrapper
            
    App.py --> You run the whole application from here
    
  Read.me
  
**Operation**
Intallation: git clone: https://github.com/SimonUnlimited/CS429Proj.git
To start flask app: navigate to src dir + type: python3 app.py
To run query: go to: web browser & write query similar to and same as : http://localhost:5000/search?query=Hello+Wikipedia&url=https://en.wikipedia.org/wiki/Main_Page&k=3

Caveats: **IMPORTANT** mentioned in conclusion

Conclusion
Successes: 

  Part1: Was able to create a crawler, with a base url (that can be specified) and with a depth limit, and works for multiple websites 
  
  Part2: Provided documents, was able to write an indexer that successfully calculates tfidf and cosines 
  
  Part3: Was able wite functions that 1. sucessfully error check and return top k ranked documents in json format
  
Failures:
  Part 1: i) Although the cralwer works, I do not think I was able to fully figure out how to limit max pages as asked. 
     In the projspider.py in line 21: i commented out 'CLOSESPIDER_PAGECOUNT': MAX_PAGES in the settings which would close the spider the once the max pages have been achieved. However, I don't believe my output was as expected. I was not fully able to figure this out.
     i) if the crawler in run the terminal sometimes in would have errors in the json it store and if I ran it in a script I would definitely has errors (it is a minor error where for exampel between entries in the json we this: "[]" which would make it imporssible for my whole project to run properly. Therefore I used a good json output from the crwaler statically as I was working with the latter parts of the project.
  
  Part 2: In indexer.py and ranker.py I open a total of 3 files using an absolute path **I would recommend chaning this absolute path to represent the new (absolute path) location of the files once the project has been downloaded** 

Data Sources
sklearn: https://scikit-learn.org/stable/
pickle: https://docs.python.org/3/library/pickle.html
multiprocessing: https://docs.python.org/3/library/multiprocessing.html
scrapy: https://scrapy.org/
flask: https://flask.palletsprojects.com/en/2.1.x/

Test Cases
Project works for multiple websites, any query (that appears in the downloaded docs), 

Source Code
  Libraries used:
    sklearn, pickle, multiprocessing, json, scrapy, flask
  
  Intallation: git clone: https://github.com/SimonUnlimited/CS429Proj.git

Bibliography




