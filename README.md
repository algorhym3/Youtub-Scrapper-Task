# Youtube-Scrapper-Task
Flask application which recieves requests to download video details for youtube channels or playlists , there are two ways you can call the api , synchronously and asynchronously  , you would't want to wait an hour for an hour to download channel or playlists videos details, also whenever you insert a channel or a playlist periodically the application is going to crawl the urls and retrieve the requested Data .


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
