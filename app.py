from flask import Flask, render_template, request, jsonify, current_app, redirect, url_for
from database import Database
import os
import subprocess

app = Flask(__name__)
db = Database()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/budget")
def budget():
    expenses = db.get_all_expenses()
    incomes = db.get_all_incomes()
    return render_template("budget.html", expenses=expenses, incomes=incomes)

@app.route("/api/expenses", methods=["GET", "POST"])
def expenses():
    if request.method == "GET":
        expenses = db.get_all_expenses()
        return jsonify(expenses)
    elif request.method == "POST":
        expense_name = request.json["expenseName"]
        expense_amount = request.json["expenseAmount"]
        db.add_expense(expense_name, expense_amount)
        return redirect(url_for("budget"))

@app.route("/api/incomes", methods=["GET", "POST"])
def incomes():
    if request.method == "GET":
        incomes = db.get_all_incomes()
        return jsonify(incomes)
    elif request.method == "POST":
        income_name = request.json["incomeName"]
        income_amount = request.json["incomeAmount"]
        db.add_income(income_name, income_amount)
        return redirect(url_for("budget"))

if __name__ == "__main__":
    # Run the command to create the database from create_database.sql
    subprocess.call(["mysql", "-u", os.environ.get("DB_USER"), "-p", "<", "create_database.sql"])
    
    app.run(debug=True)
