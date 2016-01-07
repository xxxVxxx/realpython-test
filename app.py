#!/home/madhav/.virtualenvs/flask/bin/python

from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
@app.route("/hello")

def hello_world():
    return "Hello, my juumba folks"

@app.route("/test/<search_query>")
def search(search_query):
    return "you searched for {}".format(search_query)

@app.route("/name/<name>")
def index(name):
    if name.lower() == "madhav":
        return "Hellooooooo ...Lord of my Server".format(name)
    else:
        return "Not Foooound", 404

if __name__ == "__main__":
    app.run()
