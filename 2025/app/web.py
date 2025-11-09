#!/usr/bin/env python3

from bottle import route, run, default_app
from paste import httpserver
from datetime import datetime
import subprocess

@route('/')
def time_app():
    time = subprocess.Popen(
        "date", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        ).communicate()[0]
    with open("/tmp/uloziste/zaznamy.txt", "a") as f:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{current_time}\n")
    return f"Aktualní datum a čas: {time.decode()}"

if __name__ == "__main__":
    application = default_app()
    httpserver.serve(application, host="0.0.0.0", port=8081)
