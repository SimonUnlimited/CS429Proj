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

  Part1: Was able to create a crawler, with a base url (that can be specified) and with a depth limit, 
  
  Part2: Provided documents, was able to write an indexer that successfully calculates tfidf and cosines 
  
  Part3: Was able wite functions that 1. sucessfully error check and return top k ranked documents in json format

Data Sources

Test Cases

Source Code

Bibliography




