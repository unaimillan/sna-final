#!/usr/bin/python

from flask import Flask, render_template
from redis import Redis

app = Flask(__name__)
redis = Redis(host="localhost", port=6379)


@app.route("/")
@app.route("/index")
def index():
    counter = redis.incr("counter")
    return render_template(
        "index.html",
        counter=counter
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True
    )
