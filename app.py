import flask

app =flask.Flask(__name__)

@app.route("/")
def main():
    return "Merhaba Heroku için Hazırlanmış Bir Server"


@app.route("/api")
def api():
    return "Merhaba Heroku için Hazırlanmış Bir Api"
if __name__ == '__main__':
    app.run(debug=True)