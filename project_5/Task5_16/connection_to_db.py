import psycopg2


try:


    connection = psycopg2.connect(

        host="localhost",          
        port="5433",               
        user="postgres",           
        password="example",        
        database="testdb"          
    )
    print("Подключение к базе данных прошло успешно!")

except Exception as error:
    print(f"Ошибка при подключении: {error}")