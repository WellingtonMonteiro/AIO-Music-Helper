from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def homepage():
    return "<h1>See AIO-MUsic Helper <a href='https://github.com/yasirarism/AIO-Music-Helper'>@GitHub</a></h1>"

@app.errorhandler(Exception)
def page_not_found(e):
    return f"<h1>404: Not found! Mostly wrong input. <br><br>Error: {e}</h2>", 404

if __name__ == "__main__":
    app.run()
