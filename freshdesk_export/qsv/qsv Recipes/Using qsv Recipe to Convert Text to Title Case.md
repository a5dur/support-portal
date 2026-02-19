---
title: "Using qsv Recipe to Convert Text to Title Case"
tags: []
created_at: 2024-09-06T11:50:30Z
updated_at: 2024-09-11T02:45:02Z
---

# Using qsv Recipe to Convert Text to Title Case

*from*[*qsv recipes repository*](https://github.com/dathere/qsv-recipes/tree/main/qsv/INCOMING/Recipes%200.0.1)

This recipe shows how to convert the text in a CSV column to Title Case, where the first letter of each word is capitalized.  
 

## Usage: Before running the recipe, make sure to enter the column index on which transformation needs to occur in the recipe code.

**Convert text to Title Case**

Use the following command to apply the Title Case transformation:

```
qsv luau map name Titlecase.lua filename.csv -o output_filename.csv
```

- Replace '`Titlecase.lua'` with the filename of this Lua script.
- Replace '`filename.csv'` with your input CSV file.

**Preview Title Case transformation**

To preview the transformed CSV without saving, use the following command

```
 qsv luau map name Titlecase.lua filename.csv | qsv table
```

## Example:

Suppose you have a CSV file `names.csv` with a column that contains names in lowercase. To convert these names to Title Case, run:

qsv luau map name titlecase.lua 

## Notes:

- By default, the script converts the text in the first column (index 1). You can modify the script to specify a different column.
- The transformation applies to alphabetic characters and leaves other elements (e.g., punctuation) unchanged.

## Additional Links:

Learn more about [Lua command here](https://github.com/jqnatividad/qsv/blob/master/src/cmd/luau.rs#L2)

More Articles on [qsv Recipes](https://support.dathere.com/support/solutions/folders/154000405229)