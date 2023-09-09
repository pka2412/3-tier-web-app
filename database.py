import mysql.connector
from flask import current_app
import os

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host=os.environ.get("DB_HOST"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD"),
            database=os.environ.get("DB_NAME")
        )
        self.cursor = self.conn.cursor()

    def get_all_expenses(self):
        self.cursor.execute("SELECT * FROM expenses")
        expenses = [{"id": id, "name": name, "amount": amount} for id, name, amount in self.cursor]
        return expenses

    def get_all_incomes(self):
        self.cursor.execute("SELECT * FROM incomes")
        incomes = [{"id": id, "name": name, "amount": amount} for id, name, amount in self.cursor]
        return incomes

    def add_expense(self, name, amount):
        self.cursor.execute("INSERT INTO expenses (name, amount) VALUES (%s, %s)", (name, amount))
        self.conn.commit()

    def add_income(self, name, amount):
        self.cursor.execute("INSERT INTO incomes (name, amount) VALUES (%s, %s)", (name, amount))
        self.conn.commit()
