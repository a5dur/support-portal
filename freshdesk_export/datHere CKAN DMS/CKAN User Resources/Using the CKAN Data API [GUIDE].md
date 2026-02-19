---
title: "Using the CKAN Data API [GUIDE]"
tags: []
created_at: 2024-03-19T12:12:43Z
updated_at: 2024-03-19T14:13:03Z
---

# Using the CKAN Data API [GUIDE]

Data stored in the CKAN Instance can be accessed using the Application Programmatic Interface (API), which is a built-in feature of CKAN. For secured data that is not publicly accessible, credentials must be provided along with the API call. The API is particularly helpful for tasks such as uploading, accessing, and downloading multiple files or datasets regularly for processing through software pipelines or tool sets.

API Use Cases

- Get existing projects, datasets (packages), and resources
- Edit dataset or resource level metadata
- Add new resoureces to datasets
- Add new datasets to projects

The Data API can be accessed via the following actions of the CKAN action API.

- Create    https://data.dathere.com/api/3/action/datastore\_create
- Update / Insert    https://data.dathere.com/api/3/action/datastore\_upsert
- Query    https://data.dathere.com/api/3/action/datastore\_search
- Query (via SQL)    <https://data.dathere.com/api/3/action/datastore_search_sql>

Building Requests

The format of the request is

<data.dathere>/api/3/action/<action>

Actions in CKAN adhere to a consistent format. They typically begin with an entity and end with a verb. Entities encompass items such as projects, packages, resources, and revisions, among others. Verbs include list, show, create, update, patch, and delete. For example, you might encounter actions like project\_list, resource\_show, or package\_delete, depending on the task at hand."