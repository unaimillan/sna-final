#!/usr/bin/python

from flask import Flask, render_template
from redis import Redis
from socket import gethostname

app = Flask(__name__)
redis = Redis(host="10.0.0.14", port=6379, socket_connect_timeout=30)


@app.route("/")
@app.route("/index")
def index():
    counter = redis.incr("counter")
    return render_template(
        "index.html",
        counter=counter,
        hostname=gethostname()
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True
    )
