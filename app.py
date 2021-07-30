from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from flask import Flask, escape, request
from checkprj import checkprj

app = Flask(__name__)

@app.route("/")
def hello():
    name = request.args.get("name", "World")
    return f"Hello, {escape(name)} from Flask!"
    # return "Hello from FastCGI via IIS!"

# app2 = FastAPI()

# @app2.get("/v2")
# # def read_main():
    # return {"message": "Hello World"}

# app2.mount("/v1", WSGIMiddleware(app.app))

if __name__ == "__main__":
    app.run()

# app = Flask(__name__)

# @app.route("/")
# def flask_main():
#     name = request.args.get("name", "World")
#     return f"Hello, {escape(name)} from Flask!"

# app = FastAPI()

# @app.get("/v2")
# def read_main():
#     return {"message": "Hello World"}


# app.mount("/v1", WSGIMiddleware(app))

# if __name__ == "__main__":
#     app.run()