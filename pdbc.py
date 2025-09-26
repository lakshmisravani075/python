import mysql.connector
info={
    'user':'root',
    'password':'Y21ece075@',
    'host':'localhost',
    'port':3306
    
}



try:
    mysql.connector.connect()
    print("connection successfull")
except:
    print("not able to connect")
