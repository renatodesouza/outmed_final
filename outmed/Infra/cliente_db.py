import sqlite3

def novo(cliente):
    con = sqlite3.connect('banco_dados')
    try:
        cur = con.cursor()
        cur.execute("insert into Cliente(id, first_name, last_name, email, celular, fixo, cidade, bairro, rua, numero, cep) \
            values(:id, :first_name, last_name :email, :celular, :fixo, :cidade, :bairro, :rua, :numero, :cep)", aluno.__dict__())
        con.commit()
    except:
        con.rollback()
    finally:
        con.close()