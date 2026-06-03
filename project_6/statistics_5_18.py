import psycopg2

import pandas as pd



try:

    # Устанавливаем соединение

    connection = psycopg2.connect(

        host="localhost",          # База в контейнере, но доступна через localhost

        port="5435",               # Порт из секции ports

        user="postgres",           # POSTGRES_USER

        password="student",        # POSTGRES_PASSWORD

        database="student_task"          # POSTGRES_DB

    )

    print("✓ Подключение установлено")



except Exception as error:

    print(f"Ошибка при подключении: {error}")

# SQL-запрос: объединяем prices и products, чтобы получить название товара и категорию для каждой цены
query = """
    SELECT
        p.price,
        pr.name AS product_name,
        pr.category AS product_category,
        p.created_at
    FROM prices p
    JOIN products pr ON p.product_id = pr.id
    ORDER BY p.created_at;
"""

# Загружаем результат запроса в DataFrame
df = pd.read_sql(query, connection)

# Выводим первые несколько строк, чтобы проверить результат
print(df.head())



print("\n=== Описательная статистика по ценам ===")
print(f"Среднее значение цены: {df['price'].mean():.2f} руб.")
print(f"Медиана цены: {df['price'].median():.2f} руб.")
print(f"Стандартное отклонение: {df['price'].std():.2f} руб.")
print(f"Минимальная цена: {df['price'].min():.2f} руб.")
print(f"Максимальная цена: {df['price'].max():.2f} руб.")

# Рассчитываем квартили и IQR
q1 = df['price'].quantile(0.25)
q2 = df['price'].quantile(0.50)  # медиана
q3 = df['price'].quantile(0.75)
iqr = q3 - q1

# Выводим рассчитанные показатели
print("\n=== Квартили и IQR ===")
print(f"Q1 (25%): {q1:.2f} руб.")
print(f"Q2 (50%, медиана): {q2:.2f} руб.")
print(f"Q3 (75%): {q3:.2f} руб.")
print(f"Межквартильный размах (IQR = Q3 − Q1): {iqr:.2f} руб.")

# Находим товары, цена которых превышает Q3, и выводим их с категориями
expensive_products = df[df['price'] > q3][['product_name', 'product_category', 'price']].sort_values(by='price', ascending=False)

print("\n=== Товары, цена которых превышает Q3 ===")
if not expensive_products.empty:
    for _, row in expensive_products.iterrows():
        print(f"Товар: {row['product_name']}, Категория: {row['product_category']}, Цена: {row['price']:.2f} руб.")
else:
    print("Товаров с ценой выше Q3 не найдено.")


# Группируем данные по категории и рассчитываем статистику
category_stats = df.groupby('product_category')['price'].agg(
    count='count',
    mean_price='mean',
    median_price='median',
    std_price='std'
).round(2)

# Сортируем по убыванию средней цены
category_stats = category_stats.sort_values(by='mean_price', ascending=False)

# Выводим результат
print("\n=== Статистика цен по категориям (отсортировано по убыванию средней цены) ===")
print(category_stats)


# Группируем по названию товара, рассчитываем мин/макс цену и разницу
price_spread = df.groupby('product_name')['price'].agg(
    min_price='min',
    max_price='max'
).round(2)

# Рассчитываем разницу между максимальной и минимальной ценой
price_spread['price_diff'] = price_spread['max_price'] - price_spread['min_price']

# Сортируем по убыванию разницы цен и берём 5 первых записей
top_5_spread = price_spread.sort_values(by='price_diff', ascending=False).head(5)

# Выводим результат
print("\n=== Пять товаров с наибольшим разбросом цен ===")
for product, row in top_5_spread.iterrows():
    print(f"Товар: {product}")
    print(f"  Минимальная цена: {row['min_price']:.2f} руб.")
    print(f"  Максимальная цена: {row['max_price']:.2f} руб.")
    print(f"  Разница цен: {row['price_diff']:.2f} руб.\n")
