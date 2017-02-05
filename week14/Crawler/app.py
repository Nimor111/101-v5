from make_histogram import get_data, filter_names

from flask import Flask, jsonify, render_template
app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    # return jsonify((filter_names(get_data('stat.json'))))
    return render_template('server-plot.html')
