---
title: "Advanced Search Techniques in CKAN"
tags: []
created_at: 2024-02-29T14:15:00Z
updated_at: 2024-03-05T14:21:31Z
---

# Advanced Search Techniques in CKAN

From basic searches to advanced queries, CKAN provides a versatile toolkit for discovering the right data at the right time. Whether you're a researcher seeking specific insights or a data enthusiast exploring diverse datasets, understanding CKAN's search functionality is the key to unlocking the full potential of your data catalog.  
  
![](images/Mf43IxuV05zJV_7FVY6G6sN7Mv78fdxPww.png)

### Searching by Metadata Field

When you're searching and want to be more precise, you can concentrate on a specific type of information. Start by typing the kind of information you're interested in, such as "city," followed by a colon (":"). Then, write the specific term you're looking for after the colon.

For example: 

```
title: New York
```

### Boolean Operators

These operators act like filters, helping you broaden your search to get more relevant results.

**"AND" or "&&"**

When you use "AND," or "&&," it indicates that both terms on either side must be present for a match.

```
County && City
```

[Try it out on data.dathere.com](https://data.dathere.com/dataset?q=US+AND+elections&sort=score+desc%2C+metadata_modified+desc&ext_bbox=)

In this example, the search is narrowed to datasets where both "County" and "City" are present, providing more focused and relevant results.

**"NOT" or "!"**

When you use "NOT" or "!", it's like saying, "I want results that have the first term but without the second term.

```
County NOT city
```

 It helps you exclude specific terms you don't want in your search results.

**“OR” or “||”**

It signifies that either one or both of the specified terms must be present for a match.

letting you broaden your search to find datasets that have either one term, the other, or even both. 

It's a nice way to cast a wider net and gather datasets that match any of your specified terms. 

```
County OR city
```

Here, you're saying, "Give me datasets that mention either 'County,' 'City,' or both." 

```
Remember, when you're using keywords like AND or NOT as Boolean operators in your CKAN searches, they need to be in all uppercase letters. For example, type AND, NOT, or any other Boolean operator in capital letters to make sure CKAN recognizes and processes them correctly.
```

**"+" (Symbol)**

The "+" symbol is like a tag for making sure a specific term is a must-have in your search. 

```
title: US + States
```

**[Try it out on data.dathere.com](https://data.dathere.com/dataset?q=US%2BStates&sort=score+desc%2C+metadata_modified+desc&ext_bbox=)**

This is saying, "Find me datasets where the title has 'US,' and it absolutely has to include 'States' too."

**'-' (Symbol)**

The "-" symbol is like a filter for excluding specific terms you don't want in your search. 

```
title: Counties - Demographics
```

### Placeholders

**Placeholder - Single Character****"?"**

"?" symbol acts as a placeholder for a single character in your search term

for example

```
N?C
```

This search might yield matches like "NYC," "NAC," or "NOC."

**Placeholder - Multiple Characters****"\*"**

"\*". This symbol acts as a dynamic placeholder, allowing for the inclusion of multiple characters in your search term.

for example

```
NYPD*
```

[Try it out on data.dathere.com](https://data.dathere.com/dataset?q=NYPD*&sort=score+desc%2C+metadata_modified+desc&ext_bbox=)

Here, the "\*" acts as a placeholder, indicating, "Retrieve datasets related to NYPD and any subsequent characters." This search might yield matches like "NYPD Incidents," "NYPD Statistics," or "NYPD Crime Rates.

### Additional Searching Techniques

For information on even more search query parameters, check out the following article [Searching 101](https://support.dathere.com/en/support/solutions/articles/154000133906)