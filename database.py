import mysql.connector

def initialize_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )

    cursor = conn.cursor()
    create_database(cursor)
    create_table(cursor)
    create_table2(cursor)

    return conn, cursor

def create_database(cursor):
    
    cursor.execute("SHOW DATABASES")
    temp = cursor.fetchall()
    databases = [item[0] for item in temp]
    
    cursor.execute("CREATE DATABASE IF NOT EXISTS registrocarros")
    cursor.execute("USE registrocarros")

def create_table(cursor):  
    cursor.execute("SHOW TABLES")
    temp = cursor.fetchall()
    tables = [item[0] for item in temp]
     
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, firstName VARCHAR(100), lastName VARCHAR(100), password VARCHAR(30), email VARCHAR(100) UNIQUE, gender VARCHAR(1), age INT, address VARCHAR(200))")
 
def login(cursor, data):
    cursor.execute(f"""SELECT * FROM users WHERE email = '{data["email"]}' 
                       AND password = '{data["password"]}' """)
     
    if cursor.fetchone() != None:
        return True
    return False
 
def register(cursor, conn, data):
    print(data)
 
    cursor.execute(f"""INSERT INTO users values(
        NULL,
        '{data["firstName"]}', 
        '{data["lastName"]}', 
        '{data["password"]}', 
        '{data["email"]}', 
        '{data["gender"]}', 
        '{data["age"]}', 
        '{data["address"]}'
    )""")
 
    conn.commit()

def create_table2(cursor):  
    cursor.execute("SHOW TABLES")
    temp = cursor.fetchall()
    tables = [item[0] for item in temp]
     
    if "carros" not in tables:
        cursor.execute("CREATE TABLE carros(id INT AUTO_INCREMENT PRIMARY KEY, marca VARCHAR(100), modelo VARCHAR(100), ano INT(4), placa VARCHAR(100) UNIQUE, km FLOAT, preco FLOAT, cor VARCHAR(200))")
        
def register2(cursor, conn, data):
    cursor.execute(f"""INSERT INTO carros (marca, modelo, ano, placa, km, preco, cor) VALUES (
        '{data["marca"]}',
        '{data["modelo"]}',
        {data["ano"]},
        '{data["placa"]}',
        {data["km"]},
        {data["preco"]},
        '{data["cor"]}'
    )""")
    conn.commit()


def excluir_carro_por_placa(cursor, conn, data):
    cursor.execute(f"""DELETE FROM carros WHERE placa = (
                   '{data["placa"]}'
    )""")
    conn.commit()

def atualizar_carro_preco(cursor, conn, data):
    cursor.execute(f"""UPDATE carros SET preco = {data["preco"]} WHERE placa = '{data["placa"]}'""")
    conn.commit()

conn, cursor = initialize_connection()