from flask import Blueprint, render_template, request, make_response, redirect, session
import traceback
lab4 = Blueprint('lab4', __name__)


@lab4.route('/lab4/')
def lab():

    return render_template('lab4/lab4.html')


@lab4.route('/lab4/div-form')
def div_form():
    
    return render_template('lab4/div-form.html')


@lab4.route('/lab4/div', methods=['POST'])
def div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    
    if x1 == '' or x2 == '':
        return render_template('lab4/div.html', error='Оба поля должны быть заполнены!')

    try:
        x1 = int(x1)
        x2 = int(x2)
        
        if x2 == 0:
            return render_template('lab4/div.html', error='Деление на ноль невозможно!')
        
        result = x1 / x2
        return render_template('lab4/div.html', x1=x1, x2=x2, result=result)
    
    except ValueError:
        return render_template('lab4/div.html', error='Пожалуйста, введите корректные числа!')


@lab4.route('/lab4/sum-form')
def sum_form():
    return render_template('lab4/sum-form.html')


@lab4.route('/lab4/sum', methods=['POST'])
def sum():
    x1 = request.form.get('x1', 0)
    x2 = request.form.get('x2', 0)
    
    try:
        x1 = int(x1)
        x2 = int(x2)
        result = x1 + x2
        return render_template('lab4/sum.html', x1=x1, x2=x2, result=result)
    
    except ValueError:
        return render_template('lab4/sum.html', error='Пожалуйста, введите корректные числа!')


@lab4.route('/lab4/mul-form')
def mul_form():
    return render_template('lab4/mul-form.html')


@lab4.route('/lab4/mul', methods=['POST'])
def mul():
    x1 = request.form.get('x1', 1)
    x2 = request.form.get('x2', 1)
    
    try:
        x1 = int(x1)
        x2 = int(x2)
        result = x1 * x2
        return render_template('lab4/mul.html', x1=x1, x2=x2, result=result)
    
    except ValueError:
        return render_template('lab4/mul.html', error='Пожалуйста, введите корректные числа!')


@lab4.route('/lab4/sub-form')
def sub_form():
    return render_template('lab4/sub-form.html')


@lab4.route('/lab4/sub', methods=['POST'])
def sub():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    
    if x1 == '' or x2 == '':
        return render_template('lab4/sub.html', error='Оба поля должны быть заполнены!')
    
    try:
        x1 = int(x1)
        x2 = int(x2)
        result = x1 - x2
        return render_template('lab4/sub.html', x1=x1, x2=x2, result=result)
    
    except ValueError:
        return render_template('lab4/sub.html', error='Пожалуйста, введите корректные числа!')


@lab4.route('/lab4/pow-form')
def pow_form():
    return render_template('lab4/pow-form.html')


@lab4.route('/lab4/pow', methods=['POST'])
def pow():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    
    if x1 == '' or x2 == '':
        return render_template('lab4/pow.html', error='Оба поля должны быть заполнены!')
    
    try:
        x1 = int(x1)
        x2 = int(x2)
        
        if x1 == 0 and x2 == 0:
            return render_template('lab4/pow.html', error='Недопустимые значения!')
        
        result = x1 ** x2
        return render_template('lab4/pow.html', x1=x1, x2=x2, result=result)
    
    except ValueError:
        return render_template('lab4/pow.html', error='Пожалуйста, введите корректные числа!')


tree_count = 0


@lab4.route('/lab4/tree', methods=['GET', 'POST'])
def tree():
    global tree_count
    if request.method == 'GET':
        return render_template('lab4/tree.html', tree_count=tree_count)

    operation = request.form.get('operation')

    if operation == 'cut':
        if tree_count > 0:
            tree_count -= 1
    elif operation == 'plant':
        if tree_count < 10:
            tree_count += 1

    return redirect('/lab4/tree')


users = [
    {'login': 'alex', 'password': '123', 'name': 'Александр Петров', 'gender': 'М'},
    {'login': 'bob', 'password': '555', 'name': 'Боб Смирнов', 'gender': 'М'},
    {'login': 'alik', 'password': '666', 'name': 'Алик Гапшис', 'gender': 'М'},
    {'login': 'egor', 'password': '777', 'name': 'Егор Лапшин', 'gender': 'М'}
]


def is_authorized():
    current_app.logger.info(f"is_authorized() called, session: {session}")
    if 'user_id' in session:
        current_app.logger.info("User is authorized")
        return True
    else:
        current_app.logger.info("User is not authorized")
        return False


@lab4.route('/lab4/users')
def users_list():
    if not is_authorized():
        current_app.logger.info("User is not authorized, redirecting to login")
        return redirect('/lab4/login')
    
    try:
        current_app.logger.info("Rendering users_list.html")
        return render_template('lab4/users_list.html', users=users)
    except KeyError as e:
        current_app.logger.error(f"KeyError in users_list: {e}")
        return messages.ERRORS['users_list_error'], 500
    except TypeError as e:
        current_app.logger.error(f"TypeError in users_list: {e}")
        return messages.ERRORS['users_list_error'], 500
    except Exception as e:
        current_app.logger.error(f"Unexpected error in users_list: {e}")
        return messages.ERRORS['users_list_error'], 500


