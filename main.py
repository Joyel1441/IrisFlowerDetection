from flask import Flask,render_template,request,redirect,url_for,session
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
import joblib
import random

app = Flask(__name__)
app.config["SECRET_KEY"] = "fusuhhu"

@app.route("/",methods=["POST","GET"])
def form():
  if request.method == "POST":
    sl = request.form["sl"]
    sw = request.form["sw"]
    pl = request.form["pl"]
    pw = request.form["pw"]
    session["sl"] = sl
    session["sw"] = sw
    session["pl"] = pl
    session["pw"] = pw
    return redirect(url_for("classify"))
  else:
    return render_template("form.html")

@app.route("/type")
def classify():
  if "sl" and "sw" and "pl" and "pw" in session:
      sl = session["sl"]
      sw = session["sw"]
      pl = session["pl"]
      pw = session["pw"]
      arr = np.array([[float(sl),float(sw),float(pl),float(pw)]])
      classifier = joblib.load("classifier.pkl")
      pred = classifier.predict(arr)
      iris_class = {0:"Iris-Setosa",1:"Iris-Versicolour",2:"Iris-Verginica"}
      return render_template("form.html",flower=iris_class[pred[0]])
  else:
     return redirect(url_for("form.html"))
  
if __name__ == "__main__":
  app.run(debug = True)
  