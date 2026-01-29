from ex_def import get_session

# Открываем сессию spark и показываем таблицу
spark = get_session()

df = spark.sql("SELECT * FROM my_catalog.my_table")
df.show()