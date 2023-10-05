from flask import Flask
import random

app = Flask(__name__)


fakta = ['8 dari 10 siswa kecanduan gadget',
         'Kebanyakan orang yang menderita kecanduan teknologi mengalami stres yang kuat ketika mereka berada di luar area jangkauan jaringan atau tidak dapat menggunakan perangkat mereka',
         'Menurut sebuah studi yang dilakukan pada tahun 2018, lebih dari 50 persen orang berusia 18 hingga 34 tahun menganggap diri mereka bergantung pada ponsel pintar mereka.',
         'Elon musk pemilik x']

heroes = ['iron man', 'spiderman', 'superman', 'batman']
         
@app.route('/')
def home():
    return "<h1>Website bruh</h1><a href = 'random_fact'>Klik untuk mencari fakta</a><a href = 'superhero'>pahlawan</a>"

@app.route("/random_fact")
def hello_world():
    return f"<h1>Fakta random</h1><p>{random.choice(fakta)}</p>"

@app.route("/superhero")
def yes():
    return f"<h1>superhero</h1><p>{random.choice(heroes)}</p>"


app.run(debug=True)
