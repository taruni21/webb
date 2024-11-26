from flask import Flask, render_template, request, redirect
import sqlite3
app=Flask(__name__)

def create_connection():
    conn=sqlite3.connect("contactt.db")
    return conn

def create_table():
    conn = create_connection()
    cur=conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS contactt(id INTEGER AUTO INCREMENT,name TEXT, number TEXT)')
    conn.commit()
    conn.close()

@app.route('/admin')
def admin():
    conn = create_connection()
    cur=conn.cursor()
    cur.execute('SELECT * FROM contactt')
    data=cur.fetchall()
    print(data)
    return render_template("admin.html",users=data)

@app.route("/")

def home():
    return render_template("index.html")

@app.route("/homepage",methods=["GET","POST"])
def homepage():
    if request.method =='POST':
        name= request.form['inp1']
        num= request.form['inp2']
        conn = create_connection()
        cur=conn.cursor()
        cur.execute('''INSERT INTO contactt(name,number) VALUES(?,?)''',(name,num))
        conn.commit()
        conn.close()
        return redirect("/feedback")

      
    return render_template("homepage.html")

@app.route("/feedback")
def feedback():
    return render_template("feedback.html")

if __name__ =="__main__":
    create_connection()
    create_table()
    app.run(debug=True)