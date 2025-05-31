from flask import Flask, request, render_template, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)

# Data storage file
DATA_FILE = 'data/expenses.json'

# Ensure the data directory exists
os.makedirs('data', exist_ok=True)

# Load existing expenses or initialize an empty list
def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

# Save expenses to the data file
def save_expenses(expenses):
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

@app.route('/')
def index():
    expenses = load_expenses()
    return render_template('expenses.html', expenses=expenses)

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        description = request.form['description']
        amount = float(request.form['amount'])
        category = request.form['category']
        expense = {
            'description': description,
            'amount': amount,
            'category': category
        }
        expenses = load_expenses()
        expenses.append(expense)
        save_expenses(expenses)
        return redirect(url_for('index'))
    return render_template('add_expense.html')

@app.route('/delete/<int:index>', methods=['POST'])
def delete_expense(index):
    expenses = load_expenses()
    if 0 <= index < len(expenses):
        del expenses[index]
        save_expenses(expenses)
    return redirect(url_for('index'))

@app.route('/api/expenses')
def api_expenses():
    expenses = load_expenses()
    return jsonify(expenses)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)