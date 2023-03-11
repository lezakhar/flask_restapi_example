import sqlite3
from flask import Flask, jsonify
from flask import request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/api/customers', methods=['GET'])
def get_records():
    connection = sqlite3.connect("db")
    query = 'select * from customers'
    data = connection.execute(query).fetchall()

    return jsonify(data)


@app.route('/api/customers/<int:customer_id>', methods=['PUT'])
def put_records(customer_id):
    connection = sqlite3.connect("db")
    item = dict(request.json).popitem()

    query = f''' 
        UPDATE customers
        SET 
            name = '{item[0]}',
            mail = '{item[1]}'
        WHERE 
            id = {customer_id};
    '''

    connection.execute(query)
    connection.commit()

    return jsonify({'result': True})


if __name__ == '__main__':
    connection = sqlite3.connect("db")
    with connection as conn:
        conn.execute('''
            create table if not exists customers(
                id integer primary key autoincrement,
                name text,
                mail text
            ) '''
                     )

        conn.execute(''' insert into customers values (1, 'Vasya', 'Vasya@mailru') ''')
        conn.execute(''' insert into customers values (2, 'Petya', 'Petya@mailru') ''')
    try:
        app.run()
    finally:
        with connection as conn:
            conn.execute(''' drop table customers ''')
