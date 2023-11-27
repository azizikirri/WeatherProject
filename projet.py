from flask import Flask , render_template,request,send_file
import pymongo as myprojet
from pymongo import MongoClient
import matplotlib.pyplot as plt 
from matplotlib.figure import Figure
import io
from io import BytesIO
import base64
import matplotlib
import json
user = myprojet.MongoClient()

db = user.projet
projet = Flask (__name__)

list_Az = []
@projet.route("/",methods = ("POST","GET"))

def first ():
    return render_template("Form.html")
@projet.route("/Donnesform",methods = ("POST","GET"))
def Donnesform ():

    station_ = request.form["user_station"].upper()
    Date_ = request.form["user_date"]#fetch data for the user
    for i in db.colprojet.find({"nom":station_, "date":Date_}):
        list_Az.append(i)
    
    return render_template("Donnesform.html",list = list_Az[-8:],champ1 = station_,champ2 =Date_,Graph = plt.show())
@projet.route("/graphs",methods = ("POST","GET"))
def graphs():
    x=[]
    y = []
    for j in list_Az:
        x.append(j['hours'])
        y.append(j['tc'])
    fig = Figure()
    ax = fig.subplots()
    ax.bar(x,y)
    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    #plt.bar(x,y,color=['green'])
    return f"<img src='data:image/png;base64,{data}'/>"
@projet.route("/save",methods = ("POST","GET"))
def save ():
    Dow= 'data_saved.json'
    with open(Dow, 'w', encoding='utf-8') as f:
        json.dump(str(list_Az), f, ensure_ascii=False, indent=4)
    return "<h3>data saved </h3>"



if __name__ == "__main__":
        projet.run(debug=True,port=(1999))
 
    
















