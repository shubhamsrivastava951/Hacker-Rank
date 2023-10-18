select h.hacker_id, h.name, count(c.challenge_id) as c_count
from hackers h 
inner join challenges c
on h.hacker_id=c.hacker_id
group by h.hacker_id, h.name
having c_count = (select max(a.a_cnt) from
(select count(hacker_id) as a_cnt from challenges
group by hacker_id
order by hacker_id )a )
or 
c_count in (select b.b_cnt from
(select count(*) b_cnt from challenges
group by hacker_id) b 
group by b.b_cnt having count(b.b_cnt)=1)
order by c_count desc, h.hacker_id;
