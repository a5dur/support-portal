---
title: "Using qsv recipe to Validate ISBN codes"
tags: []
created_at: 2024-04-23T13:37:55Z
updated_at: 2024-05-06T13:26:59Z
---

# Using qsv recipe to Validate ISBN codes

## Usage:

1. Before running the recipe, make sure to enter the column index which contains the ISBN numbers in the code.
2. Use the following qsv command to validate ISBN numbers and add the validation result as a new column named 'Validation' in the CSV:  

   ```
   qsv luau map 'Validation' validate_isbn.luau filename.csv -o newfile.csv
   ```

   - Replace 'validate\_isbn.luau' with the filename of this Lua script.  
   - Replace 'filename.csv' with the name of your input CSV file.  
   - The '-o' option is used to specify the output filename ('newfile.csv' in this example).
3. When you have the file and the recipe in different file locations  

   ```
   qsv luau map 'Validation' file:<Path of this recipe> filename.csv -o newfile.csv
   ```

   When you need real-time preview of the csv file 

   ```
   qsv luau map 'Validation' validate_isbn.luau filename.csv | qsv table
   ```

## Example:

Suppose the input CSV file 'books.csv' contains a column 'ISBN' which contains ISBN numbers. To validate these ISBN numbers and add the validation result as a new column named 'Validation' in the CSV, use the following command:

```
qsv luau map 'Validation' validate_isbn.luau books.csv -o books_with_validation.csv
```

## Additional Links:

Learn more about [Lua command here](https://github.com/jqnatividad/qsv/blob/master/src/cmd/luau.rs#L2)

More Articles on [qsv Recipes](https://support.dathere.com/support/solutions/folders/154000405229)