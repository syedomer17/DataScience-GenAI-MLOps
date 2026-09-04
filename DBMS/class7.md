funcations in psql: 
1.string
2.Numaric
3.Date/time
4.Aggregation 
5.case (condition experation)

string: 
built-in operations used to manipulate, clean, and format text data within databases
lower,upper,length,substring,left,right,concate,trim ,replace 

ex:SELECT UPPDER(name),age FROM customers;
ex:SELECT LOWER(name),LENGTH(name) as name_lenght FROM customers; 
ex:SELECT SUBSTRING(name,3,3) FROM customers;
ex:SELECT id,name,LEFT(name,4) FROM customers;
ex:SELECT RIGHT(name,4) FROM customers;
ex:SELECT id,name,CONCAT(LEFT(name,3),LEFT(id::text,3)) as CODE FROM customers;
ex:SELECT TRIM('   HELLO WORLD.   ') AS trim;
ex:SELECT name, REPLACE(name,'a','A') FROM coustomers; 

Numaric: 
ABS,ceil,floay,round,truncat,power,sqrt,mod
