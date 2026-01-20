
import sys
sys.path.append('/usr/lib/spark/python')
sys.path.append('/usr/lib/spark/python/lib/py4j-0.10.9-src.zip')
from pyspark.sql import SparkSession

def get_session():
    """
    Функция принимает число a и возвращает a + 1.
    :param a: число (int или float)
    :return: a + 1
    """
    return SparkSession.builder \
        .appName("IcebergInsertRead") \
        .config("spark.eventLog.enabled", "true") \
        .config("spark.eventLog.dir", "s3a://s3aszlobin/logs") \
        .config("spark.jars.packages",
                "org.apache.iceberg:iceberg-spark-runtime-3.0_2.12:1.0.0") \
        .config("spark.sql.extensions",
                "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
        .config("spark.sql.catalog.my_catalog",
                "org.apache.iceberg.spark.SparkCatalog") \
        .config("spark.sql.catalog.my_catalog.type", "hadoop") \
        .config("spark.sql.catalog.my_catalog.warehouse",
                "s3a://s3aszlobin/iceberg_warehouse/") \
        .getOrCreate()

# Задаём значение аргумента a
#a = 5

# Вызываем функцию и сохраняем результат
#result = add_one(a)

# Выводим результат
#print(f"Результат: {result}")  # Выведет: Результат: 6