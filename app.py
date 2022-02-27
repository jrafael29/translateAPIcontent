from cgitb import text
from flask import Flask, render_template
import requests
from googletrans import Translator

def traduzir(advice):
    translator = Translator()
    adviceTraduzido = translator.translate(advice, src='en',dest='pt').text
    return adviceTraduzido
    
app = Flask(__name__)

@app.route('/')
def home():
    req = requests.get('https://api.adviceslip.com/advice').json()
    id = req['slip']['id']
    advice = traduzir(req['slip']['advice'])
    return render_template('index.html', id=id, advice=advice)

if __name__ == "__main__":
    app.run(debug=True)
