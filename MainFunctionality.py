from pytube import YouTube
from pytube import Playlist as pyTubePlaylist
from DataModel import Channel, Video, Playlist
from DatabaseManager import DatabaseManager
from bs4 import BeautifulSoup
import ssl
import urllib2


def save_video_list_by_playlist(playlist):
    pytplaylist = pyTubePlaylist(playlist.url)
    pytplaylist.populate_video_urls()
    videos = []
    for videoUrl in pytplaylist.video_urls:
        try:
            CurrentVideo = YouTube(videoUrl)
        except:
            print "Error parsing videoUrl:- {0}", videoUrl
        try:
            url = videoUrl
            title = CurrentVideo.title
            duration = CurrentVideo.length
            views = CurrentVideo.views
            thumbnailUrl = CurrentVideo.thumbnail_url
            fullimageUrl = thumbnailUrl
            playlistUrl = playlist.url
            video = Video(url, title, duration, views, thumbnailUrl, fullimageUrl, playlistUrl)
            videos.append(video)
        except:
            print "Error occured Extracting Data videoUrl :- {0}", videoUrl
    db = DatabaseManager()
    for vid in videos:
        try:
            db.insert_video(vid)
        except:
            print "Error occurred inserting video to db , VideoUrl :-{0}", videoUrl
        db.insert_playlist(playlist)


def extract_playlist_url_from_channel(channel):
    req = urllib2.Request(channel.url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib2.urlopen(req)
    webpage = response.read()

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    soup = BeautifulSoup(webpage, 'html.parser')
    html = soup.prettify('utf-8')
    playlist_link = soup.findAll('a', {'class': 'play-all-icon-btn'})[0]['href']
    youtube_playlist_link = 'https://youtube.com' + playlist_link
    playlist_to_save = Playlist(youtube_playlist_link, channel.url)
    channel_to_save = Channel(channel.url,youtube_playlist_link)
    db= DatabaseManager()
    db.insert_playlist(playlist_to_save)
    db.insert_channel(channel_to_save)
    return youtube_playlist_link


def save_video_list_by_channel(channel):
    playlist_url = extract_playlist_url_from_channel(channel)
    playlist = Playlist(playlist_url, channel.url)
    save_video_list_by_playlist(playlist)


def get_video_list_by_channel(channel):
    db = DatabaseManager()
    videos_list = db.get_videos_by_channel(channel)
    return videos_list


def get_video_list_by_playlist(playlist):
    db = DatabaseManager()
    videos_list = db.get_videos_by_playlist(playlist)
    return videos_list
