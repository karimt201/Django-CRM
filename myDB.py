import mysql.connector

database = mysql.connector.connect(
    host = 'localhost' ,
    user = 'root' ,
    password = '123456'

)

cursorobject = database.cursor()

cursorobject.execute("CREATE DATABASE crm")
print('all done')