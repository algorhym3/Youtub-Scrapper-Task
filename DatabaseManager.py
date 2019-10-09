import sqlite3
from DataModel import Channel, Playlist, Video


class DatabaseManager:
    conn = ''
    c = ''

    def __init__(self):
        self.conn = sqlite3.connect('YoutubeScrapper.db')
        self.c = sqlite3.connect('YoutubeScrapper.db')
        self.create_tables()

    def __del__(self):
        self.conn.close()

    def create_tables(self):
        self.c.execute('CREATE TABLE IF NOT EXISTS channels(url,playlistUrl)')
        self.c.execute('CREATE TABLE IF NOT EXISTS playlists(url,channelUrl)')
        self.c.execute(
            'CREATE TABLE IF NOT EXISTS videos(videoUrl,title,duration,views,thumbnailUrl,fullImageUrl,playlistUrl)')
        print "tables Created"
        self.conn.commit()

    def get_channel_list(self):
        channelList = []
        self.c.execute('SELECT * FROM channels')
        for row in self.c.fetchall():
            channel = Channel(row[0], row[1])
            channelList.append(channel)
        return  channelList

    def insert_channel(self, channel):
        self.c.execute('INSERT INTO channels(url,playlistUrl) Values(?,?)', (channel.url, channel.playlistUrl))
        self.conn.commit()

    def get_playlists_list(self):
        playlistList = []
        self.c.execute('SELECT * FROM playlists')
        for row in self.c.fetchall():
            playlist = Playlist(row[0], row[1])
            playlistList.append(playlist)
        return playlistList

    def insert_playlist(self, playlist):
        self.c.execute('INSERT INTO playlists(url,channelUrl) Values(?,?)', (playlist.url, playlist.channelUrl))
        self.conn.commit()

    def get_videos_by_playlist(self, playlist):
        videoList = []
        self.c.execute('SELECT * FROM videos WHERE playlistUrl = {0}'.format(playlist.url))
        for row in self.c.fetchall():
            video = Video(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            videoList.append(video)
        return  videoList

    def get_videos_by_channel(self, channel):
        videoList = []
        self.c.execute('SELECT * FROM videos where playlistUrl = {0}'.format(channel.playlistUrl))
        for row in self.c.fetchall():
            video = Video(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            videoList.append(video)
        return videoList

    def insert_video(self, video):
        self.c.execute(
            'INSERT INTO videos(videoUrl,title,duration,views,thumbnailUrl,fullImageUrl,playlistUrl) Values(?,?,?,?,?,?,?)',
            (video.url, video.title, video.duration, video.views, video.thumbnailUrl, video.fullImageUrl,
             video.playlistUrl))
        self.conn.commit()
