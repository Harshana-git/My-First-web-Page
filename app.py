import sqlite3
from urllib import request
from flask import render_template

from crud import app


@app.route("/savedetails", methods=["POST", "GET"])
def saveDetails():
    msg = "msg"
    if request.method == "POST":
        def render_template(param, msg):
            pass


try:
    name = request.form["name"]
    email = request.form["email"]
    address = request.form["address"]
    with sqlite3.connect("student.db") as con:
        cur = con.cursor()
        cur.execute("INSERT into Student (name, email, address) values (?,?,?)", (name, email, address))
        con.commit()
        msg = "Student  successfully Added"
except:
    con.rollback()
    msg = "We can not add the student to the list"
finally:
    con.close()


@app.route("/deleterecord", methods=["POST"])
def deleterecord():
    id = request.form["id"]
    with sqlite3.connect("student.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from Student where id = ?", id)
            msg = "record successfully deleted"
        except:
            msg = "can not be deleted"
        finally:
            return render_template("delete_record.html", msg=msg)


app.route("/view")

def view():
    con = sqlite3.connect("employee.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from Employees")
    rows = cur.fetchall()
    return render_template("view.html", rows=rows)

@app.route("/view")
def view():
 con = sqlite3.connect("Student.db")
 con.row_factory = sqlite3.Row
 cur = con.cursor()
 cur.execute("select * from Student")
 rows = cur.fetchall()
 return render_template("view.html",rows = rows)
