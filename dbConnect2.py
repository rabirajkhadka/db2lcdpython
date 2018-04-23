from mysql.connector import MySQLConnection, Error
from dbConfig import read_db_config
 
old_id = 0
new_id = 0
Humidity = 0
Temperature = 0

def connect():
    """ Connect to MySQL database """
 
    db_config = read_db_config()

    global old_id
    
    try:
        conn = MySQLConnection(**db_config)
 
        if conn.is_connected():
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM dht11 ORDER BY id DESC LIMIT 1")
            
            for row in cursor:
                new_id = row["id"]

            if(old_id != new_id):
                old_id = new_id
                Humidity = row["Humidity"]
                Temperature = row["Temperature"]
                print("Humidity:{} \nTemperature:{}".format(Humidity,Temperature))            
        else:
            print('connection failed.')
 
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()
 

if __name__ == '__main__':
    connect()