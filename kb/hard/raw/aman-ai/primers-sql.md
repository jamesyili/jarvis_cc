# Primers • SQL

**Source:** https://aman.ai/primers/sql/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Overview](#overview)
* [Barebones SQL query](#barebones-sql-query)
* [Common SQL Keywords](#common-sql-keywords)
* [SQL Clauses Order](#sql-clauses-order)
* [Example: Solving a crime (and learning SQL!)](#example-solving-a-crime-and-learning-sql)
  + [Overview](#overview-1)
  + [Step 1: Identify tables](#step-1-identify-tables)
  + [Step 2: Check table schema (columns)](#step-2-check-table-schema-columns)
  + [Step 3:](#step-3)
* [Further Reading](#further-reading)
* [Citation](#citation)

## Overview

* SQL (Structured Query Language) is a way of interacting with an RDBMS (Relational Data Base Management System).
* SQL is one of the most widely used languages historically. ANSI SQL is a standard which is implemented in many different flavors (with intricate differences under the hood similar to how different shell scripting languages such as Bash, Zsh, Ksh, etc. differ) as multiple products such as PostgresSQL, SQLite, MYSQL, MSSQL, etc.
* Although to understand SQL and to use it efficiently, some understanding of the theory of RDBMS is necessary, in this article we will look at SQL from the perspective of an end-user who only uses SQL to find information from a database.
* SQL can widely be used for four types of tasks:
  + Query,
  + Definition,
  + Manipulation, and
  + Control.
* While all the aforementioned tasks are important and meant to be studied with the larger scope of RDBMS, we will only be looking at query tasks in this article.
* Query tasks are the tasks that we use most commonly: Business Analysts query to answer Business Questions, Data Scientists and Machine Learning Engineers query to explore the data and define hypothesis, Backend Engineers query to create systems which are in accordance to the data being worked on.
* While Data Engineers and Backend Engineers often use the other tasks of SQL, they cannot escape the use of queries. So in a way queries are very basic to anyone who has any sort of SQL usage. This is what we’ll be looking at this article.
* The following article has been written by [Soham Ghosh](https://www.linkedin.com/in/soham-ghosh-b92ba0164/) with contributions from [Aman Chadha](http://linkedin.aman.ai).

## Barebones SQL query

* The most barebones form of a query is:

```
SELECT col1,col2 FROM db.schm.tbl;
```

* This would return to us an output table in a format similar to:

| col1 | col2 |
| --- | --- |
| val1col1 | val1col2 |
| val2col1 | val2col2 |
| val3coł1 | val3col2 |

## Common SQL Keywords

* Some of the most common SQL query keywords are:
  + `SELECT`
  + `FROM`
  + `LIMIT`
  + `WHERE`
  + `LIKE/BETWEEN/IN/AND/OR/NOT`
  + `ORDER BY`
  + `(OUTER/INNER/LEFT/RIGHT) JOIN ON`
  + `UNION/UNION ALL`
  + `GROUP BY`
  + `UNIQUE` (and other AGGREGATIONS)
  + `HAVING`
  + `EXISTS (ANY/ALL)`
  + `WITH (for SUBQUERIES)`
* The [SQL Basics Cheat Sheet](https://learnsql.com/blog/sql-basics-cheat-sheet/) offers a brilliant primer of the aforementioned commands.
* It is important to note that there are multiple “means to an end” for achieving a particular end result in any SQL. In other words, the the examples and patterns in the below sections are one way of achieving the end result, but multiple ways exist. It is highly recommended to try other methods depending on their flavor of SQL and use-case.

## SQL Clauses Order

* The general order in SQL clauses feature in a SQL query are as follows:

```
SELECT DISTINCT column, AGG_FUNC(
*column_or_expression*
), …
FROM mytable
JOIN another_table
ON mytable.column = another_table.column
WHERE
*constraint_expression*
GROUP BY column
HAVING
*constraint_expression*
ORDER BY
*column*
ASC/DESC
LIMIT
*count*
OFFSET
*COUNT*
;
```

## Example: Solving a crime (and learning SQL!)

### Overview

* In the spirit of learning by doing, let’s look at a fun exercise to get a grasp of how we would approach an SQL solution.
* We shall learn SQL by way of solving a crime using SQL queries. Please refer [Knightlab Mystery](https://mystery.knightlab.com/) for the example.

### Step 1: Identify tables

> The first thing we know about this problem is, that the crime was a `murder` which took place in `SQL City` and happened on the date `Jan 15,2018`.

* To proceed with this hint, we would need to know a basic structure of how the data is laid out. To do this, let’s see what tables exist:

```
SELECT name 
  FROM sqlite_master
 where type = 'table'
```

* This output shows us the tables that exist. We see a table that is named `crime_scene_report`. This would be a likely location of the reports which could have the details we have.

### Step 2: Check table schema (columns)

* To check whether that’s possible, let’s go ahead check the structure of the table:

```
SELECT sql 
  FROM sqlite_master
 where name = 'crime_scene_report'
```

* Here it shows us that the table does contain `date integer, type text, description text, city text`
* This matches what we’re looking for. Now, let’s do a query to see if we have any hits:

```
SELECT *
FROM 'crime_scene_report' AS t
WHERE
t.type LIKE 'murder'
AND
t.city LIKE 'SQL City'
AND
t.date = 20180115
```

* Good! We have a hit. It seems like there is a record that matches the facts we have.
* This also gives us the next clue:

> Security footage shows that there were two witnesses. The first witness lives at the last house on “Northwestern Dr”. The second witness, named Annabel, lives somewhere on “Franklin Ave”.

### Step 3:

* Alright, so now we have to find what these two witnesses said as the police report mentions. Looking at the list of tables we had earlier, we can create four more queries to find what the witnesses had said (two to find who the witnesses are and two to find what each of them said).

```
SELECT * FROM 'person' AS p
WHERE
p.address_street_name LIKE 'Northwestern Dr'
ORDER BY
p.address_number DESC
LIMIT 1
;
```

```
SELECT * FROM 'person' AS p
WHERE
p.name LIKE '%Annabel%'
AND
p.address_street_name LIKE 'Franklin Ave'
;
```

* At this stage we know who the witnesses were. Now, on to finding out what they said. For this, we will query the table `interviews`

```
SELECT * FROM 'interview'
WHERE
person_id = 16371 OR person_id = 14887
;
```

* Now we have quite a few hints from both these interviews. We are getting close to finding the murderer. From the multiple first hand interviews, we see they have a specific type of gym membership (`gold`) and we know when they were last there (`20160109`). We also find out partial information about the car they drive.
* Using this, let’s query the gym database to see what we can find out the members who match the criteria:

```
SELECT * FROM 'get_fit_now_member'
WHERE
membership_status LIKE 'gold'
AND
id LIKE '48Z%'
AND
membership_start_date < 20160109
;
```

* Interesting, we find only one match for this. The police must have been able to narrow this down from the interviews. Let’s see what he had to say when the police interviewed him.

```
SELECT * FROM 'interview'
WHERE
person_id = 67318
;
```

* Well, it turns out the the killer was not able to withstand the police questioning and did give up quite a few details about the person who hired him. From his interview, we can gather a lot of information about the characteristics of the person. Let’s look at the `persons` , `drivers_license` and `facebook_event_checkin`.

```
SELECT * FROM 'drivers_license'
WHERE
car_make LIKE 'Tesla'
AND
car_model LIKE 'Model S'
AND
hair_color LIKE 'red'
AND
gender LIKE 'female'
;
```

```
SELECT f.person_id,count(f.person_id), substr(f.date,1,6) FROM 'facebook_event_checkin' as f
WHERE
event_name like 'SQL Symphony Concert'
GROUP BY
substr(f.date,1,6),f.person_id
HAVING
substr(f.date,1,6) LIKE '201712'
AND
count(f.person_id)==3
;
```

* This narrows us down to the last two people. One of them must be the person who hired the killer.

```
select person.name,person.address_street_name,person.ssn,drivers_license.gender
from person
join drivers_license
on person.license_id==drivers_license.id
where person.id == 99716
;
```

* The above query returns `Miranda Priestly` as the name of the person who hired the killer.
* Let’s check this answer on the last section of the page which asks us to input the name of criminal, and indeed it turns out that she’s the one!
* This exercise can be condensed to a single query. Next, let’s look at creating large queries and testing them next. Thanks for reading till here.

## Further Reading

* Here are some optional resources for further reading:
* [sqlbolt](https://www.sqlbolt.com)
* [Learn SQL](https://www.learnsql.com)
* [Knightlab Mystery](https://mystery.knightlab.com)

## Citation

If you found our work useful, please cite it as:

```
@article{GhoshChadha2022DistilledSQLPrimer,
  title   = {SQL Primer},
  author  = {Ghosh, Soham and Chadha, Aman},
  journal = {Distilled AI},
  year    = {2022},
  note    = {\url{https://aman.ai}}
}
```
