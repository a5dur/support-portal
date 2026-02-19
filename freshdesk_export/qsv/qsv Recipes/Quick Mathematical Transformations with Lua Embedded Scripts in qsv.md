---
title: "Quick Mathematical Transformations with Lua Embedded Scripts in qsv"
tags: []
created_at: 2024-06-24T13:27:51Z
updated_at: 2024-09-10T14:15:24Z
---

# Quick Mathematical Transformations with Lua Embedded Scripts in qsv

*from*[*qsv recipes repository*](https://github.com/dathere/qsv-recipes/blob/main/qsv/INCOMING/Recipes%200.0.1/Mathematical%20Transformation.md)

#### Steps to apply Mathematical Transformations using luau command in qsv:

**Navigate to Your CSV Directory**

- Open your terminal.
- Use the `cd` command to navigate to the directory containing your CSV file.

**Copy the Command**

- Use the following command from the recipes directory (sin transformation in this case)

  ```
  qsv luau map Sine "local value = math.rad(tonumber(col['Angle'])); return math.sin(value)" angles.csv
  ```
- **qsv luau map Sine**: This part invokes qsv to apply a Lua script transformation named `Sine`.

`local value = math.rad(tonumber(col['Angle']))`: Converts the value in the 'Angle' column from degrees to radians.

`return math.sin(value)`: Computes the sine of the radian value.

**angles.csv**: This is the name of your CSV file.

**Edit the Command**

- Modify the column name (`'Angle'`) and the file name (`angles.csv`) to match your specific file and column.

**Run the Command**

- Execute the command in your terminal.
- Your CSV file will now have a new column with the transformed sine values.

And that’s it! You’ve successfully applied the Sine function to your data.

Try more from the [qsv recipes repository](https://github.com/dathere/qsv-recipes/blob/main/qsv/INCOMING/Recipes%200.0.1/Mathematical%20Transformation.md)