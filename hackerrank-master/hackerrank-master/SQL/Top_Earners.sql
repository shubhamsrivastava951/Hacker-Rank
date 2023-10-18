select salary*months as sal,count(name) from employee 
group by sal
order by 1 desc limit 1   