---
title: "Using qsv Recipe to Trim Whitespaces from Multiple Columns"
tags: []
created_at: 2024-09-06T11:38:08Z
updated_at: 2024-09-10T14:15:33Z
---

# Using qsv Recipe to Trim Whitespaces from Multiple Columns

This recipe demonstrates how to trim leading and trailing whitespaces from one or more columns in a CSV file using qsv.

## Usage:

**Trim whitespaces from a single column**

Use the following command to trim whitespaces and save the output:

```
qsv luau map --remap Newcolumn Trim.lua filename.csv -o output_filename.csv
```

- Replace Trim.lua with the filename of this Lua script.
- Replace filename.csv with the input CSV file.
- The --remap option is used to create a new column with the trimmed values.

**Trim whitespaces from multiple columns**

To trim whitespaces from multiple columns at once, specify the column names in the --remap option:

```
qsv luau map --remap col1,col2,col3 Trim.lua filename.csv -o output_filename.csv
```

**Preview the trimmed CSV without saving**

You can also preview the trimmed CSV file directly in the terminal without saving the output:

```
qsv luau map --remap col1,col2,col3 Trim.lua filename.csv | qsv table
```

**Example:**

Suppose the CSV file data.csv contains several columns with extra whitespaces. To remove the whitespaces from Name and Address columns, run the following command:

```
qsv luau map --remap Name,Address Trim.lua data.csv -o data_trimmed.csv
```

**Notes:**

Ensure to specify the correct column names when using the --remap option.

If you only need to trim a single column, you can omit additional column names.

## Additional Links:

Learn more about [Lua command here](https://github.com/jqnatividad/qsv/blob/master/src/cmd/luau.rs#L2)

More Articles on [qsv Recipes](https://support.dathere.com/support/solutions/folders/154000405229)