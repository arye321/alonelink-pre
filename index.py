from flask import Flask, render_template, request
import yt_dlp
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    streamlink = ""
    submitted_link = None
    if request.method == 'POST':
        submitted_link = request.form.get('link')
        submitted_link
        ydl_opts = {}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(submitted_link, download=False)
            streamlink = ydl.sanitize_info(info)['formats'][0]['manifest_url']
            if ",en_commentary" in streamlink:
                streamlink= streamlink.replace(',en_commentary','')
    return render_template('index.html', link=streamlink)

