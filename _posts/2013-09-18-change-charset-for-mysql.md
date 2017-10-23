---
title: change charset for mysql
author: gjergj.sheldija
layout: post
permalink: /change-charset-for-mysql/
categories:
  - code
  - sql
tags:
  - error 1267
  - latin1_general_ci
  - latin1_swedish_ci
  - mysql
  - sql
comments: true
---
a quick stored procedure to get rid of the infamous : {% raw %}Error Code: 1267. Illegal mix of collations (latin1_general_ci,IMPLICIT) and (latin1_swedish_ci,IMPLICIT) for operation &#8216;=&#8217;{% endraw %}

first of all i had to find those tables and databases, and to do so i used the following sql code

```mysql
SELECT 
	table_schema, 
	TABLE_NAME, 
	column_name, 
	character_set_name, 
	collation_name
FROM 
	information_schema.COLUMNS
WHERE 
	collation_name = ‘latin1_swedish_ci’
	AND 
	table_schema = ‘siis_qsut’
ORDER BY 
	table_schema, 
	TABLE_NAME,
	ordinal_position 
```


reaplce your\_db\_name with the name od the db you want to change the charset.

```mysql
DELIMITER $$
 CREATE PROCEDURE change_charset_and_collation_for_tables()
     BEGIN
        DECLARE TABLE_NAME VARCHAR(255);
        DECLARE end_of_tables INT DEFAULT ;
        DECLARE num_tables INT DEFAULT ;
        DECLARE cur CURSOR FOR
            SELECT 
				t.TABLE_NAME
            FROM 
				information_schema.TABLES t
            WHERE 
				t.table_schema = ‘your_db_name’ 
				AND 
				t.table_type=‘BASE TABLE’;
         DECLARE CONTINUE HANDLER FOR NOT FOUND SET end_of_tables = 1;
         OPEN cur;

         tables_loop: LOOP
             FETCH cur INTO TABLE_NAME;
            
            IF end_of_tables = 1 THEN
                LEAVE tables_loop;
            END IF;
 
            SET num_tables = num_tables + 1;
 
            SET @s = CONCAT(‘ALTER TABLE ’ , TABLE_NAME , ’ CONVERT TO CHARACTER SET latin1 COLLATE latin1_general_ci’);
 
            PREPARE stmt FROM @s;
            EXECUTE stmt;
        END LOOP;

        CLOSE cur;
    END $$ 
```

