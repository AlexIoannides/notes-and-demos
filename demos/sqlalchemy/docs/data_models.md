# ORM Basics

SQL Alchemy uses classes to define database table schema with class attributes used to define the type of each column. These classes and the objects created from then can then be used to read and write from the table without the need to write any SQL, as each object is mapped to a row in the table; this is object relational mapping.

The script below defines two classes that define the schema for two tables - `Person` and `Address` - that are related to one another via one-to-many relationship.

```python title="demos/sqlalchemy/models.py"
--8<-- "demos/sqlalchemy/models.py"
```
