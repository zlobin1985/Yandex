from ex_def import get_session

# Задаём значение аргумента a
a = 51

# Вызываем функцию и сохраняем результат
#result = get_session(

# Выводим результат
spark = get_session()

df = spark.sql("SELECT * FROM my_catalog.my_table")
df.show()