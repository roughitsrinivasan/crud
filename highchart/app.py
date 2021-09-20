from flask import Flask,  render_template, request 
import pymongo
from pymongo import MongoClient


cluster = MongoClient('mongodb+srv://roughit:peter@cluster0.woqgl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = cluster["highchart"]
col = db["info"]

app  = Flask(__name__)


@app.route("/", methods=["GET","POST"])
def startpy():
     
    res = []
    all_data = col.find()
    for entry in all_data:
        res.append(entry["gold"])
        res.append(entry["country"])
    print("res", res)
    con = res.append(entry["country"])
    go = res.append(entry["gold"])
    return render_template("index.html",myresult = {"country" : con, "gold" : go}) 
    #return str(res)

@app.route("/api")
def crud():
    return render_template("crud.html")

@app.route("/update", methods=["POST","GET"])
def update():
    con = request.form.get('country')
    go = request.form.get('gold')
    con2 = request.form.get('country2')
    go2 = request.form.get('gold2')
    
    col.update_one( 
        {
            "country" : con,
            "gold" : go
        }, 
        {
            "$set":{"country" : con2,"gold" : go2}} 
    )

    return render_template('update.html')

@app.route("/delete", methods=["POST","GET"])
def delete():
    con = request.form.get('country')
    go = request.form.get('gold')
    col.delete_one(
        {
            "country" : con,
            "gold" : go
        }
    )
    for x in col.find():
            val=x['country']
            val2=x['gold'] 
    result = {
        'country' : val ,
        'gold' : val2
    } 

    return render_template('delete.html', result = result)

@app.route("/insert", methods=["POST","GET"])
def insert():
    con = request.form.get('country')
    go =  request.form.get('gold')
    col.insert_one(
        {
            "country" : con,
            "gold" : go
        }
    )
    for x in col.find():
        val=x['country']
        val2=x['gold'] 
    result = {
        'country' : val ,
        'gold' : val2
    } 


    return render_template('insert.html', result = result)  
    


if __name__ == "__main__":
    app.run(debug = True)