@lab4.route('/lab4/delete_user/<login>', methods=['POST'])
def delete_user(login):
    global users

    if not is_authorized():
        return redirect('/lab4/login')

    # Удаляем пользователя
    users = [user for user in users if user['login'] != login]

    if session.get('login') == login:
        logout()  # Если текущий пользователь удаляет себя, выходим из системы
        
    return redirect('/lab4/users')



@lab4.route('/lab4/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'login' in session:
            authorized = True
            login = session['login']
            name = next((user['name'] for user in users if user['login'] == login), '')
        else:
            authorized = False
            login = ''
            name = ''
        return render_template('lab4/login.html', authorized=authorized, login=login, name=name)

    login = request.form.get('login')
    password = request.form.get('password')

    if not login:
        error = 'Не введён логин'
        return render_template('lab4/login.html', error=error, authorized=False, login=login)

    if not password:
        error = 'Не введён пароль'
        return render_template('lab4/login.html', error=error, authorized=False, login=login)

    for user in users:
        if login == user['login'] and password == user['password']:
            session['login'] = login
            return redirect('/lab4/login')
    
    error = 'Неверные логин и/или пароль'
    return render_template('lab4/login.html', error=error, authorized=False, login=login)


@lab4.route('/lab4/logout', methods=['POST'])
def logout():
    session.pop('login', None)
    return redirect('/lab4/login')


@lab4.route('/lab4/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        login = request.form.get('login')
        password = request.form.get('password')

        # Проверка на уникальность логина
        if any(user['login'] == login for user in users):
            error = 'Такой логин уже существует. Пожалуйста, выберите другой.'
            return render_template('lab4/register.html', error=error)
        
        # Добавление нового пользователя
        users.append({
            'login': login,
            'password': password,
            'name': name,
            'gender': 'М'  # Можно расширить данными о поле
        })

        return redirect('/lab4/login')  # После успешной регистрации перенаправляем на страницу логина

    return render_template('lab4/register.html')


@lab4.route('/lab4/edit_user/<login>', methods=['GET', 'POST'])
def edit_user(login):
    if not is_authorized():
        return redirect('/lab4/login')

    user = next((user for user in users if user['login'] == login), None)

    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')

        if user:
            user['name'] = name
            user['password'] = password
            return redirect('/lab4/users')

    return render_template('lab4/edit_user.html', user=user)



@lab4.route('/lab4/refrigerator', methods=['GET', 'POST'])
def refrigerator():
    result = None
    
    if request.method == 'POST':
        temperature = request.form.get('temperature')

        # Проверьте, что temperature всегда строка, и обработайте это
        if temperature:
            try:
                temperature = float(temperature)  # Преобразование, возможно, вызовет ошибку
            except ValueError:
                return render_template('lab4/refrigerator.html', result='Ошибка: введено некорректное значение температуры')

            # Здесь ваши проверки
            if temperature < -12:
                result = 'Не удалось установить температуру — слишком низкое значение'
            elif temperature > -1:
                result = 'Не удалось установить температуру — слишком высокое значение'
            elif -12 <= temperature < -9:
                result = f'Установлена температура: {temperature}°C ❄️❄️❄️'
            elif -8 <= temperature < -5:
                result = f'Установлена температура: {temperature}°C ❄️❄️'
            elif -4 <= temperature < -1:
                result = f'Установлена температура: {temperature}°C ❄️'
        else:
            result = 'Ошибка: не задана температура'

    return render_template('lab4/refrigerator.html', result=result)


# Цены на зерно
grain_prices = {
    'barley': 12345,  # Ячмень
    'oats': 8522,     # Овёс
    'wheat': 8722,    # Пшеница
    'rye': 14111      # Рожь
}
 
@lab4.route('/lab4/order_grain', methods=['GET', 'POST'])
def order_grain():
    result = None
    
    if request.method == 'POST':
        grain_type = request.form.get('grain_type')
        weight = request.form.get('weight')

        if not weight:
            result = 'Ошибка: не указан вес.'
        else:
            try:
                weight = float(weight)
                if weight <= 0:
                    result = 'Ошибка: вес должен быть больше 0.'
                elif weight > 500:
                    result = 'Ошибка: такого объёма сейчас нет в наличии.'
                else:
                    price_per_ton = grain_prices[grain_type]
                    total_cost = price_per_ton * weight
                    
                    # Применение скидки
                    discount = 0
                    if weight > 50:
                        discount = total_cost * 0.10
                        total_cost -= discount
                        result = f'Заказ успешно сформирован. Вы заказали {grain_type}.' \
                                 f' Вес: {weight} т. Сумма к оплате: {total_cost} руб. Применена скидка: {discount} руб.'
                    else:
                        result = f'Заказ успешно сформирован. Вы заказали {grain_type}.' \
                                 f' Вес: {weight} т. Сумма к оплате: {total_cost} руб.'

            except ValueError:
                result = 'Ошибка: введено некорректное значение веса.'
    
    return render_template('lab4/order_grain.html', result=result)



