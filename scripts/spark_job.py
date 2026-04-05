from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("BasicAnalytics").getOrCreate()

# Load CSV
df = spark.read.csv("data/data.csv", header=True, inferSchema=True)

# Basic analytics
df.describe().show()

spark.stop()
