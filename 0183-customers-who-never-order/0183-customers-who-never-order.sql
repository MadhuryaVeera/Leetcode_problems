/* Write your PL/SQL query statement below */
select name as Customers
from 
Customers c
left join
Orders o
ON c.id=o.customerId
where c.id  NOT IN 
(
    select customerId from Orders
);