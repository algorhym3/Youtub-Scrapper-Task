# Youtube-Scrapper-Task
Flask application which recieves requests to download video details for youtube channels or playlists , there are two ways you can call the api , synchronously and asynchronously  , you would't want to wait an hour for an hour to download channel or playlists videos details, also whenever you insert a channel or a playlist periodically the application is going to crawl the urls and retrieve the requested Data .



# Architecture and Design choices
The application is based on three main components  **Flask Api , Celery Workers and sqlite3 Database** the reason behind using celery over cron or a simple while loop to keep tasks running periodically was the ability to asyncronously and in parallel as well user's request to retrieve video data or even downloading them will not be waited for , also it's much cleaner to enforce periodical processing using it ,using sqlite3 and flask were mainly for simplicities sake to avoid adding more complexity , however I have implemented a database class which would only interact with classes to be more like **orm** without using orm which I dont believe was the best approach , using sqlAlchemy would have been much better , Flask is very simple and was very easily integrated with celery.


# Main Libraries and components

-Pytube:- used it to fetch data for each video in a playlist

-Beautiful soup and Urllib2 :- used to to scrape the Youtube Channels and retrieve a playlist to process later

-Sqlite :- Simple database to save and retrieve data as a file without needing much work

-Celery :- Queue based workers which allows for the async functionality as well as repeating functionality periodically

-rabbitMQ :- server queue which is used by the celery library inorder to be able to organise taske


# installation and requirments
-python 2.7

-pytube 9.52

-flask

-bs4

-beautifulsoup

-urllib2

-celery installation and running celery worker

-rabbitMq server installation and running


# Usage

Step 1 :- install rabbitmq sudo apt -y ```install rabbitmq-server```

Step 2 :- run flask 

Step 3 :- run celery  ```celery -A tasks worker --loglevel=info```


# API Calls

**ASYNC CALLS**

* url : http://localhost:5000/ProcessPlaylistAsync
* request type : POST
* content/type : json 
* content : {"url" :"https://www.youtube.com/watch?v=ofnzHbGIE_4&list=RDofnzHbGIE_4&start_radio=1'}
* describtion : responsible starting async task to collect videos data from a playlist url

<br/>

* url : http://localhost:5000/ProcessChannelAsync
* request type : POST
* content/type : json 
* content : {"url" :"https://www.youtube.com/user/wwwChesscom'}
* describtion : responsible for starting async task to collect videos data from channel url

<br/>

**SYNCHRONOUS CALLS**
* url : http://localhost:5000/ProcessPlaylist
* request type : POST
* content/type : json 
* content : {"url" :"https://www.youtube.com/watch?v=ofnzHbGIE_4&list=RDofnzHbGIE_4&start_radio=1'}
* describtion : responsible starting a task to collect videos data from a playlist url

<br/>

* url : http://localhost:5000/ProcessChannelAsync
* request type : POST
* content/type : json 
* content : {"url" :"https://www.youtube.com/user/wwwChesscom'}
* describtion : responsible for starting async task to collect videos data

<br/>

* url : http://localhost:5000/GetVideoListProgressByPlaylist
* request type : GET
* queryString : http://localhost:5000/GetVideoListProgressByPlaylist?url=https://www.youtube.com/watch?v=3myEq6qC_mw&list=UU5kS0l76kC0xOzMPtOmSFGw
* describtion : retrieve playlist video details as json list

<br/>

* url : http://localhost:5000/GetVideoListProgressByChannel
* request type : GET
* queryString : http://localhost:5000/GetVideoListProgressByPlaylist?url=https://www.youtube.com/watch?v=3myEq6qC_mw&list=UU5kS0l76kC0xOzMPtOmSFGw
* describtion : retrieve playlist video details as json list from the channel videos


# Missing Work
- thumbnail and fullimage download not implemented
- celery workers need more testing on linux
- static values should be added to configurations instead
- Inconsistent naming in several areas

