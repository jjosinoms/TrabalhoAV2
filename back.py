import sqlite3

""" CRUD BACKEND """


def connect():
    conn = sqlite3.connect("consultas.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS consulta (id INTEGER PRIMARY KEY, nomealuno text, nomemateria text, notaaluno number)")
    conn.commit()
    conn.close()


def insert(nomealuno, nomemateria, notaaluno):
    conn = sqlite3.connect("consultas.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO consulta VALUES (NULL,?,?,?)",
                (nomealuno, nomemateria, notaaluno))
    conn.commit()
    conn.close()
    view()


def view():
    conn = sqlite3.connect("consultas.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM consulta")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(nomealuno="", nomemateria="", notaaluno=""):
    conn = sqlite3.connect("consultas.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM consulta WHERE nomealuno=? OR nomemateria=? OR notaaluno=?",
                (nomealuno, nomemateria, notaaluno))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("consultas.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM consulta WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, nomealuno, nomemateria, notaaluno):
    conn = sqlite3.connect("consultas.db")
    cur = conn.cursor()
    cur.execute("UPDATE consulta SET nomealuno=?, nomemateria=?, notaaluno=? WHERE id=?",
                (nomealuno, nomemateria, notaaluno, id))
    conn.commit()
    conn.close()


connect()
