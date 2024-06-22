from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    submitted_link = None
    if request.method == 'POST':
        submitted_link = request.form.get('link')
        submitted_link += "123"
    return render_template('index.html', link=submitted_link)

