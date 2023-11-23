CREATE DATABASE fitnessmanagement;
USE fitnessmanagement;

CREATE TABLE diet_plan (
  ex_id varchar(20) NOT NULL ,
  recipe varchar(30) DEFAULT NULL,
  calories int(10) DEFAULT NULL
);

CREATE TABLE exercise_routine (
  ex_routine_id varchar(20) NOT NULL,
  duration int NOT NULL,
  calories int(10) DEFAULT NULL,
  ex_id varchar(20) NOT NULL 
);

CREATE TABLE daily_log (
  loyalty_id varchar(20) NOT NULL,
  duration int NOT NULL,
  calories_burnt int(10) DEFAULT NULL,
  calories_consumed int(10) DEFAULT NULL,
  feedback varchar(20) DEFAULT NULL,
  ex_routine_id varchar(20) NOT NULL 
);

CREATE TABLE diet_plan_recipe (
  recipe varchar(30) DEFAULT NULL
);

CREATE TABLE does (
  id varchar(20) NOT NULL,
  ex_routine_id varchar(20) NOT NULL
);

CREATE TABLE exercise_list (
  ex_id varchar(20) NOT NULL ,
  description varchar(30) DEFAULT NULL,
  type varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE loyalty_pts (
  loyalty_id varchar(20) NOT NULL ,
  level int(3) NOT NULL,
  streaks int(10) NOT NULL DEFAULT 0
);

CREATE TABLE user_info(
  id varchar(20) NOT NULL,
  PRIMARY KEY(id),
  gender int(2) DEFAULT 3,
  height int NOT NULL,
  weight int NOT NULL,
  fname varchar(20) NOT NULL,
  mname varchar(20) DEFAULT NULL,
  lname varchar(20) DEFAULT NULL,
  age int,
  bmi int
);

CREATE TABLE membership_type (
  type_id varchar(20) NOT NULL,
  duration int NOT NULL,
  amount decimal(10,2) NOT NULL,
  id varchar(20) NOT NULL ,
  trainer_id varchar(20) NOT NULL 
);

CREATE TABLE user_info_email (
  id varchar(20) NOT NULL ,
  email varchar(30) NOT NULL
);

CREATE TABLE trainer (
  trainer_id varchar(20) NOT NULL,
  PRIMARY KEY (trainer_id),
  phoneno int(10) NOT NULL,
  amount decimal(10,2) NOT NULL,
  name varchar(20) NOT NULL
);

ALTER TABLE diet_plan
  ADD KEY ex_id (ex_id),
  ADD KEY recipe (recipe);

ALTER TABLE exercise_routine
  ADD PRIMARY KEY (ex_routine_id),
  ADD KEY ex_id (ex_id);

ALTER TABLE daily_log
  ADD PRIMARY KEY (loyalty_id),
  ADD KEY ex_routine_id (ex_routine_id);

ALTER TABLE diet_plan_recipe
  ADD KEY recipe (recipe);

ALTER TABLE does
  ADD PRIMARY KEY (id,ex_routine_id),
  ADD KEY id (id),
  ADD KEY ex_routine_id (ex_routine_id);

ALTER TABLE exercise_list
  ADD PRIMARY KEY (ex_id);

ALTER TABLE loyalty_pts
  ADD KEY (loyalty_id);  

ALTER TABLE membership_type
  ADD PRIMARY KEY (type_id),
  ADD KEY id (id),
  ADD KEY trainer_id (trainer_id);

ALTER TABLE user_info_email
  ADD PRIMARY KEY (id,email),
  ADD KEY id (id);

ALTER TABLE diet_plan
  ADD CONSTRAINT diet_plan_ibfk_1 FOREIGN KEY (ex_id) REFERENCES exercise_routine (ex_routine_id);

ALTER TABLE diet_plan
  ADD CONSTRAINT diet_plan_ibfk_2 FOREIGN KEY (recipe) REFERENCES diet_plan_recipe (recipe);

ALTER TABLE exercise_routine
  ADD CONSTRAINT exercise_routine_ibfk_1 FOREIGN KEY (ex_id) REFERENCES exercise_list (ex_id);

ALTER TABLE does
  ADD CONSTRAINT does_ibfk_1 FOREIGN KEY (ex_routine_id) REFERENCES exercise_routine (ex_routine_id);

ALTER TABLE daily_log
  ADD CONSTRAINT daily_log_ibfk_1 FOREIGN KEY (ex_routine_id) REFERENCES exercise_routine (ex_routine_id);

ALTER TABLE loyalty_pts
  ADD CONSTRAINT loyalty_pts_ibfk_1 FOREIGN KEY (loyalty_id) REFERENCES daily_log (loyalty_id);

ALTER TABLE does
  ADD CONSTRAINT does_ibfk_2 FOREIGN KEY (id) REFERENCES user_info (id);

ALTER TABLE user_info_email
  ADD CONSTRAINT user_info_email_ibfk_1 FOREIGN KEY (id) REFERENCES user_info (id);

ALTER TABLE membership_type
  ADD CONSTRAINT membership_type_ibfk_1 FOREIGN KEY (id) REFERENCES user_info (id);

ALTER TABLE membership_type
  ADD CONSTRAINT membership_type_ibfk_2 FOREIGN KEY (trainer_id) REFERENCES trainer (trainer_id);