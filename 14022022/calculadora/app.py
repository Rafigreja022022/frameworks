from asyncio.windows_events import NULL
from flask import Flask,render_template, request
 
app = Flask(__name__)

@app.route("/calculadora",methods =["GET","POST"])
def calculate():
    resultado =""
    if request.method == "POST":
        n1 =float(request.form.get("n1"))
        n2 =float(request.form.get("n2"))
        resultado = (n1+n2)
    if resultado == 0 or resultado == NULL:
        resultado = str(0)
    return render_template("index.html",resultado = resultado)
