# CS429Proj

Abstract

The goal was to build a basic search enginer using a crawler that grabs data online, passing it to an indexer that creates a tfidf and calculates cosine similarity and then uses that data to rank webpages. My objective was to be able to build all these 3 components correctly and make them work together such that a person can go on my flask server, provide a url, and query and my project would output ranked documents based on the query. I was a ble to get most things running however, there are a few kinks worth mentioning (which will be mentioned below).

Overview

From a user standpoint this is how the user would interact with the system. First they would run the app (app.py) on vscode and access the application via, localhost:5000. A user could go to the route /search and then input a query. This is an example query: http://localhost:5000/search?query=Hello+Wikipedia&url=https://en.wikipedia.org/wiki/Main_Page&k=3. And then the application would do it's magic and output a json that would contani 1. The query that user user input 2. A corrected query (since our application would do error checking on the query) 3. The K number that the user wanted and 4. The top K documents.


Design

Architecture

Operation

Conclusion

Data Sources

Test Cases

Source Code

Bibliography




