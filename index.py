from flask import Flask, render_template, request
from datetime import datetime, timezone, timedelta

import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>吳若耶Python+flask+Vercel網頁</h1>"
    homepage += "<a href=/mis>MIS</a><br>"
    homepage += "<a href=/today>顯示日期時間</a><br>"
    homepage += "<a href=/welcome?nick=若耶>傳送使用者暱稱</a><br>"
    homepage += "<a href=/account>表單輸入實例</a><br><br>"
    homepage += "<a href=/about>wendy簡介網頁</a><br>"
    homepage += "<a href=/search>選修課程查詢</a><br><br>"
    return homepage

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
    tz = timezone(timedelta(hours=+8))
    now = datetime.now(tz)
    return render_template("today.html", datetime = str(now))

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    user = request.values.get("nick")
    return render_template("welcome.html", name=user)

@app.route("/about")
def about():
    return render_template("wendy.html")

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd 
        return result
    else:
        return render_template("account.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        cond = request.form["keyword"]
        pwd = request.form["pwd"]
        result = "您輸入的課程關鍵字是：" + cond 
        return result
    else:
        return render_template("search.html")
        
        if result == "":
            result = "抱歉，找不到相關結果"
        
        return result
    else:
        return render_template("search.html")

#if __name__ == "__main__":
#    app.run()