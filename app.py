from flask import Flask, render_template, request, jsonify
from testing import plot_html

app = Flask(__name__)

page_title = "Home"

@app.route('/')
def index():
    return render_template('index.html', page_title=page_title, plot_html=plot_html)

@app.route('/learning')
def learning_page():
    page_title = "Learning"
    return render_template('learning.html', page_title=page_title)

# A decorator used to tell the application
# which URL is associated function
@app.route('/learning/add_seq', methods =["GET", "POST"])
def add_seq_to_list():
    if 'input_seq' in request.form:
        input_seq = request.form['input_seq']
        return jsonify(message=f'Hello, {input_seq}.')
    return '', 400

@app.route('/prediction')
def prediction_page():
    page_title = "Prediction"
    return render_template('prediction.html', page_title=page_title)

@app.route('/evaluation')
def evaluation_page():
    page_title = "Evaluation"
    return render_template('evaluation.html', page_title=page_title)


if __name__ == '__main__':
    app.run(debug=True)
