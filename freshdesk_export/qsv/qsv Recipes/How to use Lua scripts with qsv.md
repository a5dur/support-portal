---
title: "How to use Lua scripts with qsv"
tags: ["qsv", "recipes", "lua", "video tutorial", "tutorial"]
created_at: 2024-05-01T12:21:42Z
updated_at: 2024-05-02T13:17:11Z
---

# How to use Lua scripts with qsv

## Introduction:

qsv offers a wide range of commands for the endless wrangling applications. But what if you encounter a specific operation that requires a tailored solution? —qsv has you covered with its own domain-specific language for data wrangling: **Lua.**

Imagine you're using the lua command for a simple operation like this:

```
qsv luau map c "a + b" (where a, b, and c = column names).
```

However, as your data wrangling needs grow more complex, typing out long scripts on the command line becomes tedious.

This is where Lua scripts come into play. By using the "file:" prefix or the ".lua/.luau" file extension, you can read non-trivial scripts directly from the filesystem. These scripts, often referred to as **'Recipes,'**offer a broader application and streamline the process of handling intricate data operations.  
  
Your qsv command now looks more like this

```
qsv luau map 'Age' age.luau filename.csv -o newfile.csv
```

This guide introduces you to the fundamentals of Lua scripts with qsv, providing practical examples for better understanding for the first time user. Lua scripts offer a powerful way to extend the capabilities of qsv, enabling you to automate repetitive tasks, perform complex data transformations, and unlock new insights from your csv files

## Video Guide:

## Instructions:

Using Lua scripts with qsv can be summarized in 3 simple steps.

- Preparation
- Navigation
- Execution

## Step 1: Prepare

- Ensure familiarity with the dataset to be utilized and define the desired outcome. In this context, the objective is to compute the running total for the "Amount" field.![](images/24Lva9UXmkv_VPJB6sABhAXuGLiQIMkQHA.png)
- Subsequently, a Lua recipe is crafted with the purpose of facilitating the computation of the running total. This tailored script is designed to streamline the process and ensure accurate calculations.![](images/5df5wYA9c3xSUt2o4k953ANW_iQwojackw.png)

### 

## Step 2: Navigation

- Open up your terminal and navigate to the directory where your dataset is stored.

  ```
  cd <file-path>  
  ```

## Step 3: Execution

- Next , using the qsv command we'll type in the command, **qsv**, new column name, in this case **"Running total"**, the filename of the Lua recipe, **file:test2.lua** and the csv, **data.csv**  

  ```
  qsv luau map "Running total" file:test2.lua data.csv
  ```

  ![](images/uZLsSapMY-lIS5PI9_SlCmMk3qL6Ew7Rvg.png)
- ```
  qsv luau map "Running total" file:test2.lua data.csv | qsv table
  ```

  We can utilize the other qsv commands like qsv table here so we can get a real time preview of our data
- ```
  qsv luau map "Running total" file:<Path of this recipe> test2.lua data.csv -o newfile.csv
  ```

  Here a new file is created by qsv which contains the changes made by the recipe

```
If the script and the dataset are saved in the same directory, the 'file:' keyword isn't necessary
```

By following the outlined steps, from gathering data to crafting Lua scripts and utilizing qsv commands, users can efficiently manipulate data and achieve precise outcomes.

## Additional Links

Learn more about [Lua command here](https://github.com/jqnatividad/qsv/blob/master/src/cmd/luau.rs#L2)

More Articles on [qsv Recipes](https://support.dathere.com/support/solutions/folders/154000405229)