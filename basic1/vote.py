from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def score():
    score=80
    return render_template('score.html',score=score)

app.run(debug=True)