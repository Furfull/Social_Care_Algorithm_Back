from app.dao.dao import connect_database
from app.schemas.form import Form
from mysql.connector import Error

def CreateForm():

    try:
        connection, cursor = connect_database()

        query = f""" INSERT INTO sca_db.form(
        pcd,
        gender,
        sexuality,
        ethny,
        money)
        VALUES (
        "null",
        "null",
        "null",
        "null",
        "null");
        """

        cursor.execute(query)
        connection.commit()

        if (connection.is_connected()):
            cursor.close()
            connection.close()
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def UpdateFormByUserId(form: Form, user_id: int):

    try:
        connection, cursor = connect_database()

        query = f"""UPDATE sca_db.form
        SET 
        pcd = "{form.pcd}",
        gender = "{form.gender}",
        sexuality = "{form.sexuality}",
        ethny = "{form.ethny}",
        money = "{form.money}"
        WHERE id = {user_id};
        """
        cursor.execute(query)
        connection.commit()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return "UPDATED"
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def GetFormByRate(column: str, item: str):

    try:
        connection, cursor = connect_database()

        query = f""" SELECT * FROM sca_db.form WHERE {column} = "{item}";"""

        cursor.execute(query)
        item = cursor.fetchall()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return item
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def GetFormByUserId(user_id: int):

    try:
        connection, cursor = connect_database()

        query = f""" SELECT * FROM sca_db.form WHERE id = "{user_id}";"""

        cursor.execute(query)
        item = cursor.fetchall()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return item
    
    except Error as erro:
        return {"Error: {}".format(erro)}
    
def GetAllForm():

    try:
        connection, cursor = connect_database()

        query = f""" SELECT * FROM sca_db.form;"""

        cursor.execute(query)
        item = cursor.fetchall()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return item
    
    except Error as erro:
        return {"Error: {}".format(erro)}