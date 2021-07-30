from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from flask import Flask, escape, request
from checkprj import checkprj
from pywebio.platform.flask import webio_view

flask_app = Flask(__name__)

wsgi_app=flask_app.wsgi_app

# flask_app.wsgi_app= checkprj(flask_app.wsgi_app)

@flask_app.route("/")
def flask_main():
    name = request.args.get("name", "World")
    return f"Hi, {escape(name)}, please navigate to /tool to use the app."

flask_app.add_url_rule('/tool', 'webio_view,', webio_view(checkprj), methods=['GET','POST','OPTIONS'])

# app = FastAPI()

# @app.get("/v2")
# def read_main():
#     return {"message": "Hello World"}

# app.mount("/v1", WSGIMiddleware(checkprj))

if __name__ == "__main__":
    flask_app.run(host='localhost', port=80)

# flask_app = Flask(__name__)

# @flask_app.route("/")
# def flask_main():
#     name = request.args.get("name", "World")
#     return f"Hello, {escape(name)} from Flask!"

# flask_app = FastAPI()

# @flask_app.get("/v2")
# def read_main():
#     return {"message": "Hello World"}


# flask_app.mount("/v1", WSGIMiddleware(flask_app))

# if __name__ == "__main__":
#     flask_app.run()