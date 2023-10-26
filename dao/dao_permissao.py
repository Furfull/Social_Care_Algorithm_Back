from app.dao.dao import connect_database
from app.schemas.permissao import *
from mysql.connector import Error

def CreatePermission():

    try:
        connection, cursor = connect_database()

        query = f""" INSERT INTO sca_db.permissions(
        facebook,
        instagram,
        twitter,
        spotify,
        tiktok)
        VALUES (0,
        0,
        0,
        0,
        0);
        """

        cursor.execute(query)
        connection.commit()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return "OK"
    
    except Error as erro:
        return {"Error: {}".format(erro)}


def PermissionFacebookState(id: int) -> PermissionFacebookGetState:

    try:
        connection, cursor = connect_database()

        query = f""" SELECT facebook FROM sca_db.permissions WHERE id = {id};"""

        cursor.execute(query)

        item = cursor.fetchall()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return item
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def UpdatePermission(id: int, state: int) -> int:

    try:
        connection, cursor = connect_database()

        query = f""" UPDATE sca_db.permissions 
        SET facebook = {state}
        WHERE id = {id};"""

        cursor.execute(query)
        connection.commit()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return id, state
    
    except Error as erro:
        return {"Error: {}".format(erro)}
    