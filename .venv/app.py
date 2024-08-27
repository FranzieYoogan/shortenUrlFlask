from flask import Flask, render_template, request
import pyshorteners

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():

    if(request.method == "POST"):
        
        inputUrl = request.form['inputUrl']

        s = pyshorteners.Shortener()
        result = s.tinyurl.short(inputUrl)

        return render_template('index.htm', result = result)

    return render_template('index.htm')

if __name__ == '__main__':
    app.run(debug=True)