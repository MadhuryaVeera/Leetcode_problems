# Write your MySQL query statement below
Delete from Person
where id NOT IN (
select * from (
    select min(id) from Person 
    Group by email
)AS temp
)