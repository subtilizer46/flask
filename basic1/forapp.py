from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def fa():
    fa=['alex','ram','shyam']
    return render_template('for.html',fa=fa)

app.run(debug=True)