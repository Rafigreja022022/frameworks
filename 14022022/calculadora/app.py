from asyncio.windows_events import NULL
from flask import Flask,render_template, request
 
app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def calculate():
    conta=''
    if request.method == "POST":
        num1 =float(request.form.get("num1"))
        num2 =float(request.form.get("num2"))
        op =str(request.form.get("op"))
        if op == '+':
            conta = num1+num2
        elif op == '-':
            conta = num1-num2
        elif op == '/':
            conta = num1/num2
        elif op == '*':
            conta = num1*num2
    return render_template("index.html",x = conta)

if __name__ == '__main__':
    app.run(debug = True, host = 'localhost', port = 5000)