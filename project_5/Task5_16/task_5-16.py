import psycopg2

# Параметры подключения к базе данных (из вашего docker-compose.yml)
DB_CONFIG = {
    'host': 'localhost',
    'port': '5435',  # Порт проброшен как 5435:5432
    'user': 'postgres',  # POSTGRES_USER
    'password': 'student',  # POSTGRES_PASSWORD
    'database': 'student_task'  # POSTGRES_DB
}

try:
    # Устанавливаем соединение с базой данных
    connection = psycopg2.connect(**DB_CONFIG)
    print("Успешно подключились к базе данных PostgreSQL!")

    # Создаём курсор для выполнения запросов
    cursor = connection.cursor()

    # Выполняем SQL‑запрос: выбираем все записи из таблицы products, где категория — «Электроника»
    cursor.execute("SELECT * FROM products WHERE category = 'Электроника';")

    # Извлекаем все строки результата
    products_data = cursor.fetchall()

    # Выводим результат в удобном формате
    print("\nТовары из категории «Электроника»:")
    if products_data:
      for row in products_data:
        print(row)
    else:
     print("В категории «Электроника» нет товаров.")


except Exception as error:
    print(f"Ошибка при работе с PostgreSQL: {error}")

finally:
    # Закрываем курсор и соединение (выполняется всегда, даже при ошибке)
    if cursor:
        cursor.close()
    if connection:
        connection.close()
        print("\nСоединение с базой данных закрыто.")
