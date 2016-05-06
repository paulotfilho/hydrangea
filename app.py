from flask import Flask
from flask import render_template
import codecs
import markdown
import os
import datetime

app = Flask(__name__)

def fetch():
    basepath = 'posts'
    posts = []
    for filename in os.listdir(basepath):
        post = codecs.open(basepath + "/" + filename, mode="r", encoding="utf-8")
        posts.append({'date': datetime.datetime.fromtimestamp(os.path.getctime(basepath + "/" + filename)).strftime(format='%d.%m.%Y'), 'html': markdown.markdown(post.read())})
    return posts

@app.route("/")
def index():
    return render_template('index.html', posts=fetch())

if __name__ == "__main__":
    app.run()
