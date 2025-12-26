---
title: postgres change column type from boolean to integer
author: gjergj.sheldija
layout: post
permalink: /postgres-change-column-type-from-boolean-to-integer/
categories:
  - code
tags:
  - database
  - postgres
---
postgres change column type from boolean to integer

```sql
ALTER TABLE table_name ALTER column_name SET DEFAULT null;
 
ALTER TABLE table_name
ALTER column_name TYPE INTEGER
USING
CASE
	WHEN false THEN 0 ELSE 1
END;
 
ALTER TABLE table_name ALTER column_name SET DEFAULT 0;
COMMIT;
```
