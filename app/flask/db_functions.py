import mysql.connector


def create_db_connection(db_host, db_port, db_user, db_password, db_name):
    connection = mysql.connector.connect(
        host=f"{db_host}",
        port=f"{db_port}",
        user=f"{db_user}",
        password=f"{db_password}",
        database=f"{db_name}"
    )
    print("DB connected!")
    return connection


def getHealthCheck(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT 1;")
    result = cursor.fetchall()
    cursor.close()
    return result[0][0]
    
        
def add_mail(connection, name, email, time):
    cursor = connection.cursor()
    sql = f"INSERT INTO Emails (`name`, `email`, `time`) VALUES ('{name}', '{email}', '{time}');"
    cursor.execute(sql)
    connection.commit()
    cursor.close()

    
def get_mails(connection):
    cursor = connection.cursor()
    sql = "SELECT email FROM Emails;"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    return result


def get_all(connection):
    cursor = connection.cursor()
    sql = "SELECT * FROM Emails;"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    return result    


def get_mail_from_name(connection, name):
    cursor = connection.cursor()
    sql = f"SELECT email FROM Emails WHERE name='{name}';"
    cursor.execute(sql)
    try:
        result = cursor.fetchall()[0]
    except:
        result = {"No mails where found"}
    cursor.close()
    return result


def get_name_from_mail(connection, mail):
    cursor = connection.cursor()
    sql = f"SELECT name FROM Emails WHERE email='{mail}';"
    cursor.execute(sql)
    try:
        result = cursor.fetchall()[0]
    except:
        result = "No names where found"
    cursor.close()
    return result

def delete_by_name(connection, name):
    cursor = connection.cursor()
    sql = f"DELETE FROM Emails WHERE name='{name}';"
    try:
        cursor.execute(sql)
    except:
        pass
    result = "Your name has removed from the database"
    cursor.close()
    return result

def add_score(connection, user, score):
    cursor = connection.cursor()
    sql = f"INSERT INTO Scores (`user`, `score`) VALUES ('{user}', '{score}');"
    cursor.execute(sql)
    connection.commit()
    cursor.close()

def get_scores(connection):
    cursor = connection.cursor()
    sql = "SELECT score, user FROM Scores ORDER BY score DESC LIMIT 5;"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    return result   
