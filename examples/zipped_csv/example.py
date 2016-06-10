from flask import Flask
from flask.ext import excel

app = Flask(__name__)


@app.route("/download", methods=['GET'])
def download_file():
    return excel.make_response_from_array([[1, 2], [3, 4]], "csvz")


if __name__ == "__main__":
    app.run()
