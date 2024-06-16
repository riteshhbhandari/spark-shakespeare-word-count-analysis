# Databricks notebook source
#create a directory to store the text file
dbutils.fs.mkdirs("/FileStore/shared_uploads/500097161@stu.upes.ac.in/Shakespeare-work-count-analysis/")

# COMMAND ----------

# Display the text file
rdd = spark.sparkContext.textFile("/FileStore/shared_uploads/500097161@stu.upes.ac.in/Shakespeare-work-count-analysis/Shakespeare_work_count_analysis-1.txt")
rdd.collect()

# COMMAND ----------

#read the text file and store it in a new RDD
file_path = "/FileStore/shared_uploads/500097161@stu.upes.ac.in/Shakespeare-work-count-analysis/Shakespeare_work_count_analysis-1.txt"  
# Update with your uploaded file path
text_rdd = sc.textFile(file_path)


# COMMAND ----------

rdd_flatmap=text_rdd.flatMap(lambda line: line.split())
rdd_map=rdd_flatmap.map(lambda word: (word.lower(),1))
rdd_reduce=rdd_map.reduceByKey(lambda x,y : x+y)
rdd_reduce.collect()

# COMMAND ----------

# Step 3: Convert to DataFrame for easier analysis
word_counts_df = rdd_reduce.toDF(["word", "count"])

# COMMAND ----------

# Step 4: Analyze the most frequent words
most_frequent_words = word_counts_df.orderBy(word_counts_df["count"].desc())

# COMMAND ----------

# Display the results
most_frequent_words.show(20)
