---
title: "Setting Up DataStore on CKAN"
tags: []
created_at: 2024-03-15T12:33:34Z
updated_at: 2024-03-15T13:59:35Z
---

# Setting Up DataStore on CKAN

This article outlines the essential steps to seamlessly configure the DataStore extension, ensuring optimal functionality for your CKAN instance.

### Step 1: Enable the Plugin

Add the DataStore plugin to your CKAN configuration file:

```
ckan.plugins = datastore
```

### Step 2: Set Up the Database

The DataStore requires its own PostgreSQL database to store resources. To list existing databases, use the command:

```
sudo -u postgres psql -l
```

Verify that the database encoding is UTF8 to prevent internationalization issues. Changing the encoding of PostgreSQL may entail deleting existing databases, so it's crucial to address this before proceeding with the DataStore setup

### Step 3: Create users and databases

To ensure proper access control, create a database user named 'datastore\_default' with read-only access to your DataStore database, as outlined below:

Create a database\_user 'datastore\_default' this user will be given read-only access to the DataStore:

```
sudo -u postgres createuser -S -D -R -P -l datastore_default
```

Create the database 'datastore\_default' owned by 'ckan\_default':

```
sudo -u postgres createdb -O ckan_default datastore_default -E utf-8"
```

### Step 4: Setting Permissions

After creating the DataStore database and users, it's essential to configure permissions for both the DataStore and CKAN databases. CKAN offers a ckan command to assist in properly configuring these permissions.

If you have superuser privileges and can utilize the 'psql' command to connect to your database, you can employ the 'datastore set-permissions' command to generate the necessary SQL for setting permissions.

```
sudo -u postgres psql
```

this connects the database server as the postgres superuser.

To set permissions you can use this Connections 

```
ckan -c /etc/ckan/default/ckan.ini datastore set-permissions | sudo -u postgres␣ ˓→psql --set ON_ERROR_STOP=1
```

If your database server isn't local but accessible via SSH, you can transmit the permissions script over SSH using the following command:

```
ckan -c /etc/ckan/default/ckan.ini datastore set-permissions | ssh dbserver sudo -u postgres psql --set ON_ERROR_STOP=1
```

Alternatively, if you're unable to utilize the 'psql' command in this manner, you can manually copy and paste the output of:

```
ckan -c /etc/ckan/default/ckan.ini datastore set-permissions
```

into a PostgreSQL superuser console

### Step 5: Verify

Restart CKAN and run the following command to list all DataStore

resources:

```
curl -X GET "http://127.0.0.1:5000/api/3/action/datastore_search?resource_id=_table_metadata"
```

This should return a JSON page without errors.

---

### Additional Resources

For an in-depth understanding of CKAN extensions, check out the [official documentation here](https://docs.ckan.org/en/2.9/user-guide.html#datasets-and-resources).

If you need assistance or have queries, visit our [support page](http://support.dathere.com/) for more information

[►Publishing Datasets in CKAN: [Guide]](https://support.dathere.com/en/support/solutions/articles/154000133604)

[►Reordering Resources in CKAN Dataset: [Guide]](https://support.dathere.com/en/support/solutions/articles/154000133613)