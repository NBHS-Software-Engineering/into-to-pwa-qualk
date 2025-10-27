import sqlite3 as sql

def listExtension():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    data = cur.execute('SELECT * FROM extension').fetchall()
    con.close()
    return data

def insertContact(email, name):
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    try:
        cur.execute("INSERT INTO contact_list (email,name) VALUES (?,?)", (email, name))
        con.commit()
        result = True
    except sql.IntegrityError as e:
        if "UNIQUE constraint failed: contact_list.email" in str(e): # duplicate check
            result = "duplicate"
        else:
            result = False
    con.close()
    return result