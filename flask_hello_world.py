from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def hello_world():
    return "greetings from maddy's world of mac"

if __name__ == "__main__":
    app.run()
