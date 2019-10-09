class Channel:
    def __init__(self, url, playlistUrl):
        self.url = url
        self.playlistUrl = playlistUrl


class Playlist:
    def __init__(self,url,channelUrl):
        self.url = url
        self.channelUrl=channelUrl


class Video:
    def __init__(self, url, title, duration,views, thumbnailUrl, fullimageUrl, playlistUrl):
        self.url = url
        self.title = title
        self.duration = duration
        self.views = views
        self.thumbnailUrl = thumbnailUrl
        self.fullImageUrl = fullimageUrl
        self.playlistUrl = playlistUrl
