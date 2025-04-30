import sqlite3

def film_db():
    conn = sqlite3.connect("films.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS films (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            genre TEXT,
            year TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_film(name, genre, year):
    conn = sqlite3.connect('films.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO films (name, genre, year) VALUES (?, ?, ?)", (name, genre, year))
    conn.commit()
    conn.close()

def get_films():
    conn = sqlite3.connect("films.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, genre, year FROM films")
    films = cursor.fetchall()
    conn.close()
    return films

def delete_all_films():
    conn = sqlite3.connect("films.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM films")
    conn.commit()
    conn.close()

def delete_film_by_id(film_id):
    conn = sqlite3.connect("films.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM films WHERE id=?", (film_id,))
    conn.commit()
    conn.close()
