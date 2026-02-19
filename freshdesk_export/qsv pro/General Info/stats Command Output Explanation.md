---
title: "stats Command Output Explanation"
tags: []
created_at: 2024-09-06T13:02:03Z
updated_at: 2024-09-08T11:20:46Z
---

# stats Command Output Explanation

The `qsv stats` command computes summary statistics and infers data types for each column in a CSV file. Here's a detailed explanation of the output: 

## Basic Information

- **field**: The name of the column (or its index if --no-headers is used).
- **type**: Inferred data type (NULL, Integer, String, Float, Date, DateTime, or Boolean).
- **is\_ascii**: Whether the column contains only ASCII characters (true/false).

## Numeric Statistics

- **sum**: The total sum of all numeric values in the column.
- **min**: The minimum value in the column.
- **max**: The maximum value in the column.
- **range**: The difference between the maximum and minimum values.
- **sort\_order**: The sorting order of the column (ASCENDING, DESCENDING, or UNSORTED).
- **min\_length**: The length of the shortest value in the column.
- **max\_length**: The length of the longest value in the column.
- **mean**: The average value of the column.
- **sem**: Standard Error of the Mean, a measure of the precision of the sample mean.
- **stddev**: Standard deviation, a measure of variability in the data.
- **variance**: The average of the squared differences from the mean.
- **cv**: Coefficient of Variation, the ratio of the standard deviation to the mean.
- **nullcount**: The number of null or empty values in the column.
- **max\_precision**: The maximum number of decimal places in numeric values.
- **sparsity**: The proportion of null or empty values in the column.

## Advanced Statistics (requires --everything or specific flags)

- **median**: The middle value when the data is sorted (requires --median or --everything).
- **mad**: Median Absolute Deviation, a robust measure of variability (requires --mad or --everything).
- **lower\_outer\_fence**: Q1 - 3 \* IQR, used to identify extreme outliers.
- **lower\_inner\_fence**: Q1 - 1.5 \* IQR, used to identify mild outliers.
- **q1**: First quartile (25th percentile).
- **q2\_median**: Second quartile (50th percentile, same as median).
- **q3**: Third quartile (75th percentile).
- **iqr**: Interquartile Range, the difference between Q3 and Q1.
- **upper\_inner\_fence**: Q3 + 1.5 \* IQR, used to identify mild outliers.
- **upper\_outer\_fence**: Q3 + 3 \* IQR, used to identify extreme outliers.
- **skewness**: A measure of the asymmetry of the probability distribution.
- **cardinality**: The number of unique values in the column (requires --cardinality or --everything).
- **mode**: The most frequent value(s) in the column (requires --mode or --everything).
- **mode\_count**: The number of modes.
- **mode\_occurrences**: The number of times the mode(s) appear.
- **antimode**: The least frequent non-zero value(s) in the column.
- **antimode\_count**: The number of antimodes.
- **antimode\_occurrences**: The number of times the antimode(s) appear.

## Date and Time Statistics

When --infer-dates is enabled, additional date-specific statistics are computed:

- Date range, standard deviation, variance, MAD, and IQR are returned in days.
- DateTime results are in RFC3339 format.
- Date results are in "yyyy-mm-dd" format in the UTC timezone.

## Notes

- The default "streaming" statistics (sum, min/max/range, sort order, min/max length, mean, sem, stddev, variance, cv, nullcount, max\_precision, sparsity) can be computed efficiently on large CSV files.
- Advanced statistics require loading the entire file into memory and must be explicitly enabled.
- The command supports various caching options to improve performance on subsequent runs.
- The stats command is central to qsv and underpins other commands like `frequency`, `schema`, `validate`, and `tojsonl`.  
    
  For more detailed information on specific options and usage, refer to the `qsv stats --help` output.