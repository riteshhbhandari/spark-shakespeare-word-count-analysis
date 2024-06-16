# Shakespeare Word Count Analysis

This project demonstrates a word count analysis on the complete works of William Shakespeare using Apache Spark on Databricks. The objective is to showcase how Spark can be used to process large text files and perform simple data analysis tasks such as counting word frequencies.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Data](#data)
- [Steps](#steps)
- [Results](#results)
- [Conclusion](#conclusion)
- [Contributing](#contributing)

## Introduction

Word count is a common example to illustrate the power of distributed data processing. In this project, we analyze the text of Shakespeare's works to count the frequency of each word. This demonstrates the use of Spark's RDDs and DataFrames to perform parallel data processing.

## Prerequisites

- Databricks account
- Basic knowledge of Spark and PySpark
- Familiarity with Databricks notebooks

## Setup

1. **Create a Databricks Account:**
   - Sign up for a free Databricks account if you don’t already have one.

2. **Create a New Databricks Workspace:**
   - Follow the instructions on the Databricks website to set up your workspace.

3. **Upload Data:**
   - Download the text file containing the complete works of Shakespeare from [Project Gutenberg](https://www.gutenberg.org/ebooks/100).
   - Upload the text file to the Databricks file system (DBFS).

## Data

The dataset used in this project is the complete works of William Shakespeare, available for free from Project Gutenberg. The file is in plain text format and contains all of Shakespeare's plays, sonnets, and poems.

## Steps

1. **Create a Spark Session:**
   - Initialize a Spark session in your Databricks notebook.

2. **Read the Text File:**
   - Load the text file into an RDD.

3. **Process the Data:**
   - Split each line into words.
   - Normalize the words to lowercase.
   - Remove punctuation and special characters.
   - Filter out empty words.

4. **Perform Word Count:**
   - Map each word to a (word, 1) pair.
   - Use `reduceByKey` to sum the counts for each word.

5. **Convert to DataFrame:**
   - Convert the RDD of word counts to a DataFrame for easier analysis and visualization.

6. **Display Results:**
   - Show the top N most frequent words.

### Example Code

```python
from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("ShakespeareWordCount").getOrCreate()

# Read text file into an RDD
rdd = spark.sparkContext.textFile("/path/to/shakespeare.txt")

# Process data
words_rdd = rdd.flatMap(lambda line: line.split(" ")) \
               .map(lambda word: ''.join(filter(str.isalnum, word)).lower()) \
               .filter(lambda word: word != "")

# Perform word count
word_pairs_rdd = words_rdd.map(lambda word: (word, 1))
word_counts_rdd = word_pairs_rdd.reduceByKey(lambda x, y: x + y)

# Convert to DataFrame
word_counts_df = word_counts_rdd.toDF(["word", "count"])

# Show top 20 most frequent words
word_counts_df.orderBy("count", ascending=False).show(20)

# Stop Spark session
spark.stop()
```

## Results

The output of the analysis will show the most frequent words in Shakespeare's works. Common English words such as "the", "and", "to" will likely top the list. More interestingly, you can filter out common stop words to find words more specific to Shakespeare's vocabulary.

## Conclusion

This project demonstrates the use of Apache Spark for processing and analyzing large text datasets. Using Databricks simplifies the setup and allows for easy scaling and sharing of the analysis.

## Contributing

Contributions are welcome! If you have any improvements or suggestions, feel free to open an issue or submit a pull request.

---

Feel free to modify this README according to the specifics of your project and environment.
