from flask import Blueprint, render_template, request, session, jsonify

lab6 = Blueprint('lab6', __name__)

# Инициализация офисов
offices = [{"number": i, "tenant": "", "price": 1000} for i in range(1, 11)]

@lab6.route('/lab6/')
def main():
    return render_template('lab6/lab6.html')

@lab6.route('/lab6/json-rpc-api/', methods=['POST'])
def api():
    data = request.json
    id = data['id']
    method = data['method']

    if method == 'info':
        return {
            'jsonrpc': '2.0',
            'result': offices,
            'id': id
        }

    login = session.get('login')
    if not login:
        return jsonify({
            'jsonrpc': '2.0',
            'error': {
                'code': 1,
                'message': 'Unauthorized'
            },
            'id': id
        }), 401

    if method == 'cancellation':
        office_number = data['params']
        office_found = False
        for office in offices:
            if office['number'] == office_number:
                office_found = True
                if office['tenant'] == '':
                    return jsonify({
                        'jsonrpc': '2.0',
                        'error': {
                            'code': 4,
                            'message': 'Office is not rented'
                        },
                        'id': id
                    }), 409
                elif office['tenant'] != login:
                    return jsonify({
                        'jsonrpc': '2.0',
                        'error': {
                            'code': 5,
                            'message': 'You did not rent this office'
                        },
                        'id': id
                    }), 403
                else:
                    office['tenant'] = ''  # Снимаем аренду
                    return jsonify({
                        'jsonrpc': '2.0',
                        'result': 'Success',
                        'id': id
                    })

        if not office_found:
            return jsonify({
                'jsonrpc': '2.0',
                'error': {
                    'code': 3,
                    'message': 'Office not found'
                },
                'id': id
            }), 404

    if method == 'booking':
        office_number = data['params']
        office_found = False
        for office in offices:
            if office['number'] == office_number:
                office_found = True
                if office['tenant'] != '':
                    return jsonify({
                        'jsonrpc': '2.0',
                        'error': {
                            'code': 2,
                            'message': 'Already booked'
                        },
                        'id': id
                    }), 409
                else:
                    office['tenant'] = login  # Бронируем офис, присваиваем имя пользователя
                    return jsonify({
                        'jsonrpc': '2.0',
                        'result': "Success",
                        'id': id
                    })

        if not office_found:
            return jsonify({
                'jsonrpc': '2.0',
                'error': {
                    'code': 3,
                    'message': 'Office not found'
                },
                'id': id
            }), 404

    return jsonify({
        'jsonrpc': '2.0',
        'error': {
            'code': -32601,
            'message': 'Method not found'
        },
        'id': id
    }), 404

