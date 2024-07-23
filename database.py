import mysql.connector
def get_data():
    mydb=mysql.connector.connect(host="localhost",user="root",password="ajin123",database="db")
    mycursor=mydb.cursor()
    mycursor.execute("SELECT * FROM todo")
    result=mycursor.fetchall()
    mydb.close()
    return result