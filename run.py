from flask import Flask
from flask import render_template,url_for
from modal import chan_dong

app = Flask(__name__)
@app.route('/')
def index_page():
    person = chan_dong

    return render_template('index.html',person=person)

if __name__ == '__main__':

    app.run(debug=True)