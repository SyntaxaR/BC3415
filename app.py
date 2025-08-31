from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["POST"])
def main():
    name = str(request.form.get("name"))
    return(render_template("main.html",name=name))

@app.route("/dbs",methods=["POST"])
def dbs():
    q = float(request.form.get("q"))
    name = str(request.form.get("name"))
    return(render_template("dbs.html",r=(-50.6*q)+90.2,name=name))

if __name__ == "__main__":
    app.run()