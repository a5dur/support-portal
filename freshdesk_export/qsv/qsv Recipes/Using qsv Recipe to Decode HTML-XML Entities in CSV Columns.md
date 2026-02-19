---
title: "Using qsv Recipe to Decode HTML/XML Entities in CSV Columns"
tags: []
created_at: 2024-09-06T11:43:27Z
updated_at: 2024-09-10T14:15:44Z
---

# Using qsv Recipe to Decode HTML/XML Entities in CSV Columns

This recipe helps you decode common HTML/XML entities (like `&amp;`, `&lt;`, etc.) in a specific CSV column, replacing them with their respective characters.

## Usage:

**Decode entities in a column**

Use the following command to decode HTML/XML entities and save the output:

```
qsv luau map --map DecodedColumn decode_entities.lua filename.csv -o output_filename.csv 
```

- Replace `decode_entities.lua` with the filename of this Lua script.
- Replace `filename.csv` with the input CSV file.

**Preview the decoded content**

To preview the decoded column without saving the file, use this command:  

```
qsv luau map --remap DecodedColumn decode_entities.lua filename.csv | qsv table
```

#### 

#### **Notes:**

- This script decodes common entities like `&amp;`, `&lt;`, `&gt;`, `&quot;`, and `&apos;`.

## 

## Additional Links:

Learn more about [Lua command here](https://github.com/jqnatividad/qsv/blob/master/src/cmd/luau.rs#L2)

More Articles on [qsv Recipes](https://support.dathere.com/support/solutions/folders/154000405229)