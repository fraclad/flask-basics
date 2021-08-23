from app import app
from flask import render_template

@app.route("/admin/dashboard")
def adminDashboard():
    return render_template("admin/dashboard.html")

@app.route("/admin/profile")
def adminProfile():
    return "<h1 style = 'color: red'> Admin Profile </h1>"