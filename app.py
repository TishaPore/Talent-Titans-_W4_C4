from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    prediction = ""

    if request.method == 'POST':

        url = request.form['url']

        if "google" in url:
            prediction = "Safe URL ✅"
        else:
            prediction = "Phishing URL Detected ⚠️"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)