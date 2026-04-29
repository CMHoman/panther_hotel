from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from database import init_db

app = Flask(__name__)
init_db()

def get_db():
    conn = sqlite3.connect('hotel.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/reservation', methods=['GET', 'POST'])
def reservation():
    if request.method == 'POST':
        guest_name = request.form['guest_name']
        check_in = request.form['check_in']
        check_out = request.form['check_out']
        room_type = request.form['room_type']

        conn = get_db()
        conn.execute(
                "INSERT INTO Reservation (guest_name, check_in, check_out, room_type) values (?,?,?,?)", (guest_name, check_in, check_out, room_type)
        )
        conn.commit()
        conn.close()

        return render_template('confirmation.html',
            guest_name = guest_name,
            check_in = check_in,
            check_out = check_out,
            room_type = room_type
        )

    return render_template('reservation.html')

@app.route('/manager')
def manager():
    conn = get_db()
    reservations = conn.execute("SELECT * FROM Reservation").fetchall()
    conn.close()
    return render_template('manager.html', reservations=reservations)

if __name__ == '__main__':
    app.run(debug=True)
