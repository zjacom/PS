# Write your MySQL query statement below
(select u.name as results
from users u
inner join movierating mr on u.user_id = mr.user_id
group by u.name
order by count(mr.rating) desc, 1
limit 1)

union all

(select m.title as results
from movies m
inner join movierating mr on m.movie_id = mr.movie_id
where mr.created_at like '2020-02%'
group by mr.movie_id
order by avg(mr.rating) desc, 1
limit 1)