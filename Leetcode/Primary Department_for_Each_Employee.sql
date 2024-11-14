# Write your MySQL query statement below
select a.employee_id,
case when count(*) > 1 then (select department_id from employee where primary_flag = 'Y' and employee_id = a.employee_id)
else department_id end department_id
from employee a
group by a.employee_id