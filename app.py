from flask import Flask,render_template,request,redirect,url_for
import numpy as np
import joblib

app = Flask(__name__)
data = {"sl":None,"sw":None,"pl":None,"pw":None}
flower = {"flower":None}
error= {"type_error":""}

@app.route("/")
def index():
    data = {"sl":None,"sw":None,"pl":None,"pw":None}
    flower = {"flower":None}
    error= {"type_error":""}
    return redirect(url_for("form"))

@app.route("/form",methods=["POST","GET"])
def form():
  if request.method == "POST":
    sl = request.form["sl"]
    sw = request.form["sw"]
    pl = request.form["pl"]
    pw = request.form["pw"]
    data["sl"] = sl
    data["sw"] = sw
    data["pl"] = pl
    data["pw"] = pw
    return redirect(url_for("classify")) 
  else:
     return render_template("form.html",flower=flower["flower"],error=error["type_error"])

@app.route("/type")
def classify():
      sl = data["sl"]
      sw = data["sw"]
      pl = data["pl"]
      pw = data["pw"]
      try:
        arr = np.array([[float(sl),float(sw),float(pl),float(pw)]])
        error["type_error"] = "" 
      except:
        data["sl"] = None
        data["sw"] = None
        data["pl"] = None
        data["pw"] = None
        flower["flower"] = None
        error["type_error"] = "ERROR: All values should be number type"
        return redirect(url_for("form"))
      classifier = joblib.load("classifier.pkl")
      pred = classifier.predict(arr)
      iris_class = {0:"Iris-Setosa",1:"Iris-Versicolour",2:"Iris-Verginica"}
      flower["flower"]=iris_class[pred[0]]
      data["sl"] = None
      data["sw"] = None
      data["pl"] = None
      data["pw"] = None
      return redirect(url_for("form"))   
  
if __name__ == "__main__":
  app.run(debug = True)
  
