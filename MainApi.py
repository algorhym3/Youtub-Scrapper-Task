from flask import Flask, request, jsonify
from MainFunctionality import save_video_list_by_playlist, save_video_list_by_channel, get_video_list_by_channel, \
    get_video_list_by_playlist
from DataModel import Playlist, Channel
from celery_tasks import make_celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqp://localhost//'
celery = make_celery(app)


@celery.task(name='celery_worker.insertPlaylist')
def insert_playlist_async(url):
    try:
        playlist = Playlist(url, '')
        save_video_list_by_playlist(playlist)
    except:
        return "500"
    return "200"


@celery.task(name='celery_worker.insertChannel')
def insert_channel_async(url):
    try:
        channel = Channel(url, '')
        save_video_list_by_channel(channel)
    except:
        return "500"
    return "200"


@app.route('/ProcessPlaylistAsync', methods=['POST'])
def insert_playlist_celery():
    url = request.json['url']
    try:
        insert_playlist_async.delay(url)
    except:
        "500"
    return "200"

@app.route('/ProcessPlaylist', methods=['POST'])
def insert_playlist():
    try:
        url = request.json['url']
        playlist = Playlist(url, '')
        save_video_list_by_playlist(playlist)
    except:
        return "500"
    return "200"


@app.route('/ProcessChannelAsync', methods=['POST'])
def insert_channel_celery():
    url = request.json['url']
    try:
        insert_channel_async.delay(url)
    except:
        "500"
    return "200"

@app.route('/ProcessChannel', methods=['POST'])
def insert_channel():
    try:
        url = request.json['channelUrl']
        channel = Channel(url, '')
        save_video_list_by_channel(channel)
    except:
        return "500"
    return "200"


@app.route('/GetVideoListProgressByChannel')
def get_videos_by_channel():
    url = request.args.get('url')
    channel = Channel(url, '')
    video_list = get_video_list_by_channel(channel)
    json_result = jsonify(video_list)
    if video_list.count() == 0:
        return 'Data is still being fetched'
    else:
        return json_result


if __name__ == '__main__':
    app.run(debug=True)
