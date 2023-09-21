from flask import Flask, redirect, render_template
import firebase_admin
from firebase_admin import db
import os

cred_obj = firebase_admin.credentials.Certificate('./ServiceAccountKey.json')
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': 'https://url-shortener-app-6565b-default-rtdb.firebaseio.com/'
    })

app = Flask(__name__, static_folder = "./dist/assets", template_folder = "./dist")

@app.route("/")
def hello_world():
    return redirect("/app")

@app.route("/app")
def homepage():
    return render_template("index.html")

@app.route('/<path:generatedKey>', methods = ['GET'])
def fetch_from_firebase(generatedKey):
    ref = db.reference("/" + generatedKey)
    data = ref.get()
    if not data:
        return '404 not found'
    else:
        longUrl = data['longURL']
        return redirect(longUrl)
    