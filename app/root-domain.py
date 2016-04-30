from flask import Flask, redirect
import os

app = Flask(__name__)

domain = os.environ['WWW_DOMAIN']


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return redirect(domain + path, code=301)


if __name__ == '__main__':
    app.run()
