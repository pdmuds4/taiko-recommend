from flask import Flask, Response, request, render_template
from flask_bootstrap import Bootstrap
import json
from search import result
from dataaccess import DataAccess

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['JSON_AS_ASCII'] = False
bootstrap = Bootstrap(app)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        title = request.form["title"]
        da = DataAccess()
        if title in [t[0] for i in range(5,11) for t in da.get_table(i)]:
            data = result(10, title, master=False, level=None)
            return render_template("index.html", data=data)
        else:
            return render_template("index.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
