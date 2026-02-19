---
title: "Using "Calculate Age" recipe with qsv"
tags: []
created_at: 2024-04-23T13:00:20Z
updated_at: 2024-05-06T13:30:15Z
---

# Using "Calculate Age" recipe with qsv

## Usage:

1. Before running the recipe, make sure to enter the column index which contains the birthdate in the code
2. Use the following qsv command to calculate the age and add it as a new column named 'Age' in the CSV:

   ```
       qsv luau map 'Age' age.luau filename.csv -o newfile.csv
   ```

       

   - Replace 'age.luau' with the filename of this Lua script.
   - Replace 'filename.csv' with the name of your input CSV file.
   - The '-o' option is used to specify the output filename ('newfile.csv' in this example).
3. Let's say you have the file and the recipe is in different location

   ```
       qsv luau map 'Age' file:<Path of the recipe> filename.csv -o newfile.csv
   ```

   When you need real-time preview of the csv file

   ```
       qsv luau map 'Age' age.luau filename.csv | qsv table
   ```

## Example:

Suppose the input CSV file 'people.csv' contains a column 'Birthdate' which contains birthdates in the format 'dd-mm-yyyy'.   
To calculate the age based on these birthdates and add it as a new column named 'Age' in the CSV, use the following command:

```
    qsv luau map 'Age' age.luau people.csv -o people_with_age.csv
```

## Additional Links:

Learn more about [Lua command here](https://github.com/jqnatividad/qsv/blob/master/src/cmd/luau.rs#L2)

More Articles on [qsv Recipes](https://support.dathere.com/support/solutions/folders/154000405229)