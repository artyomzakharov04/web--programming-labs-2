from flask import Flask, redirect, url_for, render_template, session, request
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'секретно-секретный секрет')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')

app.secret_key = 'секретно-секретный секрет'

# Регистрация blueprint'ов для лабораторных работ
app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)

# Корневой маршрут и маршрут /menu
@app.route("/")
@app.route("/index")
def start():
    return redirect(url_for("menu"), code=302)

@app.route("/menu")
def menu():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>НГТУ, ФБ, Лабораторные работы</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 0;
            background-color: #f9f9f9;
        }
        header {
            background-color: #007bff;
            color: white;
            padding: 10px;
            text-align: center;
            margin-bottom: 20px;
        }
        h1 {
            color: #333;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin: 10px 0;
        }
        a {
            text-decoration: none;
            color: #007bff;
            font-weight: bold;
        }
        a:hover {
            text-decoration: underline;
        }
        footer {
            margin-top: 20px;
            text-align: center;
            color: #777;
        }
    </style>
</head>
<body>
    <header>
        НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
    </header>

    <h1>web-сервер на flask</h1>
    <ul>
        <li><a href="/lab1">Лабораторная работа 1</a></li>
        <li><a href="/lab2">Лабораторная работа 2</a></li>
        <li><a href="/lab3">Лабораторная работа 3</a></li>
        <li><a href="/lab4">Лабораторная работа 4</a></li>
        <li><a href="/lab5">Лабораторная работа 5</a></li>
        <li><a href="/lab6">Лабораторная работа 6</a></li>
        <li><a href="/lab7">Лабораторная работа 7</a></li>
    </ul>
    <footer>
        &copy; Артём Захаров, ФБИ-23, 3 курс, 2024
    </footer>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True)




     