---
title: "Using "Accent2English" recipe with qsv"
tags: []
created_at: 2024-04-23T13:28:22Z
updated_at: 2024-05-06T13:29:18Z
---

# Using "Accent2English" recipe with qsv

## Usage:

1. Before running the recipe, make sure to enter the column index which contains the names with diacritic characters in the code.

2. Use the following qsv command to replace diacritic characters with English characters and add them as a new column named 'Names' in the CSV:

   

```
qsv luau map 'Names' diacritic_to_english.luau filename.csv -o newfile.csv
```

    

   - Replace 'diacritic\_to\_english.luau' with the filename of this **Lua script**.

   - Replace 'filename.csv' with the name of your input **CSV file**.

   - The '-o' option is used to specify the **output filename** ('newfile.csv' in this example).

3. When you have the file and the recipe in different file locations 

```
qsv luau map 'Names' file:<Path of this recipe> filename.csv -o newfile.csv
```

    When you need real-time preview of the csv file

```
qsv luau map 'Names' diacritic_to_english.luau filename.csv | qsv table
```

## Example:

Suppose the input CSV file 'people.csv' contains a column 'Name' which contains names with diacritic characters. To replace these diacritic characters with English characters and add them as a new column named 'Names' in the CSV, use the following command:

```
qsv luau map 'Names' diacritic_to_english.luau people.csv -o people_with_english_names.csv
```

## Additional Links:

Learn more about [Lua command here](https://github.com/jqnatividad/qsv/blob/master/src/cmd/luau.rs#L2)

More Articles on [qsv Recipes](https://support.dathere.com/support/solutions/folders/154000405229)