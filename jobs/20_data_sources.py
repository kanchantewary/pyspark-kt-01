#spark certification practice - definitive guide - chapter 9 - data sources

from pyspark.sql import SparkSession
spark = SparkSession.Builder().appName("chapter7").master("local[3]").getOrCreate()


#read csv

spark.read.format("csv")\
        .option("mode","permissive")\
        .option("inferSchema","true")\
        .option("path","")\
        .schema(someschema)\
        .load

#write csv


#read json

#write json


#read parquet files


#write parquet files


#read ORC files


#write ORC files


#read from SQL databases (MySQL say) using jdbc

#write into MySQL

#query pushdown

#read from db in parallel

#reading text files

#writing text files

#reading file data in parallel

#writing data in parallel


#bucketing


#managing file size



#--------------------------

#read from Mongo DB

#write into Mongo DB


#read xml files

#write xml files
