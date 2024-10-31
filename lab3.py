from flask import Blueprint, render_template, request, make_response, redirect, session
lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name', 'неизвестный')
    name_color = request.cookies.get('name_color')
    age = request.cookies.get('age', 'неизвестен') 
    return render_template('lab3/lab3.html', name=name, name_color=name_color, age=age)


@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'magenta')
    return resp


@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp


@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'

    age = request.args.get('age')
    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user=user, age=age, sex=sex, errors=errors)

@lab3.route('/lab3/order')
def order():
    return render_template('lab3/order.html')

@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70
    
    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10
    return render_template('lab3/pay.html', price=price)


@lab3.route('/lab3/success')
def success():
    price = 0
    drink = request.args.get('drink')
    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70
    
    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10
    return render_template('lab3/success.html', price=price)


@lab3.route('/lab3/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        if 'clear' in request.form:  # Проверяем, была ли нажата кнопка "Очистить куки"
            resp = make_response(redirect('/lab3/settings'))
            # Очистка всех кук
            resp.set_cookie('color', '', expires=0)
            resp.set_cookie('background_color', '', expires=0)
            resp.set_cookie('font_size', '', expires=0)
            resp.set_cookie('text_align', '', expires=0)
            return resp

        # Обработка обновления куки
        color = request.form.get('color')
        background_color = request.form.get('background_color')
        font_size = request.form.get('font_size')
        text_align = request.form.get('text_align')

        resp = make_response(redirect('/lab3/settings'))
        if color:
            resp.set_cookie('color', color)
        if background_color:
            resp.set_cookie('background_color', background_color)
        if font_size:
            resp.set_cookie('font_size', font_size)
        if text_align:
            resp.set_cookie('text_align', text_align)
        return resp

    # Обработка GET-запроса
    color = request.cookies.get('color')
    background_color = request.cookies.get('background_color')
    font_size = request.cookies.get('font_size')
    text_align = request.cookies.get('text_align')


    resp = make_response(render_template('lab3/settings.html', 
                                        color=color,
                                        background_color=background_color,
                                        font_size=font_size,
                                        text_align=text_align))
    return resp






@lab3.route('/lab3/ticketform')
def ticket_form():
    return render_template('lab3/ticketform.html')


@lab3.route('/lab3/ticket', methods=['POST'])
def ticket():
    # Получаем данные из формы
    fio = request.form.get('fio')
    shelf = request.form.get('shelf')
    bed = request.form.get('bed') == 'on'
    luggage = request.form.get('luggage') == 'on'
    age = int(request.form.get('age'))
    departure = request.form.get('departure')
    destination = request.form.get('destination')
    date = request.form.get('date')
    insurance = request.form.get('insurance') == 'on'

    # Проверка полей
    if not all([fio, shelf, age, departure, destination, date]):
        flash("Все поля должны быть заполнены")
        return redirect(url_for('lab3.ticketform'))

    if not (1 <= age <= 120):
        flash("Возраст должен быть от 1 до 120 лет")
        return redirect(url_for('lab3.ticketform'))

    # Рассчет стоимости
    price = 1000 if age >= 18 else 700  # Взрослый или детский билет

    if shelf in ["нижняя", "нижняя боковая"]:
        price += 100
    if bed:
        price += 75
    if luggage:
        price += 250
    if insurance:
        price += 150

    ticket_type = "Детский билет" if age < 18 else "Взрослый билет"

    return render_template('lab3/ticket.html', fio=fio, shelf=shelf,
                           bed=bed, luggage=luggage, age=age,
                           departure=departure, destination=destination,
                           date=date, insurance=insurance, price=price,
                           ticket_type=ticket_type)





cars = [
    {"name": "Toyota Camry", "price": 2500000, "brand": "Toyota", "color": "серебристый"},
    {"name": "Honda Civic", "price": 1800000, "brand": "Honda", "color": "черный"},
    {"name": "Hyundai Solaris", "price": 1200000, "brand": "Hyundai", "color": "белый"},
    {"name": "Audi A4", "price": 3000000, "brand": "Audi", "type": "седан"},
    {"name": "Volkswagen Polo", "price": 1500000, "brand": "Volkswagen", "engine": "1.6 л"},
    {"name": "BMW 3 Series", "price": 3500000, "brand": "BMW", "engine": "2.0 л"},
    {"name": "Kia Sportage", "price": 2200000, "brand": "Kia", "engine": "2.0 л"},
    {"name": "Mazda CX-5", "price": 2700000, "brand": "Mazda", "type": "кроссовер"},
    {"name": "Nissan Qashqai", "price": 2100000, "brand": "Nissan", "type": "кроссовер"},
    {"name": "Ford Mustang", "price": 4000000, "brand": "Ford", "type": "купе"},
    {"name": "Chevrolet Tahoe", "price": 4500000, "brand": "Chevrolet", "type": "внедорожник"},
    {"name": "Mercedes-Benz C-Class", "price": 3800000, "brand": "Mercedes-Benz", "engine": "2.0 л"},
    {"name": "Subaru Forester", "price": 2400000, "brand": "Subaru", "type": "кроссовер"},
    {"name": "Jeep Wrangler", "price": 3300000, "brand": "Jeep", "type": "внедорожник"},
    {"name": "Lexus RX", "price": 4700000, "brand": "Lexus", "type": "кроссовер"},
    {"name": "Mitsubishi Outlander", "price": 2000000, "brand": "Mitsubishi", "type": "кроссовер"},
    {"name": "Volvo XC90", "price": 4900000, "brand": "Volvo", "type": "кроссовер"},
    {"name": "Škoda Octavia", "price": 1800000, "brand": "Škoda", "engine": "1.4 л"},
    {"name": "Tesla Model 3", "price": 4500000, "brand": "Tesla", "type": "седан"},
    {"name": "Porsche Cayenne", "price": 6000000, "brand": "Porsche", "type": "внедорожник"},
]

@lab3.route('/lab3/product_search', methods=['GET', 'POST'])
def car_search():
    if request.method == 'POST':
        min_price = float(request.form.get('min_price', 0))
        max_price = float(request.form.get('max_price', float('inf')))

        # Фильтруем автомобили по цене
        filtered_cars = [
            car for car in cars 
            if min_price <= car['price'] <= max_price
        ]
        return render_template('lab3/product_results.html', cars=filtered_cars)

    return render_template('lab3/product_search.html', cars=cars)


 









    