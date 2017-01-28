from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route('/')
@app.route('/home')
def hello_world():
    return "greetings from maddy's world of mac"

@app.route('/test/<search_query>')
def search(search_query):
    return "Hello.. you searched for {0}".format(search_query)


@app.route('/test_int/<int:value>')
def int_type(value):
    value = value + 5
    return "the value you entered incremented by 5 is {0}".format(value)


@app.route('/name/<name>')
def selective_name(name):
    if name == 'maddy':
        return "cool , you are authorized in {}".format(name), 200
    else:
        return "not cool .. you are NOT authorized in here {}".format(name), 404

if __name__ == "__main__":
    app.run()
