from mysql.connector import MySQLConnection, Error
from dbConfig import read_db_config
 
old_Humidity = 15.5
old_Temperature = 15.5
new_Humidity = 0.0
new_Temperature = 0.0
def connect():
    """ Connect to MySQL database """
 
    db_config = read_db_config()
    
    global old_Humidity
    global old_Temperature
    
    try:
        #print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)
 
        if conn.is_connected():
            #print('connection established.')
            cursor = conn.cursor(dictionary=True)
            #cursor.execute("SELECT Humidity,Temperature FROM dht11 ORDER BY id DESC LIMIT 1")
            cursor.execute("SELECT Humidity, Temperature FROM dht11_display where id=1")
            #print("Old Humidity: {a} \nOld Temperature: {b}".format(a=old_Humidity,b=old_Temperature))
            
            for row in cursor:
                #print("New Humidity: {Humidity} \nNew Temperature: {Temperature}" .format(Humidity=row['Humidity'], Temperature=row['Temperature']))
                new_Humidity = row["Humidity"]
                new_Temperature = row["Temperature"]

            if(old_Humidity != new_Humidity):
                old_Humidity = new_Humidity
                print("Humidity:{}".format(old_Humidity))
            if(old_Temperature != new_Temperature):
                old_Temperature = new_Temperature
                print("Temperature:{}".format(old_Temperature))    
                
            #row = cursor.fetchall()
            #print(row)
        else:
            print('connection failed.')
 
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()
        #print('Connection closed.')
 
def compare(Humidity,Temperature):
    print("A")

if __name__ == '__main__':
    connect()