from flask import Flask,render_template,request,redirect,url_for
import numpy as np
import joblib

app = Flask(__name__)

@app.route("/")
def index():
   return render_template("form.html")

@app.route("/form",methods=["POST","GET"])
def form():
 data = {"sl":None,"sw":None,"pl":None,"pw":None}
 error= {"type_error":""}
 sl = request.form["sl"]
 sw = request.form["sw"]
 pl = request.form["pl"]
 pw = request.form["pw"]
 try:
   arr = np.array([[float(sl),float(sw),float(pl),float(pw)]])
   error["type_error"] = "" 
 except:
    error["type_error"] = "ERROR: All values should be number type"
    return render_template("form.html",error=error["type_error"])
 classifier = joblib.load("classifier.pkl")
 pred = classifier.predict(arr)
 iris_class = {0:"Iris-Setosa",1:"Iris-Versicolour",2:"Iris-Verginica"}
 flower=iris_class[pred[0]]
 return render_template("form.html",error=error["type_error"]) 
     
if __name__ == "__main__":
  app.run(debug = True)
  
