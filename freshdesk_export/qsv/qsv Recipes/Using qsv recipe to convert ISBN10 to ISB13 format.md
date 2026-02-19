---
title: "Using qsv recipe to convert ISBN10 to ISB13 format"
tags: []
created_at: 2024-04-23T13:31:56Z
updated_at: 2024-05-06T13:27:59Z
---

# Using qsv recipe to convert ISBN10 to ISB13 format

## Usage:

1. Before running the recipe, make sure to enter the column index which contains the ISBN-10 numbers in the code.

2. Use the following qsv command to convert ISBN-10 numbers to ISBN-13 format and add them as a new column named 'ISBN-13' in the CSV:

   

```
    qsv luau map 'ISBN-13' isbn_conversion.luau filename.csv -o newfile.csv
```

    

   - Replace 'isbn\_conversion.luau' with the filename of this Lua script.

   - Replace 'filename.csv' with the name of your input CSV file.

   - The '-o' option is used to specify the output filename ('newfile.csv' in this example).

3. When you have the file and the recipe in different file locations

        

```
        qsv luau map 'ISBN-13' file:<Path of this recipe> filename.csv -o newfile.csv
```

        When you need real-time preview of the csv file 

        qsv luau map 'ISBN-13' isbn\_conversion.luau filename.csv | qsv table

## Example:

Suppose the input CSV file 'books.csv' contains a column 'ISBN-10' which contains ISBN-10 numbers. To convert these ISBN-10 numbers to ISBN-13 format and add them as a new column named 'ISBN-13' in the CSV, use the following command:

```
qsv luau map 'ISBN-13' isbn_conversion.luau books.csv -o books_with_isbn13.csv
```

## Additional Links:

Learn more about [Lua command here](https://github.com/jqnatividad/qsv/blob/master/src/cmd/luau.rs#L2)

More Articles on [qsv Recipes](https://support.dathere.com/support/solutions/folders/154000405229)