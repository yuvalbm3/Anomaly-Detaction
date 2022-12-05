# Imports
import pandas as pd
from flask import Flask, request, render_template

# file path - this for linux windows you will need "//"
f_path = "conn_attack.csv"
df = pd.read_csv(f_path, names=["record ID", "duration_", "src_bytes", "dst_bytes", "sub", "div"], header=None)


def classif(dur, src, dst):
    if int(dur) in df["duration_"].unique():
        x1 = {}
        x2 = df[(df["duration_"] == int(dur))]
        x1['sub'] = abs((x2['dst_bytes'] * 0.010770 - (x2['src_bytes'])))
        x1['sub'] = x1['sub']
        anom1 = abs((int(dst) * 0.010770 - int(src)))
        x1['ID'] = x2['record ID']
        x3 = x1['sub'].median()
        anom1 = abs(anom1 - x3)
        x1['sub'] = abs(x1['sub'] - x3)

        if anom1 > x3 / 0.010770:
            return "anomaly"
        else:
            return "standard"
    else:
        return "anomaly"


app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('index.html')


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/result", methods=['POST', "GET"])
def result():
    output = request.form.to_dict()
    _duration = output["duration"]
    src_bytes = output["src_bytes"]
    dst_bytes = output["dst_bytes"]
    print(_duration, src_bytes, dst_bytes)
    classification = classif(_duration, src_bytes, dst_bytes)
    print(classification)
    return render_template("index.html", name=classification)


if __name__ == '__main__':
    app.run()
