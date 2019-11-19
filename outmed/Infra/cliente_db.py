import sqlite3


def novo(cliente):
    nome = cliente.values()
    sobrenome = cliente.values()
    email = cliente.values()
    print("Dados passados para a funcao", cliente)
    con = sqlite3.connect('db.sqlite3')
    try:
        cur = con.cursor()
        cur.execute("insert into Cliente(first_name, last_name, email) \
            values(?, ?, ?)", nome, sobrenome, email)
        con.commit()
    except:
        con.rollback()
    finally:
        con.close()