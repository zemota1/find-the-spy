from random import randrange

from flask import Flask, render_template, request

from vocab import get_word

app = Flask(__name__)

@app.route("/")
def student():
    return render_template('index.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    word = get_word()
    if request.method == 'POST':
        result = request.form["text"]
        spy = randrange(int(result))
        while spy == 0:
            spy = randrange(int(result))
        return render_template("result.html", result=int(result), word=word, spy=spy)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
