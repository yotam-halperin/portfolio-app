from flask import Flask, render_template, jsonify, request, send_file
import os
import datetime
import db_functions


#create flask
app = Flask(__name__)

### database configurations
db_host = "mysql"
db_port = "3306"
db_user = "root"
db_password = "password"
db_name = "mydb"


# create a database connection
connection = db_functions.create_db_connection(f"{db_host}", f"{db_port}", f"{db_user}", f"{db_password}", f"{db_name}")



@app.route("/")
def home_page():
    return render_template("index.html")



# health check of both the flask and the database
@app.route("/health", methods=["GET"])
def isHealthy():
    status=db_functions.getHealthCheck(connection)
    if status == 1:
        answer ={"OK : server is up and run"}
        return render_template("base.html", pagetitle="HEALTH", data=answer), 200
    else:
        answer ={"OK : server is up and run"}
        return render_template("base.html", pagetitle="HEALTH", data=answer), 500



@app.route("/download")
def download():
    return send_file('crossy_road.zip', as_attachment=True)



@app.route("/get_mails", methods=["GET"])
def get_all():
    answer = db_functions.get_mails(connection)
    return render_template("base.html", pagetitle="GET_MAILS", data=answer), 200



@app.route("/get_all", methods=["GET"])
def get_mails():
    answer = db_functions.get_all(connection)
    return render_template("base.html", pagetitle="GET_ALL", data=answer), 200



@app.route("/add_mail", methods=["POST"])
def add_mail():
    try:
        name = request.form['name']
        email = request.form['mail']
    except:
        name = request.args.get('name')
        email = request.args.get('mail')
    time = datetime.datetime.now()
    answer = {f"name : {name}", f"email :{email}", f"time : {time}"}
    db_functions.add_mail(connection, name, email, time)
    return render_template("base.html", pagetitle="Mail Added", data=answer), 200
    
    
    
@app.route("/get_mail/<name>", methods=["GET"])
def mail_of_name(name):
    answer = db_functions.get_mail_from_name(connection, name)
    return render_template("base.html", pagetitle="Your Mail", data=answer), 200



@app.route("/get_name/<mail>", methods=["GET"])
def name_of_mail(mail):
    answer = db_functions.get_name_from_mail(connection, mail)
    return render_template("base.html", pagetitle="Your Name", data=answer), 200


@app.route("/delete_mail", methods=['DELETE'])
def delete_mail():
    name = request.args.get('name')
    answer = db_functions.delete_by_name(connection, name)
    return jsonify({"DELETED":answer}), 200


@app.route("/add_score", methods=['POST'])
def add_score():
    user = request.args.get("user")
    score = request.args.get("score")
    db_functions.add_score(connection, user, score)
    return jsonify({"OK": "success"}), 200


@app.route("/get_leaderboard", methods=["GET"])
def get_leaderboard():
    answer = db_functions.get_scores(connection)
    return render_template("base.html", pagetitle="LEADERBOARD", data=answer), 200


if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)