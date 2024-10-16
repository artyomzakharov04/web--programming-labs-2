from flask import Flask, redirect, url_for, render_template
from lab1 import lab1
from lab2 import lab2

app = Flask(__name__)
app.register_blueprint(lab1)
app.register_blueprint(lab2)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
        return """
<!DOCTYPE html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список Лабораторных
        </header>

        <a href="/lab1">Первая лабораторная</a> <br>
        <a href="/lab2">Вторая лабораторная</a>
        

        <footer>
            &copy; Артём Захаров, ФБИ-23, 3 курс, 2024
        </footer>
    </body>
</html>
"""




     