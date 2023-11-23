DROP VIEW IF EXISTS completeuserinfo;
DROP VIEW IF EXISTS loyalty_pts_feedback;
DROP VIEW IF EXISTS exercise_routine_dailylog;
DROP VIEW IF EXISTS exercise_routine_fname;
DROP VIEW IF EXISTS no_of_user_per_trainer;
DROP VIEW IF EXISTS userid_of_trainer_3and7;
DROP VIEW IF EXISTS user_level;


-- natural join
create view completeuserinfo as  select * from user_info ui natural join user_info_email;
select * from completeuserinfo;
-- join operation
create view loyalty_pts_feedback as select dl.loyalty_id,feedback from daily_log dl join loyalty_pts lp on dl.loyalty_id = lp.loyalty_id;
select* from loyalty_pts_feedback;
-- 2 more examples for join
create view exercise_routine_dailylog as select * from exercise_routine natural join daily_log;
select * from exercise_routine_dailylog;

create view exercise_routine_fname as select d.ex_routine_id,ui.fname from user_info ui join does d on d.id = ui.id;
select * from exercise_routine_fname;

-- aggregate function
create view no_of_user_per_trainer as select trainer_id,count(*) as no_of_user_per_trainer from membership_type group by trainer_id;
select * from no_of_user_per_trainer;

select max(calories_burnt) from exercise_routine_dailylog;

select min(calories_consumed) from exercise_routine_dailylog;

select avg(calories_burnt) as calories_burnt,duration from exercise_routine_dailylog group by duration;  
-- set operator
create view userid_of_trainer_3and7 as select id from membership_type where trainer_id = "TRAINER3" union select id from membership_type where trainer_id = "TRAINER7";

select fname from exercise_routine_fname where ex_routine_id="EX_routine52"and exists (select fname from exercise_routine_fname where ex_routine_id="EX_routine93");

select fname from exercise_routine_fname where ex_routine_id="EX_routine39"and exists (select fname from exercise_routine_fname where ex_routine_id="EX_routine29");

(select ex_id from exercise_routine where ex_routine_id="EX_routine52") union (select ex_id from exercise_routine where ex_routine_id="EX_routine93");


select count(u.id),t.trainer_id from user_info u,membership_type m,trainer t where u.id=m.id and t.trainer_id=m.trainer_id group by t.trainer_id;

insert into membership_type values ("MEM6",3,5955.00,"USR79","TRAINER11");


SELECT d.calories,r.calories,d.recipe 
FROM exercise_routine as r, (
    SELECT dp.calories,dpr.recipe,dp.ex_id
    FROM diet_plan as dp,diet_plan_recipe as dpr
    WHERE dp.recipe=dpr.recipe
) as d 
WHERE r.ex_routine_id = d.ex_id;


SELECT u.id,u.fname,t.trainer_id,t.name,t.duration,t.type_id
FROM user_info as u 
JOIN (
    SELECT m.id,m.duration,m.type_id,t.trainer_id,t.name 
    FROM trainer as t 
    JOIN 
    membership_type as m 
    WHERE 
    t.trainer_id=m.trainer_id
) as t
WHERE u.id=t.id ;

select avg(calories_burnt),avg(calories_consumed),avg(duration) from daily_log;

SELECT  trainer_id from trainer
EXCEPT (SELECT trainer_id from membership_type);

CREATE view user_level as 
SELECT u.fname,l.streaks,l.level 
FROM user_info u,does d,exercise_routine r,daily_log dl,loyalty_pts l 
WHERE d.id = u.id and d.ex_routine_id=r.ex_routine_id and r.ex_routine_id=dl.ex_routine_id and dl.loyalty_id=l.loyalty_id;

SELECT t.name,m.amount 
FROM membership_type m,trainer t
WHERE m.trainer_id=t.trainer_id 
AND m.amount< (
    SELECT avg(amount) 
    FROM membership_type
);

SELECT u.id,u.fname 
FROM user_info u 
WHERE EXISTS (
    select * from does d,exercise_routine r,daily_log dl
    WHERE d.id = u.id and d.ex_routine_id=r.ex_routine_id and r.ex_routine_id=dl.ex_routine_id 
    AND ((dl.calories_burnt/dl.calories_consumed) > 0.3)
);