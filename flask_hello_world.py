from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def hello_world():
    return "greetings from maddy's world of mac"

@app.route('/test/<search_query>')
def search(search_query):
    return "Hello.. you searched for {0}".format(search_query)


if __name__ == "__main__":
    app.run()
