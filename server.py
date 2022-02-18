from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['DEBUG']=True

  
@app.route('/', methods=['GET'])
def index():
 
    return render_template("index.html")

@app.route('/<string:nome>')
def error(nome):
  variavel = f'Página ({nome}) não encontrada!'
  return render_template('error.html', variavel=variavel)

if __name__ == "__main__":
  app.run(debug=True)

