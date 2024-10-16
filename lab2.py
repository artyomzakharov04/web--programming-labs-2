from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2', __name__)

@lab2.route('/lab2/example')
def example():
     name = 'Захаров Артём'
     group = 'ФБИ-23'
     course = '3 курс'
     fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321},
        
    ]
     

     books = [
    {'name': 'Война и мир', 'price': 450},
    {'name': 'Преступление и наказание', 'price': 320},
    {'name': 'Мастер и Маргарита', 'price': 280},
    {'name': 'Гарри Поттер и Философский камень', 'price': 400},
    {'name': 'Властелин колец', 'price': 550},
    {'name': '1984', 'price': 250},
    {'name': 'Гордость и предубеждение', 'price': 300},
    {'name': 'Дубровский', 'price': 180},
    {'name': 'Анна Каренина', 'price': 420},
    {'name': 'Евгений Онегин', 'price': 200}
]


     return render_template('example.html', name=name, group=group, course=course, fruits=fruits, books=books)


@lab2.route('/lab2/')
def lab():
     return render_template('lab2.html')

@lab2.route('/lab2/cars')
def cars():
    cars = [
        {
            'image': 'car1.jpg',
            'name': 'Toyota Camry',
            'price': 25000
        },
        {
            'image': 'car2.jpg',
            'name': 'Honda Civic',
            'price': 20000
        },
        {
            'image': 'car3.jpg',
            'name': 'Ford Mustang',
            'price': 35000
        },
        {
            'image': 'car4.jpg',
            'name': 'Chevrolet Silverado',
            'price': 30000
        },
        {
            'image': 'car5.jpg',
            'name': 'Nissan Altima',
            'price': 22000
        }
    ]
    return render_template("cars.html", cars=cars)

if __name__ == "__main__":
    lab2.run()