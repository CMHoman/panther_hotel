import sqlite3

def init_db():
    conn = sqlite3.connect('hotel.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS Room (
            room_id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_number TEXT NOT NULL UNIQUE,
            room_type TEXT NOT NULL,
            price REAL NOT NULL,
            available INTEGER NOT NULL DEFAULT 1
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS Reservation(
            reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
            guest_name TEXT NOT NULL,
            check_in TEXT NOT NULL,
            check_out TEXT NOT NULL,
            room_type TEXT NOT NULL
        )
    ''')

    # Insert Sample Rooms

    c.execute("SELECT COUNT(*) FROM Room")
    if c.fetchone()[0] == 0:
        c.executemany("INSERT INTO Room(room_number, room_type, price, available) values (?,?,?,?)", [('101', 'Single', 98.99, 1), ('102', 'Double', 119.99, 1), ('103', 'Suite', 199.99, 1), ('104', 'Single', 89.99, 1), ('105', 'Double', 119.99, 1)])

    conn.commit()
    conn.close()
